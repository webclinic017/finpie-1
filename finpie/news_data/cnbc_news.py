


def cnbc(self, datestop=False):

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                            CNBC
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# may want to change keywords

source = 'cnbc'

url = 'https://www.cnbc.com/search/?query=' + self.keywords.replace(' ', '%20') + '&qsearchterm=' + self.keywords.replace \
    (' ', '%20')

driver = self._load_driver(caps = 'none')

try:
    # Set and retrive url
    driver.get(url)

    try:
        xpath = '//button[@id="onetrust-accept-btn-handler"]'
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
        driver.find_element_by_xpath(xpath).click()
    except:
        pass

    #
    try:
        element = WebDriverWait(driver, 30).until \
            (EC.presence_of_element_located((By.XPATH, '//span[@class="SearchResult-publishedDate"]')))
    except:
        element = WebDriverWait(driver, 30).until \
            (EC.presence_of_element_located((By.XPATH, '//button[@class="Search-submitBtn icon-search"]')))
        driver.get(url)
        element = WebDriverWait(driver, 30).until \
            (EC.presence_of_element_located((By.XPATH, '//span[@class="SearchResult-publishedDate"]')))

    # driver.refresh()
    try:
        try:
            element = WebDriverWait(driver, 10).until \
                (EC.presence_of_element_located((By.XPATH, '//div[@id="sortdate"]')))
            element = driver.find_element_by_xpath('//div[@id="sortdate"]')
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)
            ActionChains(driver).move_to_element( element).click().perform()
            time.sleep(3)
        except:
            pass
    except:
        pass

    # element = driver.find_element_by_tag_name('head')
    # driver.execute_script("""
    # var element = arguments[0];
    # element.parentNode.removeChild(element);
    # """, element)

    k = 0
    t = 100
    SCROLL_PAUSE_TIME = 0.5
    while k < t:
        k = 0

        if datestop:
            element = driver.find_elements_by_xpath('//span[@class="SearchResult-publishedDate"]')[-1].text
            element = pd.to_datetime( element.split(' ')[0], format = '%m/%d/%Y' )
            if element < pd.to_datetime(datestop):
                k = 110
        # SearchResult-searchResultImage
        # SearchResult-searchResultCard SearchResult-standardVariant
        try:
            elements = driver.find_elements_by_xpath \
                ('//div[@class="SearchResult-searchResultCard SearchResult-standardVariant"]')
            for element in elements:
                driver.execute_script("""
                var element = arguments[0];
                element.parentNode.removeChild(element);
                """, element)
        except:
            pass

        try:
            elements = driver.find_elements_by_xpath('//a[@class="Card-mediaContainer resultlink"]')
            for element in elements:
                driver.execute_script("""
                var element = arguments[0];
                element.parentNode.removeChild(element);
                """, element)
        except:
            pass

        last_height       = driver.execute_script( 'return document.documentElement.scrollHeight' )

        # Scroll down to bottom
        driver.execute_script( 'window.scrollTo(0, document.documentElement.scrollHeight);' )
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script( 'return document.documentElement.scrollHeight;' )

        time.sleep(random.randint(0 ,4) * 0.43)

        while new_height == last_height:

            driver.execute_script("window.scrollTo(0, -document.documentElement.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIM E /3)

            driver.execute_script( 'window.scrollTo(0, document.documentElement.scrollHeight);' )
            time.sleep(SCROLL_PAUSE_TIM E /3)

            # Wait to load page
            new_height = driver.execute_script( 'return document.documentElement.scrollHeight;' )
            time.sleep(SCROLL_PAUSE_TIM E /3)

            if datestop:
                element = driver.find_elements_by_xpath('//span[@class="SearchResult-publishedDate"]')[-1].text
                element = pd.to_datetime( element.split(' ')[0], format = '%m/%d/%Y' )
                if element < pd.to_datetime(datestop):
                    k = 110
            k += 1
            if k >= t:
                break
            time.sleep(random.randint(0 ,2) * 0.43)
    content = driver.page_source
    driver.close()
    driver.quit()
except:
    print('Failed to load data...\n')
    driver.quit()
    return None

headline, link, date, description, author, tag = [], [], [], [], [], []

soup  = bs( content, "lxml" )
articles  = soup.find_all('div', class_ = 'SearchResult-searchResult' )
len(articles)
for article in articles:
    link.append( article.find('a', class_ = 'resultlink' ).get('href') )
    headline.append( article.find('span', class_ = 'Card-title').text )
    date.append( article.find('span', class_ = 'SearchResult-publishedDate' ).text )
    try:
        tag.append( article.find('div', class_ = 'SearchResult-searchResultEyebrow').text )
    except:
        tag.append( 'nan' )
    try:
        description.append( article.find('p', class_ = 'SearchResult-searchResultPreview' ).text )
    except:
        description.append( 'nan' )
    try:
        author.append( article.find('a', class_ = 'SearchResult-author').text )
    except:
        author.append( 'nan' )


data = pd.DataFrame(
    {
        'link': link,
        'headline': headline,
        'date': date,
        'description': description,
        'tag': tag,
        'author': author
    }
)

data['date_retrieved'] = dt.datetime.today()
data['ticker'] = self.ticker
data['comments'] = 'nan'
data['newspaper'] = 'CNBC'

data['search_term'] = self.keywords

data['id'] = data['newspaper'] +  data['headline'] + data['link']
columns = [ 'link', 'headline', 'date', 'description', 'date_retrieved', 'author', 'tag', 'newspaper', 'comments', 'ticker', 'search_term', 'id' ]
for col in columns:
    if col not in data.columns:
        data[col] = 'nan'

data['source'] = source