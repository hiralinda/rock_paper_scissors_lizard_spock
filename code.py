import random


def play():
    user = input("Choose: rock, paper, scissors, lizard or spock\n")
    user = user.lower()
    computer = random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])


    if user == computer:
        print(f"Computer chose {computer} so, ")
        print ('It\'s a tie')

    elif is_win(user, computer):
        print(f"Computer chose {computer} so, ")
        print ('You won')

    else:
        print(f"Computer chose {computer} so, ")
        print ('You lost')

def is_win(player, opponent):
    if(player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper')\
        or (player == 'paper' and opponent == 'rock') or (player == 'rock' and opponent == 'lizard') \
        or (player == 'scissors' and opponent == 'lizard') or (player == 'paper' and opponent == 'spock') \
        or (player == 'spock' and opponent == 'rock') or (player == 'spock' and opponent == 'scissors') \
        or (player == 'lizard' and opponent == 'spock') or (player == 'lizard' and opponent == 'paper'):
        return True

play()
