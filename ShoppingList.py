from LinkedList import LinkedList


def prompt():
    try:
        user_input = input("Enter your choice: ")
        user_input = int(user_input)
        return user_input
    except ValueError:
        print("Invalid input. Please enter a number.")

def add_to_list(ll):
    item = input("Enter item to add: ")
    ll.add(item)

def remove_from_list(ll):
    index = int(input("Enter item number to remove: "))
    ll.remove_specific_index(index=index-1)

def view_list(ll):
    print("Current items in the shopping list:")
    ll.display_list()


ll = LinkedList()

print("Welcome to your Shopping List!\n")
print("1. Add an item to the shopping list.")
print("2. Remove an item from the shopping list.")
print("3. View the current items in the shopping list.")
print("4. Quit\n")

user_input = prompt()

while user_input != 4:

    if user_input == 1:
        add_to_list(ll)
        user_input = prompt()
    elif user_input == 2:
        remove_from_list(ll)
        user_input = prompt()
    elif user_input == 3:
        view_list(ll)
        user_input = prompt()
    else:
        if isinstance(user_input, int):
            print("Number invalid, try again.")
        user_input = prompt()

print("Thank you for using your shopping list!")
