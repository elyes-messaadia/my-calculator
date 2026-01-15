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
        return result 

    except :
        print("Oops! Something went wrong in calculator function..., maybe you gave me something I can't handle.")
        print(f"number_a: {number_a}")
        print(f"number_b: {number_b}")
        print(f"operator: {operator}")