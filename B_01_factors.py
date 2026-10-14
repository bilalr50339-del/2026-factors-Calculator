# Generate headings (eg: ---- Heading ----)
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


# Ask user for an integer between 1 and 200
def num_check(question) :

    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)

            # check that the number is more than zero
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Works out factors, returns sorted list
def get_factors(to_factor):
    # x**(0.5) is the square root of x

    # We want to loop until we get the square root of to_factor
    # stop is the square root of the factor.
    # Basically instead of going from one to the number,
    # we go from 1 to 'stop' (which is the square root
    # of the number we are trying to factorise)

    factors_list = []

    # Square root the number to work out when to stop looping
    stop = to_factor**0.5
    stop = int(stop)

    for item in range(1, stop + 1):

        # if modulo is zero, then the number is a factor
        if to_factor % item == 0:
            # Add first factor to list
            factors_list.append(item)

            # find second factor by dividing 'to factor' by the first factor
            partner = to_factor // item

            # check second factor is not in list and add it
            if partner not in factors_list:
                factors_list.append(partner)

    # output
    factors_list.sort()
    return factors_list



# Main Routine Goes Here

statement_generator("The Ultimate Factor Finder", "-")

# Display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions "
                          " or any key to continue ")

if want_instructions == "":
    instructions()


while True:

    comment = ""

    #ask user for number to be factorised
    to_factor = num_check("\nEnter an integer (or xxx to quit): ")
    print("You chose to factor", to_factor)


    if to_factor == "xxx":
        break

    # get factors for integers that are 2 or more
    elif to_factor != 1:
        all_factors = get_factors(to_factor)

    # Set up comment for unity
    else:
        all_factors = ""
        comment = "One is UNITY! It only has one factor. Itself :)"

    # comments for squares / primes

    # Prime numbers have only two factors
    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number"

    # check if the list has an odd number of factors
    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square"

    # Set up headings
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."

    # output factors and comment
    print()
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)

print("Thank you for using the factors calculator.")
