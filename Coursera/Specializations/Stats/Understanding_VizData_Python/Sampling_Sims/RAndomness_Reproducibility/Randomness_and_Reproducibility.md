
# Randomness and Reproducibility

As we learned in the beginning of this week, the concept of randomness is a cornerstone for statistical inference when drawing samples from larger populations.

In this tutorial, we are going to cover the following:

* Randomness and its uses in python.

* Utilizing python seeds to reproduce analysis.

* Generating random variables from a probability distribution.

* Random sampling from a population.


## What is Randomness?

In the beginning of this week's lectures, we touched on the significance of randomness when it comes to performing statistical inference on population samples.  If we have complete randomness, our estimates of means, proportions, and totals are ubiased.  This means our estimates are equal to the population values on average. 

In Python, we refer to randomness as the ability to generate data, strings, or, more generally, numbers at random.

However, when conducting analysis it is important to consider reproducibility.  If we are creating random data, how can we enable reproducible analysis?

We do this by utilizing pseudo-random number generators (PRNGs).  PRNGs start with a random number, known as the seed, and then use an algorithm to generate a psuedo-random sequence based on it.

This means that we can replicate the output of a random number generator in python simply by knowing which seed was used.

We can showcase this by using the functions in the python library *__random__*.

### Setting a Seed and Generating Random Numbers


```python
import random # import the python library
```


```python
random.seed(1234) # Set the Sequence

random.random() # Choose any number between 0 or 1
```




    0.9664535356921388




```python
# This would be our first 10 numbers in our pseudo sequence with the seed we set above
random.seed(1234)
for _ in range(10):
    print(random.random())
```

    0.9664535356921388
    0.4407325991753527
    0.007491470058587191
    0.9109759624491242
    0.939268997363764
    0.5822275730589491
    0.6715634814879851
    0.08393822683708396
    0.7664809327917963
    0.23680977536311776



```python
# a different seed to illustrate
random.seed(35)
for _ in range(5):
    print(random.random()) # print next sequence (first five numbers (between 0 -1) for random pseudo algo with set seed)
```

    0.5486946056438222
    0.7505409503856707
    0.7473067294096041
    0.8650451239500099
    0.2859067949036169


### Random Numbers from Real-Valued Distributions 
#### Uniform

* Equal probability : any value within the given interval is equally likely to be drawn by uniform.
* Uniform distributions are probability distributions with equally likely outcomes



```python
## Set same seed 
random.seed(1234)

random.random()
```




    0.9664535356921388




```python
random.uniform(25,50) # pull between interval
```




    36.01831497938382




```python
unifNumbers = [random.uniform(0,1) for _ in range(1000)] # list comprehension
```


```python
display(len(unifNumbers)) # 1,000 from uniform distribution
display(unifNumbers[:10])
```


    1000



    [0.007491470058587191,
     0.9109759624491242,
     0.939268997363764,
     0.5822275730589491,
     0.6715634814879851,
     0.08393822683708396,
     0.7664809327917963,
     0.23680977536311776,
     0.030814021726609964,
     0.7887727172362835]


#### Normal

Probability Distribution (passed to the below access)
* Requies mu (mean) 
* Requires sigma (standard deviation)


```python
mu = 0

sigma = 1

random.normalvariate(mu, sigma) # random numbers from normal distribution
```




    1.4456726257278167




```python
mu = 5

sigma = 2

random.normalvariate(mu, sigma) # more of a positive distribution 
```




    3.553844253828884




```python
mu = 0

sigma = 1

norm_zero_one_dist = [random.normalvariate(mu, sigma) for _ in range(10000)]
```

#### Here is some Variance Stads on our Normal Distribution Sample From Above


```python
import numpy as np
print(np.std(norm_zero_one_dist)) # What'ya know we see our standard distribution at our (very near) our set sigmna (std)
print(np.mean(norm_zero_one_dist)) # same with our mean
print(np.var(norm_zero_one_dist)) # Here's our variance
print(np.sqrt(np.var(norm_zero_one_dist))) # Equation for standard deviation


```

    1.0051900205420206
    0.0009173925488258931
    1.010406977397268
    1.0051900205420206


### Random Sampling from a Population

From lecture, we know that **Simple Random Sampling (SRS)** has the following properties:

* Start with known list of *N* population units, and randomly select *n* units from the list
* Every unit has **equal probability of selection = _n/N_**
* All possible samples of size *n* are equaly likely
* Estimates of means, proportions, and totals based on SRS are **UNBIASED** (meaning they are equal to the population values on average)


```python
import random
```


```python
mu = 0
    
sigma = 1

Population = [random.normalvariate(mu, sigma) for _ in range(10000)]
```


```python
SampleA = random.sample(Population, 500) # Sequence and number/quantity to pull
SampleB = random.sample(Population, 500)
```


```python
np.mean(SampleA)
```




    0.05969707955234938




```python
np.std(SampleA)
```




    0.9399431169092429




```python
np.mean(SampleB)
```




    0.06830181832279161




```python
np.std(SampleB)
```




    1.0200467353745102




```python
means = [np.mean(random.sample(Population, 1000)) for _ in range(100)] # list comprehension of the mean for 100 random samples of 1000 selected quantities
print(len(means))
np.mean(means)
```

    100





    0.009483864034944878



* We can see the mean is very close to our mu! 


```python
stdevs = [np.std(random.sample(Population, 1000)) for _ in range(100)]
print(len(stdevs))
print(np.mean(stdevs)) # What's the mean or average of our standard deviations
```

    100
    1.014376236532327


* Very close to 1 which was our set sigma (stdev) when creation our Population above 
