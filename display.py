def display(final_result):
    """
    Displays the result or the error message on the calculator interface.
    """
    print("\n" + "="*30)
    # Check if the result is a numeric value (success)
    if isinstance(final_result, (int, float)):
        # Formatting: remove .0 for integers and limit decimals
        formatted = int(final_result) if final_result % 1 == 0 else round(final_result, 4)
        print(f" RESULT : {formatted}")
    else:
        # Display the error string returned by ask_operation
        print(f" STATUS : {final_result}")
    print("="*30 + "\n")