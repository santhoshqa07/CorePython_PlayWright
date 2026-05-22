
name, age, sal = "John",30, 50000.50

#Approach1
print(name, age, sal)

#Approach 2

# Name is: John
# Age is: 30
# Sal is: 50000.50

print("Name is:" + name)
# print("Age is:" + age) it is invalid
print("Age is:",age)
print("Salary is:",sal)

#Approach 3

# %s-- String, %d-- int, %g-- decimal

print("Name:%s Age:%d Salary:%g "%(name, age, sal))
print("Age:%d Name:%s  Salary:%g "%(age, name, sal))

#Approach 4 {} format()

print("Name{} Age:{} Salary:{} ".format(name, age, sal))

#Approach 5 {} format()

print("Name{0} Age:{1} Salary:{2} ".format(name, age, sal))
print("Name{1} Age:{0} Salary:{2} ".format(age,name, sal))










