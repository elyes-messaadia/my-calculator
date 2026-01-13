import re

def ask_operation(last_result=None):
    """
    Asks the user for a mathematical expression and validates it.
    - last_result: The previous calculation result (default is None).
    - Returns: A validated string ready for processing.
    """
    # Ask the user for the operation
    user_input = input("Enter your operation: ").strip()

    # 1. EMPTY INPUT CHECK
    if not user_input:
        return "Error: The input cannot be empty."

    # 2. START/END CHARACTER CHECK (Dot and Comma)
    # The string cannot start or end with a dot or a comma
    if user_input[0] in ".," or user_input[-1] in ".,":
        return "Error: Expression cannot start or end with a dot or a comma."

    # 3. LAST_RESULT LOGIC (Cumulative calculation)
    # If last_result is None, it cannot start with an operator
    operators = "+-*/"
    if user_input[0] in operators:
        if last_result is None:
            return "Error: Cannot start with an operator because there is no previous result."
        else:
            # If last_result exists, prepend it to the string
            user_input = str(last_result) + user_input

    # 4. CHARACTER VALIDATION (Regex)
    # Allows only numbers, operators, parentheses, spaces, dots, and commas
    if not re.match(r'^[0-9\+\-\*\/\(\)\.\s,]+$', user_input):
        return "Error: Forbidden characters or letters detected."

    # 5. TRANSFORMATION (Comma to Point)
    # Convert every comma to a dot for Python compatibility
    user_input = user_input.replace(',', '.')

    # 6. END-OF-STRING OPERATOR CHECK
    # A calculation cannot end with an operator (e.g., "5 +")
    if user_input[-1] in operators:
        return "Error: The expression is incomplete (ends with an operator)."

    # 7. MATHEMATICAL SANITY CHECKS
    # Check for balanced parentheses
    if user_input.count('(') != user_input.count(')'):
        return "Error: Missing or mismatched parentheses."

    # Check for division by zero
    if "/0" in user_input.replace(" ", ""):
        return "Error: Division by zero is impossible."

    # Return the clean string as requested
    return user_input