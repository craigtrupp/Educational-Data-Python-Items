<p style="text-align:center">
    <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2022-01-01" target="_blank">
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
    </a>
</p>


# **Web Scraping Lab**


Estimated time needed: **30** minutes


## Objectives


After completing this lab you will be able to:


<h2>Table of Contents</h2>
<div class="alert alert-block alert-info" style="margin-top: 20px">
    <ul>
        <li>
            <a href="https://bso/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2021-01-01">Beautiful Soup Object</a>
            <ul>
                <li>Tag</li>
                <li>Children, Parents, and Siblings</li>
                <li>HTML Attributes</li>
                <li>Navigable String</li>
            </ul>
        </li>
     </ul>
    <ul>
        <li>
            <a href="https://filter/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2021-01-01">Filter</a>
            <ul>
                <li>find All</li>
                <li>find </li>
                <li>HTML Attributes</li>
                <li>Navigable String</li>
            </ul>
        </li>
     </ul>
     <ul>
        <li>
            <a href="https://dscw/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2021-01-01">Downloading And Scraping The Contents Of A Web</a>
    </li>
         </ul>
    <p>
        Estimated time needed: <strong>25 min</strong>
    </p>

</div>

<hr>


For this lab, we are going to be using Python and several Python libraries. Some of these libraries might be installed in your lab environment or in SN Labs. Others may need to be installed by you. The cells below will install these libraries when executed.



```python
!mamba install bs4==4.10.0 -y
!pip install lxml==4.6.4
!mamba install html5lib==1.1 -y
# !pip install requests==2.26.0
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
    
    pkgs/r/noarch            [<=>                 ] (00m:00s) 
    pkgs/r/noarch            [=>                ] (00m:00s) 492 KB / ?? (1.59 MB/s)
    pkgs/r/noarch            [=>                ] (00m:00s) 492 KB / ?? (1.59 MB/s)
    pkgs/main/linux-64       [<=>                 ] (00m:00s) 
    pkgs/r/noarch            [=>                ] (00m:00s) 492 KB / ?? (1.59 MB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 520 KB / ?? (1.67 MB/s)
    pkgs/r/noarch            [=>                ] (00m:00s) 492 KB / ?? (1.59 MB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 520 KB / ?? (1.67 MB/s)
    pkgs/main/noarch         [<=>                 ] (00m:00s) 
    pkgs/r/noarch            [=>                ] (00m:00s) 492 KB / ?? (1.59 MB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 520 KB / ?? (1.67 MB/s)
    pkgs/main/noarch         [=>                ] (00m:00s) 380 KB / ?? (1.22 MB/s)
    pkgs/r/noarch            [=>                ] (00m:00s) 492 KB / ?? (1.59 MB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 520 KB / ?? (1.67 MB/s)
    pkgs/main/noarch         [=>                ] (00m:00s) 380 KB / ?? (1.22 MB/s)
    pkgs/r/linux-64          [<=>                 ] (00m:00s) 
    pkgs/r/noarch            [=>                ] (00m:00s) 492 KB / ?? (1.59 MB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 520 KB / ?? (1.67 MB/s)
    pkgs/main/noarch         [=>                ] (00m:00s) 380 KB / ?? (1.22 MB/s)
    pkgs/r/linux-64          [=>                ] (00m:00s) 348 KB / ?? (1.11 MB/s)
    pkgs/r/noarch            [=>                ] (00m:00s) 492 KB / ?? (1.59 MB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 520 KB / ?? (1.67 MB/s)
    pkgs/main/noarch         [<=>                 ] (00m:00s) Finalizing...
    pkgs/r/linux-64          [=>                ] (00m:00s) 348 KB / ?? (1.11 MB/s)
    pkgs/r/noarch            [=>                ] (00m:00s) 492 KB / ?? (1.59 MB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 520 KB / ?? (1.67 MB/s)
    pkgs/main/noarch         [<=>                 ] (00m:00s) Done
    pkgs/r/linux-64          [=>                ] (00m:00s) 348 KB / ?? (1.11 MB/s)
    pkgs/main/noarch         [====================] (00m:00s) Done
    pkgs/r/noarch            [=>                ] (00m:00s) 492 KB / ?? (1.59 MB/s)
    pkgs/main/linux-64       [=>                ] (00m:00s) 520 KB / ?? (1.67 MB/s)
    pkgs/r/linux-64          [=>                ] (00m:00s) 348 KB / ?? (1.11 MB/s)
    pkgs/r/noarch            [=>                ] (00m:00s) 492 KB / ?? (1.59 MB/s)
    pkgs/main/linux-64       [<=>               ] (00m:00s) 520 KB / ?? (1.67 MB/s)
    pkgs/r/linux-64          [=>                ] (00m:00s) 348 KB / ?? (1.11 MB/s)
    pkgs/r/noarch            [=>                ] (00m:00s) 492 KB / ?? (1.59 MB/s)
    pkgs/main/linux-64       [ <=>                ] (00m:00s) 1 MB / ?? (2.62 MB/s)
    pkgs/r/linux-64          [=>                ] (00m:00s) 348 KB / ?? (1.11 MB/s)
    pkgs/r/noarch            [<=>               ] (00m:00s) 492 KB / ?? (1.59 MB/s)
    pkgs/main/linux-64       [ <=>                ] (00m:00s) 1 MB / ?? (2.62 MB/s)
    pkgs/r/linux-64          [=>                ] (00m:00s) 348 KB / ?? (1.11 MB/s)
    pkgs/r/noarch            [ <=>                ] (00m:00s) 1 MB / ?? (2.39 MB/s)
    pkgs/main/linux-64       [ <=>                ] (00m:00s) 1 MB / ?? (2.62 MB/s)
    pkgs/r/linux-64          [=>                ] (00m:00s) 348 KB / ?? (1.11 MB/s)
    pkgs/r/noarch            [ <=>                ] (00m:00s) 1 MB / ?? (2.39 MB/s)
    pkgs/main/linux-64       [ <=>                ] (00m:00s) 1 MB / ?? (2.62 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 348 KB / ?? (1.11 MB/s)
    pkgs/r/noarch            [ <=>                ] (00m:00s) 1 MB / ?? (2.39 MB/s)
    pkgs/main/linux-64       [ <=>                ] (00m:00s) 1 MB / ?? (2.62 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 728 KB / ?? (1.56 MB/s)
    pkgs/r/noarch            [ <=>                ] (00m:00s) Finalizing...
    pkgs/main/linux-64       [ <=>                ] (00m:00s) 1 MB / ?? (2.62 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 728 KB / ?? (1.56 MB/s)
    pkgs/r/noarch            [ <=>                ] (00m:00s) Done
    pkgs/main/linux-64       [ <=>                ] (00m:00s) 1 MB / ?? (2.62 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 728 KB / ?? (1.56 MB/s)
    pkgs/r/noarch            [====================] (00m:00s) Done
    pkgs/main/linux-64       [ <=>                ] (00m:00s) 1 MB / ?? (2.62 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 728 KB / ?? (1.56 MB/s)
    pkgs/main/linux-64       [  <=>               ] (00m:00s) 1 MB / ?? (2.62 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 728 KB / ?? (1.56 MB/s)
    pkgs/main/linux-64       [  <=>               ] (00m:00s) 2 MB / ?? (3.02 MB/s)
    pkgs/r/linux-64          [<=>               ] (00m:00s) 728 KB / ?? (1.56 MB/s)
    pkgs/main/linux-64       [  <=>               ] (00m:00s) 2 MB / ?? (3.02 MB/s)
    pkgs/r/linux-64          [ <=>              ] (00m:00s) 728 KB / ?? (1.56 MB/s)
    pkgs/main/linux-64       [  <=>               ] (00m:00s) 2 MB / ?? (3.02 MB/s)
    pkgs/r/linux-64          [  <=>               ] (00m:00s) 1 MB / ?? (1.80 MB/s)
    pkgs/main/linux-64       [  <=>               ] (00m:00s) 2 MB / ?? (3.02 MB/s)
    pkgs/r/linux-64          [  <=>               ] (00m:00s) Finalizing...
    pkgs/main/linux-64       [  <=>               ] (00m:00s) 2 MB / ?? (3.02 MB/s)
    pkgs/r/linux-64          [  <=>               ] (00m:00s) Done
    pkgs/r/linux-64          [====================] (00m:00s) Done
    pkgs/main/linux-64       [  <=>               ] (00m:00s) 2 MB / ?? (3.02 MB/s)
    pkgs/main/linux-64       [   <=>              ] (00m:00s) 2 MB / ?? (3.02 MB/s)
    pkgs/main/linux-64       [   <=>              ] (00m:00s) 2 MB / ?? (3.24 MB/s)
    pkgs/main/linux-64       [    <=>             ] (00m:00s) 2 MB / ?? (3.24 MB/s)
    pkgs/main/linux-64       [    <=>             ] (00m:00s) 3 MB / ?? (3.41 MB/s)
    pkgs/main/linux-64       [     <=>            ] (00m:00s) 3 MB / ?? (3.41 MB/s)
    pkgs/main/linux-64       [     <=>            ] (00m:00s) 4 MB / ?? (3.58 MB/s)
    pkgs/main/linux-64       [      <=>           ] (00m:00s) 4 MB / ?? (3.58 MB/s)
    pkgs/main/linux-64       [      <=>           ] (00m:00s) 4 MB / ?? (3.68 MB/s)
    pkgs/main/linux-64       [      <=>           ] (00m:00s) Finalizing...
    pkgs/main/linux-64       [      <=>           ] (00m:01s) Done
    pkgs/main/linux-64       [====================] (00m:01s) Done
    
    Pinned packages:
      - python 3.7.*
    
    
    Transaction
    
      Prefix: /home/jupyterlab/conda/envs/python
    
      Updating specs:
    
       - bs4==4.10.0
       - ca-certificates
       - certifi
       - openssl
    
    
      Package               Version  Build           Channel                  Size
    ────────────────────────────────────────────────────────────────────────────────
      Install:
    ────────────────────────────────────────────────────────────────────────────────
    
    [32m  + bs4            [00m      4.10.0  hd3eb1b0_0      pkgs/main/noarch        10 KB
    
      Change:
    ────────────────────────────────────────────────────────────────────────────────
    
    [31m  - openssl        [00m      1.1.1q  h166bdaf_0      installed                    
    [32m  + openssl        [00m      1.1.1q  h7f8727e_0      pkgs/main/linux-64       3 MB
    
      Upgrade:
    ────────────────────────────────────────────────────────────────────────────────
    
    [31m  - ca-certificates[00m   2022.6.15  ha878542_0      installed                    
    [32m  + ca-certificates[00m  2022.07.19  h06a4308_0      pkgs/main/linux-64     124 KB
    [31m  - certifi        [00m   2022.6.15  py37h89c1867_0  installed                    
    [32m  + certifi        [00m   2022.9.14  py37h06a4308_0  pkgs/main/linux-64     155 KB
    
      Downgrade:
    ────────────────────────────────────────────────────────────────────────────────
    
    [31m  - beautifulsoup4 [00m      4.11.1  pyha770c72_0    installed                    
    [32m  + beautifulsoup4 [00m      4.10.0  pyh06a4308_0    pkgs/main/noarch        85 KB
    
      Summary:
    
      Install: 1 packages
      Change: 1 packages
      Upgrade: 2 packages
      Downgrade: 1 packages
    
      Total download: 3 MB
    
    ────────────────────────────────────────────────────────────────────────────────
    
    Downloading  [>                                        ] (00m:00s)  326.35 KB/s
    Extracting   [>                                                      ] (--:--) 
    [2A[0KFinished beautifulsoup4                       (00m:00s)              85 KB    325 KB/s
    Downloading  [>                                        ] (00m:00s)  326.35 KB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [==>                                      ] (00m:00s)  798.05 KB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [==>                                      ] (00m:00s)  798.05 KB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [==>                                      ] (00m:00s)  798.05 KB/s
    Extracting   [>                                                      ] (--:--) 
    [2A[0KFinished ca-certificates                      (00m:00s)             124 KB    474 KB/s
    Downloading  [==>                                      ] (00m:00s)  798.05 KB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [====>                                    ] (00m:00s)    1.34 MB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [====>                                    ] (00m:00s)    1.34 MB/s
    Extracting   [>                                                      ] (--:--) 
    [2A[0KFinished certifi                              (00m:00s)             155 KB    585 KB/s
    Downloading  [====>                                    ] (00m:00s)    1.34 MB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [====>                                    ] (00m:00s)    1.34 MB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [====>                                    ] (00m:00s)    1.34 MB/s
    Extracting   [========>                                ] (00m:00s)        1 / 5
    Downloading  [====>                                    ] (00m:00s)    1.34 MB/s
    Extracting   [========>                                ] (00m:00s)        1 / 5
    Downloading  [====>                                    ] (00m:00s)    1.31 MB/s
    Extracting   [========>                                ] (00m:00s)        1 / 5
    [2A[0KFinished bs4                                  (00m:00s)              10 KB     36 KB/s
    Downloading  [====>                                    ] (00m:00s)    1.31 MB/s
    Extracting   [========>                                ] (00m:00s)        1 / 5
    Downloading  [====>                                    ] (00m:00s)    1.31 MB/s
    Extracting   [========>                                ] (00m:00s)        1 / 5
    Downloading  [====>                                    ] (00m:00s)    1.31 MB/s
    Extracting   [================>                        ] (00m:00s)        2 / 5
    Downloading  [====>                                    ] (00m:00s)    1.31 MB/s
    Extracting   [================>                        ] (00m:00s)        2 / 5
    Downloading  [====>                                    ] (00m:00s)    1.31 MB/s
    Extracting   [========================>                ] (00m:00s)        3 / 5
    Downloading  [====>                                    ] (00m:00s)    1.31 MB/s
    Extracting   [========================>                ] (00m:00s)        3 / 5
    Downloading  [=============>                           ] (00m:00s)    3.22 MB/s
    Extracting   [========================>                ] (00m:00s)        3 / 5
    Downloading  [=============>                           ] (00m:00s)    3.22 MB/s
    Extracting   [========================>                ] (00m:00s)        3 / 5
    Downloading  [=============>                           ] (00m:00s)    3.22 MB/s
    Extracting   [================================>        ] (00m:00s)        4 / 5
    Downloading  [=========================================] (00m:00s)    8.28 MB/s
    Extracting   [================================>        ] (00m:00s)        4 / 5
    [2A[0KFinished openssl                              (00m:00s)               3 MB      7 MB/s
    Downloading  [=========================================] (00m:00s)    8.28 MB/s
    Extracting   [================================>        ] (00m:00s)        4 / 5
    Downloading  [=========================================] (00m:00s)    8.28 MB/s
    Extracting   [================================>        ] (00m:00s)        4 / 5
    Downloading  [=========================================] (00m:00s)    8.28 MB/s
    Extracting   [================================>        ] (00m:00s)        4 / 5
    Downloading  [=========================================] (00m:00s)    8.28 MB/s
    Extracting   [=========================================] (00m:00s)        5 / 5
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    Collecting lxml==4.6.4
      Downloading lxml-4.6.4-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl (6.3 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m6.3/6.3 MB[0m [31m52.0 MB/s[0m eta [36m0:00:00[0m00:01[0m00:01[0m
    [?25hInstalling collected packages: lxml
      Attempting uninstall: lxml
        Found existing installation: lxml 4.9.1
        Uninstalling lxml-4.9.1:
          Successfully uninstalled lxml-4.9.1
    Successfully installed lxml-4.6.4
    
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
    
    Downloading  [======>                                  ] (00m:00s)   75.18 KB/s
    Extracting   [>                                                      ] (--:--) 
    [2A[0KFinished webencodings                         (00m:00s)              19 KB     75 KB/s
    Downloading  [======>                                  ] (00m:00s)   75.18 KB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [======>                                  ] (00m:00s)   75.18 KB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [=========================================] (00m:00s)  431.05 KB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [=========================================] (00m:00s)  431.05 KB/s
    Extracting   [>                                                      ] (--:--) 
    [2A[0KFinished html5lib                             (00m:00s)              91 KB    355 KB/s
    Downloading  [=========================================] (00m:00s)  431.05 KB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [=========================================] (00m:00s)  431.05 KB/s
    Extracting   [>                                                      ] (--:--) 
    Downloading  [=========================================] (00m:00s)  431.05 KB/s
    Extracting   [====================>                    ] (00m:00s)        1 / 2
    Downloading  [=========================================] (00m:00s)  431.05 KB/s
    Extracting   [====================>                    ] (00m:00s)        1 / 2
    Downloading  [=========================================] (00m:00s)  431.05 KB/s
    Extracting   [=========================================] (00m:00s)        2 / 2
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done


Import the required modules and functions



```python
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
```

<h2 id="BSO">Beautiful Soup Objects</h2>


Beautiful Soup is a Python library for pulling data out of HTML and XML files, we will focus on HTML files. This is accomplished by representing the HTML as a set of objects with methods used to parse the HTML.  We can navigate the HTML as a tree and/or filter out what we are looking for.

Consider the following HTML:



```python
%%html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
<h3><b id='boldest'>Lebron James</b></h3>
<p> Salary: $ 92,000,000 </p>
<h3> Stephen Curry</h3>
<p> Salary: $85,000, 000 </p>
<h3> Kevin Durant </h3>
<p> Salary: $73,200, 000</p>
</body>
</html>
```


<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
<h3><b id='boldest'>Lebron James</b></h3>
<p> Salary: $ 92,000,000 </p>
<h3> Stephen Curry</h3>
<p> Salary: $85,000, 000 </p>
<h3> Kevin Durant </h3>
<p> Salary: $73,200, 000</p>
</body>
</html>



We can store it as a string in the variable HTML:



```python
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
```

To parse a document, pass it into the <code>BeautifulSoup</code> constructor, the <code>BeautifulSoup</code> object, which represents the document as a nested data structure:



```python
soup = BeautifulSoup(html, "html.parser")
```

First, the document is converted to Unicode, (similar to ASCII),  and HTML entities are converted to Unicode characters. Beautiful Soup transforms a complex HTML document into a complex tree of Python objects. The <code>BeautifulSoup</code> object can create other types of objects. In this lab, we will cover <code>BeautifulSoup</code> and <code>Tag</code> objects that for the purposes of this lab are identical, and <code>NavigableString</code> objects.


We can use the method <code>prettify()</code> to display the HTML in the nested structure:



```python
print(soup.prettify())
print(type(soup))
```

    <!DOCTYPE html>
    <html>
     <head>
      <title>
       Page Title
      </title>
     </head>
     <body>
      <h3>
       <b id="boldest">
        Lebron James
       </b>
      </h3>
      <p>
       Salary: $ 92,000,000
      </p>
      <h3>
       Stephen Curry
      </h3>
      <p>
       Salary: $85,000, 000
      </p>
      <h3>
       Kevin Durant
      </h3>
      <p>
       Salary: $73,200, 000
      </p>
     </body>
    </html>
    <class 'bs4.BeautifulSoup'>


## Tags


Let's say we want the  title of the page and the name of the top paid player we can use the <code>Tag</code>. The <code>Tag</code> object corresponds to an HTML tag in the original document, for example, the tag title.



```python
tag_object=soup.title
print("tag object:",tag_object)
```

    tag object: <title>Page Title</title>


we can see the tag type <code>bs4.element.Tag</code>



```python
print("tag object type:",type(tag_object))
```

    tag object type: <class 'bs4.element.Tag'>


If there is more than one <code>Tag</code>  with the same name, the first element with that <code>Tag</code> name is called, this corresponds to the most paid player:



```python
tag_object=soup.h3
tag_object
```




    <h3><b id="boldest">Lebron James</b></h3>



Enclosed in the bold attribute <code>b</code>, it helps to use the tree representation. We can navigate down the tree using the child attribute to get the name.


### Children, Parents, and Siblings


As stated above the <code>Tag</code> object is a tree of objects we can access the child of the tag or navigate down the branch as follows:



```python
tag_child =tag_object.b
tag_child
```




    <b id="boldest">Lebron James</b>



You can access the parent with the <code> parent</code>



```python
parent_tag=tag_child.parent
parent_tag
```




    <h3><b id="boldest">Lebron James</b></h3>



this is identical to



```python
tag_object
```




    <h3><b id="boldest">Lebron James</b></h3>



<code>tag_object</code> parent is the <code>body</code> element.



```python
tag_object.parent
```




    <body><h3><b id="boldest">Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body>



<code>tag_object</code> sibling is the <code>paragraph</code> element



```python
sibling_1=tag_object.next_sibling
sibling_1
```




    <p> Salary: $ 92,000,000 </p>



`sibling_2` is the `header` element which is also a sibling of both `sibling_1` and `tag_object`



```python
sibling_2=sibling_1.next_sibling
sibling_2
```




    <h3> Stephen Curry</h3>



<h3 id="first_question">Exercise: <code>next_sibling</code></h3>


Using the object <code>sibling\_2</code> and the property <code>next_sibling</code> to find the salary of Stephen Curry:



```python
sibling_2.next_sibling
```




    <p> Salary: $85,000, 000 </p>



<details><summary>Click here for the solution</summary>

```
sibling_2.next_sibling

```

</details>


### HTML Attributes


If the tag has attributes, the tag <code>id="boldest"</code> has an attribute <code>id</code> whose value is <code>boldest</code>. You can access a tag’s attributes by treating the tag like a dictionary:



```python
print(tag_child)
print(tag_child['id'])
```

    <b id="boldest">Lebron James</b>
    boldest


You can access that dictionary directly as <code>attrs</code>:



```python
tag_child.attrs
```




    {'id': 'boldest'}



You can also work with Multi-valued attribute check out <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2021-01-01">\[1]</a> for more.


We can also obtain the content if the attribute of the <code>tag</code> using the Python <code>get()</code> method.



```python
tag_child.get('id')
```




    'boldest'



### Navigable String


A string corresponds to a bit of text or content within a tag. Beautiful Soup uses the <code>NavigableString</code> class to contain this text. In our HTML we can obtain the name of the first player by extracting the sting of the <code>Tag</code> object <code>tag_child</code> as follows:



```python
tag_string=tag_child.string
tag_string
```




    'Lebron James'



we can verify the type is Navigable String



```python
type(tag_string)
```




    bs4.element.NavigableString



A NavigableString is just like a Python string or Unicode string, to be more precise. The main difference is that it also supports some  <code>BeautifulSoup</code> features. We can covert it to sting object in Python:



```python
unicode_string = str(tag_string)
unicode_string
```




    'Lebron James'



<h2 id="filter">Filter</h2>


Filters allow you to find complex patterns, the simplest filter is a string. In this section we will pass a string to a different filter method and Beautiful Soup will perform a match against that exact string.  Consider the following HTML of rocket launchs:



```python
%%html
<table>
  <tr>
    <td id='flight' >Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
   </tr>
  <tr> 
    <td>1</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td>
    <td>80 kg</td>
  </tr>
</table>
```


<table>
  <tr>
    <td id='flight' >Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
   </tr>
  <tr> 
    <td>1</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td>
    <td>80 kg</td>
  </tr>
</table>



We can store it as a string in the variable <code>table</code>:



```python
table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
```


```python
table_bs = BeautifulSoup(table, "html.parser")
```

## find All


The <code>find_all()</code> method looks through a tag’s descendants and retrieves all descendants that match your filters.

<p>
The Method signature for <code>find_all(name, attrs, recursive, string, limit, **kwargs)<c/ode>
</p>


### Name


When we set the <code>name</code> parameter to a tag name, the method will extract all the tags with that name and its children.



```python
table_rows=table_bs.find_all('tr')
print(table_rows)
```

    [<tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>, <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr>, <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>, <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr>]


The result is a Python Iterable just like a list, each element is a <code>tag</code> object:



```python
first_row =table_rows[0]
[first_row, type(table_rows), type(table_rows[0])]
```




    [<tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>,
     bs4.element.ResultSet,
     bs4.element.Tag]



The type is <code>tag</code>



```python
print(type(first_row))
```

    <class 'bs4.element.Tag'>


we can obtain the child



```python
[first_row.td, first_row.td['id']]
```




    [<td id="flight">Flight No</td>, 'flight']



If we iterate through the list, each element corresponds to a row in the table:



```python
for i,row in enumerate(table_rows):
    print("row",i,"is",row , type(row))
```

    row 0 is <tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr> <class 'bs4.element.Tag'>
    row 1 is <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr> <class 'bs4.element.Tag'>
    row 2 is <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr> <class 'bs4.element.Tag'>
    row 3 is <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr> <class 'bs4.element.Tag'>


As <code>row</code> is a <code>cell</code> object, we can apply the method <code>find_all</code> to it and extract table cells in the object <code>cells</code> using the tag <code>td</code>, this is all the children with the name <code>td</code>. The result is a list, each element corresponds to a cell and is a <code>Tag</code> object, we can iterate through this list as well. We can extract the content using the <code>string</code>  attribute.



```python
for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)
```

    row 0
    colunm 0 cell <td id="flight">Flight No</td>
    colunm 1 cell <td>Launch site</td>
    colunm 2 cell <td>Payload mass</td>
    row 1
    colunm 0 cell <td>1</td>
    colunm 1 cell <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td>
    colunm 2 cell <td>300 kg</td>
    row 2
    colunm 0 cell <td>2</td>
    colunm 1 cell <td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td>
    colunm 2 cell <td>94 kg</td>
    row 3
    colunm 0 cell <td>3</td>
    colunm 1 cell <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td>
    colunm 2 cell <td>80 kg</td>


If we use a list we can match against any item in that list.



```python
list_input=table_bs .find_all(name=["tr", "td"])
list_input
```




    [<tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>,
     <td id="flight">Flight No</td>,
     <td>Launch site</td>,
     <td>Payload mass</td>,
     <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr>,
     <td>1</td>,
     <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td>,
     <td>300 kg</td>,
     <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>,
     <td>2</td>,
     <td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td>,
     <td>94 kg</td>,
     <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr>,
     <td>3</td>,
     <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td>,
     <td>80 kg</td>]



## Attributes


If the argument is not recognized it will be turned into a filter on the tag’s attributes. For example the <code>id</code>  argument, Beautiful Soup will filter against each tag’s <code>id</code> attribute. For example, the first <code>td</code> elements have a value of <code>id</code> of <code>flight</code>, therefore we can filter based on that <code>id</code> value.



```python
table_bs.find_all(id="flight")
```




    [<td id="flight">Flight No</td>]



We can find all the elements that have links to the Florida Wikipedia page:



```python
list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input
```




    [<a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a>,
     <a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a>]



If we set the  <code>href</code> attribute to True, regardless of what the value is, the code finds all tags with <code>href</code> value:



```python
table_bs.find_all(href=True)
```




    [<a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a>,
     <a href="https://en.wikipedia.org/wiki/Texas">Texas</a>,
     <a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a>]



There are other methods for dealing with attributes and other related methods; Check out the following <a href='https://www.crummy.com/software/BeautifulSoup/bs4/doc/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2021-01-01#css-selectors'>link</a>


<h3 id="exer_type">Exercise: <code>find_all</code></h3>


Using the logic above, find all the elements without <code>href</code> value



```python
table_bs.find_all(href=False)
```




    [<table><tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr><tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr></table>,
     <tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>,
     <td id="flight">Flight No</td>,
     <td>Launch site</td>,
     <td>Payload mass</td>,
     <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr>,
     <td>1</td>,
     <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td>,
     <a></a>,
     <td>300 kg</td>,
     <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>,
     <td>2</td>,
     <td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td>,
     <td>94 kg</td>,
     <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr>,
     <td>3</td>,
     <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td>,
     <a> </a>,
     <td>80 kg</td>]



<details><summary>Click here for the solution</summary>

```
table_bs.find_all(href=False)

```

</details>


Using the soup object <code>soup</code>, find the element with the <code>id</code> attribute content set to <code>"boldest"</code>.



```python
soup.find_all(id="boldest")
```




    [<b id="boldest">Lebron James</b>]



<details><summary>Click here for the solution</summary>

```
soup.find_all(id="boldest")

```

</details>


### string


With string you can search for strings instead of tags, where we find all the elments with Florida:



```python
table_bs.find_all(string="Florida")
```




    ['Florida', 'Florida']



## find


The <code>find_all()</code> method scans the entire document looking for results, it’s if you are looking for one element you can use the <code>find()</code> method to find the first element in the document. Consider the following two table:



```python
%%html
<h3>Rocket Launch </h3>

<p>
<table class='rocket'>
  <tr>
    <td>Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
  </tr>
  <tr>
    <td>1</td>
    <td>Florida</td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Texas</td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Florida </td>
    <td>80 kg</td>
  </tr>
</table>
</p>
<p>

<h3>Pizza Party  </h3>
  
    
<table class='pizza'>
  <tr>
    <td>Pizza Place</td>
    <td>Orders</td> 
    <td>Slices </td>
   </tr>
  <tr>
    <td>Domino's Pizza</td>
    <td>10</td>
    <td>100</td>
  </tr>
  <tr>
    <td>Little Caesars</td>
    <td>12</td>
    <td >144 </td>
  </tr>
  <tr>
    <td>Papa John's </td>
    <td>15 </td>
    <td>165</td>
  </tr>

```


<h3>Rocket Launch </h3>

<p>
<table class='rocket'>
  <tr>
    <td>Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
  </tr>
  <tr>
    <td>1</td>
    <td>Florida</td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Texas</td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Florida </td>
    <td>80 kg</td>
  </tr>
</table>
</p>
<p>

<h3>Pizza Party  </h3>


<table class='pizza'>
  <tr>
    <td>Pizza Place</td>
    <td>Orders</td> 
    <td>Slices </td>
   </tr>
  <tr>
    <td>Domino's Pizza</td>
    <td>10</td>
    <td>100</td>
  </tr>
  <tr>
    <td>Little Caesars</td>
    <td>12</td>
    <td >144 </td>
  </tr>
  <tr>
    <td>Papa John's </td>
    <td>15 </td>
    <td>165</td>
  </tr>



We store the HTML as a Python string and assign <code>two_tables</code>:



```python
two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
```

We create a <code>BeautifulSoup</code> object  <code>two_tables_bs</code>



```python
two_tables_bs= BeautifulSoup(two_tables, 'html.parser')
```

We can find the first table using the tag name table



```python
print(two_tables_bs.find("table"))
print('First Table found above')
print(two_tables_bs.find_all('table'), len(two_tables_bs.find_all('table')))
```

    <table class="rocket"><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table>
    First Table found above
    [<table class="rocket"><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table>, <table class="pizza"><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td>144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr></table>] 2


We can filter on the class attribute to find the second table, but because class is a keyword in Python, we add an underscore.



```python
two_tables_bs.find("table",class_='pizza')
```




    <table class="pizza"><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td>144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr></table>



<h2 id="DSCW">Downloading And Scraping The Contents Of A Web Page</h2> 


We Download the contents of the web page:



```python
url = "http://www.ibm.com"
```

We use <code>get</code> to download the contents of the webpage in text format and store in a variable called <code>data</code>:



```python
data  = requests.get(url).text 
```

We create a <code>BeautifulSoup</code> object using the <code>BeautifulSoup</code> constructor



```python
soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'
```

Scrape all links



```python
for link in soup.find_all('a', href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))

```

    #main-content
    http://www.ibm.com
    https://www.ibm.com/sports/fantasy/?lnk=ushpv18l1
    #ibm-hp--tech-section
    https://www.ibm.com/consulting/?lnk=ushpv18intro2
    https://www.ibm.com/products/linuxone-emperor-4?lnk=ushpv18f1
    https://www.ibm.com/consulting/resources/state-of-salesforce?lnk=ushpv18f2
    https://www.ibm.com/blogs/jobs/2022/07/06/entry-level-consultant-the-secrets-to-becoming-a-successful-candidate/?lnk=ushpv18f3
    https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/healthcare-interoperability?lnk=ushpv18f4
    https://research.ibm.com/blog/year-three-quantum-coding-school?lnk=ushpv18r1
    https://research.ibm.com/blog/year-three-quantum-coding-school?lnk=ushpv18r1
    https://research.ibm.com/blog/goldeneye-cryogenic-concept-system?lnk=ushpv18r2
    https://research.ibm.com/blog/what-is-confidential-computing?lnk=ushpv18r3
    https://research.ibm.com/blog/deliberate-innovation-open-source-osi?lnk=ushpv18r4
    https://www.ibm.com/case-studies/search?lnk=ushpv18mAll
    https://www.ibm.com/case-studies/change-machine/?lnk=ushpv18m1
    https://www.ibm.com/case-studies/meemoo/?lnk=ushpv18m2
    https://www.ibm.com/case-studies/united-states-tennis-association-us-open/?lnk=ushpv18m3
    https://www.ibm.com/products?types[0]=trial&lnk=STW_US_MPDISC_BNR_BTN&lnk2=THP&lnk3=ushpv18tAll
    https://www.ibm.com/products/offers-and-discounts?link=ushpv18t5&lnk2=trial_mktpl_MPDISC
    https://www.ibm.com/products/cognos-analytics?lnk=ushpv18t1
    https://www.ibm.com/cloud/openshift?lnk=ushpv18t2
    https://www.ibm.com/verify/verify-identity?lnk=ushpv18t3
    https://www.ibm.com/search?lnk=ushpv18srch&locale=en-us&q=
    https://www.ibm.com/products?lnk=ushpv18p1&lnk2=trial_mktpl&psrc=none&pexp=def
    https://www.ibm.com/cloud/hybrid?lnk=ushpv18pt14
    https://www.ibm.com/watson?lnk=ushpv18pt17
    https://www.ibm.com/it-infrastructure?lnk=ushpv18pt19
    https://www.ibm.com/blockchain?lnk=ushpv18pt4
    https://www.ibm.com/security/products?lnk=ushpv18pt9
    https://www.ibm.com/analytics/products?lnk=ushpv18pt1
    https://www.ibm.com/cloud/automation?lnk=ushpv18ct21
    https://www.ibm.com/quantum-computing?lnk=ushpv18pt16
    https://www.ibm.com/mysupport/s/?language=en_US&lnk=ushpv18ct11
    https://www.ibm.com/training/?lnk=ushpv18ct15
    https://community.ibm.com/community/user/home/?lnk=ushpv18ct20
    https://developer.ibm.com/?lnk=ushpv18ct9
    https://www.ibm.com/garage?lnk=ushpv18pt18
    https://www.ibm.com/docs/en?lnk=ushpv18ct14
    https://www.redbooks.ibm.com/?lnk=ushpv18ct10
    https://www.ibm.com/subscribe/?lnk=ushpv18ct22
    https://www-03.ibm.com/employment/technicaltalent/developer/?lnk=ushpv18ct2
    https://www.ibm.com/


## Scrape  all images  Tags



```python
for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))
```

    <img alt="" aria-hidden="true" role="presentation" src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA1NSIgaGVpZ2h0PSI1MjcuNSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2ZXJzaW9uPSIxLjEiLz4=" style="max-width:100%;display:block;margin:0;border:none;padding:0"/>
    data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTA1NSIgaGVpZ2h0PSI1MjcuNSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2ZXJzaW9uPSIxLjEiLz4=
    <img alt="Eli Manning in jeans and a checked shirt, holding a football with a stadium in the background" class="ibm-resize" decoding="async" src="https://1.dam.s81c.com/p/08f951359da70bf3/20220912-ls-fantasy-football-26929-720x360.jpg" style="position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%"/>
    https://1.dam.s81c.com/p/08f951359da70bf3/20220912-ls-fantasy-football-26929-720x360.jpg
    <img alt=" " class="bx--image__img bx--card__img" src="https://1.dam.s81c.com/p/0935e0e70346bf67/20220913-f-linux-one-chevrons-26793-444x254.jpg"/>
    https://1.dam.s81c.com/p/0935e0e70346bf67/20220913-f-linux-one-chevrons-26793-444x254.jpg
    <img alt="abstract image of stacks of squares in blue and white" class="bx--image__img bx--card__img" src="https://1.dam.s81c.com/p/0944d5632246b09f/20220919-26893-salesforce-for-dreamforce-444x333.jpg"/>
    https://1.dam.s81c.com/p/0944d5632246b09f/20220919-26893-salesforce-for-dreamforce-444x333.jpg
    <img alt="Two men having a discussion around a glass coffee table, one taking notes" class="bx--image__img bx--card__img" src="https://1.dam.s81c.com/p/08f951353c2707ad/052022_CaitOppermann_InsideIBM_London_1681_02.jpg.global.s_4x3.jpg"/>
    https://1.dam.s81c.com/p/08f951353c2707ad/052022_CaitOppermann_InsideIBM_London_1681_02.jpg.global.s_4x3.jpg
    <img alt="two scientists load machinery in a lab" class="bx--image__img bx--card__img" src="https://1.dam.s81c.com/p/06e5de41cf23fda3/bld130965.jpg.global.s_4x3.jpg"/>
    https://1.dam.s81c.com/p/06e5de41cf23fda3/bld130965.jpg.global.s_4x3.jpg
    <img alt="a man points to an equation on a whiteboard" class="bx--image__img" src="https://1.dam.s81c.com/p/0868c64e38bcf8db/20220627-r1-quantum-educator-summit-1600x900.jpg"/>
    https://1.dam.s81c.com/p/0868c64e38bcf8db/20220627-r1-quantum-educator-summit-1600x900.jpg
    <img alt="a man works on a large, round metallic portal door" class="bx--image__img bx--card__img" src="https://1.dam.s81c.com/p/08f951359da70bf9/20220912-r1-super-fridge-1600x900.jpg"/>
    https://1.dam.s81c.com/p/08f951359da70bf9/20220912-r1-super-fridge-1600x900.jpg
    <img alt="Abstract image of clouds in a vivid sky" class="bx--image__img bx--card__img" src="https://1.dam.s81c.com/p/08b38f4a8026565b/20220725-r-confidential-computing-800x450.jpg"/>
    https://1.dam.s81c.com/p/08b38f4a8026565b/20220725-r-confidential-computing-800x450.jpg
    <img alt="co-worker discussion around a window-view conference table at IBM Austin" class="bx--image__img bx--card__img" src="https://1.dam.s81c.com/p/08f95134b227038f/20220822-r-open-source-incubator-800x450.jpg"/>
    https://1.dam.s81c.com/p/08f95134b227038f/20220822-r-open-source-incubator-800x450.jpg
    <img alt="A Black woman at a desk with a laptop and a calculator, holding a printout in her left hand, making notes with her right" class="bx--image__img" src="https://1.dam.s81c.com/p/0944d5632246b0c6/20220919-m-change-machine-26971-1600x900.jpg"/>
    https://1.dam.s81c.com/p/0944d5632246b0c6/20220919-m-change-machine-26971-1600x900.jpg
    <img alt="A boy and a girl react to something on a laptop operated by their young, bearded teacher" class="bx--image__img" src="https://1.dam.s81c.com/p/08f951359da70bfc/20220912-m-meemooo-26950-1600x900.jpg"/>
    https://1.dam.s81c.com/p/08f951359da70bfc/20220912-m-meemooo-26950-1600x900.jpg
    <img alt="Person using a laptop to compare stats about two female tennis players" class="bx--image__img" src="https://1.dam.s81c.com/p/08f95135982706de/20220905-m-us-open-case-studies-26945-1600x900.jpg"/>
    https://1.dam.s81c.com/p/08f95135982706de/20220905-m-us-open-case-studies-26945-1600x900.jpg
    <img alt="software interface featuring three colorful waves of bar graphs" class="bx--image__img bx--card__img" src="https://1.dam.s81c.com/p/08b38f4a80a656ec/cognos-analytics-dashboard-trial-800x450.jpg"/>
    https://1.dam.s81c.com/p/08b38f4a80a656ec/cognos-analytics-dashboard-trial-800x450.jpg
    <img alt="software dashboard showing information such as a pie chart" class="bx--image__img bx--card__img" src="https://1.dam.s81c.com/public/content/dam/worldwide-content/homepage/ul/g/ea/62/Redhat-Openshift-on-Cloud-trial-800x450.jpg"/>
    https://1.dam.s81c.com/public/content/dam/worldwide-content/homepage/ul/g/ea/62/Redhat-Openshift-on-Cloud-trial-800x450.jpg
    <img alt="software product interface featuring bar graphs and other information" class="bx--image__img bx--card__img" src="https://1.dam.s81c.com/public/content/dam/worldwide-content/homepage/ul/g/ac/2e/Security-Verify-Trial-800x450.jpg"/>
    https://1.dam.s81c.com/public/content/dam/worldwide-content/homepage/ul/g/ac/2e/Security-Verify-Trial-800x450.jpg


## Scrape data from HTML tables



```python
#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
```

Before proceeding to scrape a web site, you need to examine the contents, and the way data is organized on the website. Open the above url in your browser and check how many rows and columns are there in the color table.



```python
# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text
```


```python
soup = BeautifulSoup(data,"html.parser")
```


```python
#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>
```


```python
#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))
```

    Color Name--->None
    lightsalmon--->#FFA07A
    salmon--->#FA8072
    darksalmon--->#E9967A
    lightcoral--->#F08080
    coral--->#FF7F50
    tomato--->#FF6347
    orangered--->#FF4500
    gold--->#FFD700
    orange--->#FFA500
    darkorange--->#FF8C00
    lightyellow--->#FFFFE0
    lemonchiffon--->#FFFACD
    papayawhip--->#FFEFD5
    moccasin--->#FFE4B5
    peachpuff--->#FFDAB9
    palegoldenrod--->#EEE8AA
    khaki--->#F0E68C
    darkkhaki--->#BDB76B
    yellow--->#FFFF00
    lawngreen--->#7CFC00
    chartreuse--->#7FFF00
    limegreen--->#32CD32
    lime--->#00FF00
    forestgreen--->#228B22
    green--->#008000
    powderblue--->#B0E0E6
    lightblue--->#ADD8E6
    lightskyblue--->#87CEFA
    skyblue--->#87CEEB
    deepskyblue--->#00BFFF
    lightsteelblue--->#B0C4DE
    dodgerblue--->#1E90FF


## Scrape data from HTML tables into a DataFrame using BeautifulSoup and Pandas



```python
import pandas as pd
```


```python
#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"
```

Before proceeding to scrape a web site, you need to examine the contents, and the way data is organized on the website. Open the above url in your browser and check the tables on the webpage.



```python
# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text
```


```python
soup = BeautifulSoup(data,"html.parser")
```


```python
#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>
```


```python
# we can see how many tables were found by checking the length of the tables list
print(len(tables))
```

    25


Assume that we are looking for the `10 most densly populated countries` table, we can look through the tables list and find the right one we are look for based on the data in each table or we can search for the table name if it is in the table but this option might not always work.



```python
table_headings = []
for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)
test = tables[5]
# Side work here to get all table headings from first row in found table index above 
for row in test.find_all('tr'):
    if '<th>' in str(row):
        for heading in row.find_all('th'):
            heading_str = str(heading)
            # Get end of opending table heading (.string property can't get the last two table columns we want)
            close_th = heading_str[heading_str.find('>')+1:]
            th_text = close_th[:close_th.find('<')]
            #print(heading.string, heading, th_text)
            table_headings.append(th_text)
print(table_headings)
```

    5
    ['Rank', 'Country', 'Population', 'Area', 'Density']


See if you can locate the table name of the table, `10 most densly populated countries`, below.



```python
#print(tables[table_index].prettify())
```


```python
# Use table_headings list from a few cellls above to set columns!
population_data = pd.DataFrame(columns=table_headings)

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        # Insert row into dataframe instance created above
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

population_data
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
      <th>Rank</th>
      <th>Country</th>
      <th>Population</th>
      <th>Area</th>
      <th>Density</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Singapore</td>
      <td>5,704,000</td>
      <td>710</td>
      <td>8,033</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bangladesh</td>
      <td>173,440,000</td>
      <td>143,998</td>
      <td>1,204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>\n Palestine\n\n</td>
      <td>5,266,785</td>
      <td>6,020</td>
      <td>847</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Lebanon</td>
      <td>6,856,000</td>
      <td>10,452</td>
      <td>656</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Taiwan</td>
      <td>23,604,000</td>
      <td>36,193</td>
      <td>652</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>South Korea</td>
      <td>51,781,000</td>
      <td>99,538</td>
      <td>520</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Rwanda</td>
      <td>12,374,000</td>
      <td>26,338</td>
      <td>470</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Haiti</td>
      <td>11,578,000</td>
      <td>27,065</td>
      <td>428</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Netherlands</td>
      <td>17,740,000</td>
      <td>41,526</td>
      <td>427</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Israel</td>
      <td>9,580,000</td>
      <td>22,072</td>
      <td>434</td>
    </tr>
  </tbody>
</table>
</div>



## Scrape data from HTML tables into a DataFrame using BeautifulSoup and read_html


Using the same `url`, `data`, `soup`, and `tables` object as in the last section we can use the `read_html` function to create a DataFrame.

Remember the table we need is located in `tables[table_index]`

We can now use the `pandas` function `read_html` and give it the string version of the table as well as the `flavor` which is the parsing engine `bs4`.



```python
pd.read_html(str(tables[5]), flavor='bs4')
```




    [   Rank      Country  Population  Area(km2)  Density(pop/km2)
     0     1    Singapore     5704000        710              8033
     1     2   Bangladesh   173440000     143998              1204
     2     3    Palestine     5266785       6020               847
     3     4      Lebanon     6856000      10452               656
     4     5       Taiwan    23604000      36193               652
     5     6  South Korea    51781000      99538               520
     6     7       Rwanda    12374000      26338               470
     7     8        Haiti    11578000      27065               428
     8     9  Netherlands    17740000      41526               427
     9    10       Israel     9580000      22072               434]



The function `read_html` always returns a list of DataFrames so we must pick the one we want out of the list.



```python
population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]

population_data_read_html
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
      <th>Rank</th>
      <th>Country</th>
      <th>Population</th>
      <th>Area(km2)</th>
      <th>Density(pop/km2)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Singapore</td>
      <td>5704000</td>
      <td>710</td>
      <td>8033</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bangladesh</td>
      <td>173440000</td>
      <td>143998</td>
      <td>1204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Palestine</td>
      <td>5266785</td>
      <td>6020</td>
      <td>847</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Lebanon</td>
      <td>6856000</td>
      <td>10452</td>
      <td>656</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Taiwan</td>
      <td>23604000</td>
      <td>36193</td>
      <td>652</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>South Korea</td>
      <td>51781000</td>
      <td>99538</td>
      <td>520</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Rwanda</td>
      <td>12374000</td>
      <td>26338</td>
      <td>470</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Haiti</td>
      <td>11578000</td>
      <td>27065</td>
      <td>428</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Netherlands</td>
      <td>17740000</td>
      <td>41526</td>
      <td>427</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Israel</td>
      <td>9580000</td>
      <td>22072</td>
      <td>434</td>
    </tr>
  </tbody>
</table>
</div>



## Scrape data from HTML tables into a DataFrame using read_html


We can also use the `read_html` function to directly get DataFrames from a `url`.



```python
dataframe_list = pd.read_html(url, flavor='bs4')
```

We can see there are 25 DataFrames just like when we used `find_all` on the `soup` object.



```python
len(dataframe_list)
```




    25



Finally we can pick the DataFrame we need out of the list.



```python
dataframe_list[5]
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
      <th>Rank</th>
      <th>Country</th>
      <th>Population</th>
      <th>Area(km2)</th>
      <th>Density(pop/km2)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Singapore</td>
      <td>5704000</td>
      <td>710</td>
      <td>8033</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bangladesh</td>
      <td>173440000</td>
      <td>143998</td>
      <td>1204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Palestine</td>
      <td>5266785</td>
      <td>6020</td>
      <td>847</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Lebanon</td>
      <td>6856000</td>
      <td>10452</td>
      <td>656</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Taiwan</td>
      <td>23604000</td>
      <td>36193</td>
      <td>652</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>South Korea</td>
      <td>51781000</td>
      <td>99538</td>
      <td>520</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Rwanda</td>
      <td>12374000</td>
      <td>26338</td>
      <td>470</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Haiti</td>
      <td>11578000</td>
      <td>27065</td>
      <td>428</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Netherlands</td>
      <td>17740000</td>
      <td>41526</td>
      <td>427</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Israel</td>
      <td>9580000</td>
      <td>22072</td>
      <td>434</td>
    </tr>
  </tbody>
</table>
</div>



We can also use the `match` parameter to select the specific table we want. If the table contains a string matching the text it will be read.



```python
pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]
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
      <th>Rank</th>
      <th>Country</th>
      <th>Population</th>
      <th>Area(km2)</th>
      <th>Density(pop/km2)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Singapore</td>
      <td>5704000</td>
      <td>710</td>
      <td>8033</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bangladesh</td>
      <td>173440000</td>
      <td>143998</td>
      <td>1204</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Palestine</td>
      <td>5266785</td>
      <td>6020</td>
      <td>847</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Lebanon</td>
      <td>6856000</td>
      <td>10452</td>
      <td>656</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Taiwan</td>
      <td>23604000</td>
      <td>36193</td>
      <td>652</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>South Korea</td>
      <td>51781000</td>
      <td>99538</td>
      <td>520</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Rwanda</td>
      <td>12374000</td>
      <td>26338</td>
      <td>470</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Haiti</td>
      <td>11578000</td>
      <td>27065</td>
      <td>428</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Netherlands</td>
      <td>17740000</td>
      <td>41526</td>
      <td>427</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Israel</td>
      <td>9580000</td>
      <td>22072</td>
      <td>434</td>
    </tr>
  </tbody>
</table>
</div>



## Authors


Ramesh Sannareddy


### Other Contributors


Rav Ahuja


## Change Log


| Date (YYYY-MM-DD) | Version | Changed By                                               | Change Description |
| ----------------- | ------- | -------------------------------------------------------- | ------------------ |
| 2021-08-04        | 0.2     | Made changes to markdown of nextsibling                  |                    |
| 2020-10-17        | 0.1     | Joseph Santarcangelo  Created initial version of the lab |                    |


Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2021-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork-19487395&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).



```python

```


```python

```
