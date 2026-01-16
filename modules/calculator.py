def factorial(n):
  if n == 1:
    return n
  else:
    return n*factorial(n-1)

def calculator(number_a, number_b, operator): 
    """Take a number a and number b and return the result of the operation"""
    
    try :
        match operator:
            case "+":
                result = number_a + number_b
            case "-":
                result = number_a - number_b
            case "*":
                result = number_a * number_b
            case "/":
                result = number_a / number_b
            case "//": # Floor division
                result = number_a // number_b
            case "^":
                result = pow(number_a,number_b)
            case "%":
                result = number_a % number_b
            case "!":
                result = factorial(number_a)
            
        return result 

    except :
        print("Oops! Something went wrong in calculator function..., maybe you gave me something I can't handle.")
        print(f"number_a: {number_a}")
        print(f"number_b: {number_b}")
        print(f"operator: {operator}")