# problem 1
s = 'django'
print(s[0])
print(s[-1])
print(s[0:4])
print(s[1:4])
print(s[-2:0])
print(s[4:])
print(s[::-1])

# Problem 2: Reassign  Hello to say goodbye
list = [3, 7, [1, 4, 'hello']]
list[2][2] = "Goodbye"
print(list)

# Problwm 3: Get hello from the dictionary
d1 = {'simple_key': 'hello'}
d2 = {'k1': {'k2': 'hello'}}
d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print("this is the answer for d1")
print("this is the answer for d2")
print(d2['k1']['k2'])

print("The answer for d3:")
print(d3['k1'][0]['nest_key'][1])

# problem 4
print("Thse are the unique values in my list")
mylist = [2, 9, 8, 7, 4, 1, 3, 5, 5, 7, 4, 2, 2, 4, 5, 8, 9, 8, 8, 7, 4, 4, 4]
print(set(mylist))

# Problem 5:


print("Hello my dog's name is {fname} and he is {age}".format(fname="John", age=25))

theValue = input("Enter a number")
print(theValue)
