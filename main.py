from sys import path,exit
path.append('modules')

from ask_operation import ask_operation
from operation_parser import operation_parser
from calcul_orchestrator import calcul_orchestrator
from display import display

def main():
    while True:
        try:
            operation = ask_operation()
            parsed_operation = operation_parser(operation)
            result = calcul_orchestrator(parsed_operation)
            display(result)
        except KeyboardInterrupt:
            print("\nThank you for using my-calculator.")
            exit(0)
        except:
            print("Something went wrong in the main function.")

if __name__ == "__main__":
    exit(main())