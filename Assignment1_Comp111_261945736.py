'''one="1"
username=input("Username:")
password=input("Password:")
userp="user123"
adminp="admin123"
if password==userp:
    print("WELCOME USER:")
    print("1.Book a ticket")
    print("2.Cancel a booking")
    print("3.Show flights")
    choice=input("Enter the corresponding number:")
    if choice==one:
        print("Available flights:")
        print("1.Flight company A")
        print("2.Flight company B")
        choice2=input("Choose a flight (enter the corresponding number)")


seat_layout=[['*'for _ in range(6)]for _ in range(5)]
for i in range(len(seat_layout)):
        print('Row ',i+1,'.',seat_layout[i])

# Function to display the seat layout
def display_seat_layout(seat_layout):
    for i in range(len(seat_layout)):
        print('Row', i + 1, ':', ' '.join(seat_layout[i]))

# Initialize the seat layout as a 2D array
rows = 5
columns = 6
seat_layout = [['*' for _ in range(columns)] for _ in range(rows)]

# Display the current seat layout
print("Current seat layout:")
display_seat_layout(seat_layout)

# Prompt the user for their name
user_name = input("Enter your name: ")


# Prompt the user for seat booking
while True:
    try:
        row = int(input("Enter the row number (1-5) for booking (0 to exit): "))
        if row == 0:
            break
        column = int(input("Enter the column number (1-6) for booking: "))
        
        if 1 <= row <= rows and 1 <= column <= columns and seat_layout[row - 1][column - 1] == '*':
            seat_layout[row - 1][column - 1] = 'X'
            print("Seat booked successfully!")
            
            # Generate and print a booking confirmation ticket
            print("\nBooking Confirmation Ticket")
            print("----------------------------")
            print("Name:", user_name)
            print("Flight Company:", choice2)
            print("Seat:", f"Row {row}, Column {column}")
            print("----------------------------\n")
        else:
            print("Invalid seat selection. Please try again.")
        
        # Display the updated seat layout
        print("Updated seat layout:")
        display_seat_layout(seat_layout)
    except ValueError:
        print("Invalid input. Please enter valid row and column numbers.")

# Save the updated seat layout to a file
with open("seat_layout.txt", "w") as file:
    for row in seat_layout:
        file.write(' '.join(row) + '\n')

print("Seat layout saved to seat_layout.txt.")
'''
# Function to display the seat layout
def display_seat_layout(seat_layout):
    for i in range(len(seat_layout)):
        print('Row', i + 1, ':', ' '.join(seat_layout[i]))

# Initialize the seat layout as a 2D array
rows = 5
columns = 6
seat_layout = [['*' for _ in range(columns)] for _ in range(rows)]

# Display the current seat layout
print("Current seat layout:")
display_seat_layout(seat_layout)

# Prompt the user for their name
user_name = input("Enter your name: ")

while True:
    try:
        one = "1"
        two = "2"
        username = input("Username:")
        password = input("Password:")
        userp = "user123"
        adminp = "admin123"

        if password == userp:
            print("WELCOME USER:")
            print("1.Book a ticket")
            print("2.Cancel a booking")
            print("3.Show flights")
            choice = input("Enter the corresponding number:")

            if choice == one:
                print("Available flights:")
                print("1.Flight company A")
                print("2.Flight company B")
                choice2 = input("Choose a flight (enter the corresponding number)")

            elif choice == two:
                # Allow the user to cancel a booking
                try:
                    row = int(input("Enter the row number (1-5) to cancel the booking (0 to exit): "))
                    if row == 0:
                        break
                    column = int(input("Enter the column number (1-6) to cancel the booking: "))

                    if 1 <= row <= rows and 1 <= column <= columns and seat_layout[row - 1][column - 1] == 'X':
                        seat_layout[row - 1][column - 1] = '*'
                        print("Booking canceled successfully!")
                        
                        # Generate and print a cancellation confirmation
                        print("\nBooking Cancellation Confirmation")
                        print("----------------------------")
                        print("Name:", user_name)
                        print("Flight Company:", choice2)
                        print("Seat Canceled:", f"Row {row}, Column {column}")
                        print("----------------------------\n")
                    else:
                        print("Invalid seat selection. Please try again.")

                    # Display the updated seat layout
                    print("Updated seat layout:")
                    display_seat_layout(seat_layout)
                except ValueError:
                    print("Invalid input. Please enter valid row and column numbers.")
            
        else:
            print("Invalid username or password. Please try again.")

    except ValueError:
        print("Invalid input. Please enter valid row and column numbers.")

# Save the updated seat layout to a file
with open("seat_layout.txt", "w") as file:
    for row in seat_layout:
        file.write(' '.join(row) + '\n')

print("Seat layout saved to seat_layout.txt.")
