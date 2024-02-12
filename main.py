

def addition(num1, num2):
    
    return num1 + num2

def subtraction(num1, num2):
  
    return num1 - num2

def division(num1, num2):
    
    if num2 == 0:
        return "Nelze dělit nulou!"
    return num1 / num2

def multiplication(num1, num2):
   
    return num1 * num2


if __name__ == "__main__":
    num1 = 10.5
    num2 = 2.5

    print("Sčítání:", addition(num1, num2))
    print("Odčítání:", subtraction(num1, num2))
    print("Dělení:", division(num1, num2))
    print("Násobení:", multiplication(num1, num2))
