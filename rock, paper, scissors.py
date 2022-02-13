import random

print("WELCOME TO THIS GAME OF ROCK, PAPER AND SCISSORS")
print("I HAVE CHOOSEN MINE, NOW YOU CHOOSE!")

comp_turn = random.randint(1,3)

ui= input(str("R (ROCK), P (PAPER),S (SCISSORS): "))
ui.lower()

while True:
    if ui== "r":
        if comp_turn==1:
            print("IT'S A TIE")
            print("COMPUTER CHOSE: ROCK")
        
        if comp_turn==2:
            print("COMPUTER WON, BETTER LUCK NEXT TIME")
            print("COMPUTER CHOSE: PAPER")
        
        if comp_turn==3:
            print("YOU WON!!")
            print("COMPUTER CHOSE: SCISSORS")

    elif ui=="p":
        if comp_turn==1:
            print("YOU WON!!")
            print("COMPUTER CHOSE: ROCK")
        
        if comp_turn==2:
            print("IT'S A TIE")
            print("COMPUTER CHOSE: PAPER")
        
        if comp_turn==3:
            print("COMPUTER WON, BETTER LUCK NEXT TIME")
            print("COMPUTER CHOSE: SCISSORS")

    elif ui=="s":
        if comp_turn==1:
            print("COMPUTER WON, BETTER LUCK NEXT TIME")
            print("COMPUTER CHOSE: ROCK")
        
        if comp_turn==2:
            print("YOU WON!!")
            print("COMPUTER CHOSE: PAPER")

        if comp_turn==3:
            print("IT'S A TIE")
            print("COMPUTER CHOSE: SCISSORS")

    else:
        print("INVAID INPUT")

    exit_input = input(str("DO YOU WANT TO PLAY AGAIN?? (Y/N): ")).lower()

    if exit_input=="y":            
        comp_turn = random.randint(1,3)
        ui= input(str("R (ROCK), P (PAPER),S (SCISSORS): "))
        ui.lower()
    elif exit_input=="n":
        exit("THANKS FOR PLAYING!!!")
        break
    else:
        print("INVALID INPUT!!")
        while True:
            second_exit_input = input(str("DO YOU WANT TO PLAY AGAIN?? (Y/N): ")).lower()
            if second_exit_input=="y":
                comp_turn = random.randint(1,3)
                ui= input(str("R (ROCK), P (PAPER),S (SCISSORS): "))
                ui.lower()
                break
            elif second_exit_input=="n":
                exit("THANKS FOR PLAYING")
                break
            else:
                print("INVALID INPUT!!")
                continue