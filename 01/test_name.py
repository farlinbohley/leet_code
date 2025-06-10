print(f"In test_name.py: __name__ = '{__name__}'")

def show_name():
    print(f"Inside function: __name__ = '{__name__}'")

if __name__ == "__main__":
    print("This file was run directly!")
    show_name()
else:
    print("This file was imported as a module!")
