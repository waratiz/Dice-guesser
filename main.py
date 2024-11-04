import random


dice_All = {
    1: ("┌─────────┐\n"
        "│         │\n"
        "│    ●    │\n"
        "│         │\n"
        "└─────────┘"),
    2: ("┌─────────┐\n"
        "│  ●      │\n"
        "│         │\n"
        "│      ●  │\n"
        "└─────────┘"),
    3: ("┌─────────┐\n"
        "│  ●      │\n"
        "│    ●    │\n"
        "│      ●  │\n"
        "└─────────┘"),
    4: ("┌─────────┐\n"
        "│  ●   ●  │\n"
        "│         │\n"
        "│  ●   ●  │\n"
        "└─────────┘"),
    5: ("┌─────────┐\n"
        "│  ●   ●  │\n"
        "│    ●    │\n"
        "│  ●   ●  │\n"
        "└─────────┘"),
    6: ("┌─────────┐\n"
        "│  ●   ●  │\n"
        "│  ●   ●  │\n"
        "│  ●   ●  │\n"
        "└─────────┘")
}

def get_payout(dice, guess, bet):

    if dice == guess:
        return bet * 2
    return 0

def main():
    balance = 100

    print("**********************************")
    print("Welcome to Dice guessing game :D ")
    print("**********************************")

    while balance > 0:
        print(f"Current balance: {balance} Baht")

        bet = input("Place your bet! : ")
        guess = input("Guess the number (1-6)! : ")

        if not bet.isdigit() or not guess.isdigit():  # Check int
            print("Please enter a valid number")
            continue

        bet = int(bet)
        guess = int(guess)

        if guess < 1 or guess > 6:
            print("Please guess a number between 1 and 6.")
            continue

        if bet > balance:
            print("Not enough money!!")
            continue

        if bet <= 0:
            print("Bet must be greater than 0!!")
            continue


        balance -= bet

        # Random
        dice = random.randint(1, 6)
        print("Dice rolled:")
        print(dice_All[dice])

        # Calculate
        payout = get_payout(dice, guess, bet)
        if payout > 0:
            print("Congratulations! You guessed correctly!")
            balance += payout
        else:
            print("Sorry, you guessed incorrectly.")

    print("Game over! You ran out of money.")


main()
