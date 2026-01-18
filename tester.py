from sys import path,exit
path.append('modules')

from ask_operation import ask_operation
from operation_parser import operation_parser
from calcul_orchestrator import calcul_orchestrator
from display import display

good_taste = (  ("1+1",2.0),
            ("2-1", 1.0),
            ("3*4", 12.0),
            ("8/2", 4.0),
            ("5//2", 2.0),
            ("7%3", 1.0),
            ("2^3", 8.0),
            ("0+5", 5.0),
            ("9-0", 9.0),
            ("4.5+1.5", 6.0),
            ("2+3*4", 14.0),
            ("10-6/3", 8.0),
            ("8%3+1", 3.0),
            ("2^3+1", 9.0),
            ("4*2-3",5.0),
            ("6/3+7",9.0),
            ("5//2+4",6.0),
            ("3.2*2",6.4),
            ("7.5-2.5",10.0),
            ("-3+8",5.0),
            ("(2+3)*4",20.0),
            ("6*(4-1)",18.0),
            ("10/(5-3)",5.0),
            ("(8%3)+4",6.0),
            ("(2^3)-1",7.0),
            ("(-3+5)*2",4.0),
            ("(4.5+1.5)*2",12.0),
            ("(7-2)//2", 2.0),
            ("(9-3)%4", 2.0),
            ("2*(3*(4))",24.0),
            ("((2+3)*4)-5", 15.0),
            ("6/(2*(1+2))", 1.0),
            ("(3*(2+(1*4)))",18.0),
            ("((8//3)+2)*3", 12.0),
            ("(2^3)+(4*(1+1))", 16.0),
            ("((5%3)+1)*4", 12.0),
            ("(3.5*(2+(1.5)))", 12.25),
            ("((7-3)*(2+2))", 16.0),
            ("(10-(3*(2+1)))", 1.0),
            ("((2^3)^1)+4", 12.0),
            ("((2+3)(4+(12)))", 80.0),
            ("(5*(3+(2*(1+1)))))",35.0),
            ("((8%3)+(4*(2^2)))", 18.0),
            ("(10-(3*(2+(1*1)))))", 1.0),
            ("((3.5+1.5)*(2+(3//2)))", 15.0),
            ("(2^3)+(3*(4-(2%2)))", 20,0),
            ("((7//3)*(5-(2/1)))", 6.0),
            ("(4*(3+(2*(1+(1))))))", 28.0),
            ("((2+(3*(4-(1)))))", 11.0),
            ("((2^3)+(4*(3-(1+(1)))))", 12.0))

bad_taste = ("2 & 3",
            "4a + 5",
            "3 + €5",
            "2++3",
            "4**2",
            "5//%2",
            "3+-*2",
            "*3+2",
            "/4+1",
            "%5+2",
            "3+",
            "4*",
            "7//",
            "(2+3",
            "2+3)",
            "((3+2)*2",
            "(3+())",
            "(*3+2)",
            "(+4*2)",
            "(3+2-)",
            "(4*3/)",
            "3 4 + 2",
            "12(3+2)")



def main():
    try:
        for operation in good_taste:
            parsed_operation = operation_parser(operation[0])
            result = calcul_orchestrator(parsed_operation)
            if result == operation[1]:
                display(result)
            else:
                print(f"The operation {operation[0]} returned {result} but we expected {operation[1]}.")
        
        for operation in bad_taste:
            parsed_operation = operation_parser(operation[0])
            result = calcul_orchestrator(parsed_operation)
            if result.isinstance(float):
                print(f"The operation {operation[0]} should've return an error.")

            
    except KeyboardInterrupt:
        print("\nThank you for using my-calculator.")
        exit(0)
    except:
        print("Something went wrong in the main function.")

if __name__ == "__main__":
    exit(main())