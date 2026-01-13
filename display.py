def display(final_result):
    """
    Displays the result on the calculator's screen.
    Handles both numerical results and error messages.
    """
    print("\n--- CALCULATOR SCREEN ---")
    
    # Check if the result is a number (int or float)
    if isinstance(final_result, (int, float)):
        # Optimization: remove .0 if it's a whole number, 
        # otherwise round to 4 decimal places for clarity.
        if final_result % 1 == 0:
            formatted_res = int(final_result)
        else:
            formatted_res = round(final_result, 4)
            
        print(f"|  RESULT: {formatted_res}")
    else:
        # If the result is an error string (from ask_operation)
        print(f"|  STATUS: {final_result}")
        
    print("--------------------------\n")