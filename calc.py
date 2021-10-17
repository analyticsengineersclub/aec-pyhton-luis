# calc.py
import argparse

parser = argparse.ArgumentParser(description = "CLI Calculator.")

subparsers = parser.add_subparsers(help = "sub-command help", dest="command")

# Add
add = subparsers.add_parser("add", help = "add integers. Use as many digits as desired")
add.add_argument("ints_to_sum", nargs=4, type=int)

# Sub 
sub = subparsers.add_parser("sub", help='substaract integers. Use 4 digits')
sub.add_argument("ints_to_sub", nargs=4, type=int)

# Multiplication
multiply = subparsers.add_parser("multiply", help='multiply integers. Use 4 digits')
multiply.add_argument("ints_to_multiply", nargs=4, type=int)

# Division
divide = subparsers.add_parser("divide", help='divide integers. Use 4 digits')
divide.add_argument("ints_to_divide", nargs=2, type=int)

args = parser.parse_args()

if args.command == "add":
    our_sum = sum(args.ints_to_sum)
    print(f"the sum of values is: {our_sum}")

if args.command == 'sub':
	our_sub = args.ints_to_sub[0] - args.ints_to_sub[1] - args.ints_to_sub[2] - args.ints_to_sub[3]
	print(f"The subtracted of values is  {our_sub}")

if args.command == 'multiply':
	our_multiply = args.ints_to_multiply[0] * args.ints_to_multiply[1] * args.ints_to_multiply[2] * args.ints_to_multiply[3]
	print(f"The product of values is  {our_multiply}")

if args.command == 'divide':
	our_division = (args.ints_to_divide[0] / args.ints_to_divide[1]) if args.ints_to_divide[1] != 0 else 'Check denominator for non-zero value'
	print(f"The division of values is: {our_division}")