<center>
    <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/Logos/organization_logo/organization_logo.png" width="300" alt="cognitiveclass.ai logo"  />
</center>


<h1>Extracting Stock Data Using a Python Library</h1>


A company's stock share is a piece of the company more precisely:

<p><b>A stock (also known as equity) is a security that represents the ownership of a fraction of a corporation. This
entitles the owner of the stock to a proportion of the corporation's assets and profits equal to how much stock they own. Units of stock are called "shares." [1]</p></b>

An investor can buy a stock and sell it later. If the stock price increases, the investor profits, If it decreases,the investor with incur a loss.  Determining the stock price is complex; it depends on the number of outstanding shares, the size of the company's future profits, and much more. People trade stocks throughout the day the stock ticker is a report of the price of a certain stock, updated continuously throughout the trading session by the various stock market exchanges.

<p>You are a data scientist working for a hedge fund; it's your job to determine any suspicious stock activity. In this lab you will extract stock data using a Python library. We will use the <coode>yfinance</code> library, it allows us to extract data for stocks returning data in a pandas dataframe. You will use the lab to extract.</p>


<h2>Table of Contents</h2>
<div class="alert alert-block alert-info" style="margin-top: 20px">
    <ul>
        <li>Using yfinance to Extract Stock Info</li>
        <li>Using yfinance to Extract Historical Share Price Data</li>
        <li>Using yfinance to Extract Historical Dividends Data</li>
        <li>Exercise</li>
    </ul>
<p>
    Estimated Time Needed: <strong>30 min</strong></p>
</div>

<hr>



```python
!pip install yfinance==0.1.67
#!pip install pandas==1.3.3
```

    Collecting yfinance==0.1.67
      Downloading yfinance-0.1.67-py2.py3-none-any.whl (25 kB)
    Requirement already satisfied: pandas>=0.24 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from yfinance==0.1.67) (1.3.5)
    Requirement already satisfied: requests>=2.20 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from yfinance==0.1.67) (2.28.1)
    Requirement already satisfied: lxml>=4.5.1 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from yfinance==0.1.67) (4.9.1)
    Collecting multitasking>=0.0.7
      Downloading multitasking-0.0.11-py3-none-any.whl (8.5 kB)
    Requirement already satisfied: numpy>=1.15 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from yfinance==0.1.67) (1.21.6)
    Requirement already satisfied: python-dateutil>=2.7.3 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from pandas>=0.24->yfinance==0.1.67) (2.8.2)
    Requirement already satisfied: pytz>=2017.3 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from pandas>=0.24->yfinance==0.1.67) (2022.2.1)
    Requirement already satisfied: charset-normalizer<3,>=2 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from requests>=2.20->yfinance==0.1.67) (2.1.1)
    Requirement already satisfied: certifi>=2017.4.17 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from requests>=2.20->yfinance==0.1.67) (2022.9.14)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from requests>=2.20->yfinance==0.1.67) (1.26.11)
    Requirement already satisfied: idna<4,>=2.5 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from requests>=2.20->yfinance==0.1.67) (3.4)
    Requirement already satisfied: six>=1.5 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from python-dateutil>=2.7.3->pandas>=0.24->yfinance==0.1.67) (1.16.0)
    Installing collected packages: multitasking, yfinance
    Successfully installed multitasking-0.0.11 yfinance-0.1.67



```python
import yfinance as yf
import pandas as pd
```

## Using the yfinance Library to Extract Stock Data


Using the `Ticker` module we can create an object that will allow us to access functions to extract data. To do this we need to provide the ticker symbol for the stock, here the company is Apple and the ticker symbol is `AAPL`.



```python
apple = yf.Ticker("AAPL")
print(type(apple))
print(dir(apple))
print(help(apple.option_chain))
```

    <class 'yfinance.ticker.Ticker'>
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_analysis', '_balancesheet', '_base_url', '_calendar', '_cashflow', '_download_options', '_earnings', '_expirations', '_financials', '_fundamentals', '_get_fundamentals', '_history', '_info', '_institutional_holders', '_isin', '_major_holders', '_mutualfund_holders', '_news', '_options2df', '_recommendations', '_scrape_url', '_sustainability', 'actions', 'analysis', 'balance_sheet', 'balancesheet', 'calendar', 'cashflow', 'dividends', 'earnings', 'financials', 'get_actions', 'get_analysis', 'get_balance_sheet', 'get_balancesheet', 'get_calendar', 'get_cashflow', 'get_dividends', 'get_earnings', 'get_financials', 'get_info', 'get_institutional_holders', 'get_isin', 'get_major_holders', 'get_mutualfund_holders', 'get_news', 'get_recommendations', 'get_splits', 'get_sustainability', 'history', 'info', 'institutional_holders', 'isin', 'major_holders', 'mutualfund_holders', 'news', 'option_chain', 'options', 'quarterly_balance_sheet', 'quarterly_balancesheet', 'quarterly_cashflow', 'quarterly_earnings', 'quarterly_financials', 'recommendations', 'session', 'splits', 'stats', 'sustainability', 'ticker']
    Help on method option_chain in module yfinance.ticker:
    
    option_chain(date=None, proxy=None, tz=None) method of yfinance.ticker.Ticker instance
    
    None


Now we can access functions and variables to extract the type of data we need. You can view them and what they represent here [https://aroussi.com/post/python-yahoo-finance](https://aroussi.com/post/python-yahoo-finance?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2022-01-01).


### Stock Info


Using the attribute  <code>info</code> we can extract information about the stock as a Python dictionary.



```python
apple_info=apple.info
apple_info
```




    {'zip': '95014',
     'sector': 'Technology',
     'fullTimeEmployees': 154000,
     'longBusinessSummary': 'Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. It also sells various related services. In addition, the company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; AirPods Max, an over-ear wireless headphone; and wearables, home, and accessories comprising AirPods, Apple TV, Apple Watch, Beats products, HomePod, and iPod touch. Further, it provides AppleCare support services; cloud services store services; and operates various platforms, including the App Store that allow customers to discover and download applications and digital content, such as books, music, video, games, and podcasts. Additionally, the company offers various services, such as Apple Arcade, a game subscription service; Apple Music, which offers users a curated listening experience with on-demand radio stations; Apple News+, a subscription news and magazine service; Apple TV+, which offers exclusive original content; Apple Card, a co-branded credit card; and Apple Pay, a cashless payment service, as well as licenses its intellectual property. The company serves consumers, and small and mid-sized businesses; and the education, enterprise, and government markets. It distributes third-party applications for its products through the App Store. The company also sells its products through its retail and online stores, and direct sales force; and third-party cellular network carriers, wholesalers, retailers, and resellers. Apple Inc. was incorporated in 1977 and is headquartered in Cupertino, California.',
     'city': 'Cupertino',
     'phone': '408 996 1010',
     'state': 'CA',
     'country': 'United States',
     'companyOfficers': [],
     'website': 'https://www.apple.com',
     'maxAge': 1,
     'address1': 'One Apple Park Way',
     'industry': 'Consumer Electronics',
     'ebitdaMargins': 0.3343,
     'profitMargins': 0.25709,
     'grossMargins': 0.43313998,
     'operatingCashflow': 118224003072,
     'revenueGrowth': 0.019,
     'operatingMargins': 0.30533,
     'ebitda': 129556996096,
     'targetLowPrice': 122,
     'recommendationKey': 'buy',
     'grossProfits': 152836000000,
     'freeCashflow': 83344621568,
     'targetMedianPrice': 185,
     'currentPrice': 150.43,
     'earningsGrowth': -0.077,
     'currentRatio': 0.865,
     'returnOnAssets': 0.22204,
     'numberOfAnalystOpinions': 42,
     'targetMeanPrice': 182.01,
     'debtToEquity': 205.984,
     'returnOnEquity': 1.62816,
     'targetHighPrice': 220,
     'totalCash': 48230998016,
     'totalDebt': 119691001856,
     'totalRevenue': 387541991424,
     'totalCashPerShare': 3.001,
     'financialCurrency': 'USD',
     'revenuePerShare': 23.732,
     'quickRatio': 0.697,
     'recommendationMean': 1.9,
     'exchange': 'NMS',
     'shortName': 'Apple Inc.',
     'longName': 'Apple Inc.',
     'exchangeTimezoneName': 'America/New_York',
     'exchangeTimezoneShortName': 'EDT',
     'isEsgPopulated': False,
     'gmtOffSetMilliseconds': '-14400000',
     'quoteType': 'EQUITY',
     'symbol': 'AAPL',
     'messageBoardId': 'finmb_24937',
     'market': 'us_market',
     'annualHoldingsTurnover': None,
     'enterpriseToRevenue': 6.422,
     'beta3Year': None,
     'enterpriseToEbitda': 19.211,
     '52WeekChange': 0.034807682,
     'morningStarRiskRating': None,
     'forwardEps': 6.45,
     'revenueQuarterlyGrowth': None,
     'sharesOutstanding': 16070800384,
     'fundInceptionDate': None,
     'annualReportExpenseRatio': None,
     'totalAssets': None,
     'bookValue': 3.61,
     'sharesShort': 113066596,
     'sharesPercentSharesOut': 0.0069999998,
     'fundFamily': None,
     'lastFiscalYearEnd': 1632528000,
     'heldPercentInstitutions': 0.59746,
     'netIncomeToCommon': 99632996352,
     'trailingEps': 6.05,
     'lastDividendValue': 0.23,
     'SandP52WeekChange': -0.16877365,
     'priceToBook': 41.67036,
     'heldPercentInsiders': 0.0007,
     'nextFiscalYearEnd': 1695600000,
     'yield': None,
     'mostRecentQuarter': 1656115200,
     'shortRatio': 1.72,
     'sharesShortPreviousMonthDate': 1659052800,
     'floatShares': 16054199125,
     'beta': 1.234119,
     'enterpriseValue': 2488983093248,
     'priceHint': 2,
     'threeYearAverageReturn': None,
     'lastSplitDate': 1598832000,
     'lastSplitFactor': '4:1',
     'legalType': None,
     'lastDividendDate': 1659657600,
     'morningStarOverallRating': None,
     'earningsQuarterlyGrowth': -0.106,
     'priceToSalesTrailing12Months': 6.2381124,
     'dateShortInterest': 1661904000,
     'pegRatio': 2.64,
     'ytdReturn': None,
     'forwardPE': 23.32248,
     'lastCapGain': None,
     'shortPercentOfFloat': 0.0069999998,
     'sharesShortPriorMonth': 107535584,
     'impliedSharesOutstanding': 0,
     'category': None,
     'fiveYearAverageReturn': None,
     'previousClose': 152.74,
     'regularMarketOpen': 151.19,
     'twoHundredDayAverage': 160.5922,
     'trailingAnnualDividendYield': 0.005826895,
     'payoutRatio': 0.1471,
     'volume24Hr': None,
     'regularMarketDayHigh': 151.47,
     'navPrice': None,
     'averageDailyVolume10Day': 104166860,
     'regularMarketPreviousClose': 152.74,
     'fiftyDayAverage': 160.2058,
     'trailingAnnualDividendRate': 0.89,
     'open': 151.19,
     'toCurrency': None,
     'averageVolume10days': 104166860,
     'expireDate': None,
     'algorithm': None,
     'dividendRate': 0.92,
     'exDividendDate': 1659657600,
     'circulatingSupply': None,
     'startDate': None,
     'regularMarketDayLow': 148.56,
     'currency': 'USD',
     'trailingPE': 24.86446,
     'regularMarketVolume': 96029909,
     'lastMarket': None,
     'maxSupply': None,
     'openInterest': None,
     'marketCap': 2417530503168,
     'volumeAllCurrencies': None,
     'strikePrice': None,
     'averageVolume': 75663236,
     'dayLow': 148.56,
     'ask': 150.56,
     'askSize': 800,
     'volume': 96029909,
     'fiftyTwoWeekHigh': 182.94,
     'fromCurrency': None,
     'fiveYearAvgDividendYield': 1.03,
     'fiftyTwoWeekLow': 129.04,
     'bid': 150.52,
     'tradeable': False,
     'dividendYield': 0.0061000003,
     'bidSize': 1100,
     'dayHigh': 151.47,
     'coinMarketCapLink': None,
     'regularMarketPrice': 150.43,
     'preMarketPrice': None,
     'logo_url': 'https://logo.clearbit.com/apple.com'}



We can get the <code>'country'</code> using the key country



```python
apple_info['country']
```




    'United States'



### Extracting Share Price


A share is the single smallest part of a company's stock  that you can buy, the prices of these shares fluctuate over time. Using the <code>history()</code> method we can get the share price of the stock over a certain period of time. Using the `period` parameter we can set how far back from the present to get data. The options for `period` are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.



```python
apple_share_price_data = apple.history(period="max")
print(type(apple_share_price_data))
print(apple_share_price_data.columns)
```

    <class 'pandas.core.frame.DataFrame'>
    Index(['Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits'], dtype='object')


The format that the data is returned in is a Pandas DataFrame. With the `Date` as the index the share `Open`, `High`, `Low`, `Close`, `Volume`, and `Stock Splits` are given for each day.



```python
apple_share_price_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
      <th>Dividends</th>
      <th>Stock Splits</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1980-12-12</th>
      <td>0.100039</td>
      <td>0.100474</td>
      <td>0.100039</td>
      <td>0.100039</td>
      <td>469033600</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1980-12-15</th>
      <td>0.095255</td>
      <td>0.095255</td>
      <td>0.094820</td>
      <td>0.094820</td>
      <td>175884800</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1980-12-16</th>
      <td>0.088296</td>
      <td>0.088296</td>
      <td>0.087861</td>
      <td>0.087861</td>
      <td>105728000</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1980-12-17</th>
      <td>0.090035</td>
      <td>0.090470</td>
      <td>0.090035</td>
      <td>0.090035</td>
      <td>86441600</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1980-12-18</th>
      <td>0.092646</td>
      <td>0.093081</td>
      <td>0.092646</td>
      <td>0.092646</td>
      <td>73449600</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



We can reset the index of the DataFrame with the `reset_index` function. We also set the `inplace` paramter to `True` so the change takes place to the DataFrame itself.



```python
apple_share_price_data.reset_index(inplace=True)
```

We can plot the `Open` price against the `Date`:



```python
apple_share_price_data.plot(x="Date", y="Open")
```




    <AxesSubplot:xlabel='Date'>




    
![png](output_23_1.png)
    


### Extracting Dividends


Dividends are the distribution of a companys profits to shareholders. In this case they are defined as an amount of money returned per share an investor owns. Using the variable `dividends` we can get a dataframe of the data. The period of the data is given by the period defined in the 'history\` function.



```python
apple.dividends
```




    Date
    1987-05-11    0.000536
    1987-08-10    0.000536
    1987-11-17    0.000714
    1988-02-12    0.000714
    1988-05-16    0.000714
                    ...   
    2021-08-06    0.220000
    2021-11-05    0.220000
    2022-02-04    0.220000
    2022-05-06    0.230000
    2022-08-05    0.230000
    Name: Dividends, Length: 76, dtype: float64



We can plot the dividends overtime:



```python
apple.dividends.plot()
```




    <AxesSubplot:xlabel='Date'>




    
![png](output_28_1.png)
    


## Exercise


Now using the `Ticker` module create an object for AMD (Advanced Micro Devices) with the ticker symbol is `AMD` called; name the object <code>amd</code>.



```python
amd = yf.Ticker('AMD')
print(amd.info)
if 'country' in amd.info.keys():
    print(amd.info['country'])
```

    {'zip': '95054', 'sector': 'Technology', 'fullTimeEmployees': 15500, 'longBusinessSummary': 'Advanced Micro Devices, Inc. operates as a semiconductor company worldwide. The company operates in two segments, Computing and Graphics; and Enterprise, Embedded and Semi-Custom. Its products include x86 microprocessors as an accelerated processing unit, chipsets, discrete and integrated graphics processing units (GPUs), data center and professional GPUs, and development services; and server and embedded processors, and semi-custom System-on-Chip (SoC) products, development services, and technology for game consoles. The company provides processors for desktop and notebook personal computers under the AMD Ryzen, AMD Ryzen PRO, Ryzen Threadripper, Ryzen Threadripper PRO, AMD Athlon, AMD Athlon PRO, AMD FX, AMD A-Series, and AMD PRO A-Series processors brands; discrete GPUs for desktop and notebook PCs under the AMD Radeon graphics, AMD Embedded Radeon graphics brands; and professional graphics products under the AMD Radeon Pro and AMD FirePro graphics brands. It also offers Radeon Instinct, Radeon PRO V-series, and AMD Instinct accelerators for servers; chipsets under the AMD trademark; microprocessors for servers under the AMD EPYC; embedded processor solutions under the AMD Athlon, AMD Geode, AMD Ryzen, AMD EPYC, AMD R-Series, and G-Series processors brands; and customer-specific solutions based on AMD CPU, GPU, and multi-media technologies, as well as semi-custom SoC products. It serves original equipment manufacturers, public cloud service providers, original design manufacturers, system integrators, independent distributors, online retailers, and add-in-board manufacturers through its direct sales force, independent distributors, and sales representatives. The company was incorporated in 1969 and is headquartered in Santa Clara, California.', 'city': 'Santa Clara', 'phone': '408 749 4000', 'state': 'CA', 'country': 'United States', 'companyOfficers': [], 'website': 'https://www.amd.com', 'maxAge': 1, 'address1': '2485 Augustine Drive', 'industry': 'Semiconductors', 'ebitdaMargins': 0.26122, 'profitMargins': 0.14507, 'grossMargins': 0.50755, 'operatingCashflow': 3704000000, 'revenueGrowth': 0.701, 'operatingMargins': 0.16834, 'ebitda': 5635999744, 'targetLowPrice': 85, 'recommendationKey': 'buy', 'grossProfits': 7929000000, 'freeCashflow': 3622874880, 'targetMedianPrice': 121, 'currentPrice': 67.96, 'earningsGrowth': -0.534, 'currentRatio': 2.437, 'returnOnAssets': 0.05806, 'numberOfAnalystOpinions': 38, 'targetMeanPrice': 123.13, 'debtToEquity': 5.798, 'returnOnEquity': 0.10059, 'targetHighPrice': 200, 'totalCash': 5992000000, 'totalDebt': 3199000064, 'totalRevenue': 21575999488, 'totalCashPerShare': 3.712, 'financialCurrency': 'USD', 'revenuePerShare': 15.876, 'quickRatio': 1.819, 'recommendationMean': 2, 'exchange': 'NMS', 'shortName': 'Advanced Micro Devices, Inc.', 'longName': 'Advanced Micro Devices, Inc.', 'exchangeTimezoneName': 'America/New_York', 'exchangeTimezoneShortName': 'EDT', 'isEsgPopulated': False, 'gmtOffSetMilliseconds': '-14400000', 'quoteType': 'EQUITY', 'symbol': 'AMD', 'messageBoardId': 'finmb_168864', 'market': 'us_market', 'annualHoldingsTurnover': None, 'enterpriseToRevenue': 4.955, 'beta3Year': None, 'enterpriseToEbitda': 18.97, '52WeekChange': -0.37167162, 'morningStarRiskRating': None, 'forwardEps': 4.87, 'revenueQuarterlyGrowth': None, 'sharesOutstanding': 1614320000, 'fundInceptionDate': None, 'annualReportExpenseRatio': None, 'totalAssets': None, 'bookValue': 34.224, 'sharesShort': 30934716, 'sharesPercentSharesOut': 0.019199999, 'fundFamily': None, 'lastFiscalYearEnd': 1640390400, 'heldPercentInstitutions': 0.68494004, 'netIncomeToCommon': 3129999872, 'trailingEps': 2.3, 'lastDividendValue': None, 'SandP52WeekChange': -0.16877365, 'priceToBook': 1.985741, 'heldPercentInsiders': 0.00336, 'nextFiscalYearEnd': 1703462400, 'yield': None, 'mostRecentQuarter': 1656115200, 'shortRatio': 0.4, 'sharesShortPreviousMonthDate': 1659052800, 'floatShares': 1605248417, 'beta': 1.967638, 'enterpriseValue': 106916249600, 'priceHint': 2, 'threeYearAverageReturn': None, 'lastSplitDate': 966902400, 'lastSplitFactor': '2:1', 'legalType': None, 'lastDividendDate': None, 'morningStarOverallRating': None, 'earningsQuarterlyGrowth': -0.37, 'priceToSalesTrailing12Months': 5.084779, 'dateShortInterest': 1661904000, 'pegRatio': 0.6, 'ytdReturn': None, 'forwardPE': 13.954825, 'lastCapGain': None, 'shortPercentOfFloat': 0.019199999, 'sharesShortPriorMonth': 35275192, 'impliedSharesOutstanding': 0, 'category': None, 'fiveYearAverageReturn': None, 'previousClose': 69.5, 'regularMarketOpen': 68, 'twoHundredDayAverage': 103.7709, 'trailingAnnualDividendYield': 0, 'payoutRatio': 0, 'volume24Hr': None, 'regularMarketDayHigh': 69.08, 'navPrice': None, 'averageDailyVolume10Day': 76856680, 'regularMarketPreviousClose': 69.5, 'fiftyDayAverage': 88.555, 'trailingAnnualDividendRate': 0, 'open': 68, 'toCurrency': None, 'averageVolume10days': 76856680, 'expireDate': None, 'algorithm': None, 'dividendRate': None, 'exDividendDate': 798940800, 'circulatingSupply': None, 'startDate': None, 'regularMarketDayLow': 66.8216, 'currency': 'USD', 'trailingPE': 29.547827, 'regularMarketVolume': 87689951, 'lastMarket': None, 'maxSupply': None, 'openInterest': None, 'marketCap': 109709189120, 'volumeAllCurrencies': None, 'strikePrice': None, 'averageVolume': 80270055, 'dayLow': 66.8216, 'ask': 68.44, 'askSize': 900, 'volume': 87689951, 'fiftyTwoWeekHigh': 164.46, 'fromCurrency': None, 'fiveYearAvgDividendYield': None, 'fiftyTwoWeekLow': 66.82, 'bid': 68.3, 'tradeable': False, 'dividendYield': None, 'bidSize': 1100, 'dayHigh': 69.08, 'coinMarketCapLink': None, 'regularMarketPrice': 67.96, 'preMarketPrice': None, 'logo_url': 'https://logo.clearbit.com/amd.com'}
    United States


<b>Question 1</b> Use the key  <code>'country'</code> to find the country the stock belongs to, remember it as it will be a quiz question.



```python
print(amd.info['country'])
```

    United States


<b>Question 2</b> Use the key  <code>'sector'</code> to find the sector the stock belongs to, remember it as it will be a quiz question.



```python
if 'sector' in amd.info.keys():
    print(amd.info['sector'])
```

    Technology


<b>Question 3</b> Obtain stock data for AMD using the `history` function, set the `period` to max. Find the `Volume` traded on the first day (first row).



```python
import matplotlib.pyplot as plt
print(help(amd.history))
amd_history = amd.history(period='max')
type(amd_history) # hey look it's a dataframe
print(amd_history.head(2)['Volume'])
plt.plot(amd_history.index, amd_history['Close'])
```

    Help on method history in module yfinance.base:
    
    history(period='1mo', interval='1d', start=None, end=None, prepost=False, actions=True, auto_adjust=True, back_adjust=False, proxy=None, rounding=False, tz=None, timeout=None, **kwargs) method of yfinance.ticker.Ticker instance
        :Parameters:
            period : str
                Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                Either Use period parameter or use start and end
            interval : str
                Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                Intraday data cannot extend last 60 days
            start: str
                Download start date string (YYYY-MM-DD) or _datetime.
                Default is 1900-01-01
            end: str
                Download end date string (YYYY-MM-DD) or _datetime.
                Default is now
            prepost : bool
                Include Pre and Post market data in results?
                Default is False
            auto_adjust: bool
                Adjust all OHLC automatically? Default is True
            back_adjust: bool
                Back-adjusted data to mimic true historical prices
            proxy: str
                Optional. Proxy server URL scheme. Default is None
            rounding: bool
                Round values to 2 decimal places?
                Optional. Default is False = precision suggested by Yahoo!
            tz: str
                Optional timezone locale for dates.
                (default data is returned as non-localized dates)
            timeout: None or float
                If not None stops waiting for a response after given number of
                seconds. (Can also be a fraction of a second e.g. 0.01)
                Default is None.
            **kwargs: dict
                debug: bool
                    Optional. If passed as False, will suppress
                    error message printing to console.
    
    None
    Date
    1980-03-17    219600
    1980-03-18    727200
    Name: Volume, dtype: int64





    [<matplotlib.lines.Line2D at 0x7fb92a531690>]




    
![png](output_37_2.png)
    


<h2>About the Authors:</h2> 

<a href="https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2022-01-01">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.

Azim Hirjani


## Change Log

| Date (YYYY-MM-DD) | Version | Changed By    | Change Description        |
| ----------------- | ------- | ------------- | ------------------------- |
| 2020-11-10        | 1.1     | Malika Singla | Deleted the Optional part |
| 2020-08-27        | 1.0     | Malika Singla | Added lab to GitLab       |

<hr>

## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>

<p>

