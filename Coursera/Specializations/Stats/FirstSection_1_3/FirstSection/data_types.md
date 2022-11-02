

```python
import math
```

## Data Types in Python 

The following data types can be used in base python:
* **boolean**
* **integer**
* **float**
* **string**
* **list**
* **None**
* complex
* object
* set
* dictionary

We will only focus on the **bolded** ones

Let's connect these data types to the the variable types we learned from the [Variable Types video](https://www.coursera.org/learn/understanding-visualization-data/lecture/iDodZ/variable-types).

###  Numerical or Quantitative (taking the mean makes sense)
* Discrete
    * Integer (int) #Stored exactly
* Continuous
    * Float (float) #Stored similarly to scientific notation. Allows for decimal places but loses precision.


```python
type(4)
```




    int




```python
type(0)
```




    int




```python
type(-3)
```




    int




```python
#try taking the mean
numbers = [2, 3, 4, 5]
print(sum(numbers)/len(numbers))
type(sum(numbers)/len(numbers)) #In Python 3 returns float, but in Python 2 would return int
```

    3.5





    float



**Floats**


```python
3/5
```




    0.6




```python
6*10**(-1)
```




    0.6000000000000001




```python
type(3/5)
```




    float




```python
type(math.pi)
```




    float




```python
type(4.0)
```




    float




```python
# Try taking the mean
numbers = [math.pi, 3/5, 4.1]
type(sum(numbers)/len(numbers))
```




    float



### Categorical or Qualitative
* Nominal
    * Boolean (bool)
    * String (str)
    * None (NoneType)
* Ordinal
    * Only defined by how you use the data
    * Often important when creating visuals
    * Lists can hold ordinal information because they have indices

**Boolean**


```python
# Boolean
type(True)
```




    bool




```python
# Boolean
if 6 < 5:
    print("Yes!")
```


```python
myList = [True, 6<5, 1==3, None is None]
for element in myList:
    print(type(element))
```

    <class 'bool'>
    <class 'bool'>
    <class 'bool'>
    <class 'bool'>



```python
print(sum(myList)/len(myList))
type(sum(myList)/len(myList))
```

    0.5





    float



**String**


```python
type("This sentence makes sense")
```




    str




```python
type("Makes sentense this sense")
```




    str




```python
type("math.pi")
```




    str




```python
strList = ['dog', 'koala', 'goose']
sum(strList)/len(strList)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-20-b0bd059010c7> in <module>()
          1 strList = ['dog', 'koala', 'goose']
    ----> 2 sum(strList)/len(strList)
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'


**Nonetype**


```python
# None
type(None)
```




    NoneType




```python
# None
x = None
type(x)
```




    NoneType




```python
noneList = [None]*5
sum(nonList)/len(nonList)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-23-08e0974f29ad> in <module>()
          1 noneList = [None]*5
    ----> 2 sum(nonList)/len(nonList)
    

    NameError: name 'nonList' is not defined


**Lists**

A list can hold many types and can also be used to store ordinal information.


```python
# List
myList = [1, 1.1, "This is a sentence", None]
for element in myList:
    print(type(element))
```

    <class 'int'>
    <class 'float'>
    <class 'str'>
    <class 'NoneType'>



```python
sum(myList)/len(myList)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-25-01620fe6b2d4> in <module>()
    ----> 1 sum(myList)/len(myList)
    

    TypeError: unsupported operand type(s) for +: 'float' and 'str'



```python
# List
myList = [1, 2, 3]
for element in myList:
    print(type(element))
sum(myList)/len(myList) # note that this outputs a float
```

    <class 'int'>
    <class 'int'>
    <class 'int'>





    2.0




```python
myList = ['third', 'first', 'medium', 'small', 'large']
myList[0]
```




    'third'




```python
myList.sort()
display(myList)
print(help(list.sort))
```


    ['first', 'large', 'medium', 'small', 'third']


    Help on method_descriptor:
    
    sort(...)
        L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
    
    None


There are more datatypes available when using different libraries such as Pandas and Numpy, which we will introduce to you as we use them.
