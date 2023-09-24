from random import *

print(" \n ")
print("There are three choices to select for user and computer \n\n")

print("======== Rules for winning this game ========== \n")

print("If you select choice 1st (Rock) \n Rock VS Paper -> Paper wins \n Rock VS Scissor -> Rock wins \n")

print("If you select choice 2nd (Paper) \n Paper VS Rock -> Paper wins \n Paper VS Scissor -> Scissor wins \n ")

print("If you select choice 3rd (Scissor) \n Scissor VS Rock -> Rock wins \n Scissor VS Paper -> Scissor wins \n ")


print("============ GAME START ============")

def check_winning():

    user_score = 0
    comp_score = 0

    while(True):
        for i in range(0,5):

            to_select = ["Rock","Paper","Scissor"]
            comp_choice = to_select[randint(0,2)]

            
            user_choice = str(input("enter your choice \n 1. Rock \n 2. Paper \n 3. Scissor \n choice should be grater than 0 and less than 4 \n"))
            if(user_choice=="1"):
                user_choice = "Rock"
            
            elif(user_choice=="2"):
                user_choice = "Paper"
            
            elif(user_choice=="3"):
                user_choice = "Scissor"
            else:
                pass
            user_choice.capitalize()

            if(user_choice==comp_choice):
                print("Computer choice name is : ",comp_choice)
                print(comp_choice," VS ",user_choice)
                print("It's Tie")
                res = "User score is : {0} \n Computer Score is : {1} \n"
                print(res.format(user_score,comp_score))

            if(comp_choice=="Rock"):
                if (user_choice=="Paper"):
                    user_score = user_score + 1
                    print("Computer choice name is : ",comp_choice)
                    print(comp_choice," VS ",user_choice)
                    print("User wins ! \n") 
                    res = "User score is : {0} \n Computer Score is : {1} \n"
                    print(res.format(user_score,comp_score))
                else:
                    comp_score = comp_score+1
                    print("Computer choice name is : ",comp_choice)
                    print(comp_choice," VS ",user_choice)
                    print("You lost ! \n")
                    res = "User score is : {0} \n Computer Score is : {1} \n"
                    print(res.format(user_score,comp_score))


            elif (comp_choice=="Paper"):
                if(user_choice=="Rock"):
                    comp_score = comp_score+1
                    print("Computer choice name is : ",comp_choice)
                    print(comp_choice," VS ",user_choice)
                    print("You lost \n")
                    res = "User score is : {0} \n Computer Score is : {1} \n"
                    print(res.format(user_score,comp_score))

                else:
                    user_score = user_score+1
                    print("Computer choice name is : ",comp_choice)
                    print(comp_choice," VS ",user_choice)
                    print("User Wins ! \n")
                    res = "User score is : {0} \n Computer Score is : {1} \n"
                    print(res.format(user_score,comp_score))

            elif(comp_choice=="Scissor"):
                if(user_choice=="Paper"):
                    comp_score=comp_score+1
                    print("Computer choice name is : ",comp_choice)
                    print(comp_choice," VS ",user_choice)
                    print("Computer Wins ! \n")
                    res = "User score is : {0} \n Computer Score is : {1} \n"
                    print(res.format(user_score,comp_score))
                else:
                    user_score = user_score+1
                    print("Computer choice name is : ",comp_choice)
                    print(comp_choice," VS ",user_choice)
                    print("User Win ! \n")
                    res = "User score is : {0} \n Computer Score is : {1} \n"
                    print(res.format(user_score,comp_score))

        if(user_score>comp_score):
            print("====== Finally User Wins !!!!  ============ \n")
        elif(comp_score>user_score):
            print("====== User lost !!!!  ============ \n")
        else:
            print("======== User and Computer have same score ========= \n")
        print("========== GAME OVER ============= \n")

        play_again_choice = str(input("do you want to play again ? Y or N "))

        if(play_again_choice == "Y" or play_again_choice == "y"):
            check_winning()

        elif(play_again_choice=="N" or play_again_choice == "n"):
            break

check_winning()


        
