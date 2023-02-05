def nyt(self, datestop=False):
    source = 'nyt'

    url = 'https://www.nytimes.com/search?dropmab=true&query=' + self.keywords.replace(' ', '%20') + '&sort=newest'

    driver = self._load_driver(caps='none')

    try:

        # Set and retrive url
        driver.get(url)
        xpath = '//button[@data-testid="search-show-more-button"]'
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        xpath = '//span[@data-testid="todays-date"]'
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
        contents = []
        bool = True
        t = 30
        k = 0
        oldnumber = 0
        time.sleep(3)
        while bool:
            try:
                newnumber = len(driver.find_elements_by_tag_name('li'))
                if newnumber != oldnumber:
                    k = 0
                    # do it with xpath
                    oldnumber = len(driver.find_elements_by_tag_name('li'))
                    element = driver.find_element_by_xpath('//button[@data-testid="search-show-more-button"]')
                    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
                    # driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
                    # driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)

                    ActionChains(driver).move_to_element(element).click().perform()
                    time.sleep(random.randint(1, 2))
                    # time.sleep(1)
                    newnumber = len(driver.find_elements_by_tag_name('li'))

                    last_date = driver.find_elements_by_xpath('//span[@data-testid="todays-date"]')[-1].text
                    if ',' in last_date:
                        y = last_date.split(' ')[-1]
                    else:
                        y = str(dt.datetime.today().year)
                    try:  # because of minute timestamp
                        m = self.months[last_date.split(' ')[0][:3].replace('.', '').replace(',', '').lower()]
                        if len(last_date.split(' ')[1].replace(',', '')) < 2:
                            d = '0' + last_date.split(' ')[1].replace(',', '')
                        else:
                            d = last_date.split(' ')[1].replace(',', '')
                        if datestop:
                            if pd.to_datetime(f'{y}-{m}-{d}', format='%Y-%m-%d') < pd.to_datetime(datestop):
                                content = driver.page_source
                                contents.append(content)
                                bool = False
                    except:
                        pass

                k += 1
                if k > t:
                    content = driver.page_source
                    contents.append(content)

                    # try:
                    # last_date = driver.find_elements_by_tag_name('time')[-1].text
                    last_date = driver.find_elements_by_xpath('//div[@data-testid="todays-date"]')[-1].text

                    if ',' in last_date:
                        y = last_date.split(' ')[-1]
                    else:
                        y = str(dt.datetime.today().year)
                    try:  # because of minute timestamp
                        m = self.months[last_date.split(' ')[0][:3].replace('.', '').replace(',', '').lower()]
                        if len(last_date.split(' ')[1].replace(',', '')) < 2:
                            d = '0' + last_date.split(' ')[1].replace(',', '')
                        else:
                            d = last_date.split(' ')[1].replace(',', '')
                        if datestop:
                            if pd.to_datetime(f'{y}-{m}-{d}', format='%Y-%m-%d') < pd.to_datetime(datestop):
                                content = driver.page_source
                                contents.append(content)
                                bool = False
                    except:
                        pass

                    url = 'https://www.nytimes.com/search?dropmab=true&endDate=' + y + m + d + '&query=' + self.keywords.replace(
                        ' ', '%20') + '&sort=newest&startDate=' + '20000101'
                    driver.get(url)
                    time.sleep(1)
                    newnumber = len(driver.find_elements_by_tag_name('li'))
                    k = 0
                    # t = 25
                    # except:
                    #    bool = False
            except:
                content = driver.page_source
                contents.append(content)
                bool = False
        driver.close()
        driver.quit()
    except:
        print('Failed to load data...\n')
        driver.quit()
        return None

    headline, link, date, description, author, tag, comment = [], [], [], [], [], [], []
    for content in contents:
        soup = bs(content, "lxml")
        articles = soup.find_all('li', attrs={'data-testid': 'search-bodega-result'})
        for article in articles:
            link.append(article.find('a').get('href'))
            headline.append(article.find('h4').text)
            try:
                date.append(article.find('span', attrs={'data-testid': 'todays-date'}).text)
            except:
                time.sleep(0.5)
                date.append(article.find('div', attrs={'data-testid': 'todays-date'}).text)
            try:
                description.append(article.find('p', class_='css-16nhkrn').text)
            except:
                description.append('nan')
            tag.append(article.find('p', class_='css-myxawk').text)
            try:
                author.append(article.find('p', class_='css-15w69y9').text.replace('By ', ''))
            except:
                author.append('nan')
            try:
                comment.append(article.find('span', class_='css-h4mf4').text)
            except:
                comment.append('nan')
    # clean dates
    data = pd.DataFrame(
        {
            'link': link,
            'headline': headline,
            'date': date,
            'description': description,
            'tag': tag,
            'author': author,
            'comments': comment
        }
    )

    data.drop_duplicates(inplace=True)

    data['date_retrieved'] = dt.datetime.today()
    data['ticker'] = self.ticker
    data['newspaper'] = 'NYT'
    data['search_term'] = self.keywords
    data['id'] = data['newspaper'] + data['headline'] + data['link']
    columns = ['link', 'headline', 'date', 'description', 'date_retrieved', 'author', 'tag', 'newspaper', 'comments',
               'ticker', 'search_term', 'id']
    for col in columns:
        if col not in data.columns:
            data[col] = 'nan'
    data['source'] = source

    data = self._clean_dates(data)

    if self.verbose:
        print('-' * 78)
        print(source.upper(), 'done.', len(data), 'articles collected.')
        print('-' * 78)

    return data
