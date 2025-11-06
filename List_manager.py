mini_mang = [] 


def show_options(): 
    print("a. add to list")
    print("b. remove from list")
    print("c. view current list alphabetically")
    print("d. leave program")
    
while True: 
    show_options()
    choice = input("pick letters a-d: ")
    
    if choice == ("a"):
       letter_to_add = input("what letter would you like to add?: ")
       mini_mang.append(letter_to_add)
       print(f"{mini_mang} success")
       
    elif choice == ("b"):
        letter_to_remove = input("what letter would you like to remove?: ")
        if letter_to_remove in mini_mang:
            mini_mang.remove(letter_to_remove) 
            print(f"{mini_mang} success")
        else:
            print("not found")
            
    elif choice == ("c"):
        mini_mang.sort()
        print(f"{mini_mang} success")
        
    elif choice == ("d"):
        break
