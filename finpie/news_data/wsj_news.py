def wsj(self, datestop=False):
    source = 'wsj'

    # change to date today
    td_1 = dt.datetime.today() - dt.timedelta(days=320)
    y, m, d = self._format_date(td_1)
    start_date = y + '%2F' + m + '%2F' + d
    td_2 = dt.datetime.today()
    y, m, d = self._format_date(td_2)
    end_date = y + '%2F' + m + '%2F' + d

    url = 'https://www.wsj.com/search?&query=' + self.keywords.replace(' ',
                                                                       '%20') + '&sort=date-desc&duration=4y&startDate=' + start_date + '&endDate=' + end_date + '&source=wsjie%2Cblog%2Cwsjvideo%2Cinteractivemedia%2Cwsjsitesrch%2Cwsjpro%2Cautowire%2Capfeed'
    driver = self._load_driver(caps='none')

    try:
        # Set and retrive url
        driver.get(url)
        time.sleep(10)
        try:
            driver.switch_to.frame(2)
            xPath = '//button[@title="YES, I AGREE"]'
            driver.find_element_by_xpath(xPath).click()
            driver.switch_to.default_content()
        except:
            pass
        driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')

        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "next")]')))
        bool2 = True
        contents = []
        # max = int( driver.find_element_by_xpath('//div[@class="results-menu-wrapper bottom"]//li[@class="results-count"]').text.replace('of ', '') )
        max = int(driver.find_element_by_xpath(
            '//div[@class="WSJTheme--dropdown--3cxtZgDl "]/following::span[contains(text(), "of")]').text.replace('of ',
                                                                                                                  ''))
        contents.append(driver.page_source)
        for i in range(max - 1):
            try:
                time.sleep(random.randint(0, 2))
                driver.get(url + f'&page={i + 2}')
                element = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "next")]')))
                driver.find_element_by_xpath('//a[contains(text(), "next")]').click()
                contents.append(driver.page_source)
            except:
                try:
                    # driver.get(url)
                    driver.get(url + f'&page={i + 2}')
                    # driver.find_element_by_xpath('//a[contains(text(), "next")]').click()
                    element = WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "next")]')))
                    contents.append(driver.page_source)
                except:
                    driver.get(url + f'&page={i + 2}')
                    # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "next")]')))
                    time.sleep(5)
                    contents.append(driver.page_source)

            time.sleep(5)
            if datestop:
                try:
                    # d = driver.find_elements_by_xpath('//time[@class="date-stamp-container"]')[-1].text
                    d = driver.find_elements_by_xpath('//p[contains(@class, "WSJTheme--timestamp")]')[-1].text
                    d = pd.to_datetime(' '.join(d.split(' ')[:3]))
                    if d < pd.to_datetime(datestop):
                        bool2 = False
                        break
                except:
                    # d = driver.find_elements_by_xpath('//time[@class="date-stamp-container highlight"]')[-1].text
                    d = driver.find_elements_by_xpath('//p[contains(@class, "WSJTheme--timestamp")]')[-1].text

                    pass

        if bool2:
            bool = True
        else:
            bool = False
            # Record progress
            # _print_progress(i, max-1)
        contents.append(driver.page_source)

        while bool:
            try:
                td_2 = td_1
                y, m, d = self._format_date(td_2)
                start_date = y + '/' + m + '/' + d
                td_1 = td_1 - dt.timedelta(days=320)
                y, m, d = self._format_date(td_1)
                end_date = y + '/' + m + '/' + d

                url = 'https://www.wsj.com/search?&query=' + self.keywords.replace(' ',
                                                                                   '%20') + '&sort=date-desc&duration=4y&startDate=' + start_date + '&endDate=' + end_date + '&source=wsjie%2Cblog%2Cwsjvideo%2Cinteractivemedia%2Cwsjsitesrch%2Cwsjpro%2Cautowire%2Capfeed'

                driver.get(url)

                element = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "next")]')))

                # driver.switch_to.frame(0)
                # driver.find_elements_by_xpath('//article')

                # max = int( driver.find_element_by_xpath('//div[@class="results-menu-wrapper bottom"]//li[@class="results-count"]').text.replace('of ', '') )
                max = int(driver.find_element_by_xpath(
                    '//div[@class="WSJTheme--dropdown--3cxtZgDl "]/following::span[contains(text(), "of")]').text.replace(
                    'of ', ''))
                contents.append(driver.page_source)

                for i in range(max - 1):
                    try:
                        time.sleep(random.randint(0, 2))
                        driver.get(url + f'&page={i + 2}')
                        # driver.find_element_by_xpath('//a[contains(text(), "next")]').click()
                        element = WebDriverWait(driver, 15).until(
                            EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "next")]')))
                        contents.append(driver.page_source)
                    except:
                        try:
                            driver.get(url + f'&page={i + 2}')
                            # driver.get(url)
                            # driver.find_element_by_xpath('//a[contains(text(), "next")]').click()
                            element = WebDriverWait(driver, 15).until(
                                EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "next")]')))
                            contents.append(driver.page_source)
                        except:
                            driver.get(url + f'&page={i + 2}')
                            contents.append(driver.page_source)

                    if datestop:
                        # d = driver.find_elements_by_xpath('//time[@class="date-stamp-container"]')[-1].text
                        d = driver.find_elements_by_xpath('//p[contains(@class, "WSJTheme--timestamp")]')[-1].text
                        d = pd.to_datetime(' '.join(d.split(' ')[:3]))
                        if d > pd.to_datetime(datestop):
                            bool = False
            except:
                bool = False

        driver.close()
        driver.quit()
    except:
        print('Failed to load data...\n')
        driver.quit()
        return None
    headline, link, date, description, author, tag = [], [], [], [], [], []

    for content in contents:
        soup = bs(content, "lxml")
        # articles  = soup.find_all('div', class_ = 'headline-item' )
        articles = soup.find_all('article')

        for article in articles:

            try:
                date.append(article.find('p', class_=re.compile('^WSJTheme--timestamp')).text)
            except:
                continue

            headline.append(article.find('h3').text.strip())
            link.append(article.find('h3').find('a').get('href'))
            try:
                tag.append(article.find('li', class_=re.compile('^WSJTheme--type')).text)
            except:
                tag.append('nan')
            # date.append( article.find('time').text )

            try:
                # author.append( article.find('li', class_ = 'byline').text.replace('By', '').strip() )
                author.append(article.find('p', class_=re.compile('^WSJTheme--byline')).text.strip())
            except:
                author.append('nan')
            try:
                description.append(article.find('p', class_=re.compile('^WSJTheme--summary')).text.strip())
            except:
                description.append('nan')

    data = pd.DataFrame(
        {
            'link': link,
            'headline': headline,
            'date': date,
            'description': description,
            'author': author,
            'tag': tag
        }
    )

    data['date_retrieved'] = dt.datetime.today()
    data['ticker'] = self.ticker
    data['newspaper'] = 'WSJ'
    data['search_term'] = self.keywords

    data['id'] = data['newspaper'] + data['headline'] + data['link']
    columns = ['link', 'headline', 'date', 'description', 'date_retrieved', 'author', 'tag', 'newspaper', 'comments',
               'ticker', 'search_term', 'id']
    for col in columns:
        if col not in data.columns:
            data[col] = 'nan'

    data['source'] = source

    data = self._clean_dates(data)
    # write to parquet file with ticker as partition

    if self.verbose:
        print('-' * 78)
        print(source.upper(), 'done.', len(data), 'articles collected.')
        print('-' * 78)

    return data
