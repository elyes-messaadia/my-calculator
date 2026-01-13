def calculator(number_a, number_b, operator): # Return the result with 2 numbers 
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