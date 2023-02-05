import re
import time
import random
import numpy as np
import pandas as pd
import datetime as dt
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from finpie.news_data.clean_news import CleanNews
from finpie.news_data.news import CleanNews

class BarronsNews(CleanNews):
    def __init__(self, ticker, keywords, head=False, verbose=False):
        CleanNews.__init__(self, ticker, keywords, head, verbose)
        self.ticker = ticker
        self.keywords = keywords
        self.verbose = verbose
        self.head = True
            
    def barrons(self, datestop = False, companyNews = False):
    
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #                            Barrons
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
        # problem with older data having concatenated strings in their headlines
        driver = self._load_driver()
        source = 'barrons'
    
        if companyNews:
    
            url = f'https://www.barrons.com/quote/stock/{self.ticker}'
    
    
            try:
                # Set and retrive url
                driver.get(url)
    
                xpath = '//div[@class="news bgNews more-news-capable"]'
                element = driver.find_element(By.XPATH, xpath)
    
                bool = True
                while bool:
                    driver.execute_script('arguments[0].scrollTop += 1000', element)
                    if datestop:
                        d = driver.find_elements(By.XPATH, '//span[@class="date"]')[0].text
                        if pd.to_datetime( d ) < pd.to_datetime(datestop):
                            bool = False
                    try:
                        xpath = '//div[@class="no-more-news"][contains(@style,"display: block")]'
                        driver.find_element(By.XPATH, xpath)
                        bool = False
                    except:
                        pass
    
                articles = bs( driver.page_source, "lxml").find('ul', class_='news-columns').find_all('li' )
    
                driver.close()
                driver.quit()
            except:
                print('Failed to load data...\n')
                driver.quit()
                return None
    
            headline, link, date, description, author, tag, newspaper = [], [], [], [], [], [], []
            for article in articles:
                link.append( article.find('a').get('href') )
                headline.append( article.find('a').text )
                date.append( article.find('span', class_ = 'date' ).text )
                newspaper.append( article.find('span', class_='provider').text )
    
            data = pd.DataFrame(
                {
                    'link': link,
                    'headline': headline,
                    'date': date,
                    'newspaper': newspaper,
                }
            )
    
            headline, link, date, description, author, tag = [], [], [], [], [], []
            contents = None
    
            data['date_retrieved'] = dt.datetime.today()
            data['ticker'] = self.ticker
            data['comments'] = 'nan'
            data['tag'] = 'nan'
            data['search_term'] = 'nan'
    
            data['id'] = data['newspaper'] +  data['headline'] + data['link']
            columns = [ 'link', 'headline', 'date', 'description', 'date_retrieved', 'author', 'tag', 'newspaper', 'comments', 'ticker', 'search_term', 'id' ]
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
    
        else:
            url = 'https://www.barrons.com/search?query=' + self.keywords + '&quotequery=' + self.keywords.lower() +'&isToggleOn=true&operator=OR&sort=date-desc&duration=4y&source=barrons%2Cbarronsblog%2Cbarronsvideos%2Cbarronswebstory%2Cbarronslivecoverage%2Cautowire'
            try:
                # Set and retrive url
                driver.get(url)
                # close popup
                contents = []
                try:
                    contents.append(bs(driver.page_source, "lxml").find_all('articles')
                except:
                    pass
                bool = True
                while bool:
                    try:
                        #####____
                        driver.get(driver.find_element(By.XPATH, '//a[@class="BarronsTheme--button--ZaJGOY2h BarronsTheme--pagination--3A4DPjMD"]').get_attribute('href'))
                        contents.append( bs( driver.page_source, "lxml").find('div', class_='section-content').find_all('li'))
                        if len(driver.find_elements_by_class_name('headline')) == 0:
                            bool = False
                        if datestop:
                            d = driver.find_elements(By.XPATH, '//span[@class="date"]')[-1].text
                            if pd.to_datetime( d ) < pd.to_datetime(datestop):
                                bool = False
                    except:
                        bool = False
    
                driver.close()
                driver.quit()
            except:
                print('Failed to load data...\n')
                driver.quit()
                return None
    
            headline, link, date, description, author, tag, newspaper = [], [], [], [], [], [], []

            for articles in contents:
                # soup  = bs( content, "lxml" )
                # articles  = soup.find('div', class_ = 'section-content').find_all('li' )
                for article in articles:
                    link.append(article.find('a').get('href'))
                    headline.append(article.find('span', class_='headline').text)
                    date.append(article.find('span', class_='date').text)
                    author.append(article.find('span', class_='author').text)
                    newspaper.append(article.find('span', class_='provider').text)
                    try:
                        description.append(article.find('p').text)
                    except:
                        description.append('nan')
    
    
            data = pd.DataFrame(
                {
                    'link': link,
                    'headline': headline,
                    'date': date,
                    'description': description,
                    'newspaper': newspaper,
                    'author': author
                }
            )
    
            headline, link, date, description, author, tag = [], [], [], [], [], []
            contents = None
            data['date_retrieved'] = dt.datetime.today()
            data['ticker'] = self.ticker
            data['comments'] = 'nan'
            data['tag'] = 'nan'
            data['search_term'] = self.keywords
            data['id'] = data['newspaper'] +  data['headline'] + data['link']
            columns = [ 'link', 'headline', 'date', 'description', 'date_retrieved', 'author', 'tag', 'newspaper', 'comments', 'ticker', 'search_term', 'id' ]
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


if __name__ == '__main__':
    p = 1
    # quick test
    barrons = BarronsNews('AAPL', 'AAPL')
    print(barrons.barrons())