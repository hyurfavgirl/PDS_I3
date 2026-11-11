#part A

print("Predicton = 10.5 ", "Python's answer = ", int ("7") + 3.5)
#Predicton = 101010
print("Python's answer = ", str(10) * 3)

#Predicton = 
print("Python's answer = ", bool (""), bool(" "))

#Predicton = 3
print("Python's answer = ", int (3.99))

#Predicton = 1e3.0
print("Python's answer = ", float ("1e3"))

#Predicton = True+2.5
print("Python's answer = ", int (True) + float("2.5"))

#Predicton = 
print("Python's answer = ", round (2.5) + round(3.5))

#Predicton = float
print("Python's answer = ", type(10 / 2))

# Part B — a safe converter
def safe_int(text):
    """Turn text into an int; return None when it is not a number."""
    text = text.strip()
    if text.lstrip("-").isdigit():         # "42" or "-42"
        return int(text)
    try:
        return int(float(text))            # "3.9" -> 3
    except ValueError:
        return None                        # "abc", "", "12a"


for sample in ["42", " -8 ", "3.9", "abc", ""]:
    print(repr(sample), "->", safe_int(sample))


#part C
num1 = safe_int(input("Please!! Enter number #1 : "))
num2 = safe_int(input("Please!! Enter number #1 : "))

if num1 is None or num2 is None  :
    print("Please enter the valid number!!")
else :
    print("The sum of two numbers is: ", num1 + num2)