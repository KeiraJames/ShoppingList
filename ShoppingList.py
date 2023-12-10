from LinkedList import LinkedList


def prompt():
    user_input = int(input("Enter your choice: "))
    return user_input

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
        print("Number invalid, try again.")
        user_input = prompt()

print("Thank you for using your shopping list!")
