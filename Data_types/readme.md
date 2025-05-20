# Python

**Set & List**
```python
l3 = [1, 2, 3, [1, 2, 3], 4, 5, 6,]
print(l3)

s3 = set(l3)      # Type casting will not work because list in list([1, 2, 3, [1, 2, 3], 4, 5, 6,])
print(s3)
```

**Data change**
```python
s1 = {1, 2, 3, 4}
s1 = 11       # It will work and Now s1 is reassigned to an integer
print(s1)

s2 = {5, 6, 7, 8}
s2[0] = 11    # It will not work and sets do not support indexing
print(s2) 
```

**Dictionary**
```python
d1 = {
    "name": "rahul",
    "subject": ["data science", "big data", "data analytics"],
    "number": 12345678
}
print(d1)
```

**pop with set**
```python
s = {100, 500, 300}
x = s.pop()
print(x)  # Any one of the elements
print(s)  # Remaining elements
```

**pop with dictionary**
```python
d = {'a': 1, 'b': 2}
x = d.pop('a')
print(x)  # 1
print(d)  # {'b': 2}