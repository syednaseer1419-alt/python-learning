x = 10
y = 5
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
#comparision operators
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
#logical operators
print(x>y and x<y)
print(x>y or x<y)
print(not(x>y))
print("or operator result ",x>y or x<y)
print("and operator result ",x>y and x<y)
print("not operator result ",not(x>y))
# take input in celcuise and print its equivalent in fahrenheit and kelvin (use explicit type conversion and artithmetic operators.)
celcuise = float(input("Enter temperature in Celsius: "))
fahrenheit = (celcuise * 9/5) + 32
kelvin = celcuise + 273.15
print("Temperature in Fahrenheit: ", fahrenheit)
print("Temperature in Kelvin: ", kelvin)
#bill split calculator
#write a programe that takes total bill amount and number of freinds as input calcurate how muche each person will pay aslo 
#print the data type of each variable used
total_bill = float(input("Enter the total bill amount : "))
number_of_frinds = int(input("Enter the number of frinds : "))
amount_per_person = total_bill / number_of_frinds
print("Each person will pay : ",amount_per_person)
print("Data type of total_bill : ",type(total_bill))
print("Data type of number_of_frinds : ",type(number_of_frinds))
print("Data type of amount_per_person : ",type(amount_per_person))

