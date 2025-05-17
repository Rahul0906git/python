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