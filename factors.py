# !/u.sr/bin/env python3
# Created by: Angel
# Created on April 28,2025
# This program asks the user to input a
# number from a user without exceeding 1000 then
#  find all the factors of that number using a for
#  loop,a break statement and while loop too.


def main():  # it will define the function
    try:  # start a try block to avoid the program
        # from crashing.
        while True:  # we will start an infinite loop to
            # keep asking until a valid input
            user_num = int(input("Enter a positive under: "))
            # asks the user for an input as a string

            if user_num < 0 and user_num > 1000:
                # checks if the number is less than 0 and is
                # not greater than 1000
                print("This number is not valid.")  # tells the
                # user that it is not valid.

                if user_num == 0:  # checks if the
                    # number is not equal 0 and also is not a decimal
                    print("Number cannot be 0 and cannot be a decimal.")
                    #  tells the user that the number can't be 0 and
                    # can't be a decimal either.
            else:  # if not
                break  # it will exit the loo[ is the valid input is received]
        print(f"\nFactors of {user_num} are: ")  # Prints the list of the factors

        # loop from 1 for the userNum to fn the factors
        for n in range(1, user_num + 1):
            if user_num % n == 0:  # if n divided a user_number and the remainder is 0,
                # then it is a factor
                print(n)  # print out the factor
    except:  # if it fails to convert to int, display this messages
        print("Wrong number. Please enter a number.")  # print out


if __name__ == "__main__":  # this will check if the program is being run directly
    main()  # it will then call the main () function to start the program
