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
        return Error