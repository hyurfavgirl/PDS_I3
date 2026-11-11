def celsius_to_fahrenheit(c, round_to=1):
    #your calculation here
    f = c * 9 / 5 +32
    return f
print(celsius_to_fahrenheit(67))
def fahrenheit_to_celsius(f, round_to = 1):
    c = (f - 32)*5/9
    return c
#a
print("converson from 0 to 100")
for i in range (0, 101, 20):
    print(i,"celsius = ",celsius_to_fahrenheit(i), "farenheits")

#b
print ("Normal body temperature in celsius = ", fahrenheit_to_celsius(98.6), "celsius")
#c
print ("Convert 37 celsius to fahrenheit and backe again : ")
print ("celsius to fahrenheit : ", celsius_to_fahrenheit(37))
print ("fahrenheit to celsius : ", fahrenheit_to_celsius(celsius_to_fahrenheit(37)))
#d
print ("celsius to fahrenheit : ", celsius_to_fahrenheit(37, round_to= 3))
print ("A default argument is useful because it provides a value automotically when the user does not specify one.")



