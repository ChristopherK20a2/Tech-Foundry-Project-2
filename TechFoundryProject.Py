import random


def cnj_check(player, comp):

    if player == "ninja" and comp == "cowboy":
        return "You win!"
    elif player == "cowboy" and comp == "bear":
        return "You win!"
    elif player == "bear" and comp == "ninja":
        return "You win!"
    elif player == comp:
        return "Tie!"
    else:
        return "The computer always wins!"


def comp_choice():

    num = random.randrange(1, 4)

    if num == 1:
        return "cowboy"
    elif num == 2:
        return "bear"
    else:
        return "ninja"


player_wins = 0
comp_wins = 0
total_games = 0


while True:

    player_input = (input("Pick cowboy, ninja, or bear(Ninja beats Cowboy, Cowboy beats Bear, Bear beats Ninja:\n")).lower()
    flag = True

    while flag:
        if player_input == "cowboy":
            flag = False
        elif player_input == "ninja":
            flag = False
        elif player_input == "bear":
            flag = False
        else:
            player_input = input("Please enter a valid input:\n")

    comp_input = comp_choice()
    print("The computer chose " + str(comp_input) + "!")
    print(cnj_check(player_input, comp_input))

    if str(cnj_check(player_input, comp_input)) == "You win!":
        player_wins += 1
        total_games += 1
    elif str(cnj_check(player_input, comp_input)) == "The computer wins!":
        comp_wins += 1
        total_games += 1
    else:
        total_games += 1

    print("You won " + str(player_wins) + " game(s) out of " + str(total_games) + ".\n")
    flag = True