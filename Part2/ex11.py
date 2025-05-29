
def calculate(num1, operator, num2):

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "something went wrong bro"
    
    


print(calculate(10,"+",10))
print(calculate(10,"-",10))
print(calculate(10,"*",10))
print(calculate(10,"/",10))
print(calculate(10,"?",10))