

print("********************************")
print("*********   HANG MAN   *********")
print("********************************")
print("")
print("")
print("Welcome to the game of HANG MAN! The objective is simple. You have to guess the hidden word one letter at a time")
print("")
attempt = 0

secretword = input("")
individualletter = []


for letter in secretword:
    individualletter.append(letter)

letter_list = ['_' for number in range(len(secretword))]


print("Enter a letter: ", end="")
inputguess = input("")


while attempt <= 6:
    correct_guess = False
    for index, letter in enumerate(individualletter):
        if inputguess == letter:
            letter_list[index] = inputguess
            correct_guess = True
        print("")
    if '_' not in letter_list:
        print("")
        print("")
        print("The correct word was:", secretword)
        print("********************************")
        print("           You Won!             ")
        print("********************************")
        break

    if not correct_guess:
        attempt += 1

    if attempt > 6:
        print("")
        print("")
        print("The correct word was:", secretword)
        print("********************************")
        print("           You Lost!            ")
        print("********************************")
        break

    print(" ".join(letter_list))
    print("")
    print("You've guessed wrong", attempt, "times")
    print("")
    print("Try again! Enter a letter: ", end="")
    inputguess = input("")
