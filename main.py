import class_info

def main():
        print("Welcome to Soul Scrape!")
        print("  * Current Studio: West 77th\n")

        option = input("Choose an option: reserve[1] or browse[2]: ")
        if option == 1:
                print("reservee")    
        elif option == 2:
               class_info.get_info()
        else:
               print("goodbye!\n")
               return


if __name__ == "__main__":
    main()