#Programmer: Hayden Coates
#Program: Variables & Methods 
#Date: 1.11.2024

quote = "You cant have good days without bad days. You need to have bad days to appreciate the good days!"

print(quote)
print(quote.upper()) #Uppercase
print(quote.lower()) #Lower
print(quote.title()) #Title Case
print(len(quote)) #Length of Characters

name = "Hayden Coates" #String
age = 16 #Int
gpa = 3.6 #Float

print(age)
print(int(gpa)) #Float to Int

print("\nMy name is ",(name), " and i am " ,(age), " and my gpa is" ,(gpa)) #Concatenate Variables While Casting Int to Str

print("My name  is ",name,'and i am',age,'years old and my gpa is  a',str(gpa)+'.') #concrasting using comma instaed of a +

print(' ')

age+=1 # adds one to the age
print(age)

print(' ')

age+=10 #adds ten to the age
print(age)

print(' ')

birthday = 1
age += birthday #add to variables with vaule as int together.
print(age)


