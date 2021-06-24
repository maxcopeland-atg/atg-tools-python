# Python Proficiency Evaluation



## Basic Syntax
* What is the difference between an int and a float?
* What is the difference between a list and a tuple?
* What is a dictionary?
* Explain why a script would have `if __name__ == "__main__":`


## Basic Routines
* Write a `for` loop to print even numbers from 0 to 10 (inclusive).
* 


# Design Scenarios
1. Consider you have the following list of arbitrary length. How would you write a routine to count the number of distinct animals? What data structure would you use?
```
animals = ['dog', 'cat', ..., 'goat', 'dog', 'snake']
```

2. What does this function do?
```
def my_func1(x):
    """
    input
    ----
    x: int

    output
    ----
    Boolean
    """

    if x % 2 == 0:
        return True
    else: 
        return False
    
```

3. Find the error in the following function, where argument `x` is an integer.
```
def my_func2(x):

    for i in range(x):
        val += 1
    
    return val
```

4. What is the output of this function?
```
def my_func3(x):
    """
    input
    -----
    x: int

    output
    -----
    int
    """

    val = None

    for i in range(x):
        val = i
    
    return val

result = my_func3(10)
print(result)
```
