import re

def ask_operation(last_result=None):
    """
    Asks the user for a mathematical expression and validates it.
    - last_result: The previous calculation result (default is None).
    - Returns: A validated string ready for processing or a command ('h', 'c').
    """
    # Ask the user for the operation
    user_input = input("Enter operation (or 'h' for history, 'c' to clear): ").strip()

    # 1. EMPTY INPUT CHECK
    if not user_input:
        return "Error: The input cannot be empty."

    # 2. COMMAND PASSTHROUGH
    # Allow history commands to pass directly to the main orchestrator
    if user_input.lower() in ['h', 'c']:
        return user_input.lower()

    # 3. START/END CHARACTER CHECK (Dot and Comma)
    if user_input[0] in ".," or user_input[-1] in ".,":
        return "Error: Expression cannot start or end with a dot or a comma."

    # 4. DOUBLE OPERATOR CHECK (Modified to allow //)
    # Block ++, --, and ** if re.search(r'([\+\-\*])\s*\1', user_input):
        return "Error: Consecutive identical operators (+, -, *) are not allowed."
    
    # Block more than two slashes (e.g., ///)
    if "///" in user_input.replace(" ", ""):
        return "Error: Too many consecutive division operators."

    # 5. LAST_RESULT LOGIC (Cumulative calculation)
    operators = "+-*/"
    if user_input[0] in operators:
        # Check if it's a negative number (e.g., "-3*3") or an operator continuation (e.g., "+5")
        # A negative number has a digit or opening parenthesis right after the minus sign
        if user_input[0] == "-" and len(user_input) > 1 and (user_input[1].isdigit() or user_input[1] == "("):
            # This is a negative number, not an operator continuation
            pass
        elif last_result is None:
            return "Error: Cannot start with an operator because there is no previous result."
        else:
            # Prepend the last result to the current input string
            user_input = str(last_result) + user_input

    # 6. CHARACTER VALIDATION (Regex)
    # Added 'h' and 'c' to the allowed characters for the history triggers
    if not re.match(r'^[0-9\+\-\*\/\(\)\%\^\!\.\s,hc]+$', user_input, re.IGNORECASE):
        return "Error: Forbidden characters or letters detected."

    # 7. TRANSFORMATION (Comma to Point)
    user_input = user_input.replace(',', '.')

    # 8. END-OF-STRING OPERATOR CHECK
    if user_input[-1] in operators:
        return "Error: The expression is incomplete (ends with an operator)."

    # 9. MATHEMATICAL SANITY CHECKS
    # Check for balanced parentheses
    if user_input.count('(') != user_input.count(')'):
        return "Error: Missing or mismatched parentheses."

    # Check for division by zero (handles both /0 and //0)
    clean_input = user_input.replace(" ", "")
    if "/0" in clean_input or "//0" in clean_input:
        return "Error: Division by zero is impossible."

    # Return the clean string for the parser
    return user_input