<center>
    <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/Logos/organization_logo/organization_logo.png" width="300" alt="cognitiveclass.ai logo"  />
</center>


<h1>Extracting Stock Data Using a Web Scraping</h1>


Not all stock data is available via API in this assignment; you will use web-scraping to obtain financial data. You will be quizzed on your results.\
Using beautiful soup we will extract historical share data from a web-page.


<h2>Table of Contents</h2>
<div class="alert alert-block alert-info" style="margin-top: 20px">
    <ul>
        <li>Downloading the Webpage Using Requests Library</li>
        <li>Parsing Webpage HTML Using BeautifulSoup</li>
        <li>Extracting Data and Building DataFrame</li>
    </ul>
<p>
    Estimated Time Needed: <strong>30 min</strong></p>
</div>

<hr>



```python
#!pip install pandas==1.3.3
#!pip install requests==2.26.0
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y
!pip install lxml==4.6.4
#!pip install plotly==5.3.1
```

    
                      __    __    __    __
                     /  \  /  \  /  \  /  \
                    /    \/    \/    \/    \
    ███████████████/  /██/  /██/  /██/  /████████████████████████
                  /  / \   / \   / \   / \  \____
                 /  /   \_/   \_/   \_/   \    o \__,
                / _/                       \_____/  `
                |/
            ███╗   ███╗ █████╗ ███╗   ███╗██████╗  █████╗
            ████╗ ████║██╔══██╗████╗ ████║██╔══██╗██╔══██╗
            ██╔████╔██║███████║██╔████╔██║██████╔╝███████║
            ██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║
            ██║ ╚═╝ ██║██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║
            ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝
    
            mamba (0.15.3) supported by @QuantStack
    
            GitHub:  https://github.com/mamba-org/mamba
            Twitter: https://twitter.com/QuantStack
    
    █████████████████████████████████████████████████████████████
    
    
    Looking for: ['bs4==4.10.0']
    
    pkgs/r/linux-64          [<=>                 ] (00m:00s) 
    pkgs/r/linux-64          [=>                ] (00m:00s) 10 KB / ?? (65.52 KB/s)
    pkgs/r/linux-64          [=>                ] (00m:00s) 10 KB / ?? (65.52 KB/s)
    pkgs/r/noarch            [<=>                 ] (00m:00s) 
    pkgs/r/linux-64          [=>                ] (00m:00s) 10 KB / ?? (65.52 KB/s)
    pkgs/r/noarch            [=>               ] (00m:00s) 31 KB / ?? (204.28 KB/s)
    pkgs/r/linux-64          [=>                ] (00m:00s) 10 KB / ?? (65.52 KB/s)
    pkgs/r/noarch            [=>               ] (00m:00s) 31 KB / ?? (204.28 KB/s)
    pkgs/main/linux-64       [<=>                 ] (00m:00s) 
    pkgs/r/linux-64          [=>                ] (00m:00s) 10 KB / ?? (65.52 KB/s)
    pkgs/r/noarch            [=>               ] (00m:00s) 31 KB / ?? (204.28 KB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 732 KB / ?? (2.37 MB/s)
    pkgs/r/linux-64          [=>                ] (00m:00s) 10 KB / ?? (65.52 KB/s)
    pkgs/r/noarch            [=>               ] (00m:00s) 31 KB / ?? (204.28 KB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 732 KB / ?? (2.37 MB/s)
    pkgs/main/noarch         [<=>                 ] (00m:00s) 
    pkgs/r/linux-64          [=>                ] (00m:00s) 10 KB / ?? (65.52 KB/s)
    pkgs/r/noarch            [=>               ] (00m:00s) 31 KB / ?? (204.28 KB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 732 KB / ?? (2.37 MB/s)
    pkgs/main/noarch         [=>                ] (00m:00s) 660 KB / ?? (2.14 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 10 KB / ?? (65.52 KB/s)
    pkgs/r/noarch            [=>               ] (00m:00s) 31 KB / ?? (204.28 KB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 732 KB / ?? (2.37 MB/s)
    pkgs/main/noarch         [=>                ] (00m:00s) 660 KB / ?? (2.14 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 712 KB / ?? (2.30 MB/s)
    pkgs/r/noarch            [=>               ] (00m:00s) 31 KB / ?? (204.28 KB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 732 KB / ?? (2.37 MB/s)
    pkgs/main/noarch         [=>                ] (00m:00s) 660 KB / ?? (2.14 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 712 KB / ?? (2.30 MB/s)
    pkgs/r/noarch            [<=>              ] (00m:00s) 31 KB / ?? (204.28 KB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 732 KB / ?? (2.37 MB/s)
    pkgs/main/noarch         [=>                ] (00m:00s) 660 KB / ?? (2.14 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 712 KB / ?? (2.30 MB/s)
    pkgs/r/noarch            [<=>               ] (00m:00s) 752 KB / ?? (2.43 MB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 732 KB / ?? (2.37 MB/s)
    pkgs/main/noarch         [=>                ] (00m:00s) 660 KB / ?? (2.14 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 712 KB / ?? (2.30 MB/s)
    pkgs/r/noarch            [<=>               ] (00m:00s) 752 KB / ?? (2.43 MB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 732 KB / ?? (2.37 MB/s)
    pkgs/main/noarch         [<=>                 ] (00m:00s) Finalizing...
    pkgs/r/linux-64          [<=>               ] (00m:00s) 712 KB / ?? (2.30 MB/s)
    pkgs/r/noarch            [<=>               ] (00m:00s) 752 KB / ?? (2.43 MB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 732 KB / ?? (2.37 MB/s)
    pkgs/main/noarch         [<=>                 ] (00m:00s) Done
    pkgs/main/noarch         [====================] (00m:00s) Done
    pkgs/r/linux-64          [<=>               ] (00m:00s) 712 KB / ?? (2.30 MB/s)
    pkgs/r/noarch            [<=>               ] (00m:00s) 752 KB / ?? (2.43 MB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 732 KB / ?? (2.37 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 712 KB / ?? (2.30 MB/s)
    pkgs/r/noarch            [ <=>                ] (00m:00s) Finalizing...
    pkgs/main/linux-64       [=>                ] (00m:00s) 732 KB / ?? (2.37 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 712 KB / ?? (2.30 MB/s)
    pkgs/r/noarch            [ <=>                ] (00m:00s) Done
    pkgs/main/linux-64       [=>                ] (00m:00s) 732 KB / ?? (2.37 MB/s)
    pkgs/r/noarch            [====================] (00m:00s) Done
    pkgs/r/linux-64          [<=>               ] (00m:00s) 712 KB / ?? (2.30 MB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 732 KB / ?? (2.37 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 712 KB / ?? (2.30 MB/s)
    pkgs/main/linux-64       [<=>               ] (00m:00s) 732 KB / ?? (2.37 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 712 KB / ?? (2.30 MB/s)
    pkgs/main/linux-64       [ <=>                ] (00m:00s) 1 MB / ?? (2.77 MB/s)
    pkgs/r/linux-64          [ <=>              ] (00m:00s) 712 KB / ?? (2.30 MB/s)
    pkgs/main/linux-64       [ <=>                ] (00m:00s) 1 MB / ?? (2.77 MB/s)
    pkgs/r/linux-64          [  <=>               ] (00m:00s) 1 MB / ?? (2.63 MB/s)
    pkgs/main/linux-64       [ <=>                ] (00m:00s) 1 MB / ?? (2.77 MB/s)
    pkgs/r/linux-64          [  <=>               ] (00m:00s) Finalizing...
    pkgs/main/linux-64       [ <=>                ] (00m:00s) 1 MB / ?? (2.77 MB/s)
    pkgs/r/linux-64          [  <=>               ] (00m:00s) Done
    pkgs/main/linux-64       [ <=>                ] (00m:00s) 1 MB / ?? (2.77 MB/s)
    pkgs/r/linux-64          [====================] (00m:00s) Done
    pkgs/main/linux-64       [ <=>                ] (00m:00s) 1 MB / ?? (2.77 MB/s)
    pkgs/main/linux-64       [  <=>               ] (00m:00s) 1 MB / ?? (2.77 MB/s)
    pkgs/main/linux-64       [  <=>               ] (00m:00s) 2 MB / ?? (3.67 MB/s)
    pkgs/main/linux-64       [   <=>              ] (00m:00s) 2 MB / ?? (3.67 MB/s)
    pkgs/main/linux-64       [   <=>              ] (00m:00s) 3 MB / ?? (3.77 MB/s)
    pkgs/main/linux-64       [    <=>             ] (00m:00s) 3 MB / ?? (3.77 MB/s)
    pkgs/main/linux-64       [    <=>             ] (00m:00s) 4 MB / ?? (4.02 MB/s)
    pkgs/main/linux-64       [     <=>            ] (00m:00s) 4 MB / ?? (4.02 MB/s)
    pkgs/main/linux-64       [     <=>            ] (00m:00s) 4 MB / ?? (4.16 MB/s)
    pkgs/main/linux-64       [     <=>            ] (00m:00s) Finalizing...
    pkgs/main/linux-64       [     <=>            ] (00m:00s) Done
    pkgs/main/linux-64       [====================] (00m:00s) Done
    
    Pinned packages:
      - python 3.7.*
    
    
    Transaction
    
      Prefix: /home/jupyterlab/conda/envs/python
    
      Updating specs:
    
       - bs4==4.10.0
       - ca-certificates
       - certifi
       - openssl
    
    
      Package             Version  Build           Channel                  Size
    ──────────────────────────────────────────────────────────────────────────────
      Install:
    ──────────────────────────────────────────────────────────────────────────────
    
    [32m  + bs4           [00m     4.10.0  hd3eb1b0_0      pkgs/main/noarch        10 KB
    
      Change:
    ──────────────────────────────────────────────────────────────────────────────
    
    [31m  - certifi       [00m  2022.9.14  pyhd8ed1ab_0    installed                    
    [32m  + certifi       [00m  2022.9.14  py37h06a4308_0  pkgs/main/linux-64     155 KB
    [31m  - openssl       [00m     1.1.1q  h166bdaf_0      installed                    
    [32m  + openssl       [00m     1.1.1q  h7f8727e_0      pkgs/main/linux-64       3 MB
    
      Downgrade:
    ──────────────────────────────────────────────────────────────────────────────
    
    [31m  - beautifulsoup4[00m     4.11.1  pyha770c72_0    installed                    
    [32m  + beautifulsoup4[00m     4.10.0  pyh06a4308_0    pkgs/main/noarch        85 KB
    
      Summary:
    
      Install: 1 packages
      Change: 2 packages
      Downgrade: 1 packages
    
      Total download: 3 MB
    
    ──────────────────────────────────────────────────────────────────────────────
    
    Downloading  [==>                                      ] (00m:00s)    1.03 MB/s
    Extracting   [>                                                      ] (--:--) 
    [2A[0KFinished certifi                              (00m:00s)             155 KB      1 MB/s
    Downloading  [==>                                      ] (00m:00s)    1.03 MB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [==>                                      ] (00m:00s)    1.03 MB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [==>                                      ] (00m:00s)    1.03 MB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [==>                                      ] (00m:00s)    1.09 MB/s
    Extracting   [>                                                      ] (--:--) 
    [2A[0KFinished bs4                                  (00m:00s)              10 KB     67 KB/s
    Downloading  [==>                                      ] (00m:00s)    1.09 MB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [==>                                      ] (00m:00s)    1.09 MB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [==>                                      ] (00m:00s)    1.48 MB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [==>                                      ] (00m:00s)    1.48 MB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [==>                                      ] (00m:00s)    1.48 MB/s
    Extracting   [==========>                              ] (00m:00s)        1 / 4
    Downloading  [==>                                      ] (00m:00s)    1.48 MB/s
    Extracting   [==========>                              ] (00m:00s)        1 / 4
    Downloading  [==>                                      ] (00m:00s)    1.48 MB/s
    Extracting   [====================>                    ] (00m:00s)        2 / 4
    Downloading  [=======================================> ] (00m:00s)   16.80 MB/s
    Extracting   [====================>                    ] (00m:00s)        2 / 4
    Downloading  [=========================================] (00m:00s)   17.20 MB/s
    Extracting   [====================>                    ] (00m:00s)        2 / 4
    [2A[0KFinished beautifulsoup4                       (00m:00s)              85 KB    523 KB/s
    Downloading  [=========================================] (00m:00s)   17.20 MB/s
    Extracting   [====================>                    ] (00m:00s)        2 / 4
    Downloading  [=========================================] (00m:00s)   17.20 MB/s
    Extracting   [====================>                    ] (00m:00s)        2 / 4
    Downloading  [=========================================] (00m:00s)   17.20 MB/s
    Extracting   [====================>                    ] (00m:00s)        2 / 4
    Downloading  [=========================================] (00m:00s)   17.20 MB/s
    Extracting   [==============================>          ] (00m:00s)        3 / 4
    [2A[0KFinished openssl                              (00m:00s)               3 MB     16 MB/s
    Downloading  [=========================================] (00m:00s)   17.20 MB/s
    Extracting   [==============================>          ] (00m:00s)        3 / 4
    Downloading  [=========================================] (00m:00s)   17.20 MB/s
    Extracting   [==============================>          ] (00m:00s)        3 / 4
    Downloading  [=========================================] (00m:00s)   17.20 MB/s
    Extracting   [==============================>          ] (00m:00s)        3 / 4
    Downloading  [=========================================] (00m:00s)   17.20 MB/s
    Extracting   [=========================================] (00m:00s)        4 / 4
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    
                      __    __    __    __
                     /  \  /  \  /  \  /  \
                    /    \/    \/    \/    \
    ███████████████/  /██/  /██/  /██/  /████████████████████████
                  /  / \   / \   / \   / \  \____
                 /  /   \_/   \_/   \_/   \    o \__,
                / _/                       \_____/  `
                |/
            ███╗   ███╗ █████╗ ███╗   ███╗██████╗  █████╗
            ████╗ ████║██╔══██╗████╗ ████║██╔══██╗██╔══██╗
            ██╔████╔██║███████║██╔████╔██║██████╔╝███████║
            ██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║
            ██║ ╚═╝ ██║██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║
            ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝
    
            mamba (0.15.3) supported by @QuantStack
    
            GitHub:  https://github.com/mamba-org/mamba
            Twitter: https://twitter.com/QuantStack
    
    █████████████████████████████████████████████████████████████
    
    
    Looking for: ['html5lib==1.1']
    
    pkgs/main/linux-64       Using cache
    pkgs/main/noarch         Using cache
    pkgs/r/linux-64          Using cache
    pkgs/r/noarch            Using cache
    
    Pinned packages:
      - python 3.7.*
    
    
    Transaction
    
      Prefix: /home/jupyterlab/conda/envs/python
    
      Updating specs:
    
       - html5lib==1.1
       - ca-certificates
       - certifi
       - openssl
    
    
      Package         Version  Build         Channel                 Size
    ───────────────────────────────────────────────────────────────────────
      Install:
    ───────────────────────────────────────────────────────────────────────
    
    [32m  + html5lib    [00m      1.1  pyhd3eb1b0_0  pkgs/main/noarch       91 KB
    [32m  + webencodings[00m    0.5.1  py37_1        pkgs/main/linux-64     19 KB
    
      Summary:
    
      Install: 2 packages
    
      Total download: 110 KB
    
    ───────────────────────────────────────────────────────────────────────
    
    Downloading  [=================================>       ] (00m:00s)  626.36 KB/s
    Extracting   [>                                                      ] (--:--) 
    [2A[0KFinished html5lib                             (00m:00s)              91 KB    626 KB/s
    Downloading  [=================================>       ] (00m:00s)  626.36 KB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [=================================>       ] (00m:00s)  626.36 KB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [=================================>       ] (00m:00s)  626.36 KB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [=================================>       ] (00m:00s)  626.36 KB/s
    Extracting   [====================>                    ] (00m:00s)        1 / 2
    Downloading  [=========================================] (00m:00s)  432.74 KB/s
    Extracting   [====================>                    ] (00m:00s)        1 / 2
    [2A[0KFinished webencodings                         (00m:00s)              19 KB     75 KB/s
    Downloading  [=========================================] (00m:00s)  432.74 KB/s
    Extracting   [====================>                    ] (00m:00s)        1 / 2
    Downloading  [=========================================] (00m:00s)  432.74 KB/s
    Extracting   [====================>                    ] (00m:00s)        1 / 2
    Downloading  [=========================================] (00m:00s)  432.74 KB/s
    Extracting   [====================>                    ] (00m:00s)        1 / 2
    Downloading  [=========================================] (00m:00s)  432.74 KB/s
    Extracting   [=========================================] (00m:00s)        2 / 2
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    Collecting lxml==4.6.4
      Downloading lxml-4.6.4-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl (6.3 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m6.3/6.3 MB[0m [31m79.2 MB/s[0m eta [36m0:00:00[0m:00:01[0m00:01[0m
    [?25hInstalling collected packages: lxml
      Attempting uninstall: lxml
        Found existing installation: lxml 4.9.1
        Uninstalling lxml-4.9.1:
          Successfully uninstalled lxml-4.9.1
    Successfully installed lxml-4.6.4



```python
import pandas as pd
import requests
from bs4 import BeautifulSoup
```

## Using Webscraping to Extract Stock Data Example


First we must use the `request` library to downlaod the webpage, and extract the text. We will extract Netflix stock data <https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html>.



```python
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data  = requests.get(url).text
```

Next we must parse the text into html using `beautiful_soup`



```python
soup = BeautifulSoup(data, 'html5lib')
print(len(soup.find_all('table')))
# Just the one table
prim_table = soup.find('table').find_all('tr')
# Let's get the headings for the pandas dataframe (within first row of table)
headings = [el.text for el in soup.find('table').find_all('tr')[0]]
print(headings)
```

    1
    ['Date', 'Open', 'High', 'Low', 'Close*', 'Adj Close**', 'Volume']


Now we can turn the html table into a pandas dataframe



```python
# Clean up column headings for close just a bit
columns_strp = [x.replace('*', '') for x in headings]
netflix_data = pd.DataFrame(columns=columns_strp)
# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
# Tbody tag gets past the first table heading
print(f"Our table should be {len(soup.find('tbody').find_all('tr'))} rows long ")
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    # Create pandas Series and concat with DataFrame
    netflix_mnth_row = pd.Series({'Date': date, 'Open': Open, 'High': high,
                                 'Low': low, 'Close': close, 'Adj Close': adj_close,
                                 'Volume': volume})
    netflix_data = pd.concat([netflix_data, netflix_mnth_row.to_frame().T], ignore_index=True)
# Look at head and tail and confirm length
print(netflix_data.head(1), '\n', netflix_data.tail(1), '\n', len(netflix_data))
```

    Our table should be 70 rows long 
               Date    Open    High     Low   Close Adj Close      Volume
    0  Jun 01, 2021  504.01  536.13  482.14  528.21    528.21  78,560,600 
                 Date    Open    High    Low   Close Adj Close       Volume
    69  Sep 01, 2015  109.35  111.24  93.55  103.26    103.26  497,401,200 
     70


We can now print out the dataframe



```python
netflix_data.head()
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
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Adj Close</th>
      <th>Volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jun 01, 2021</td>
      <td>504.01</td>
      <td>536.13</td>
      <td>482.14</td>
      <td>528.21</td>
      <td>528.21</td>
      <td>78,560,600</td>
    </tr>
    <tr>
      <th>1</th>
      <td>May 01, 2021</td>
      <td>512.65</td>
      <td>518.95</td>
      <td>478.54</td>
      <td>502.81</td>
      <td>502.81</td>
      <td>66,927,600</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Apr 01, 2021</td>
      <td>529.93</td>
      <td>563.56</td>
      <td>499.00</td>
      <td>513.47</td>
      <td>513.47</td>
      <td>111,573,300</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mar 01, 2021</td>
      <td>545.57</td>
      <td>556.99</td>
      <td>492.85</td>
      <td>521.66</td>
      <td>521.66</td>
      <td>90,183,900</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Feb 01, 2021</td>
      <td>536.79</td>
      <td>566.65</td>
      <td>518.28</td>
      <td>538.85</td>
      <td>538.85</td>
      <td>61,902,300</td>
    </tr>
  </tbody>
</table>
</div>



We can also use the pandas `read_html` function using the url



```python
# Read HTML tables into a list of DataFrame objects.
read_html_pandas_data = pd.read_html(url)
print(type(read_html_pandas_data), len(read_html_pandas_data))
[print(x.head()) for x in read_html_pandas_data]
```

    <class 'list'> 1
               Date    Open    High     Low  Close* Adj Close**     Volume
    0  Jun 01, 2021  504.01  536.13  482.14  528.21      528.21   78560600
    1  May 01, 2021  512.65  518.95  478.54  502.81      502.81   66927600
    2  Apr 01, 2021  529.93  563.56  499.00  513.47      513.47  111573300
    3  Mar 01, 2021  545.57  556.99  492.85  521.66      521.66   90183900
    4  Feb 01, 2021  536.79  566.65  518.28  538.85      538.85   61902300





    [None]



Or we can convert the BeautifulSoup object to a string



```python
read_html_pandas_data_bs_str = pd.read_html(str(soup))
[print(x.head()) for x in read_html_pandas_data_bs_str]
```

               Date    Open    High     Low  Close* Adj Close**     Volume
    0  Jun 01, 2021  504.01  536.13  482.14  528.21      528.21   78560600
    1  May 01, 2021  512.65  518.95  478.54  502.81      502.81   66927600
    2  Apr 01, 2021  529.93  563.56  499.00  513.47      513.47  111573300
    3  Mar 01, 2021  545.57  556.99  492.85  521.66      521.66   90183900
    4  Feb 01, 2021  536.79  566.65  518.28  538.85      538.85   61902300





    [None]



Beacause there is only one table on the page, we just take the first table in the list returned



```python
netflix_dataframe = read_html_pandas_data[0]

netflix_dataframe.head()
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
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close*</th>
      <th>Adj Close**</th>
      <th>Volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jun 01, 2021</td>
      <td>504.01</td>
      <td>536.13</td>
      <td>482.14</td>
      <td>528.21</td>
      <td>528.21</td>
      <td>78560600</td>
    </tr>
    <tr>
      <th>1</th>
      <td>May 01, 2021</td>
      <td>512.65</td>
      <td>518.95</td>
      <td>478.54</td>
      <td>502.81</td>
      <td>502.81</td>
      <td>66927600</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Apr 01, 2021</td>
      <td>529.93</td>
      <td>563.56</td>
      <td>499.00</td>
      <td>513.47</td>
      <td>513.47</td>
      <td>111573300</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mar 01, 2021</td>
      <td>545.57</td>
      <td>556.99</td>
      <td>492.85</td>
      <td>521.66</td>
      <td>521.66</td>
      <td>90183900</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Feb 01, 2021</td>
      <td>536.79</td>
      <td>566.65</td>
      <td>518.28</td>
      <td>538.85</td>
      <td>538.85</td>
      <td>61902300</td>
    </tr>
  </tbody>
</table>
</div>



## Using Webscraping to Extract Stock Data Exercise


Use the `requests` library to download the webpage <https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html>. Save the text of the response as a variable named `html_data`.



```python
stock_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html'
html_data = requests.get(stock_url).text
```

Parse the html data using `beautiful_soup`.



```python
soup_stock = BeautifulSoup(html_data, 'html5lib')
# Make sure the html is available
# print(soup_stock.prettify())
```

<b>Question 1</b> What is the content of the title attribute:



```python
print(soup_stock.title)
```

    <title>Amazon.com, Inc. (AMZN) Stock Historical Prices &amp; Data - Yahoo Finance</title>


Using beautiful soup extract the table with historical share prices and store it into a dataframe named `amazon_data`. The dataframe should have columns Date, Open, High, Low, Close, Adj Close, and Volume. Fill in each variable with the correct data from the list `col`.



```python
amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# Deprecated use of append (see concat above for how you adjusted a similar task)
for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)
```

Print out the first five rows of the `amazon_data` dataframe you created.



```python
print(amazon_data.head())
```

               Date    Open    High     Low   Close       Volume Adj Close
    0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
    1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
    2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
    3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
    4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85


<b>Question 2</b> What is the name of the columns of the dataframe



```python
print(amazon_data.columns)
print(amazon_data.index)
```

    Index(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'], dtype='object')
    RangeIndex(start=0, stop=70, step=1)


<b>Question 3</b> What is the `Open` of the last row of the amazon_data dataframe?



```python
# Combine range Index with column names
print(amazon_data[-1:]['Open'])
print(amazon_data.tail(1))
```

    69    109.35
    Name: Open, dtype: object
                Date    Open    High    Low   Close       Volume Adj Close
    69  Sep 01, 2015  109.35  111.24  93.55  103.26  497,401,200    103.26



```python
# Update close column to float to plot
print(amazon_data.info())
amazon_data['Close'] = amazon_data['Close'].astype('float')
print(amazon_data.info())
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 70 entries, 0 to 69
    Data columns (total 7 columns):
     #   Column     Non-Null Count  Dtype 
    ---  ------     --------------  ----- 
     0   Date       70 non-null     object
     1   Open       70 non-null     object
     2   High       70 non-null     object
     3   Low        70 non-null     object
     4   Close      70 non-null     object
     5   Volume     70 non-null     object
     6   Adj Close  70 non-null     object
    dtypes: object(7)
    memory usage: 4.0+ KB
    None
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 70 entries, 0 to 69
    Data columns (total 7 columns):
     #   Column     Non-Null Count  Dtype  
    ---  ------     --------------  -----  
     0   Date       70 non-null     object 
     1   Open       70 non-null     object 
     2   High       70 non-null     object 
     3   Low        70 non-null     object 
     4   Close      70 non-null     float64
     5   Volume     70 non-null     object 
     6   Adj Close  70 non-null     object 
    dtypes: float64(1), object(6)
    memory usage: 4.0+ KB
    None



```python
# Plot first 10 observed items
amazon_data[:10].plot('Date', 'Close')
```




    <AxesSubplot:xlabel='Date'>




    
![png](output_37_1.png)
    


<h2>About the Authors:</h2> 

<a href="https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2022-01-01">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.

Azim Hirjani


## Change Log

| Date (YYYY-MM-DD) | Version | Changed By | Change Description |
| ----------------- | ------- | ---------- | ------------------ |

```
| 2021-06-09       | 1.2     | Lakshmi Holla|Added URL in question 3 |
```

\| 2020-11-10        | 1.1     | Malika Singla | Deleted the Optional part |
\| 2020-08-27        | 1.0     | Malika Singla | Added lab to GitLab       |

<hr>

## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>

<p>

