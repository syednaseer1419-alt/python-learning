str = "gulabjamun"
firsthalf = str[0:5]
trialfirsthalf = str[ :5]
print(firsthalf)
print(trialfirsthalf)
secondhalf = str[5:9]
trialsecondhalf = str[5:9]
print(secondhalf)
print(trialsecondhalf)

# take input and print middle 3 characters , last 2 characters
str = input("Enter a string: ")
mid = len(str) // 2
output = str[mid-1:mid+2]
print(output)

output2 = str[-2:]
print(output2)     

