import class_info
import login_reserve
import getpass

my_username = "javier.friedman@tufts.edu"

def main():
        print("Welcome to Soul Scrape!")
        print("  * Current Studio: West 77th\n")

        option = input("Choose an option: reserve[1] or browse[2]: ")
        option = int(option)
        if option == 1:
                password = getpass.getpass("      Enter password: ")
                login_reserve.login(my_username, password)
        elif option == 2:
               class_info.get_info()
        else:
               print("goodbye!\n")
               return


if __name__ == "__main__":
    main()