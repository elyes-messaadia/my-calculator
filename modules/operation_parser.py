def operation_parser(operation):
    """Convert an operation string into a Tuple list of each elements"""

    try :
        elements = ()
        number = "" # Initialize number to empty string

        for char in operation: # for each character in operation string
            match char:
                case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | ".":
                    number += char #build the number

                case "(" | ")" | "+" | "-" | "/" | "*":
                    if not number=="":
                        elements += (float(number),) # add the number to elements
                        number="" # Reset the number
                    elements += (char,) 

        if not number=="":
            elements += (float(number),) # Add this if it finish with a number
        return elements

    except Exception as e:
        return ("Erreur :", e)

