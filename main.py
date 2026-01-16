from sys import path, exit
path.append('modules')

from ask_operation import ask_operation     
from operation_parser import operation_parser
from calcul_orchestrator import calcul_orchestrator
from display import display
# Import history management functions
from history_manager import save_to_history, get_history, clear_history                                    

def main():
    # Stores the last result to allow cumulative calculations (e.g., entering "+5")
    last_result = None 
    
    while True:
        try:
            # Pass last_result to allow the user to continue from the previous calculation
            operation = ask_operation(last_result)

            # 1. Handle history commands
            if operation.lower() == 'h':
                print("\n--- CALCULATOR HISTORY ---")
                print(get_history())
                print("--------------------------\n")
                continue # Skip to the next iteration
            
            if operation.lower() == 'c':
                print(clear_history())
                continue

            # 2. Check if ask_operation returned an error message
            if operation.startswith("Error"):
                print(operation)
                continue

            # 3. Standard calculation process
            parsed_operation = operation_parser(operation)
            result = calcul_orchestrator(parsed_operation)
            
            # 4. Display and SAVE the result
            display(result)
            save_to_history(operation, result)
            
            # Update last_result for the next turn
            last_result = result

        except KeyboardInterrupt:
            print("\nThank you for using my-calculator.")
            exit(0)
        except Exception as e:
            # Catch and display unexpected errors for debugging
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()