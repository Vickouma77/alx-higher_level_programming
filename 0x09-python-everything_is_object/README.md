# Python - Everything is object

## Object and values
if we execute this statements
```
>>> a = "banana"
>>> b = "banana"
```
In one case it may refer to different things an second case they can refer to the same things 

This things are called ***objects*** An object is something a variable can refer to. 

- we can test if two names have same values using >== 

```
>> a == b
True
```
- Test whether two names refer to the same object using the *is* operator:

```
>> a is b
True
```
## Aliasing
Since variables refer to objects if we sign one variable to another, both variables refer to the same object

```
>>> a = [1, 2, 3]
>>> b = a
>>> a is b
True

```
## Cloning lists
if we want to to modify a list and keep the copy of the original, we need to be able to make a copy of the list itself, not just the reference. This process is sometimes called cloning

The easiest way to clone a list is to use the slice operator
```
>>> a = [1, 2, 3]
>>> b = a[:]
>>> print b
[1, 2, 3]
