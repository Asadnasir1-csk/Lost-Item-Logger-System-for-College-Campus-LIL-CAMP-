from scripts.week1_basics import welcome
from scripts.week2_io import get_item
from scripts.week3_conditions import validate
from scripts.week4_loops import display
from scripts.week5_functions import generate_id
from scripts.week7_data_structures import create_item
from scripts.week8_advanced_ds import find_item
from scripts.week10_files import load, save
from scripts.week11_exceptions import safe_input
from scripts.week12_analytics import report

def main():
    welcome()
    items = load()

    while True:
        print("\n1. Report Lost Item")
        print("2. View Items")
        print("3. Mark as Found")
        print("4. Report")
        print("5. Exit")

        choice = safe_input()

        if choice == 1:
            name, location = get_item()
            if validate(name, location):
                iid = generate_id(items)
                item = create_item(iid, name, location)
                items.append(item)
                save(items)

        elif choice == 2:
            display(items)

        elif choice == 3:
            iid = int(input("Enter Item ID: "))
            item = find_item(items, iid)
            if item:
                item['status'] = 'Found'
                save(items)

        elif choice == 4:
            report(items)

        elif choice == 5:
            break

if __name__ == "__main__":
    main()
