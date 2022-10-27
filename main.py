import textsender as text

def main():
    print("hi" + "-"*10)
    user_name = input("Enter ur name: ")
    user_phone = input("enter ur number")

    print()
    print("what do u wanna do?")
    print("press [ Q ] to start process of scanning prescription")
    print("press [ L ] to view list of prescriptions")

    available_options = ("Q", "L")
    user_selection = ""
    while user_selection not in available_options:
        user_selection = input("choose Q or L: ")

    if user_selection == "Q":
        print("sending u a message")
        text.send("hello", "3523286375")

        # call the scanner module
        # open a video window
        # prompt user to take a picture

        # picture = scanner.picture for example

        # use picture in a text recog model

        # add the info to db

    if user_selection == "L":
        pass# list the info in the db


    # need some timer or something running constantly to
    # send notifications


if __name__ == "__main__":
    main()