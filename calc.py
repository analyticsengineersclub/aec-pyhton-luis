# calc.py
import argparse

parser = argparse.ArgumentParser(description = "CLI Calculator.")

subparsers = parser.add_subparsers(help = "sub-command help", dest="command")

# Add
add = subparsers.add_parser("add", help = "add integers. Use as many digits as desired")
add.add_argument("ints_to_sum", nargs=4, type=int)

# Sub 
sub = subparsers.add_parser("sub", help='substaract integers. Use 4 digits')
sub.add_argument("ints_to_sub", nargs="+", type=int)

def subtract_func(ints_to_sub):
    if len(ints_to_sub) > 4:
        raise Exception("Only four arguments allowed for subtraction")
    else:
        our_sub = ints_to_sub[0] - ints_to_sub[1] - ints_to_sub[2] - ints_to_sub[3]
        if our_sub < 0:
            our_sub = 0
        print(f"The subtracted of values is  {our_sub}")
    return our_sub

# Multiplication
multiply = subparsers.add_parser("multiply", help='multiply integers. Use 4 digits')
multiply.add_argument("ints_to_multiply", nargs=4, type=int)

# Division
divide = subparsers.add_parser("divide", help='divide integers. Use 4 digits')
divide.add_argument("ints_to_divide", nargs="+", type=int)

def divide_func(ints_to_divide):
    if len(ints_to_divide) > 2:
        raise Exception("Only two arguments allowed to divide")
    
    elif ints_to_divide[1] <= 0:
        print ("Error: Denominator is 0 or lower")
        return 0
    
    else:
        our_division = (ints_to_divide[0] / ints_to_divide[1]) 
        print(f"Result of division is: {our_division}")     
        return our_division

if __name__ == '__main__':
    args = parser.parse_args()

    if __name__ == "__main__":
        args = parser.parse_args()

    if args.command == "add":
        our_sum = sum(args.ints_to_sum)
        print(f"the sum of values is: {our_sum}")

    if args.command == 'sub':
        subtract_func(args.ints_to_sub)

    if args.command == 'multiply':
        our_multiply = args.ints_to_multiply[0] * args.ints_to_multiply[1] * args.ints_to_multiply[2] * args.ints_to_multiply[3]
        print(f"The product of values is  {our_multiply}")

    if args.command == 'divide':
        divide_func(args.ints_to_divide)
        