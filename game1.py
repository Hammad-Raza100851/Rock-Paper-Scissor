#ROCK PAPER SICESOR GAME
import random 
u = 0 
c = 0  

while True :
     
    you = input("Enter one of them (r , p , s ) and ( e ) for end : ").lower()
    your = {"r": 0, "p": 1, "s": 2}
    reverse = {0 : "Rock" , 1 : "Paper" , 2 : "Scissors" }
    if you == 'e' :
        break
    if you not in your :
        you = input("Enter one of them (r , p , s ): ").lower()
    else :
        your_choice = your[you]
        computer_choice = random.randint(0,2)
        print("you chose : " ,reverse[your_choice] )
        print("computer chose : " ,reverse[computer_choice] )

        if your_choice == computer_choice :
            print ("TIE \n")
        elif (your_choice == 0 and computer_choice == 2) or (your_choice == 1 and computer_choice == 0) or (your_choice == 2 and computer_choice == 1):
            print("You win! \n")
            u += 1
        else:
            print("Computer wins! \n")
            c += 1


print("\n--- FINAL SCORE ---\n")
print("Your score:", u)
print("Computer score:", c)

if u > c:
    print(" YOU WON THE TOURNAMENT!")
elif u < c:
    print(" COMPUTER WON THE TOURNAMENT!")
else:
    print(" IT'S A TIE!")