def statement_generator(statement, decoration) :
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
To use this program simply enter an integer between
1 and 200. The program will show the factors of your
chosen integer.

It will also tell you if your chosen number...
- Is a prime number (ie: It has two factors)
- Is a perfect square 

To exit the program, please type 'xxx'
  ''')



# Main Routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

print("program continues")