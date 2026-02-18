print("hello world" ) #printing hello world to the console


name ='John' #assigning the string 'John' to the variable name
age = 30 #assigning the integer 30 to the variable age
height = 1.75 #assigning the float 1.75 to the variable height
is_student = True #assigning the boolean value True to the variable is_student
print("Name:", name) #printing the value of the variable name
print("Age:", age) #printing the value of the variable age
print("Height:", height) #printing the value of the variable height
print("Is Student:", is_student) #printing the value of the variable is_student

print(f"My name is {name}, I am {age} years old, my height is {height} meters, and it is {is_student} that I am a student.") #using an f-string to print a formatted string with the variable values

name1 = input("Enter your name: ") #prompting the user to enter their name and storing it in the variable name
age1 = int(input("Enter your age: ")) #prompting the user to enter their age
print(f"Hello {name1}, you are {age1} years old.") #using an f-string to print a formatted string with the user's name and age

weight = float(input("Enter your weight in kg: ")) #prompting the user to enter their weight and converting it to a float
height1 = float(input("Enter your height in meters: ")) #prompting the user to enter their height and converting it to a float
bmi = weight / (height1 ** 2) #calculating the BMI using the formula weight divided by height squared
print(f"Your BMI is: {round(bmi, 2)}") #printing the BMI value

#age calculation
born_year= int(input("Enter your birth year: ")) #prompting the user to enter their birth year and converting it to an integer
current_year=2026
current_age=current_year-born_year
print(f"Your Born year is {born_year} and your current age is {current_age}")

#temperature conversion
temperature_celsius = float(input("Enter the temperature in Celsius: ")) #prompting the user to enter the temperature in Celsius and converting it to a float
temperature_fahrenheit = (temperature_celsius * 9/5) + 32 
print(f"The temperature in Fahrenheit is: {round(temperature_fahrenheit, 2)}") #printing the temperature in Fahrenheit

#simple addition of two numbers
print("Please enter any teo numbers to do the addition") 
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: "))
result = num1 + num2
print(f"The result of adding {num1} and {num2} is: {result}") #printing the result of the addition of the two numbers

#print numbers from 1 to 10
for i in range(1, 11):
    print(i)
    i += 1

#print the user's name 5 times
name2 = input("Enter your name: ")
for i in range(1, 6):
    print(name2)
    i += 1