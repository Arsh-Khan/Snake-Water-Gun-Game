import random
gamem=['w','g','s']

def game(n):
    countp=0
    countc=0
    print("Welcome to Snake Water Gun Game")
    print("\nInstructions :")
    print("1) This Game will be played against the Computer")
    print("2) Enter: \n\t1)'w' for Water \n\t2)'g' for Gun \n\t3)'s' for Snake")
    print('''3) Snake vs. Water: Snake drinks the water hence wins.
   Water vs. Gun: The gun will drown in water, hence a point for water
   Gun vs. Snake: Gun will kill the snake and win.''')
    print("4) If player wons any round he will be awarded with 1 points")
    print("5) If there is a tie , no points will be given")
    print("6) Whosoever Scores the most points in all rounds Wins")

    for i in range(1,n+1):
        print(f"\nRound {i} begins:")
        inp=input("Enter: \n1)'w' for Water \n2)'g' for Gun \n3)'s' for Snake\n")
        comp=random.choice(gamem)
        print("Player Choses "+inp)
        print("Computer Choses "+comp)
        if(inp=='w'or inp=='s' or inp=='g'):
            if(inp=='w'):
                if(inp==comp):
                    print("TIE")
                elif(comp=='g'):
                    print("Gun got drown in Water")
                    print("User wins")
                    countp=countp+1
                elif(comp=='s'):
                    print("Snake drank the Water")
                    print("Computer Wins")
                    countc=countc+1
            
            if(inp=='g'):
                    if(inp==comp):
                        print("TIE")
                    elif(comp=='w'):
                        print("Gun got drown in Water")
                        print("Computer wins")
                        countc=countc+1
                    elif(comp=='s'):
                        print("Snake was shot by Gun")
                        print("User Wins")
                        countp=countp+1
        
            if(inp=='s'):
                    if(inp==comp):
                        print("TIE")
                    elif(comp=='g'):
                        print("Snake got shot by Gun")
                        print("Computer wins")
                        countc=countc+1
                    elif(comp=='w'):
                        print("Snake drank the Water")
                        print("User Wins")
                        countp=countp+1
        else:
            print("OOPS! Wrong Entry \n You Wasted this round")

    print("\nFinal Score:\n ")
    print(f"Player = {countp}")        
    print(f"Computer = {countc}")

    if(countp>countc):
        print("\nCongratulations , You won the Game against the Computer")
    elif(countc>countp):
        print("\nSorry , You Lost the Game against the Computer")
    else:
        print("\nIts a Draw against the computer")            
            

print("\t\t\t\t\t\t\t\tSnake Water Gun Game")
n = int(input("\nEnter No of Rounds :\n"))
game(n)

k=input("Press any key for Exit")
