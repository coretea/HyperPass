import auth_module
import login_modules
import USB_module

def main():
    choice = input("Welcome to HyperPass! \n1. login\n2. register")
    if choice == "1":
        auth_module.login()
    if choice == "2":
        auth_module.register()





if __name__ == "__main__":
    main()
