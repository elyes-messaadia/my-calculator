def operation_parser(operation):
    """Convert an operation string into a Tuple list of each elements"""

    try :
        elements = ()
        number = "" # Initialize number to empty string

        for i, char in enumerate(operation): # for each character in operation string
            match char:
                case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | ".":
                    number += char #build the number

                case "(" | ")" | "+" | "-" | "/" | "*" | "^" | "%" | "!":
                    # Handle negative numbers: '-' is part of the number if:
                    # - it's at the start (i == 0)
                    # - or after an operator or opening parenthesis
                    if char == "-" and number == "":
                        prev_element = elements[-1] if elements else None
                        if i == 0 or prev_element in ("(", "+", "-", "*", "/", "^", "%"):
                            number = "-"
                            continue
                    
                    if not number=="":
                        elements += (float(number),) # add the number to elements
                        number="" # Reset the number
                    elements += (char,) 

        if not number=="":
            elements += (float(number),) # Add this if it finish with a number
        return elements

    except Exception as e:
        return ("Erreur :", e)

