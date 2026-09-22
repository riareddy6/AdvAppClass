# Program Name: Assignment1.py
# Course: IT 3883, SEC 01(?)
# Student Name: Ria Reddy
# Assignment Number: Assignment 1 Due
# Date: 09/22/2026

# Purpose: Python program that implements a text-based menu. The menu should present the user with
# the following 4 choices: append data to input buffer, clear input buffer, display input buffer, or exit the
# program.

# Resources Used: Course Module 1 slides, some past class notes for review (IT 1114, CSE 1321)


#Create input buffer
def main():
    input_buffer = ""

    # The options menu, as defined by AS1 instructions
    while True:
        print("What would you like to do?")
        print("1. Append data to the input buffer")
        print("2. Clear the input buffer")
        print("3. Display the input buffer")
        print("4. Exit the program")

        choice = input("Select an option(1-4): ").strip()

        # Option 1: Append buffer (can include past input)
        if choice == "1":
            additional_data = input("Enter the text you want to append: ")
            input_buffer += additional_data
            print("The input buffer has been appended.")

        # Option 2: clear buffer
        elif choice == "2":
            input_buffer = ""
            print("The input buffer has been cleared.")

        # Option 3: display buffer. If nothing, say empty.
        elif choice == "3":
            #message is separated from input buffer text display
            print("\n Current input buffer:")

            #nothing
            if input_buffer == "":
                print("[The input buffer is empty]")

            else:
                print(input_buffer)


        # Option 4: exit program.
        elif choice == "4":
            print("Bye bye user.")
            break

        # Invalid input message, will ask options again until valid input
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")





if __name__ == "__main__":
    main()
