X = "hey my name is {1} and I am from {0} country"
Y ="India"
Z = "aayush"

print(X.format(Y, Z))

print(f"hey my name is {Z} and I am from {Y}")
      
print(f"We use f-string like this: hey my name is {{Z}} and I am from {{Y}}")
price= 49.09999
txt= f"for only {price:.2f} dollars!"
print(txt)
print(type(f"(2*30)"))