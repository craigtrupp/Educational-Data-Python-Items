
# Week 2 Python Assessment

This Jupyter Notebook is auxillary to the following assessment in this week.  To complete this assessment, you will complete the 7 questions outlined in this document and use the output from your python cells as answers.

Your goal of this assignment is to construct regression and logistics models and interpret model paramters.

Run the following cell to initialize your environment and begin the assessment.


```python
#### RUN THIS

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import statsmodels.api as sm
import pandas as pd  

from sklearn.datasets import load_boston
boston_dataset = load_boston() 

boston = pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)
boston["MEDV"] = boston_dataset.target

url = "nhanes_2015_2016.csv"
NHANES = pd.read_csv(url)
vars = ["BPXSY1", "RIDAGEYR", "RIAGENDR", "RIDRETH1", "DMDEDUC2", "BMXBMI", "SMQ020"]
NHANES = NHANES[vars].dropna()
NHANES["smq"] = NHANES.SMQ020.replace({2: 0, 7: np.nan, 9: np.nan})
NHANES["RIAGENDRx"] = NHANES.RIAGENDR.replace({1: "Male", 2: "Female"})
NHANES["DMDEDUC2x"] = NHANES.DMDEDUC2.replace({1: "lt9", 2: "x9_11", 3: "HS", 4: "SomeCollege",5: "College", 7: np.nan, 9: np.nan})

np.random.seed(123)
```

Now that your notebook is ready, begin answering the questions below.

### Questions 1-3

The first three questions will be utilizing the Boston housing dataset seen in week 1. 

Here is the description for each column:

* __CRIM:__ Per capita crime rate by town
* __ZN:__ Proportion of residential land zoned for lots over 25,000 sq. ft
* __INDUS:__ Proportion of non-retail business acres per town
* __CHAS:__ Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
* __NOX:__ Nitric oxide concentration (parts per 10 million)
* __RM:__ Average number of rooms per dwelling
* __AGE:__ Proportion of owner-occupied units built prior to 1940
* __DIS:__ Weighted distances to five Boston employment centers
* __RAD:__ Index of accessibility to radial highways
* __TAX:__ Full-value property tax rate per $\$10,000$
* __PTRATIO:__ Pupil-teacher ratio by town
* __B:__ $1000(Bk — 0.63)^2$, where Bk is the proportion of [people of African American descent] by town
* __LSTAT:__ Percentage of lower status of the population
* __MEDV:__ Median value of owner-occupied homes in $\$1000$s

Uncomment and run the following code to generate a simple linear regression and output the model summary:


```python
model = sm.OLS.from_formula("MEDV ~ RM + CRIM", data=boston)
result = model.fit()
result.summary()
```




<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>          <td>MEDV</td>       <th>  R-squared:         </th> <td>   0.541</td>
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.539</td>
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   295.9</td>
</tr>
<tr>
  <th>Date:</th>             <td>Thu, 19 Jan 2023</td> <th>  Prob (F-statistic):</th> <td>1.15e-85</td>
</tr>
<tr>
  <th>Time:</th>                 <td>17:51:17</td>     <th>  Log-Likelihood:    </th> <td> -1643.5</td>
</tr>
<tr>
  <th>No. Observations:</th>      <td>   506</td>      <th>  AIC:               </th> <td>   3293.</td>
</tr>
<tr>
  <th>Df Residuals:</th>          <td>   503</td>      <th>  BIC:               </th> <td>   3306.</td>
</tr>
<tr>
  <th>Df Model:</th>              <td>     2</td>      <th>                     </th>     <td> </td>   
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   
</tr>
</table>
<table class="simpletable">
<tr>
      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>Intercept</th> <td>  -29.3017</td> <td>    2.592</td> <td>  -11.303</td> <td> 0.000</td> <td>  -34.395</td> <td>  -24.208</td>
</tr>
<tr>
  <th>RM</th>        <td>    8.3975</td> <td>    0.406</td> <td>   20.706</td> <td> 0.000</td> <td>    7.601</td> <td>    9.194</td>
</tr>
<tr>
  <th>CRIM</th>      <td>   -0.2618</td> <td>    0.033</td> <td>   -7.899</td> <td> 0.000</td> <td>   -0.327</td> <td>   -0.197</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>170.471</td> <th>  Durbin-Watson:     </th> <td>   0.805</td> 
</tr>
<tr>
  <th>Prob(Omnibus):</th> <td> 0.000</td>  <th>  Jarque-Bera (JB):  </th> <td>1034.461</td> 
</tr>
<tr>
  <th>Skew:</th>          <td> 1.331</td>  <th>  Prob(JB):          </th> <td>2.34e-225</td>
</tr>
<tr>
  <th>Kurtosis:</th>      <td> 9.479</td>  <th>  Cond. No.          </th> <td>    92.2</td> 
</tr>
</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



Utilizing the above output, answer the following three questions:

#### Question 1 (You'll answer this question within the quiz that follows this notebook)

What is the value of the coefficient for predictor __RM__? : **8.3975** 

#### Question 2 (You'll answer this question within the quiz that follows this notebook)

Are the predictors for this model statistically significant, yes or no? (Hint: What are their p-values?)

Run the following code for question 3: **Yes - low p-values (beneath default 95% confidence two-tail return from model**


```python
## For Question 3
model = sm.OLS.from_formula("MEDV ~ RM + CRIM + LSTAT", data=boston)
result = model.fit()
result.summary()
```




<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>          <td>MEDV</td>       <th>  R-squared:         </th> <td>   0.646</td> 
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.644</td> 
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   304.9</td> 
</tr>
<tr>
  <th>Date:</th>             <td>Thu, 19 Jan 2023</td> <th>  Prob (F-statistic):</th> <td>1.19e-112</td>
</tr>
<tr>
  <th>Time:</th>                 <td>17:57:02</td>     <th>  Log-Likelihood:    </th> <td> -1577.8</td> 
</tr>
<tr>
  <th>No. Observations:</th>      <td>   506</td>      <th>  AIC:               </th> <td>   3164.</td> 
</tr>
<tr>
  <th>Df Residuals:</th>          <td>   502</td>      <th>  BIC:               </th> <td>   3180.</td> 
</tr>
<tr>
  <th>Df Model:</th>              <td>     3</td>      <th>                     </th>     <td> </td>    
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>    
</tr>
</table>
<table class="simpletable">
<tr>
      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>Intercept</th> <td>   -2.4978</td> <td>    3.165</td> <td>   -0.789</td> <td> 0.430</td> <td>   -8.717</td> <td>    3.721</td>
</tr>
<tr>
  <th>RM</th>        <td>    5.2092</td> <td>    0.442</td> <td>   11.785</td> <td> 0.000</td> <td>    4.341</td> <td>    6.078</td>
</tr>
<tr>
  <th>CRIM</th>      <td>   -0.1011</td> <td>    0.032</td> <td>   -3.162</td> <td> 0.002</td> <td>   -0.164</td> <td>   -0.038</td>
</tr>
<tr>
  <th>LSTAT</th>     <td>   -0.5804</td> <td>    0.048</td> <td>  -12.201</td> <td> 0.000</td> <td>   -0.674</td> <td>   -0.487</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>171.189</td> <th>  Durbin-Watson:     </th> <td>   0.822</td> 
</tr>
<tr>
  <th>Prob(Omnibus):</th> <td> 0.000</td>  <th>  Jarque-Bera (JB):  </th> <td> 623.248</td> 
</tr>
<tr>
  <th>Skew:</th>          <td> 1.531</td>  <th>  Prob(JB):          </th> <td>4.61e-136</td>
</tr>
<tr>
  <th>Kurtosis:</th>      <td> 7.492</td>  <th>  Cond. No.          </th> <td>    216.</td> 
</tr>
</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



#### Question 3 (You'll answer this question within the quiz that follows this notebook)

What happened to our R-Squared value when we added the third predictor __LSTAT__ to our initial model?
 * **It Increased so we have greater coverage of the variability of the MEDV (Median value of owner-occupied homes in 1000s**

#### Question 4 (You'll answer this question within the quiz that follows this notebook)

What type of model should we use when our target outcome, or dependent variable is continuous?
**Linear Regression**

### Questions 5-6

The next two questions will involve the NHANES dataset.

Uncomment and run the following code to generate a logistics regression and output the model summary:


```python
NHANES["DMDEDUC2x"].unique()
```




    array(['College', 'HS', 'SomeCollege', 'x9_11', 'lt9', nan], dtype=object)




```python
model = sm.GLM.from_formula("smq ~ RIAGENDRx + RIDAGEYR + DMDEDUC2x", family=sm.families.Binomial(), data=NHANES)
result = model.fit()
result.summary()
```




<table class="simpletable">
<caption>Generalized Linear Model Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>         <td>smq</td>       <th>  No. Observations:  </th>  <td>  5093</td>  
</tr>
<tr>
  <th>Model:</th>                 <td>GLM</td>       <th>  Df Residuals:      </th>  <td>  5086</td>  
</tr>
<tr>
  <th>Model Family:</th>       <td>Binomial</td>     <th>  Df Model:          </th>  <td>     6</td>  
</tr>
<tr>
  <th>Link Function:</th>        <td>logit</td>      <th>  Scale:             </th> <td>  1.0000</td> 
</tr>
<tr>
  <th>Method:</th>               <td>IRLS</td>       <th>  Log-Likelihood:    </th> <td> -3201.2</td> 
</tr>
<tr>
  <th>Date:</th>           <td>Thu, 19 Jan 2023</td> <th>  Deviance:          </th> <td>  6402.4</td> 
</tr>
<tr>
  <th>Time:</th>               <td>17:53:33</td>     <th>  Pearson chi2:      </th> <td>5.10e+03</td> 
</tr>
<tr>
  <th>No. Iterations:</th>         <td>4</td>        <th>  Covariance Type:   </th> <td>nonrobust</td>
</tr>
</table>
<table class="simpletable">
<tr>
              <td></td>                <th>coef</th>     <th>std err</th>      <th>z</th>      <th>P>|z|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>Intercept</th>                <td>   -2.3060</td> <td>    0.114</td> <td>  -20.174</td> <td> 0.000</td> <td>   -2.530</td> <td>   -2.082</td>
</tr>
<tr>
  <th>RIAGENDRx[T.Male]</th>        <td>    0.9096</td> <td>    0.060</td> <td>   15.118</td> <td> 0.000</td> <td>    0.792</td> <td>    1.028</td>
</tr>
<tr>
  <th>DMDEDUC2x[T.HS]</th>          <td>    0.9434</td> <td>    0.090</td> <td>   10.521</td> <td> 0.000</td> <td>    0.768</td> <td>    1.119</td>
</tr>
<tr>
  <th>DMDEDUC2x[T.SomeCollege]</th> <td>    0.8322</td> <td>    0.084</td> <td>    9.865</td> <td> 0.000</td> <td>    0.667</td> <td>    0.998</td>
</tr>
<tr>
  <th>DMDEDUC2x[T.lt9]</th>         <td>    0.2662</td> <td>    0.109</td> <td>    2.438</td> <td> 0.015</td> <td>    0.052</td> <td>    0.480</td>
</tr>
<tr>
  <th>DMDEDUC2x[T.x9_11]</th>       <td>    1.0986</td> <td>    0.107</td> <td>   10.296</td> <td> 0.000</td> <td>    0.889</td> <td>    1.308</td>
</tr>
<tr>
  <th>RIDAGEYR</th>                 <td>    0.0183</td> <td>    0.002</td> <td>   10.582</td> <td> 0.000</td> <td>    0.015</td> <td>    0.022</td>
</tr>
</table>



#### Question 5 (You'll answer this question within the quiz that follows this notebook)

Which of our predictors has the largest coefficient? 
* **DMDEDUC2x[T.x9_11]**


#### Question 6 (You'll answer this question within the quiz that follows this notebook)

Which values for DMDEDUC2x and RIAGENDRx are represented in our intercept, or what is our reference level?

* **Female & College (Two-Default Coefficients Not Seen in Read-out ..thus in Intercept)**

#### Question 7 (You'll answer this question within the quiz that follows this notebook)

What model should we use when our target outcome, or dependent variable is binary, or only has two outputs, 0 and 1.

* **Logistic Regression**
