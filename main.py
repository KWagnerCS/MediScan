import textsender as text
import ocr

def print_menu():
    print("*" * 49)
    print("=" * 10 + "     Welcome to MediScan     " + "=" * 10)
    print("*" * 49)
    print("~" * 2 + " Receive Text Notifications for Prescriptions")
    print("~" * 2 + " Never Forget to Take Medicine Again")
    print("~" * 2 + " Simple and Efficient Text Based UI")
    print()
    print("~" * 2 + " Instructions:")
    print("~" * 2 + " Take a picture of a prescription")
    print("~" * 2 + " Select the picture in MediScan")
    print("~" * 2 + " Enter phone number and receive text notifications")
    print("*" * 49)
    print()

def main():
    print_menu()
    file_input = input("Select an image to scan: ")
    print()
    p_text = ocr.read_image(file_input)
    drug_name = p_text[(p_text.find("Drug Name:") + 11):(p_text.find("Concentration"))]
    print("~~ Name of Drug:")
    print(drug_name)
    drug_concentration = p_text[(p_text.find("Concentration:") + 15):(p_text.find("Directions"))]
    print("~~ Drug Concentration:")
    print(drug_concentration)
    drug_directions = p_text[(p_text.find("Directions:") + 12):]
    print("~~ Directions:")
    print(drug_directions)

    user_name = input("Enter your name: ")
    user_phone = input("Enter your phone number: ")

    prescription_message = "\n~~ MediScan Prescription Reminder ~~" + "\n" + "Hello " + user_name + "!\n" + "Drug: " + drug_name + "\n" + "Concentration: " + drug_concentration + "\n" + "Directions: " + drug_directions

    text.send(prescription_message[:128], user_phone)

if __name__ == "__main__":
    main()