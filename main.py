# Empty Dictionary to store contact details
contacts = {}

# Infinite loop to continuously run the contact book until the user chooses to exit
while True:
    print("\nWELCOME TO MY CONTACT BOOK\n")
    print("1. Create New Contact")
    print("2. Update Contact")
    print("3. View Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contacts")
    print("7. Exit Phone Book\n")

    # Ask the user to select an option from the menu
    task_number = int(input("Enter the number of the task you want to perform: "))

    # Option 1: Create a new contact
    if task_number == 1:
        add_name = input("Enter Name you want to add: ").lower()  # Convert the name to lowercase for consistency
        if add_name in contacts:
            print(f"The name {add_name} is already in the Contact Book")
        else:
            # Get contact details from the user
            age = int(input("Enter Your Age: "))
            email = input("Enter Your Email: ")
            mobile_number = int(input("Enter Your Mobile Number: "))

            # Store the contact information in the dictionary
            contacts[add_name] = {'Age': age, 'Email': email, 'Mobile Number': mobile_number}
            print(f"The Name {add_name} has been created successfully")
            print(contacts.items())  # Display all contacts for reference

    # Option 2: Update an existing contact
    elif task_number == 2:
        update_contact_info = input("Enter the name you want to update: ").lower()
        if update_contact_info in contacts:
            # Get updated information from the user
            updated_age = int(input("Enter Your Updated Age: "))
            updated_email = input("Enter Your Updated Email: ")
            updated_mobile_number = int(input("Enter Your Updated Mobile Number: "))

            # Update the contact details
            contacts[update_contact_info] = {
                'Age': updated_age,
                'Email': updated_email,
                'Mobile Number': updated_mobile_number
            }
            
            print(f"Contact '{update_contact_info}' has been updated successfully.")
        else:
            print(f"The name '{update_contact_info}' is not found in the contact book.")

    # Option 3: View a contact
    elif task_number == 3:
        view_contact = input("Enter the name you want to view in the Contact Book: ").lower()
        if view_contact in contacts:
            view = contacts[view_contact]
            print(f"The info of {view_contact} is below\n{view}")
        else:
            print(f"The Name {view_contact} is not found in the Contact Book")

    # Option 4: Delete a contact
    elif task_number == 4:
        del_contact = input("Enter the name you want to delete: ").lower()
        if del_contact in contacts:
            del contacts[del_contact]
            print(f"The contact {del_contact} has been deleted successfully!")
        else:
            print(f"The Name {del_contact} is not found in the Contact Book")

    # Option 5: Search for a contact
    elif task_number == 5:
        search_name = input("Enter the name you want to search: ").lower()
        found = False
        for contact_name, contact_info in contacts.items():
            if search_name in contact_name:  # Check if the search term matches any name
                print(f"Found _ Name: {contact_name}, 'Age': {contact_info['Age']}, 'Email': {contact_info['Email']}, 'Mobile Number': {contact_info['Mobile Number']}")
                found = True
        if not found:
            print(f"The Name {search_name} is not found in the Contact Book")

    # Option 6: Count the total number of contacts
    elif task_number == 6:
        print(f"Total number of Contacts is:", len(contacts))

    # Option 7: Exit the program
    elif task_number == 7:
        print("You have exited the Contact Book\nThank you!!")
        break

    # Invalid input handling
    else:
        print(f"\nEnter a valid number from 1 to 7")
