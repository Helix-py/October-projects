import random 


failed_attemps = 0  # score var update later for each attempt to geuss the num resest when successfully geussed! 


def show_sc_at_st():
    global failed_attemps
    print(failed_attemps)




def gen_Rnum():  # genrate a random num the user must geuss. 
    Rnum = random.randint(1, 10) 
    print("number generated")
    return Rnum


def get_G_num():  # get the geussed number from the user. 
    G_num = int(input(f"what is your geuss"))
    return G_num


def start_game(): # main function that loops untill geussed correctly count tries with best_score var 
    Rnum = gen_Rnum()
    while True: 
        global failed_attemps
        G_num = get_G_num()
        if G_num == Rnum:
         choice = input("correct geuss would you like to continue? yes or no: ")
         if choice == "no":
             break 
        
        else:
          print("incorrect geuss")
          failed_attemps += 1 
          print(failed_attemps)
       
        
show_sc_at_st()
start_game()






 
 # frist attempt failure? 
 #   while inp != "exit":
       
 #     if inp == "exit":
 #      break