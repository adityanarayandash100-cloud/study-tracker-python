def add_study():
    subject = input("Enter subject: ")
    hours = input("Enter hours studied: ")

    with open("data.txt", "a") as file:
        file.write(f"{subject},{hours}\n")

    print("Record saved!")


def view_records():
    try:
        with open("data.txt", "r") as file:
            print("\n--- Study Records ---")
            print(file.read())
    except:
        print("No records found yet.")


while True:
    print("\n===== Study Tracker =====")
    print("1. Add Study")
    print("2. View Records")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_study()
    elif choice == "2":
        view_records()
    elif choice == "3":
        print("Thank you. Bye!")
        break
    else:
        print("Invalid option. Try again.")