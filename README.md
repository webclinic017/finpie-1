[![Run tests](https://github.com/peterlacour/finpie/actions/workflows/tests.yml/badge.svg)](https://github.com/peterlacour/finpie/actions/workflows/tests.yml) [![PyPi](https://img.shields.io/pypi/v/finpie)](https://pypi.org/project/finpie/) [![Status](https://img.shields.io/badge/status-work%20in%20progress-yellow)]()

# finpie - a simple library to download some financial data

<p><b>For recreational and educational purposes. Creating easier access to some financial and news data.</b></p>

<p>This library is an ongoing project designed to facilitate access to financial and economic data. It tries to cover potentially useful or interesting data points but unfortunately some functions will only return single point data which however could be aggregated over time to construct a limited time series. On the other hand, some functions that retrieve large amounts of data or depending on the data source will take some time to run. See the <a href="#A3">function index </a> for more information on issues of data availability and relative run time.</p>

<p>The company fundamentals module includes functions to retrive data from <code>Yahoo Finance</code>, <code>MarketWatch</code>, <code>The Motley Fool</code>, <code>Finviz</code> and <code>Macrotrends</code>. The price data module retrieves data from <code>Yahoo Finance</code> and <code>CBOE</code>. The news module enables historical news headline collection from the <code>FT</code>, <code>NYT</code>, <code>WSJ</code>, <code>Barrons</code> and <code>Seeking Alpha</code> based on keyword searches. The library also provides a f

<p>If there are any issues, ideas or recommendations please feel free to reach out.</p>

<br>

span

## <div id="0">Documentation</div>

<ol>
<li>
<a href = "#A2">Installation</a>
</li>
<li><a href = "#A3">Function index</a></li>
<li>
<a href = "#A4">Company fundamental data</a><ul>
	<li><a href = "#A42">Financial statements</a></li>
	<li><a href = "#A41">Financial ratios and key metrics</a></li>
	<li><a href = "#A43">Earnings and revenue estimates</a></li>
	<li><a href = "#A48">Earnings call transcripts</a></li>
	<li><a href = "#A44">Insider transactions and analyst ratings</a></li>
	<li><a href = "#A46">ESG scores</a></li>
	<li><a href = "#A47">Company profile</a></li>
	</ul>
</li>
<li>
<a href = "#A5">Price data</a><ul>
	<li><a href = "#A51">Stock prices</a></li>
	<li><a href = "#A52">Option prices</a></li>
	<li><a href = "#A53">Futures prices</a></li>
	</ul>

</li>
<li><a href = "#A7">News data</a></li>
<li><a href = "#A8">Other data</a></li>
<li><a href = "#A9">Sources</a></li>
<li><a href = "#A10">License</a></li>
</ol>

## <div id="A2">Installation</div>

```python
$ pip install finpie
```

### Requirements

```
pandas>=1.0.1
selenium>=3.14.0
numpy>=1.18.2
tqdm
dask[complete]
beautifulsoup4
html5lib
xlrd
requests_html
requests
webdriver-manager
dateparser
```

<div align="right"><a href="#0">Back to top</a> </div>

## <div id="A3"> Index </div>


| Output                                                                             | Data Output           |     
| :--------------------------------------------------------------------------------- | :-------------------- | 
| <b>Company Fundamentals</b>                                                        |                       |  
| <b>fd = Fundamentals( ticker, source, freq )</b>                                   |                       |
| <u>Financial statements</u>                                                        |                       |
| <li> <a id='i7' href='#f7'>fd.income\_statement()</a> </li>                        | up to 2005            |
| <li> <a id='i8' href='#f8'>fd.balance\_sheet()</a> </li>                           | up to 2005            |
| <li> <a id='i9' href='#f9'>fd.cashflow\_statement()</a> </li>                      | up to 2005            |
| <u>Financial ratios and key metrics</u>                                            |                       |
| <li> <a id='i102' href='#f102'>fd.ratios()</a> </li>                               | up to 2005            |
| <li> <a id='i2' href='#f2'>fd.key_metrics()</a> </li>                              | Most recent data      |
| <u>Earnings and revenue estimates</u>                                              |                       |
| <li> <a id='i11' href='#f11'>fd.earnings\_estimates()</a> </li>                    | Most recent data      |
| <li> <a id='i12' href='#f12'>fd.earnings\_estimates\_trends()</a> </li>            | Recent trend          |
| <li> <a id='i13' href='#f13'>fd.earnings\_history()</a> </li>                      | 4 quarters            |
| <li> <a id='i14' href='#f14'>fd.revenue\_estimates()</a> </li>                     | Most recent data      |
| <li> <a id='i15' href='#f15'>fd.growth\_estimates()</a> </li>                      | Most recent data      |
| <u>Earnings call transcripts</u>                                                   |                       |
| <li> <a id='i131' href='#f131'>fd.transcripts()</a> </li>                          | up to 2018            |
| <u>Insider transactions and analyst ratings</u>                                    |                       |
| <li> <a id='i16' href='#f16'>fd.insider\_transactions()</a> </li>                  | Most recent data      |
| <li> <a id='i17' href='#f17'>fd.analyst\_ratings()</a> </li>                       | Most recent data      |
| <u>ESG data</u>                                                                    |                       |
| <li> <a id='i18' href='#f18'>fd.esg\_score()</a> </li>                             | Most recent data      |
| <li> <a id='i19' href='#f19'>fd.corporate\_governance\_score()</a> </li>           | Most recent data      |
| <u>Company profile</u>                                                             |                       |
| <li> <a id='i20' href='#f20'>fd.profile()</a> </li>                                | Most recent data      |
| <li> <a id='i21' href='#f21'>fd.executives\_info()</a> </li>                       | Most recent data      |
| <b>Price data</b>                                                                  |                       |
| <li> <a id='i22' href='#f22'>historical\_prices(ticker)</a> </li>                  | Timeseries            |
| <li> <a id='i27' href='#f27'>yahoo\_option\_chain(ticker)</a> </li>                | Most recent data      |
| <li> <a id='i106' href='#f106'>cboe\_option\_chain(ticker)</a> </li>               | Most recent data      |
| <li> <a id='i28' href='#f28'>historical\_futures\_contracts(date\_range)</a> </li> | Timeseries            |
| <li> <a id='i29' href='#f29'>futures\_contracts(date)</a> </li>                    | Any date              |
| <b>News data</b>                                                                   |                       |
| <b>news = NewsData( ticker, keyword_string )</b>                                   |                       |
| <li> <a id='i80' href='#f80'>news.cnbc()</a> </li>                                 | Timeseries            |
| <li> <a id='i81' href='#f81'>news.ft()</a> </li>                                   | Timeseries            |
| <li> <a id='i85' href='#f85'>news.wsj()</a> </li>                                  | Timeseries            |
| <b>Other data</b>                                                                  |                       |
| <li> <a id='i86' href='#f86'>nasdaq\_tickers()</a> </li>                           | List of stock tickers |
| <li> <a id='i87' href='#f87'>global\_tickers()</a> </li>                           | List of stock tickers |
| <li> <a id='i132' href='#f132'>cftc()</a> </li>                                    | Timeseries            |

---

<br>

## <div id="A4"> Company Fundamental data</a>

<div align="right"><a href="#0">Back to top</a> </div>

The functions below enable you to download financial statements, valuation ratios and key financial statistics as well as analyst ratings, insider transactions, ESG scores and company profiles.

The data is pulled from <code>Yahoo Finance</code>, <code>Marketwatch.com</code> , <code>Finviz.com</code> and <code>Macrotrends.com</code>. The macrotrends scrape runs on Selenium and the website might sometimes fail to load. The function may just need to be re-run to work (assuming the ticker is available on the website). As a remedy it might sometimes help to set <code>macrotrends().head = True</code> which will then open a browser window while scraping the data.

```python
import finpie # or import finpie.fundamental_data

# default:
# source = 'macrotrends'
# freq = 'A'
fd = finpie.Fundamentals(ticker, source = 'macrotrends', freq = 'A')

# source options for financial statements and key metrics:
# 'yahoo', 'marketwatch', 'macrotrends'
# freq options:
# 'A', 'Q'

# default key metrics for marketwatch and macrotrends come from Finviz

```

<br>

## <div id="A42"> <li> Financial statements <hr style="border:0.5px solid gray"> </hr> </li> </div>

<div align="right"><a href="#0">Back to top</a> </div>

#### <div id="f7"><i>Fundamentals(ticker, source, freq)<b>.income_statement()</b></i></div>

<ul>
<li>Returns a dataframe with income statements from either Macrotrends.com, Yahoo Finance or Marketwatch. Default source is 'macrotrends'.</li>
<ul>
<li> <i>Class Arguments:</i> </li>
	<ul>
	<li> <code>ticker</code>: valid company ticker</li>
	<li> <code>source</code>: 'yahoo', 'marketwatch', 'macrotrends', default: 'macrotrends' </li>
	<li> <code>freq</code>: 'A' (annual data), 'Q' (quarterly data), default: 'A' </li>
	</ul>
</ul>
</ul>

<br>

<details>
<summary><i> Default Example </i></summary>

```python
fd = finpie.Fundamentals('AAPL', freq = 'A')
fd.income_statement()
```

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>revenue</th>      <th>cost_of_goods_sold</th>      <th>gross_profit</th>      <th>research_and_development_expenses</th>      <th>sganda_expenses</th>      <th>other_operating_income_or_expenses</th>      <th>operating_expenses</th>      <th>operating_income</th>      <th>total_nonoperating_income_to_expense</th>      <th>pretax_income</th>      <th>income_taxes</th>      <th>income_after_taxes</th>      <th>other_income</th>      <th>income_from_continuous_operations</th>      <th>income_from_discontinued_operations</th>      <th>net_income</th>      <th>ebitda</th>      <th>ebit</th>      <th>basic_shares_outstanding</th>      <th>shares_outstanding</th>      <th>basic_eps</th>      <th>eps__earnings_per_share</th>    </tr>    <tr>      <th>date</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>2005-09-30</th>      <td>13931.0</td>      <td>9889.0</td>      <td>4042.0</td>      <td>535.0</td>      <td>1864.0</td>      <td>NaN</td>      <td>12288.0</td>      <td>1643.0</td>      <td>165.0</td>      <td>1808.0</td>      <td>480.0</td>      <td>1328.0</td>      <td>NaN</td>      <td>1328.0</td>      <td>NaN</td>      <td>1328.0</td>      <td>1822.0</td>      <td>1643.0</td>      <td>22636.0</td>      <td>23993.0</td>      <td>0.06</td>      <td>0.06</td>    </tr>    <tr>      <th>2006-09-30</th>      <td>19315.0</td>      <td>13717.0</td>      <td>5598.0</td>      <td>712.0</td>      <td>2433.0</td>      <td>NaN</td>      <td>16862.0</td>      <td>2453.0</td>      <td>365.0</td>      <td>2818.0</td>      <td>829.0</td>      <td>1989.0</td>      <td>NaN</td>      <td>1989.0</td>      <td>NaN</td>      <td>1989.0</td>      <td>2678.0</td>      <td>2453.0</td>      <td>23634.0</td>      <td>24571.0</td>      <td>0.08</td>      <td>0.08</td>    </tr>    <tr>      <th>2007-09-30</th>      <td>24578.0</td>      <td>16426.0</td>      <td>8152.0</td>      <td>782.0</td>      <td>2963.0</td>      <td>NaN</td>      <td>20171.0</td>      <td>4407.0</td>      <td>599.0</td>      <td>5006.0</td>      <td>1511.0</td>      <td>3495.0</td>      <td>NaN</td>      <td>3495.0</td>      <td>NaN</td>      <td>3495.0</td>      <td>4734.0</td>      <td>4407.0</td>      <td>24209.0</td>      <td>24900.0</td>      <td>0.14</td>      <td>0.14</td>    </tr>    <tr>      <th>2008-09-30</th>      <td>37491.0</td>      <td>24294.0</td>      <td>13197.0</td>      <td>1109.0</td>      <td>3761.0</td>      <td>NaN</td>      <td>29164.0</td>      <td>8327.0</td>      <td>620.0</td>      <td>8947.0</td>      <td>2828.0</td>      <td>6119.0</td>      <td>NaN</td>      <td>6119.0</td>      <td>NaN</td>      <td>6119.0</td>      <td>8823.0</td>      <td>8327.0</td>      <td>24685.0</td>      <td>25260.0</td>      <td>0.25</td>      <td>0.24</td>    </tr>    <tr>      <th>2009-09-30</th>      <td>42905.0</td>      <td>25683.0</td>      <td>17222.0</td>      <td>1333.0</td>      <td>4149.0</td>      <td>NaN</td>      <td>31165.0</td>      <td>11740.0</td>      <td>326.0</td>      <td>12066.0</td>      <td>3831.0</td>      <td>8235.0</td>      <td>NaN</td>      <td>8235.0</td>      <td>NaN</td>      <td>8235.0</td>      <td>12474.0</td>      <td>11740.0</td>      <td>25004.0</td>      <td>25396.0</td>      <td>0.33</td>      <td>0.32</td>    </tr>  </tbody></table>

</details>

<details>
<summary><i> Yahoo Example </i></summary>

```python
fd = finpie.Fundamentals('AAPL', source = 'yahoo') # no frequency choice for Yahoo...
fd.income_statement()
```

<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th>total_revenue</th>      <th>cost_of_revenue</th>      <th>gross_profit</th>      <th>operating_expense</th>      <th>operating_income</th>      <th>net_non_operating_interest_income_expense</th>      <th>other_income_expense</th>      <th>pretax_income</th>      <th>tax_provision</th>      <th>net_income_common_stockholders</th>      <th>diluted_ni_available_to_com_stockholders</th>      <th>basic_eps</th>      <th>diluted_eps</th>      <th>basic_average_shares</th>      <th>diluted_average_shares</th>      <th>total_operating_income_as_reported</th>      <th>total_expenses</th>      <th>net_income_from_continuing_and_discontinued_operation</th>      <th>normalized_income</th>      <th>interest_income</th>      <th>interest_expense</th>      <th>net_interest_income</th>      <th>ebit</th>      <th>ebitda</th>      <th>reconciled_cost_of_revenue</th>      <th>reconciled_depreciation</th>      <th>net_income_from_continuing_operation_net_minority_interest</th>      <th>normalized_ebitda</th>      <th>tax_rate_for_calcs</th>      <th>tax_effect_of_unusual_items</th>      <th>ticker</th>    </tr>    <tr>      <th>date</th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>2019-09-30</th>      <td>260174000</td>      <td>161782000</td>      <td>98392000</td>      <td>34462000</td>      <td>63930000</td>      <td>1385000</td>      <td>422000</td>      <td>65737000</td>      <td>10481000</td>      <td>55256000</td>      <td>55256000</td>      <td>0.003</td>      <td>0.003</td>      <td>18471336</td>      <td>18595652</td>      <td>63930000</td>      <td>196244000</td>      <td>55256000</td>      <td>55256000</td>      <td>4961000</td>      <td>3576000</td>      <td>1385000</td>      <td>69313000</td>      <td>NaN</td>      <td>161782000</td>      <td>12547000</td>      <td>55256000</td>      <td>81860000</td>      <td>0</td>      <td>0</td>      <td>AAPL</td>    </tr>    <tr>      <th>2018-09-30</th>      <td>265595000</td>      <td>163756000</td>      <td>101839000</td>      <td>30941000</td>      <td>70898000</td>      <td>2446000</td>      <td>-441000</td>      <td>72903000</td>      <td>13372000</td>      <td>59531000</td>      <td>59531000</td>      <td>0.003</td>      <td>0.003</td>      <td>19821508</td>      <td>20000436</td>      <td>70898000</td>      <td>194697000</td>      <td>59531000</td>      <td>59531000</td>      <td>5686000</td>      <td>3240000</td>      <td>2446000</td>      <td>76143000</td>      <td>NaN</td>      <td>163756000</td>      <td>10903000</td>      <td>59531000</td>      <td>87046000</td>      <td>0</td>      <td>0</td>      <td>AAPL</td>    </tr>    <tr>      <th>2017-09-30</th>      <td>229234000</td>      <td>141048000</td>      <td>88186000</td>      <td>26842000</td>      <td>61344000</td>      <td>2878000</td>      <td>-133000</td>      <td>64089000</td>      <td>15738000</td>      <td>48351000</td>      <td>48351000</td>      <td>0.0023</td>      <td>0.0023</td>      <td>20868968</td>      <td>21006768</td>      <td>61344000</td>      <td>167890000</td>      <td>48351000</td>      <td>48351000</td>      <td>5201000</td>      <td>2323000</td>      <td>2878000</td>      <td>66412000</td>      <td>NaN</td>      <td>141048000</td>      <td>10157000</td>      <td>48351000</td>      <td>76569000</td>      <td>0</td>      <td>0</td>      <td>AAPL</td>    </tr>  </tbody></table>

</details>

<details>
<summary><i> Marketwatch Example </i></summary>

```python
fd = Fundamentals('AAPL', source = 'marketwatch', freq = 'Q')
fd.income_statement()
```

<center><small><small>

<small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small>


---

#### 
<small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="f8"></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>Fundamentals(ticker, source, freq).balance<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>sheet()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small>


```pythonfd = Fundamentals('AAPL', freq = 'A')
fd.balance_sheet()
``````pythonfd = Fundamentals('AAPL', source = 'yahoo') # no frequency choice for Yahoo...
fd.balance_sheet()
``````pythonfd = Fundamentals('AAPL', source = 'marketwatch', freq = 'Q')
fd.balance_sheet()
```
<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="f9"></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>Fundamentals(ticker, source, freq).cashflow<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>statement()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonfd = Fundamentals('AAPL', freq = 'A')
fd.cashflow_statement()
``````pythonfd = Fundamentals('AAPL', source = 'yahoo') # no frequency choice for Yahoo...
fd.cashflow_statement()
``````pythonfd = Fundamentals('AAPL', source = 'marketwatch', freq = 'Q')
fd.cashflow_statement()
```
<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="A41"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><li></code></span>Financial ratios and key metrics <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><hr style="border:0.5px solid gray"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></hr></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></li></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="f102"></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>Fundamentals(ticker, source, freq).ratios()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonfd = Fundamentals('AAPL', freq = 'A')
fd.ratios()
```
<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="f2"></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>Fundamentals(ticker, source, freq).key<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>metrics()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonfd = Fundamentals('AAPL')
fd.key_metrics()
```

|   | index       |  market_cap |    income |      sales | book\_to\_sh |  .. |
| -: | :---------- | ----------: | --------: | ---------: | -----------: | --: |
| 0 | DJIA S&P500 | 1.94097e+12 | 5.842e+10 | 2.7386e+11 |         4.19 | ... |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

```pythonfd = Fundamentals('AAPL', source = 'yahoo')
fd.key_metrics()
```

|   | payout\_ratio | profit\_margin | operating\_margin\_(ttm) | return\_on\_assets\_(ttm) | return\_on\_equity\_(ttm) | ... |
| -: | ------------: | -------------: | -----------------------: | ------------------------: | ------------------------: | --: |
| 0 |        0.2373 |         0.2133 |                   0.2452 |                    0.1312 |                    0.6925 | ... |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="A43"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><li></code></span>Earnings and revenue estimates<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><hr style="border:0.5px solid gray"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></hr></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></li></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f11" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>Fundamentals( ticker, source, freq ).earnings<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>estimates()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonfd = Fundamentals('AAPL')
fd.earnings_estimates('AAPL')
```

|   | date                    | no\_of\_analysts | avg\_estimate | low\_estimate | high\_estimate | year\_ago\_eps |
| -: | :---------------------- | ---------------: | ------------: | ------------: | -------------: | -------------: |
| 1 | Current Qtr. (Sep 2020) |               28 |           2.8 |          2.18 |           3.19 |           3.03 |
| 2 | Next Qtr. (Dec 2020)    |               24 |          5.45 |          4.76 |           6.82 |           4.99 |
| 3 | Current Year (2020)     |               35 |         12.97 |         12.36 |          13.52 |          11.89 |
| 4 | Next Year (2021)        |               35 |         15.52 |         12.67 |             18 |          12.97 |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f12" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span> Fundamentals( ticker, source, freq ).earnings<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>estimate<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>trends()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonfd = Fundamentals('AAPL')
fd.earnings_estimate_trends()
```

|   | date                    | current\_estimate | 7\_days\_ago | 30\_days\_ago | 60\_days\_ago | 90\_days\_ago |
| -: | :---------------------- | ----------------: | -----------: | ------------: | ------------: | ------------: |
| 1 | Current Qtr. (Sep 2020) |               2.8 |         2.84 |          2.79 |          2.82 |           2.8 |
| 2 | Next Qtr. (Dec 2020)    |              5.45 |         5.44 |          5.22 |          5.21 |          5.22 |
| 3 | Current Year (2020)     |             12.97 |           13 |         12.41 |         12.39 |         12.32 |
| 4 | Next Year (2021)        |             15.52 |        15.54 |         14.94 |         14.86 |         14.73 |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f13" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span> Fundamentals( ticker, source, freq ).earnings<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>history()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonfd = Fundamentals('AAPL')
fd.earnings_history()
```

|   | date       | eps\_est | eps\_actual | difference | surprise\_% |
| -: | :--------- | -------: | ----------: | ---------: | ----------: |
| 1 | 9/29/2019  |     2.84 |        3.03 |       0.19 |       0.067 |
| 2 | 12/30/2019 |     4.55 |        4.99 |       0.44 |       0.097 |
| 3 | 3/30/2020  |     2.26 |        2.55 |       0.29 |       0.128 |
| 4 | 6/29/2020  |     2.04 |        2.58 |       0.54 |       0.265 |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f14" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span> Fundamentals(ticker, source, freq).revenue<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>estimates()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonfd = Fundamentals('AAPL')
fd.revenue_estimates()
```

|   | date                    | no\_of\_analysts | avg\_estimate | low\_estimate | high\_estimate | year\_ago\_sales | sales\_growth\_(yearest) |
| -: | :---------------------- | ---------------: | ------------: | ------------: | -------------: | ---------------: | -----------------------: |
| 1 | Current Qtr. (Sep 2020) |               26 |     6.351e+10 |     5.255e+10 |       6.85e+10 |        6.404e+10 |                   -0.008 |
| 2 | Next Qtr. (Dec 2020)    |               24 |    1.0036e+11 |     8.992e+10 |      1.157e+11 |         8.85e+10 |                    0.134 |
| 3 | Current Year (2020)     |               33 |    2.7338e+11 |    2.6236e+11 |     2.8089e+11 |       2.6017e+11 |                    0.051 |
| 4 | Next Year (2021)        |               33 |    3.0734e+11 |    2.7268e+11 |     3.3153e+11 |       2.7338e+11 |                    0.124 |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f15" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span> Fundamentals( ticker, source, freq ).growth<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>estimates()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonfd = Fundamentals('AAPL')
fd.growth_estimates()
```
<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span> Output <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span></small></small></small>


|                              |   aapl | industry | sector(s) | sandp_500 |
| :--------------------------- | -----: | -------: | --------: | --------: |
| Current\_Qtr.                | -0.079 |      nan |       nan |       nan |
| Next\_Qtr.                   |  0.088 |      nan |       nan |       nan |
| Current_Year                 |  0.088 |      nan |       nan |       nan |
| Next_Year                    |  0.195 |      nan |       nan |       nan |
| Next\_5\_Years\_(per\_annum) | 0.1246 |      nan |       nan |       nan |
| Past\_5\_Years\_(per\_annum) | 0.0842 |      nan |       nan |       nan |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="A48"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><li></code></span>Earnings Call Transcripts<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><hr style="border:0.5px solid gray"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></hr></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></li></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

<small><small><small>The earnings call transcripts are collected from <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><a href="https://www.fool.com/"></code></span>The Motley Fool<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></a></code></span> and are available until Q1 2018. The data returns a simple breakdown of the sections of the earnings call which will still need to be processed further. The full html of the call is also available.</small></small></small>

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f131" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span> Fundamentals( ticker, source, freq ).transcripts(html = True)<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonfd = Fundamentals('AAPL')
fd.transcripts(html = True)
```---

### 
<small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="A44"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><li></code></span>Insider transactions and analyst ratings <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><hr style="border:0.5px solid gray"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></hr></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></li></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small>

#### 
<small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f16" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span> Fundamentals( ticker, source, freq ).insider<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>transactions()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small>

```pythonfd = Fundamentals('AAPL')
fd.insider_transactions()
```

|     | insider_trading | relationship                 | date   | transaction     |   cost | #shares | value\_($) | #shares\_total | sec\_form\_4    |
| --: | :-------------- | :--------------------------- | :----- | :-------------- | -----: | ------: | ---------: | -------------: | :-------------- |
|   0 | COOK TIMOTHY D  | Chief Executive Officer      | Aug 25 | Sale            | 496.91 |  265160 |  131761779 |         837374 | Aug 25 06:45 PM |
|   1 | KONDO CHRIS     | Principal Accounting Officer | May 08 | Sale            | 305.62 |    4491 |    1372539 |           7370 | May 12 06:30 PM |
|   2 | JUNG ANDREA     | Director                     | Apr 28 | Option Exercise |  48.95 |    9590 |     469389 |          33548 | Apr 30 09:30 PM |
|   3 | O'BRIEN DEIRDRE | Senior Vice President        | Apr 16 | Sale            | 285.12 |    9137 |    2605141 |          33972 | Apr 17 06:31 PM |
|   4 | Maestri Luca    | Senior Vice President, CFO   | Apr 07 | Sale            | 264.44 |   41062 |   10858445 |          27568 | Apr 09 06:30 PM |
| ... | ...             | ...                          | ...    | ...             |    ... |     ... |        ... |            ... | ...             |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f17" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span> Fundamentals( ticker, source, freq ).analyst<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>ratings()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonfd = Fundamentals('AAPL')
fd.analyst_ratings()
```
<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span> Output <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span></small></small></small>


| date                | action     | rating_institution     | rating     | price_target    |
| :------------------ | :--------- | :--------------------- | :--------- | :-------------- |
| 2020-09-01 00:00:00 | Reiterated | JP Morgan              | Overweight | $115 → $150    |
| 2020-09-01 00:00:00 | Reiterated | Cowen                  | Outperform | $530 → $133    |
| 2020-08-31 00:00:00 | Reiterated | Monness Crespi & Hardt | Buy        | $117.50 → $144 |
| 2020-08-26 00:00:00 | Reiterated | Wedbush                | Outperform | $515 → $600    |
| 2020-08-25 00:00:00 | Reiterated | Cowen                  | Outperform | $470 → $530    |
| ...                 | ...        | ...                    | ...        | ...             |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="A46"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><li></code></span> ESG scores<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><hr style="border:0.5px solid gray"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></hr></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></li></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f18" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>Fundamentals( ticker, source, freq ).esg<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>score()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonfd = Fundamentals('AAPL')
fd.esg_score()
```

|   | date       | total\_esg\_risk_score | risk\_category | risk\_percentile | environment\_risk_score | social\_risk\_score | ... |
| -: | :--------- | ---------------------: | :------------- | :--------------- | ----------------------: | ------------------: | --: |
| 0 | 2020-08-25 |                     24 | Medium         | 33rd             |                     0.5 |                  13 | ... |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f19" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>Fundamentals( ticker, source, freq ).corporate<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>governance<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>score()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonfd = Fundamentals('AAPL')
fd.corporate_governance_score()
```
<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span> Output <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span></small></small></small>


|   | audit | board | shareholder\_rights | compensation | quality\_score | ticker | date       |
| -: | ----: | ----: | ------------------: | -----------: | -------------: | :----- | :--------- |
| 0 |     1 |     1 |                   1 |            3 |              1 | AAPL   | 2020-08-25 |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="A47"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><li></code></span>Company info<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><hr style="border:0.5px solid gray"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></hr></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></li></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f20" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>Fundamentals( ticker, source, freq ).profile()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonfd = Fundamentals('AAPL')
fd.profile()
```

|   | company\_name | sector     | industry             | number\_of\_employees | description                                                                                                                     | ticker |
| -: | :------------ | :--------- | :------------------- | --------------------: | :------------------------------------------------------------------------------------------------------------------------------ | :----- |
| 0 | Apple Inc.    | Technology | Consumer Electronics |                137000 | Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide... | AAPL   |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f21" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>Fundamentals( ticker, source, freq ).executives_info()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonfd = Fundamentals('AAPL')
fd.executives_info()
```

|   | name                    | title                       |       pay | exercised | year\_born | gender | age\_at\_end\_of\_year |
| -: | :---------------------- | :-------------------------- | --------: | --------: | ---------: | :----- | ---------------------: |
| 0 | Mr. Timothy D. Cook     | CEO & Director              | 1.156e+07 |       nan |       1961 | male   |                     59 |
| 1 | Mr. Luca Maestri        | CFO & Sr. VP                |  3.58e+06 |       nan |       1964 | male   |                     56 |
| 2 | Mr. Jeffrey E. Williams | Chief Operating Officer     |  3.57e+06 |       nan |       1964 | male   |                     56 |
| 3 | Ms. Katherine L. Adams  | Sr. VP, Gen. Counsel & Sec. |   3.6e+06 |       nan |       1964 | female |                     56 |
| 4 | Ms. Deirdre O'Brien     | Sr. VP of People & Retail   |  2.69e+06 |       nan |       1967 | female |                     53 |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

## 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">## </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="A5"></code></span> Price data <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

<small><small><small>The functions below help to retrieve daily historical price data from <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><code></code></span>Yahoo Finance<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></code></code></span> as well as most recent option prices from Yahoo Finance or CBOE.</small></small></small>

<small><small><small>Furthermore, the <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><code></code></span>historical<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>futures<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>contracts<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></code></code></span> function enables a bulk download of historical monthly futures contracts up to the year 2000 for currencies, indices, interest rates and commodities including energy, metals and agricultural contracts. The data is downloaded from <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><a href = "www.mrci.com"></code></span>www.mrci.com<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></a></code></span> but the data is not completely cleaned (yet).</small></small></small>

```pythonimport finpie.price_data

# Historical price data from Yahoo Finance, most recent option prices from Yahoo Finance and CBOE, and futures prices bulk-download...
# from finpie.price_data import price_data
import finpie
```### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="A51"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><li></code></span> Stock and ETF prices <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><hr style="border:0.5px solid gray"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></hr></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></li></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="f22"></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>historical_prices( ticker )<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonhistorical_prices('AAPL')
```

|     | Date       |    Open |    High |     Low |   Close | Adj Close |  Volume |
| --: | :--------- | ------: | ------: | ------: | ------: | --------: | ------: |
|   0 | 1993-01-29 | 43.9688 | 43.9688 |   43.75 | 43.9375 |   26.1841 | 1003200 |
|   1 | 1993-02-01 | 43.9688 |   44.25 | 43.9688 |   44.25 |   26.3703 |  480500 |
|   2 | 1993-02-02 | 44.2188 |  44.375 |  44.125 | 44.3438 |   26.4262 |  201300 |
|   3 | 1993-02-03 | 44.4062 | 44.8438 |  44.375 | 44.8125 |   26.7055 |  529400 |
|   4 | 1993-02-04 | 44.9688 | 45.0938 | 44.4688 |      45 |   26.8172 |  531500 |
| ... | ...        |     ... |     ... |     ... |     ... |       ... |     ... |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="A52"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><li></code></span> Option prices <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><hr style="border:0.5px solid gray"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></hr></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></li></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="f27"></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>yahoo<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>option_chain( ticker )<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythoncalls, puts = yahoo_option_chain('AAPL')
```
<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>Call options chain<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span></small></small></small>


|     | contract_name       | last\_trade\_date      | strike | last\_price | ... |
| --: | :------------------ | :--------------------- | -----: | ----------: | --: |
|   0 | AAPL200828C00190000 | 2020-08-25 3:40PM EDT  |    190 |      310.29 | ... |
|   1 | AAPL200828C00195000 | 2020-08-25 12:36PM EDT |    195 |       300.7 | ... |
|   2 | AAPL200828C00200000 | 2020-08-25 12:13PM EDT |    200 |       294.8 | ... |
|   3 | AAPL200828C00205000 | 2020-08-06 3:07PM EDT  |    205 |      249.54 | ... |
| ... | ...                 | ...                    |    ... |         ... | ... |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>Put options chain<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span></small></small></small>


|     | contract_name       | last_trade_date        | strike | last_price | bid |
| --: | :------------------ | :--------------------- | -----: | ---------: | --: |
|   0 | AAPL200828P00190000 | 2020-08-24 2:05PM EDT  |    190 |       0.01 | ... |
|   1 | AAPL200828P00195000 | 2020-08-10 10:38AM EDT |    195 |       0.02 | ... |
|   2 | AAPL200828P00200000 | 2020-08-24 1:36PM EDT  |    200 |       0.01 | ... |
|   3 | AAPL200828P00205000 | 2020-08-24 10:08AM EDT |    205 |       0.02 | ... |
| ... | ...                 | ...                    |    ... |        ... | ... |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="f106"></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>cboe<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>option_chain( ticker, head = False )<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythoncalls, puts = cboe_option_chain('AAPL')
```
<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>Call options chain<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span></small></small></small>


|     | expiration | calls               | last_sale |    net |   bid |   ask | vol |   iv |  delta |  gamma | open_int | strike | underlying |
| --: | :--------- | :------------------ | --------: | -----: | ----: | ----: | --: | ---: | -----: | -----: | -------: | -----: | ---------: |
|   0 | 09/25/2020 | AAPL200925C00058750 |     46.75 | -2.375 |  50.1 | 52.65 |  15 | 0.02 |      1 | 0.0002 |        0 |  58.75 |     110.13 |
|   1 | 09/25/2020 | AAPL200925C00060000 |      49.2 |  1.325 | 48.85 |  51.4 |  33 | 0.02 |      1 | 0.0001 |       38 |     60 |     110.13 |
|   2 | 09/25/2020 | AAPL200925C00061250 |      49.3 |      0 |  47.6 |  50.2 |   0 | 0.02 |      1 | 0.0002 |        0 |  61.25 |     110.13 |
|   3 | 09/25/2020 | AAPL200925C00062500 |      43.1 |   -2.3 |  47.2 | 48.05 |   2 | 0.02 | 0.9989 | 0.0002 |        6 |   62.5 |     110.13 |
| ... | ...        | ...                 |       ... |    ... |   ... |   ... | ... |  ... |    ... |    ... |      ... |    ... |        ... |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>Put options chain<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span></small></small></small>


|     | expiration | puts                | last_sale |    net | bid |  ask | vol |     iv |   delta |  gamma | open_int | strike | underlying |
| --: | :--------- | :------------------ | --------: | -----: | --: | ---: | --: | -----: | ------: | -----: | -------: | -----: | ---------: |
|   0 | 09/25/2020 | AAPL200925P00058750 |      0.06 |      0 |   0 | 0.01 |   0 |  2.001 |  -0.001 | 0.0001 |       76 |  58.75 |     110.13 |
|   1 | 09/25/2020 | AAPL200925P00060000 |      0.01 |      0 |   0 | 0.01 |   0 |  1.876 | -0.0008 | 0.0001 |      505 |     60 |     110.13 |
|   2 | 09/25/2020 | AAPL200925P00061250 |      0.03 |      0 |   0 | 0.01 |   0 | 1.8406 | -0.0009 | 0.0001 |       17 |  61.25 |     110.13 |
|   3 | 09/25/2020 | AAPL200925P00062500 |      0.01 | -0.005 |   0 | 0.03 |  10 | 1.8178 | -0.0011 | 0.0002 |      123 |   62.5 |     110.13 |
| ... | ...        | ...                 |       ... |    ... | ... |  ... | ... |    ... |     ... |    ... |      ... |    ... |        ... |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="A53"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><li></code></span> Futures prices <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><hr style="border:0.5px solid gray"></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></hr></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></li></code></span> <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="f28"></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>historical<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>futures<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>contracts( pandas.date_range )<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonhistorical_futures_contracts( pd.date_range('2020-01-01', '2020-09-01') )
```

|            | month |   date |  open |  high |   low | close | change | volume | open_interest | change_in_oi | future             |
| :--------- | :---- | -----: | ----: | ----: | ----: | ----: | -----: | -----: | ------------: | :----------- | :----------------- |
| 2020-01-06 | Jan20 | 200106 | 296.2 | 299.4 | 296.2 | 297.7 |    1.6 |   4103 |          2459 | -811         | Soybean Meal(CBOT) |
| 2020-01-06 | Mar20 | 200106 | 301.5 | 304.5 | 300.6 | 302.9 |    1.7 |  58930 |        222007 | 3,678        | Soybean Meal(CBOT) |
| 2020-01-06 | May20 | 200106 | 305.3 | 308.3 | 304.6 | 306.9 |    1.7 |  23500 |         92983 | 2,616        | Soybean Meal(CBOT) |
| ...        | ...   |    ... |   ... |   ... |   ... |   ... |    ... |    ... |           ... | ...          | ...                |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="f29"></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>futures<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>contracts( date )<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonfutures_prices('2020-01-06')
```

|            | month |   date |  open |  high |   low | close | change | volume | open_interest | change_in_oi | future             |
| :--------- | :---- | -----: | ----: | ----: | ----: | ----: | -----: | -----: | ------------: | :----------- | :----------------- |
| 2020-01-06 | Jan20 | 200106 | 296.2 | 299.4 | 296.2 | 297.7 |    1.6 |   4103 |          2459 | -811         | Soybean Meal(CBOT) |
| 2020-01-06 | Mar20 | 200106 | 301.5 | 304.5 | 300.6 | 302.9 |    1.7 |  58930 |        222007 | 3,678        | Soybean Meal(CBOT) |
| 2020-01-06 | May20 | 200106 | 305.3 | 308.3 | 304.6 | 306.9 |    1.7 |  23500 |         92983 | 2,616        | Soybean Meal(CBOT) |
| ...        | ...   |    ... |   ... |   ... |   ... |   ... |    ... |    ... |           ... | ...          | ...                |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

## 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">## </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="A7"></code></span>News data<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

<small><small><small>The functions below retrieve news headlines based on keyword searches from <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><code></code></span>Barrons<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></code></code></span>, <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><code></code></span>CNBC<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></code></code></span>, the <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><code></code></span>Financial Times<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></code></code></span>, the <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><code></code></span>New York Times<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></code></code></span>, <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><code></code></span>Reuters<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></code></code></span>, <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><code></code></span>Seeking Alpha<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></code></code></span> and the <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><code></code></span>Wall Street Journal<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></code></code></span>. The keyword for Seeking Alpha is simply the relevant stock ticker.</small></small></small>

<small><small><small>The scrape is based on Selenium and may not be very stable if the website layouts change.</small></small></small>

<small><small><small>Furthermore, some of the functions can run for a long-time so it is recommended to use a reasonable <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><code></code></span>datestop<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></code></code></span> value.</small></small></small>

<small><small><small>Some downloads may fail occasionally as access to the website could be blocked.</small></small></small>

```python# Importing the NewsData class
from finpie import NewsData #
news = NewsData('XOM', 'exxon mobil')
news.head = False # default = false, ensures selenium headless mode
news.verbose = True # default = False, prints total number of collected articles
```---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f78" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>NewsData(ticker, keywords).barrons()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```python# retrieve news article for a given search term
news = NewsData('XOM', 'exxon mobil')
df = news.barrons(datestop = '2020-06-01')
# filter news headlines with a keyword list
news.filterz = [ 'exxon', 'mobil', 'oil', 'energy' ]
df = news.filter_data(df)
```

| date       | link                                                                                                           | headline                                                           | description                                                                                                                                                                                           | newspaper   | author                  | date_retrieved             | ticker | comments | tag | search_term | id                                                                                                                                                                                          | source  |
| :--------- | :------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------- | :---------------------- | :------------------------- | :----- | -------: | --: | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------ |
| 15/09/2020 | https://www.barrons.com/articles/options-traders-are-pricing-in-an-exxon-dividend-cut-analyst-says-51600181938 | Options Traders Are Pricing In an Exxon Dividend Cut, Analyst Says | Whether Exxon can maintain its dividend is one of the most active debates right now among energy investors. The company has a strong incentive to keep making payments at current levels.             | Barrons.com | Avi Salzman             | 2020-09-16 13:35:26.574289 | XOM    |      nan | nan | exxon mobil | Barrons.comOptions Traders Are Pricing In an Exxon Dividend Cut, Analyst Sayshttps://www.barrons.com/articles/options-traders-are-pricing-in-an-exxon-dividend-cut-analyst-says-51600181938 | barrons |
| 13/09/2020 | https://www.wsj.com/articles/exxon-used-to-be-americas-most-valuable-company-what-happened-oil-gas-11600037243 | Exxon Used to Be America’s Most Valuable Company. What Happened?  | The oil giant doubled down on oil and gas at what now looks to be the worst possible time. Investors are fleeing and workers are grumbling about the direction of a company some see as out of touch. | WSJ.com     | Christopher M. Matthews | 2020-09-16 13:35:26.574289 | XOM    |      nan | nan | exxon mobil | WSJ.comExxon Used to Be America’s Most Valuable Company. What Happened?https://www.wsj.com/articles/exxon-used-to-be-americas-most-valuable-company-what-happened-oil-gas-11600037243      | barrons |
| 11/09/2020 | https://www.barrons.com/articles/where-to-find-bargains-in-oil-stocks-51599837910                              | Where to Find Bargains in Oil Stocks Now                           | Goldman Sachs analyst likes certain refiners and Canadian oil companies.                                                                                                                              | Barrons.com | Avi Salzman             | 2020-09-16 13:35:26.574289 | XOM    |      nan | nan | exxon mobil | Barrons.comWhere to Find Bargains in Oil Stocks Nowhttps://www.barrons.com/articles/where-to-find-bargains-in-oil-stocks-51599837910                                                        | barrons |
| ...        | ...                                                                                                            | ...                                                                | ...                                                                                                                                                                                                   | ...         | ...                     | ...                        | ...    |      ... | ... | ...         | ...                                                                                                                                                                                         | ...     |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f80" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>NewsData(ticker, keywords).cnbc()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```python# retrieve news article for a given search term
news = NewsData('XOM', 'exxon mobil')
df = news.cnbc(datestop = '2020-06-01')
# filter news headlines with a keyword list
news.filterz = [ 'exxon', 'mobil', 'oil', 'energy' ]
df = news.filter_data(df)
```

| date                | link                                                                                                                              | headline                                                            | description                                                                                                                                                               | tag             | author       | date_retrieved             | ticker | comments | newspaper | search_term | id                                                                                                                                                                                                       | source |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------- | :----------- | :------------------------- | :----- | -------: | :-------- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----- |
| 2020-09-10 00:00:00 | https://www.cnbc.com/video/2020/09/10/honeywell-ceo-darius-adamczyk-on-rejoining-the-dow.html?&qsearchterm=exxon mobil            | Honeywell CEO Darius Adamczyk on rejoining the Dow                  | S&P Dow Jones Indices said Monday that three new companies will be joining the 30-stock benchmark. Salesforce.com will replace Exxon Mobil, Amgen will replace Pfizer ... | Squawk Box U.S. | nan          | 2020-09-16 14:14:43.533664 | XOM    |      nan | CNBC      | exxon mobil | CNBCHoneywell CEO Darius Adamczyk on rejoining the Dowhttps://www.cnbc.com/video/2020/09/10/honeywell-ceo-darius-adamczyk-on-rejoining-the-dow.html?&qsearchterm=exxon mobil                             | cnbc   |
| 2020-09-09 00:00:00 | https://www.cnbc.com/2020/09/09/options-market-predicts-exxon-mobils-dividend-could-be-in-danger.html?&qsearchterm=exxon mobil    | Options market predicts Exxon Mobil’s dividend could be in danger  | One of the most consistent dividend payers in the history of the energy trade could be in danger of having to slash its payout, according ...                             | Options Action  | Tyler Bailey | 2020-09-16 14:14:43.533664 | XOM    |      nan | CNBC      | exxon mobil | CNBCOptions market predicts Exxon Mobil’s dividend could be in dangerhttps://www.cnbc.com/2020/09/09/options-market-predicts-exxon-mobils-dividend-could-be-in-danger.html?&qsearchterm=exxon mobil     | cnbc   |
| 2020-09-08 00:00:00 | https://www.cnbc.com/2020/09/08/exxon-downsizes-global-empire-as-wall-street-worries-about-dividend.html?&qsearchterm=exxon mobil | Exxon downsizes global empire as Wall Street worries about dividend | Ill-timed bets on rising demand have Exxon Mobil facing a shortfall of about $48 billion through 2021, according to a Reuters tally and Wall Street ...                   | Oil and Gas     | nan          | 2020-09-16 14:14:43.533664 | XOM    |      nan | CNBC      | exxon mobil | CNBCExxon downsizes global empire as Wall Street worries about dividendhttps://www.cnbc.com/2020/09/08/exxon-downsizes-global-empire-as-wall-street-worries-about-dividend.html?&qsearchterm=exxon mobil | cnbc   |
| ...                 | ...                                                                                                                               | ...                                                                 | ...                                                                                                                                                                       | ...             | ...          | ...                        | ...    |      ... | ...       | ...         | ...                                                                                                                                                                                                      | ...    |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f81" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>NewsData(ticker, keywords).ft()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```python# retrieve news article for a given search term
news = NewsData('XOM', 'exxon mobil')
df = news.ft(datestop = '2020-06-01')
# filter news headlines with a keyword list
news.filterz = [ 'exxon', 'mobil', 'oil', 'energy' ]
df = news.filter_data(df)
```

| date                | link                                          | headline                                                         | description                                                                                                                                                                                                                       | tag                  | date_retrieved             | ticker | comments | author | newspaper | search_term | id                                                                                                              | source |
| :------------------ | :-------------------------------------------- | :--------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------- | :------------------------- | :----- | -------: | -----: | :-------- | :---------- | :-------------------------------------------------------------------------------------------------------------- | :----- |
| 2020-07-31 00:00:00 | /content/64d7e86e-079c-4502-a9a4-5ab7439c732f | Big Oil gets smaller as Chevron and Exxon losses mount to $9.4bn | ...destruction in the second quarter was unprecedented in the history of modern oil markets,” Neil Chapman, Exxon senior vice-president, told analysts on an investor call.                  “To put it in context, absolute... | Oil & Gas industry   | 2020-09-16 14:20:31.865540 | XOM    |      nan |    nan | FT        | exxon mobil | FTBig Oil gets smaller as Chevron and Exxon losses mount to $9.4bn/content/64d7e86e-079c-4502-a9a4-5ab7439c732f | ft     |
| 2020-05-27 00:00:00 | /content/c43ead81-5af3-44de-af1e-b108d6491354 | Exxon shareholders vote against splitting chair and CEO roles    | ...Exxon, said the appointment of a lead director had helped improve oversight.                  A separate resolution calling for increased transparency about Exxon’s lobbying activity won 37.5 per cent support, a...        | Oil & Gas industry   | 2020-09-16 14:20:31.865540 | XOM    |      nan |    nan | FT        | exxon mobil | FTExxon shareholders vote against splitting chair and CEO roles/content/c43ead81-5af3-44de-af1e-b108d6491354    | ft     |
| 2020-05-12 00:00:00 | /content/c54ee229-f4e7-43c8-87a5-e383099542fb | Big Exxon shareholder to vote against chief                      | ...company to disclose its lobbying activities, arguing it was falling behind global peers by failing to act on climate change.                  Wednesday’s move by LGIM, whose roughly $1bn stake makes it a top-20 Exxon...   | Corporate governance | 2020-09-16 14:20:31.865540 | XOM    |      nan |    nan | FT        | exxon mobil | FTBig Exxon shareholder to vote against chief/content/c54ee229-f4e7-43c8-87a5-e383099542fb                      | ft     |
| ...                 | ...                                           | ...                                                              | ...                                                                                                                                                                                                                               | ...                  | ...                        | ...    |      ... |    ... | ...       | ...         | ...                                                                                                             | ...    |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f82" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>NewsData(ticker, keywords).nyt()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```python# retrieve news article for a given search term
news = NewsData('XOM', 'exxon mobil')
df = news.nyt(datestop = '2020-06-01')
# filter news headlines with a keyword list
news.filterz = [ 'exxon', 'mobil', 'oil', 'energy' ]
df = news.filter_data(df)
```

| date                | link                                                                                                  | headline                                                                       | description                                                                                                                                                                                                                                                             | tag      | author               | comments | date_retrieved             | ticker | newspaper | search_term | id                                                                                                                                                                                 | source |
| :------------------ | :---------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- | :------------------- | -------: | :------------------------- | :----- | :-------- | :---------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----- |
| 2020-09-08 00:00:00 | /aponline/2020/09/08/business/ap-financial-markets-stocks.html?searchResultPosition=2                 | Exxon, Tesla Fall; Nikola, Beyond Meat Rise                                    | Stocks that moved heavily or traded substantially Tuesday:                                                                                                                                                                                                              | Business | The Associated Press |      nan | 2020-09-16 14:22:13.032245 | XOM    | NYT       | exxon mobil | NYTExxon, Tesla Fall; Nikola, Beyond Meat Rise/aponline/2020/09/08/business/ap-financial-markets-stocks.html?searchResultPosition=2                                                | nyt    |
| 2020-09-08 00:00:00 | /reuters/2020/09/08/business/08reuters-exxon-mobil-spending-exclusive.html?searchResultPosition=3     | Exclusive: Exxon Downsizes Global Empire as Wall Street Worries About Dividend | Ill-timed bets on rising demand have Exxon Mobil Corp facing a shortfall of about $48 billion through 2021, according to a Reuters tally and Wall Street estimates, a situation that will require the top U.S. oil company to make deep cuts to its staff and projects. | Business | Reuters              |      nan | 2020-09-16 14:22:13.032245 | XOM    | NYT       | exxon mobil | NYTExclusive: Exxon Downsizes Global Empire as Wall Street Worries About Dividend/reuters/2020/09/08/business/08reuters-exxon-mobil-spending-exclusive.html?searchResultPosition=3 | nyt    |
| 2020-09-03 00:00:00 | /reuters/2020/09/03/business/03reuters-refinery-operations-exxon-beaumont.html?searchResultPosition=4 | Exxon Beaumont, Texas, Refinery Restarts Large Crude Unit: Sources             | Exxon Mobil Corp restarted the large crude distillation unit (CDU) at its 369,024 barrel-per-day (bpd) Beaumont, Texas, refinery on Thursday, said sources familiar with plant operations.                                                                              | Business | Reuters              |      nan | 2020-09-16 14:22:13.032245 | XOM    | NYT       | exxon mobil | NYTExxon Beaumont, Texas, Refinery Restarts Large Crude Unit: Sources/reuters/2020/09/03/business/03reuters-refinery-operations-exxon-beaumont.html?searchResultPosition=4         | nyt    |
| ...                 | ...                                                                                                   | ...                                                                            | ...                                                                                                                                                                                                                                                                     | ...      | ...                  |      ... | ...                        | ...    | ...       | ...         | ...                                                                                                                                                                                | ...    |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f84" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>NewsData(ticker, keywords).seeking<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>alpha(datestop, press_releases = False)<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```python# retrieve news article for a given search term
news = NewsData('XOM', 'exxon mobil')
df = news.seeking_alpha(datestop = '2020-06-01')
# filter news headlines with a keyword list
news.filterz = [ 'exxon', 'mobil', 'oil', 'energy' ]
df = news.filter_data(df)
```

| date                | link                                                                                                                                                                                                  | headline                                                    | author  | comments   | date_retrieved             | ticker | description | tag | newspaper | search_term | id                                                                                                                                                                                                                                                                        | source       |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------- | :------ | :--------- | :------------------------- | :----- | ----------: | --: | :-------- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------- |
| 2020-09-15 00:00:00 | /news/3614409-options-traders-pricing-in-exxon-dividend-cut-analyst-says?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:1 | Options traders pricing in Exxon dividend cut, analyst says | SA News | 0 comments | 2020-09-16 15:14:23.575898 | XOM    |         nan | nan | SA - News | exxon mobil | SA - NewsOptions traders pricing in Exxon dividend cut, analyst says/news/3614409-options-traders-pricing-in-exxon-dividend-cut-analyst-says?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:1 | sa           |
| 2020-09-14 00:00:00 | /news/3613801-connecticut-latest-state-to-sue-exxon-over-climate-change?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:2  | Connecticut latest state to sue Exxon over climate change   | SA News | 0 comments | 2020-09-16 15:14:23.575898 | XOM    |         nan | nan | SA - News | exxon mobil | SA - NewsConnecticut latest state to sue Exxon over climate change/news/3613801-connecticut-latest-state-to-sue-exxon-over-climate-change?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:2    | sa           |
| 2020-09-10 00:00:00 | /news/3612953-exxon-rated-new-buy-mkm-shares-slip?source=content_type:react\|section:News\|sectionAsset:News\|first\_level\_url:symbol\|button:Author\|lock\_status:No\|line:3                        | Exxon rated new Buy at MKM but shares slip                  | SA News | 0 comments | 2020-09-16 15:14:23.575898 | XOM    |         nan | nan | SA - News | exxon mobil | SA - NewsExxon rated new Buy at MKM but shares slip/news/3612953-exxon-rated-new-buy-mkm-shares-slip?source=content_type:react                                                                                                                                            | section:News |
| ...                 | ...                                                                                                                                                                                                   | ...                                                         | ...     | ...        | ...                        | ...    |         ... | ... | ...       | ...         | ...                                                                                                                                                                                                                                                                       | ...          |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f85" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>NewsData(ticker, keywords).wsj()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```python# retrieve news article for a given search term
news = NewsData('XOM', 'exxon mobil')
df = news.wsj(datestop = '2020-06-01')
# filter news headlines with a keyword list
news.filterz = [ 'exxon', 'mobil', 'oil', 'energy' ]
df = news.filter_data(df)
```

| date                | link                                                                                                                       | headline                                                          | description                                                                                                                                                                                                     | author                  | tag                 | date_retrieved             | ticker | newspaper | search_term | id                                                                                                                                                                                             | comments | source |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------- | :------------------ | :------------------------- | :----- | :-------- | :---------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------: | :----- |
| 2020-09-13 00:00:00 | /articles/exxon-used-to-be-americas-most-valuable-company-what-happened-oil-gas-11600037243?mod=searchresults&page=1&pos=1 | Exxon Used to Be America’s Most Valuable Company. What Happened? | The oil giant doubled down on oil and gas at what now looks to be the worst possible time. Investors are fleeing and workers are grumbling about the direction of a company some see as out of touch.           | Christopher M. Matthews | Business            | 2020-09-16 15:19:39.733511 | XOM    | WSJ       | exxon mobil | WSJExxon Used to Be America’s Most Valuable Company. What Happened?/articles/exxon-used-to-be-americas-most-valuable-company-what-happened-oil-gas-11600037243?mod=searchresults&page=1&pos=1 |      nan | wsj    |
| 2020-09-10 00:00:00 | /articles/oil-major-bp-gives-a-taste-of-how-it-will-go-green-11599745648?mod=searchresults&page=1&pos=2                    | Oil Major BP Gives a Taste of How It Will Go Green                | A deal to buy into wind farms off the coast of New York and Massachusetts showcases the British company’s ambitions in the clean-energy sector—and the risks it is taking.                                    | Rochelle Toplensky      | Heard on the Street | 2020-09-16 15:19:39.733511 | XOM    | WSJ       | exxon mobil | WSJOil Major BP Gives a Taste of How It Will Go Green/articles/oil-major-bp-gives-a-taste-of-how-it-will-go-green-11599745648?mod=searchresults&page=1&pos=2                                   |      nan | wsj    |
| 2020-09-08 00:00:00 | /articles/oil-prices-drop-on-faltering-recovery-in-demand-11599562101?mod=searchresults&page=1&pos=3                       | Oil Prices Tumble on Faltering Recovery in Demand                 | Oil prices slumped to their lowest level in nearly three months, under pressure from a stalling recovery in demand and planned production expansions by OPEC that threaten to add to an existing glut of crude. | Joe Wallace             | Oil Markets         | 2020-09-16 15:19:39.733511 | XOM    | WSJ       | exxon mobil | WSJOil Prices Tumble on Faltering Recovery in Demand/articles/oil-prices-drop-on-faltering-recovery-in-demand-11599562101?mod=searchresults&page=1&pos=3                                       |      nan | wsj    |
| ...                 | ...                                                                                                                        | ...                                                               | ...                                                                                                                                                                                                             | ...                     | ...                 | ...                        | ...    | ...       | ...         | ...                                                                                                                                                                                            |      ... | ...    |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

## 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">## </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="A8"></code></span>Other data<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f86" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>nasdaq<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>tickers()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonnasdaq_tickers()
```

|     | Symbol | Security Name                                                                                    |
| --: | :----- | :----------------------------------------------------------------------------------------------- |
|   0 | AACG   | ATA Creativity Global - American Depositary Shares, each representing two common shares          |
|   1 | AACQ   | Artius Acquisition Inc. - Class A Common Stock                                                   |
|   2 | AACQU  | Artius Acquisition Inc. - Unit consisting of one ordinary share and one third redeemable warrant |
|   3 | AACQW  | Artius Acquisition Inc. - Warrant                                                                |
|   4 | AAL    | American Airlines Group, Inc. - Common Stock                                                     |
| ... | ...    | ...                                                                                              |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f87" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>global<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>tickers()<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythonglobal_tickers()
```

|     | Symbol          | Company                      |
| --: | :-------------- | :--------------------------- |
|   0 | QNCO.Israel     | (Y.Z) Queenco Ltd            |
|   1 | ONE.Canada      | 01 Communique Laboratory Inc |
|   2 | DFK.Germany     | 01 Communique Laboratory Inc |
|   3 | OCQLF           | 01 Communique Laboratory Inc |
|   4 | 01C.Poland      | 01Cyberaton SA               |
|   5 | 1PG.Australia   | 1 Page Ltd                   |
|   6 | I8Y.Germany     | 1 Page Ltd                   |
|   8 | 8458.Taiwan     | 1 Production Film Co         |
|   9 | DRI.Austria     | 1&1 Drillisch AG             |
|  10 | DRI.Switzerland | 1&1 Drillisch AG             |
| ... | ...             | ...                          |

<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

---

#### 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">#### </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id = "f132" ></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><i></code></span>cftc( report_type = 'futures<span data-type="backslash" class="vditor-ir__node"><span class="vditor-ir__marker vditor-ir__marker--bi">\</span>_</span>traders', year = 2000 )<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></i></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

```pythoncftc(report_type = 'futures', year = 2020)
```
<small><small><small><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></small></code></span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></center></code></span></small></small></small>

---

## 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">## </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="A9"></code></span> Sources <span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

---

## 
<small><small><small><span class="vditor-ir__marker vditor-ir__marker--heading" data-type="heading-marker">## </span><span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"><div id="A10"></code></span>License<span data-type="html-inline" class="vditor-ir__node"><code class="vditor-ir__marker"></div></code></span></small></small></small>

<small><small><small>Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:</small></small></small>

<small><small><small>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</small></small></small>

<small><small><small>Copyright (c) 2020 Peter la Cour</small></small></small>
