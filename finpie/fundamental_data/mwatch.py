#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# finpie - a simple library to download some financial data
# https://github.com/peterlacour/finpie
#
# Copyright (c) 2020 Peter la Cour
#
# Licensed under the MIT License
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#


from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import pandas as pd
import numpy as np

from finpie.fundamental_data.fundamental_base import Fundamental



class mwatchData( Fundamental ):

    def __init__(self, ticker):
        self.ticker = ticker

    def _download(self, sheet, freq = 'annual'):
        '''


        '''
        if freq.lower() == 'annual' or freq.lower() == 'a':
            url = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/{sheet}'
        elif freq.lower() == 'quarterly' or freq.lower() == 'q':
            url = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/{sheet}/quarter'
        else:
            print('Please specify annual or quartlery frequency.')
            return None
        session = HTMLSession()
        r = session.get(url)
        soup = bs(r.content, 'html5lib')
        df = pd.concat( [ pd.read_html(str(s))[0] for s in soup.find('div', class_ = 'financials').find_all('table') ] )
        df = df.astype(str)
        df.iloc[:,0][ df.iloc[:,0] == 'nan' ]= df[ df.iloc[:,0] == 'nan' ].iloc[:,-1]
        df = df.iloc[:,:-2]
        df = df.transpose()
        df.index.name = 'date'
        df.columns = df.iloc[0]
        df = df[1:]
        df.columns.name = ''
        df.replace('-', np.nan, inplace = True)
        df.replace('\(', '-', regex = True, inplace = True)
        df.replace('\)', '', regex = True, inplace = True)
        # rename duplicate columns
        columns = pd.io.parsers.ParserBase({'names':df.columns})._maybe_dedup_names(df.columns)
        df.columns = [ str(col).replace('\xa0', ' ') for col in columns ]
        df = df.astype('str')
        for col in df.columns:
            try:
                df.loc[df[col].str.contains('T'), col] = (df[col][df[col].str.contains('T')] \
                                                        .replace('T', '', regex = True).replace(',', '', regex = True) \
                                                        .astype('float') * 1000000000000).astype('str')
                df.loc[df[col].str.contains('B'), col] = (df[col][df[col].str.contains('B', case=True)] \
                                                        .replace('B', '', regex = True).replace(',', '', regex = True) \
                                                        .astype('float') * 1000000000).astype('str')
                df.loc[df[col].str.contains('M'), col] = (df[col][df[col].str.contains('M', case=True)] \
                                                        .replace('M', '', regex = True).replace(',', '', regex = True) \
                                                        .astype('float') * 1000000).astype('str')
                df.loc[df[col].str.contains('k'), col] = (df[col][df[col].str.contains('k', case=True)] \
                                                        .replace('k', '', regex = True).replace(',', '', regex = True) \
                                                        .astype('float') * 1000).astype('str')
                df.loc[df[col].str.contains('%'), col] = (df[col][df[col].str.contains('%', case=True)] \
                                                        .replace('%', '', regex = True).replace(',', '', regex = True) \
                                                        .astype('float') / 100).astype('str')
            except:
                continue
        df.columns = [ col.replace(' ', '_').replace('/','_').replace('.', '').replace(',', '').replace('&', 'and').lower() for col in df.columns ]
        return self._col_to_float( df )


    def income_statement(self, freq = 'annual'):
        '''

        '''
        return self._download('income', freq)


    def balance_sheet(self, freq = 'annual'):
        '''

        '''
        return self._download('balance-sheet', freq)


    def cashflow_statement(self, freq = 'annual'):
        '''

        '''
        return self._download('cash-flow', freq)

    def statements(self, freq = 'annual'):
        '''

        '''
        income_statement = self.mwatch_income_statement(freq)
        balance_sheet = self.mwatch_balance_sheet(freq)
        cashflow_statement = self.mwatch_cashflow_statement(freq)
        return income_statement, balance_sheet, cashflow_statement