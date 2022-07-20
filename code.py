import random
options = ['rock', 'paper', 'scissors']

def again():
    again = input("do you want to try again? type yes or no: ")
    again = again.lower()
    if again == 'y' or 'yes':
        play()


def play():
    user = input("Choose: rock, paper or scissors\n")
    user = user.lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user in options:
        if user == computer:
            print(f"Computer chose {computer} so, ")
            print ('It\'s a tie')
            again()

        elif is_win(user, computer):
            print(f"Computer chose {computer} so, ")
            print ('You won')
            again()

        else:
            print(f"Computer chose {computer} so, ")
            print ('You lost')
            again()
    else:
        print("Please type rock, paper or scissors")
        play()

def is_win(player, opponent):
    if(player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper')\
        or (player == 'paper' and opponent == 'rock'):
        return True

play()
