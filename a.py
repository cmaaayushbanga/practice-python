a=5
b=6
c=7
d=input()
print(a+b+c)
print(d)


num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

num3 = num1 * num2
print("Product is: ", num3)

'''
Python program to illustrate
selection statement
'''
num1 = 8
if(num1>12):
	print("Num1 is good")
elif(num1>35):
	print("Num2 is not good")
else:
	print("Num2 is great")


def hello():
	print("hello")
	print("hello\nagain")
hello()


hello()			
 
def getInteger():
	result = int(input("Enter integer: "))
	return result

def Main():
	print("Started")

	
	output = getInteger()	
	print(output)


if __name__=="__main__":
	Main()


for step in range(5):	
	print(step)



import math

def Main():
	num = -85

	num = math.fabs(num)
	print(num)
	
	
if __name__=="__main__":
	Main()

print("hey i am a \"good boy\"\n and this viwer is also a good boy")\
    
print("hey",6,7, sep="~",end="989\n")
print("hello")

name= "aayush"
friend= "Rahul"
anotherfriend= "lokinder"
apple= '''he said
hi Harry
hey i am good
i want to eat an apple'''

print("Hello, "+ name)
print(apple)
print(name[0:4])

print("lets use a for loop\n")
for character in apple:
    print(character)
fruits="apple"
applelen= len(fruits)
print(applelen)
print(fruits[0:4])
print(fruits[0:-1])

nm="harry"
print(nm[-4:-2])

a = "!!!Harry!! !!!!!!!!! Harry"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())