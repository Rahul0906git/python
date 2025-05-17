# List

l = [7, 8, 9, 10]
print(type(l))

l1 = [1,2,3,4,5,"rahul", 2 + 3j, 24.45, True,"true"]
print(l1)
print(l1[5])
print(l1[-1])
print(l1[0:5])
print(l +l1)
print(l+ list("Gourav"))
print(l[0:3]*2)

l[0] = 11     # changed 7 to 10
print(l)


# Tuples

t = (1, 2, 3, 4, 5, "rahul", 23.34, True)
print(t)
print(type(t))
print(tuple(l) + t)
print(l + list(t))

t1 = (1, 2, 3, 4, 1, 2, 3, 4)
print(t1*2)
print(len(t))

# Set

s1 = {1, 2, 3, 4, 5, 5,4,6, 2,}
print(s1)
print(type(s1))

s2 = {1, 2, 3, "rahul", "rahul", "rahul", 4, 5, 5, 6, 3, 7}
print(s2)
print(l + list(s1) + list(s2))

s1 = 11
print(s1)

s3 = {1, 2, 3, 4}
print(s3)

t4 = (1, 2, 3, 4, 5, )
print(t4[4])


# Dictionary

d = {}
print(type(d))

d1 = {"name" :"rahul", 
      "subject" :["data science", "big data", "data analytics"], 
      "number" : 12345678}
print(d1)
