def main():
    
    num = input("Please input a number: ")
    try:
        if (int(num) > 5):
            print("thats a big number")
            print("Done")
        else: 
            print("thats a small number")
            main()
    except ValueError:
        print("thats not a number")
        main()
main()
