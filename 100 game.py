# 100_Game
# By : Mohamed Wael Ibrahim
# Date : 20/2/2022

# This game between two players that each other chooses a number from 0 to 10
# The player who reach to 100 first will win

sum = 0
print("Enter number between 0 to 10")
while True:
    player1 = int(input("Player-1 turn: "))
    if (player1 > 10 or player1 < 1):
        print("Just from 1 to 10")
        break
    sum = sum + player1
    print("The score is: " + str(sum))
    if (sum>=100):
        print("Player-1 wins")
        break
    player2 = int(input("Player-2 turn: "))
    if (player2 > 10 or player2 < 1):
        print("Just from 1 to 10")
        break
    sum = sum + player2
    print("The score is: " + str(sum))
    if (sum>=100):
        print("Player-2 wins")
        break
