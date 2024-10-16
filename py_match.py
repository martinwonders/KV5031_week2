def phone_menu(option: int):
    match option:
        case 1:
            print("Calling Customer Services...")
        case 2:
            print("Accessing account information...")
        case 3:
            print("Connecting to technical support...")
        case 4:
            print("Speaking with a sales rep...")
        case _:
            print("Invalid option, please try again ")


#Testing
phone_menu(1)
phone_menu(2)
phone_menu(3)
phone_menu(4)
phone_menu(10)