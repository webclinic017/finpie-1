
def seeking_alpha(self, datestop = False, press_releases = False):
    # Note: might be stopping scrape too early

    def _get_date(d):
        w = d.split(' ')[1:]
        if len(w) == 2:
            d = pd.to_datetime( w[1].replace(',', '')  + '/' + self.months[w[0][:3].lower()] + '/' + str(dt.datetime.today().year), format = '%d/%m/%Y' )
        else:
            d = pd.to_datetime( w[1].replace(',', '')  + '/' + self.months[w[0][:3].lower()] + '/' + str(w[2]), format = '%d/%m/%Y' )
        return d

    source = 'sa'

    if press_releases:
        url =  f'https://seekingalpha.com/symbol/{self.ticker}/press-releases'
    else:
        url = f'https://seekingalpha.com/symbol/{self.ticker}/news'
    driver = self._load_driver(caps = 'none')
    try:
        # Set and retrive url
        driver.get(url)

        time.sleep(5)

        driver.execute_script( 'window.scrollTo(0, document.documentElement.scrollHeight);' )
        driver.execute_script( 'window.scrollTo(0, 0);' )
        driver.execute_script( 'window.scrollTo(0, document.documentElement.scrollHeight);' )

        time.sleep(2)
        passed = False
        try:
            xpath = '//div[@id="px-captcha"]'
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = driver.find_element_by_tag_name('iframe')
            ActionChains(driver).click_and_hold(element).perform()
            time.sleep(5)
            ActionChains(driver).release(element).perform()
            passed = True
        except:
            pass

        try:
            xpath = '//div[@id="px-captcha"]'
            element = driver.find_element_by_xpath(xpath)
            ActionChains(driver).click_and_hold(element).perform()
            time.sleep(7)
            ActionChains(driver).release(element).perform()
            passed = True
        except:
            pass

        time.sleep(10)
        driver.switch_to.window(driver.window_handles[0])

        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//article')))
        k = 0
        t = 20
        SCROLL_PAUSE_TIME = 0.9

        while k < t:
            k = 0

            if not passed:
                try:
                    xpath = '//div[@id="px-captcha"]'
                    if len(driver.find_elements_by_xpath(xpath)) > 0:
                        element = driver.find_element_by_tag_name('iframe')
                        ActionChains(driver).click_and_hold(element).perform()
                        time.sleep(5)
                        ActionChains(driver).release(element).perform()
                        passed = False
                except:
                    pass
                try:
                    xpath = '//div[@id="px-captcha"]'
                    element = driver.find_element_by_xpath(xpath)
                    ActionChains(driver).click_and_hold(element).perform()
                    time.sleep(7)
                    ActionChains(driver).release(element).perform()
                    passed = True
                except:
                    pass
            # last_height       = driver.execute_script( 'return document.documentElement.scrollHeight' )
            # last_number = len(driver.find_elements_by_class_name('symbol_item'))
            last_number =  len(driver.find_elements_by_xpath('//article'))
            # Scroll down to bottom
            driver.execute_script( 'window.scrollTo(0, document.documentElement.scrollHeight);' )
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            # new_height = driver.execute_script( 'return document.documentElement.scrollHeight;' )
            # new_number = len(driver.find_elements_by_class_name('symbol_item'))
            new_number = len(driver.find_elements_by_xpath('//article'))

            if datestop:
                d = _get_date(driver.find_elements_by_xpath('//span[@data-test-id="post-list-date"]')[-1].text)
                if d < pd.to_datetime(datestop):
                    k = t + 10

            while new_number == last_number:

                # need to verify this
                if not passed:
                    try:
                        xpath = '//div[@id="px-captcha"]'
                        if len(driver.find_elements_by_xpath(xpath)) > 0:
                            element = driver.find_element_by_tag_name('iframe')
                            ActionChains(driver).click_and_hold(element).perform()
                            time.sleep(5)
                            ActionChains(driver).release(element).perform()
                            passed = False
                    except:
                        pass

                driver.execute_script("window.scrollTo(0, -document.documentElement.scrollHeight);")
                time.sleep(SCROLL_PAUSE_TIM E /3)

                driver.execute_script( 'window.scrollTo(0, document.documentElement.scrollHeight);' )
                time.sleep(SCROLL_PAUSE_TIM E /3)

                # Wait to load page
                # new_height = driver.execute_script( 'return document.documentElement.scrollHeight;' )
                # new_number = len(driver.find_elements_by_class_name('symbol_item'))
                new_number = len(driver.find_elements_by_xpath('//article'))
                time.sleep(SCROLL_PAUSE_TIM E /3)

                k + =1
                if k == t:
                    break
                time.sleep(0.5)



        soup  = bs( driver.page_source, "lxml" )

        driver.close()
        driver.quit()
    except:
        print('Failed to load data...\n')
        driver.quit()
        return None

    headline, link, date, author, comments = [], [], [], [], []

    # news
    headline, link, date, author, comments = [], [], [], [], []
    articles  = soup.find('div', attrs = {'data-test-id': 'post-list'} ).find_all('article' )
    for article in articles:
        try:
            headline.append( article.find('h3').text )
            link.append( article.find('a').get('href') )
            author.append( article.find('span', attrs = {'data-test-id': 'post-list-author'} ).text )
            date.append( article.find('span', attrs = {'data-test-id': 'post-list-date'} ).text )
            try:
                comments.append( article.find('span', attrs = {'data-test-id': 'post-list-comments'} ).text )
            except:
                comments.append( '0 comments' )
        except:
            continue


    df_news = pd.DataFrame(
        {
            'link': link,
            'headline': headline,
            'date': date,
            'author': author,
            'comments': comments
        }
    )

    df_news['date_retrieved'] = dt.datetime.today()
    df_news['ticker'] = self.ticker
    df_news['description'] = 'nan'
    df_news['tag'] = 'nan'
    df_news['newspaper'] = 'SA - News'


    data = df_news.copy()
    data['search_term'] = self.keywords

    data['id'] = data['newspaper'] +  data['headline'] + data['link']
    columns = [ 'link', 'headline', 'date', 'description', 'date_retrieved', 'author', 'tag', 'newspaper', 'comments', 'ticker', 'search_term', 'id' ]
    for col in columns:
        if col not in data.columns:
            data[col] = 'nan'

    headline, link, date, author, comments = [], [], [], [], []
    df_news = None
    articles = None
    soup = None

    data['source'] = source

    data = self._clean_dates(data)


    if self.verbose:
        print('-' * 78)
        print(source.upper(), 'done.', len(data), 'articles collected.')
        print('-' * 78)

    return data
