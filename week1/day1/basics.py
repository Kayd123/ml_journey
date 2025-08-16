# practicing numbers (integers, float, complex)
x = 1  # int
y = 2.3  # float
z = 1j  # complex

print(type(x))
print(type(y))
print(type(z))
x = 1  # int
y = 2.3  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# practicing string
print("It's alright")
print("She is called 'dia'")
print('She is called "Na"')
a = """ 
        Lorem ipsum dolor sit amet,
        consectetur adipiscing elit,
        sed do eiusmod tempor incididunt
        ut labore et dolore magna aliqua."""
print(a)
# practicing lists, dicts
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(len(mylist))
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
print(type(list1))
print(type(list2))
print(type(list3))
# practicing dicts
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))
# x = thisdict.items()
# x = thisdict.get("model")
# print(x)
# x = thisdict.keys()
# print(x)
# thisdict["color"] = "white"
# print(x)
# if "model" in thisdict:
# print("Yes, 'model' is one of the keys in the thisdict dictionary")
# thisdict["year"] = 2018
# hisdict.update({"year": 2025})
# print(thisdict)
# thisdict.pop("model")
# print(thisdict)
# del thisdict["year"]
# print(thisdict)
# thisdict.clear()
# print(thisdict)
# for x in thisdict:
# print(x)
# for x in thisdict:
#   print(thisdict[x])
for x in thisdict.values():
    print(x)
for x in thisdict.keys():
    print(x)
for x, y in thisdict.items():
    print(x, y)
myfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}
x = myfamily.keys()
print(x)
print(myfamily.values())
print(myfamily.items())
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ":", obj[y])

        for z in obj:
            print(z + ":", obj[z])
