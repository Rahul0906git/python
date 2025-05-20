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

d2 = {"name" : "rahul", "name" : "kumar"}
print(d2)

d2 = list
print(d2)

d3 = {1233:"rahul" , 567:"kumar"}
print(d3)

d3 = {"%sdwe" : "asfdsv"}
print(d3)

d4 = {
      "course" : ["dsa", "java", "web"],
      "mentor" : ["rahul", "gourav"],
      "price" : {10000, 20000, 25000},
      "sy" : {"python" : ["oops", "pandas", "db"]}
}

print(d4)
print("course is:", d4["course"])

d5 = {"abc" : "....."}
print(d5)

print(d4["course"])

print(d3)

d3["phone number"] = 2134534
print(d3)

d3["name"] = "rahul"
print(d3)


# Inbuild functions in python

s1 = "RahulKumarrraassdf"
print(s1.count("a"))
print(s1.find("s"))
print(s1.index("K"))
print(s1.index("s"))
print(s1.upper())
print(s1.lower())

s2 = "My name is Rahul KumAr"
print(s2.title())
print(s2.split())

s3 = "my Nmae, is, Rahul, kumar" 
print(s3.split(","))

s4 = "this is my fsds pro class . i am attending this class for 4th time"
print(s4.split(".")[0])
print(s4.split(".")[1])
print(s2.capitalize())
print(s2.replace("Rahul", "Gourav"))
print(s2)
print(s2.center(40," "))
print(s2.rstrip())

s5 = "       Rahulkumar   "
print(s5.rstrip() + s5.lstrip())

print(s2)
print(s2.isalnum())
print(s2.isnumeric())


print(l1)
print(l)

l3 = [1, 2, 3, 4, 5, 'rahul', (2+3j), 24.45, True, 'true']
l3.append(5)
print(l3)
l3.insert(3,"rahul")
print(l3)

l3.extend("rahul")
print(l3)

l3 = [1,2,3,4,5]
l3.append([2,3,4])
print(l3)
l3.insert(1,[67,46])
print(l3)
l3.extend([4,5,66])
print(l3)
l3.pop()
print(l3)
l3.pop(1)
print(l3)
print(l3)
l3.remove(5)
print(l3)