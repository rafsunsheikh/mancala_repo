binAmount = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

copyBinAmount = []

tempBinAmount = []

diff_list = list()

temp_diff_list = list()

playing = True

playerOne = True

messageCode = 0

giveawayPile = -1

lastRecipient = -1

choosenBin = -2

difference = 0

def terminal_message(messageCode, playerOne):
    message = ""
    if playerOne and messageCode == 0:
        message = "Player One's Turn..."
    elif not(playerOne) and messageCode == 0:
        message = "Player Two's Turn..."
    elif playerOne and messageCode == -2:
        message = "Invalid Input. Try again Player One.."
    elif not(playerOne) and messageCode == -2:
        message = "Invalid Input. Try again Player Two.."
    elif playerOne and messageCode == -1:
        message = "You must choose a non-empty bin player One"
    elif not(playerOne) and messageCode == -1:
        message = "You must choose a non-empty bin player Ai"

    print("")
    print(message)
    print("")

def board():
    i = 0
    for element in binAmount:
        binAmount[i] = int(binAmount[i])
        if int(binAmount[i] < 10):
            binAmount[i] = " " + str(binAmount[i])
        else:
            binAmount[i] = str(binAmount[i])
        i = i + 1
    # end of for loop
    if not(playerOne):
        print("        a    b    c    d    e    f")
    print("+----+----+----+----+----+----+----+----+")
    print("|    | " + binAmount[12] + " | " + binAmount[11] + " | " + binAmount[10] + " | " + binAmount[9] + " | " +
          binAmount[8] + " | " + binAmount[7] + " |    |")
    print("| " + binAmount[13] + " |----+----+----+----+----+----| " + binAmount[6] + " |")
    print("|    | " + binAmount[0] + " | " + binAmount[1] + " | " + binAmount[2] + " | " + binAmount[3] + " | " +
          binAmount[4] + " | " + binAmount[5] + " |    |")
    print("+----+----+----+----+----+----+----+----+")
    if playerOne:
        print("        f    e    d    c    b    a")
    print("")

def player_one_user_input(userInput,messageCode,playing):
    if userInput == 'q':
        playing = False
        choosenBin = 0
    elif userInput == "a":
        choosenBin = 5
    elif userInput == "b":
        choosenBin = 4
    elif userInput == "c":
        choosenBin = 3
    elif userInput == "d":
        choosenBin = 2
    elif userInput == "e":
        choosenBin = 1
    elif userInput == "f":
        choosenBin = 0
    else:
        choosenBin = -2
        messageCode = -2  #invalid input
    return (choosenBin,messageCode,playing)

def player_ai_user_input(userInput,messageCode,playing):
    if userInput == 'q':
        playing = False
        choosenBin = 0
    elif userInput == "a":
        choosenBin = 12
    elif userInput == "b":
        choosenBin = 11
    elif userInput == "c":
        choosenBin = 10
    elif userInput == "d":
        choosenBin = 9
    elif userInput == "e":
        choosenBin = 8
    elif userInput == "f":
        choosenBin = 7
    else:
        choosenBin = -2
        messageCode = -2  #invalid input
    return (choosenBin,messageCode,playing)

def player_one_stone_distribution(choosenBin):
    global messageCode, playerOne, giveawayPile, lastRecipeint, tempBinAmount
    if int(choosenBin) >= 0:
        giveawayPile = int(tempBinAmount[choosenBin])
        tempBinAmount[choosenBin] = 0
        if int(giveawayPile) <= 0:
            messageCode = -1 # empty bin was chosen
    
    recipient = choosenBin + 1
    while int(giveawayPile) > 0:
        if int(recipient) == 13:
            recipient = 0
        tempBinAmount[recipient] = int(tempBinAmount[recipient]) + 1
        giveawayPile = int(giveawayPile) - 1

        if int(giveawayPile) == 0:
            lastRecipeint = recipient
        else:
            recipient = int(recipient) + 1
            if int(recipient) > 13:
                recipient = 0
    
    if int(lastRecipeint) ==6:
        playerOne = True
    elif(int(tempBinAmount[lastRecipeint]) == 1 and int(lastRecipeint) < 6):
        tempBinAmount[6] = int(tempBinAmount[6]) + int(tempBinAmount[lastRecipeint]) + int(tempBinAmount[12 - int(lastRecipeint)])
        tempBinAmount[lastRecipeint] = 0
        tempBinAmount[12 - int(lastRecipeint)] = 0
        playerOne = not(playerOne)
    elif(int(messageCode) >= 0):
        playerOne = not (playerOne)
    
    return tempBinAmount


def player_one_stone_minimax_distribution(choosenBin):
    global messageCode, playerOne, giveawayPile, lastRecipeint, tempBinAmount
    if int(choosenBin) >= 0:
        giveawayPile = int(tempBinAmount[choosenBin])
        tempBinAmount[choosenBin] = 0
    
    recipient = choosenBin + 1
    while int(giveawayPile) > 0:
        if int(recipient) == 13:
            recipient = 0
        tempBinAmount[recipient] = int(tempBinAmount[recipient]) + 1
        giveawayPile = int(giveawayPile) - 1

        if int(giveawayPile) == 0:
            lastRecipeint = recipient
        else:
            recipient = int(recipient) + 1
            if int(recipient) > 13:
                recipient = 0
    
    if int(lastRecipeint) ==6:
        playerOne = True
    elif(int(tempBinAmount[lastRecipeint]) == 1 and int(lastRecipeint) < 6):
        tempBinAmount[6] = int(tempBinAmount[6]) + int(tempBinAmount[lastRecipeint]) + int(tempBinAmount[12 - int(lastRecipeint)])
        tempBinAmount[lastRecipeint] = 0
        tempBinAmount[12 - int(lastRecipeint)] = 0
        playerOne = playerOne
    elif(int(messageCode) >= 0):
        playerOne = playerOne
    
    return tempBinAmount

def player_ai_stone_distribution(choosenBin):
    global messageCode, playerOne, giveawayPile, lastRecipeint, tempBinAmount
    if int(choosenBin) >= 0:
        giveawayPile = int(tempBinAmount[choosenBin])
        tempBinAmount[choosenBin] = 0
        if int(giveawayPile) <= 0:
            messageCode = -1 # empty bin was chosen
    
    recipient = choosenBin + 1
    while int(giveawayPile) > 0:
        if int(recipient) == 6:
            recipient = 7
        tempBinAmount[recipient] = int(tempBinAmount[recipient]) + 1
        giveawayPile = int(giveawayPile) - 1

        if int(giveawayPile) == 0:
            lastRecipeint = recipient
        else:
            recipient = int(recipient) + 1
            if int(recipient) > 13:
                recipient = 0
    
    if int(lastRecipeint) ==13:
        playerOne = False
    elif(int(tempBinAmount[lastRecipeint]) == 1 and int(lastRecipeint) > 6):
        tempBinAmount[13] = int(tempBinAmount[13]) + int(tempBinAmount[lastRecipeint]) + int(tempBinAmount[12 - int(lastRecipeint)])
        tempBinAmount[lastRecipeint] = 0
        tempBinAmount[12 - int(lastRecipeint)] = 0
        playerOne = not(playerOne)
    elif(int(messageCode) >= 0):
        playerOne = not (playerOne)
    
    return tempBinAmount

def player_ai_stone_minimax_distribution(choosenBin):
    global messageCode, playerOne, giveawayPile, lastRecipeint, tempBinAmount
    if int(choosenBin) >= 0:
        giveawayPile = int(tempBinAmount[choosenBin])
        tempBinAmount[choosenBin] = 0
    
    recipient = choosenBin + 1
    while int(giveawayPile) > 0:
        if int(recipient) == 6:
            recipient = 7
        tempBinAmount[recipient] = int(tempBinAmount[recipient]) + 1
        giveawayPile = int(giveawayPile) - 1

        if int(giveawayPile) == 0:
            lastRecipeint = recipient
        else:
            recipient = int(recipient) + 1
            if int(recipient) > 13:
                recipient = 0
    
    if int(lastRecipeint) ==13:
        playerOne = False
    elif(int(tempBinAmount[lastRecipeint]) == 1 and int(lastRecipeint) > 6):
        tempBinAmount[13] = int(tempBinAmount[13]) + int(tempBinAmount[lastRecipeint]) + int(tempBinAmount[12 - int(lastRecipeint)])
        tempBinAmount[lastRecipeint] = 0
        tempBinAmount[12 - int(lastRecipeint)] = 0
        playerOne = playerOne
    elif(int(messageCode) >= 0):
        playerOne = playerOne
    
    return tempBinAmount

def gameState():
    sideOne = 0
    sideAi = 0
    for j in range(7):
        sideOne = int(sideOne) + int(binAmount[j])
        sideAi = int(sideAi) + int(binAmount[j + 7])
    return (sideOne,sideAi)
    
def end_game_check(playing):
    sideOne = 0
    sideTwo = 0
    for j in range(6):
        sideOne = int(sideOne) + int(binAmount[j])
        sideTwo = int(sideTwo) + int(binAmount[j + 7])

    if(int(sideOne) ==0 or int(sideTwo) == 0):
        playing = False
        binAmount[6] = int(binAmount[6]) + int(sideOne)
        binAmount[13] = int(binAmount[13]) + int(sideTwo)
        for k in range(6):
            binAmount[k] = 0
            binAmount[k + 7] = 0
    return playing

def copy_bin_amount_func():
    copyBinAmount = binAmount.copy()
    return copyBinAmount

def diff():
    global difference, diff_list
    sideOne = 0
    sideAi = 0
    for j in range(7):
        sideOne = int(sideOne) + int(tempBinAmount[j])
        sideAi = int(sideAi) + int(tempBinAmount[j + 7])
    difference = sideOne - sideAi
    diff_list.append(difference)
    return difference

def no_moves():
    sideOne = 0
    sideAi = 0
    for j in range(6):
        sideOne = int(sideOne) + int(copyBinAmount[j])
        sideAi = int(sideAi) + int(copyBinAmount[j + 7])
    difference = sideOne - sideAi

    if int(sideOne) == 0 or int(sideAi) == 0:
        return True
    else:
        return False


def minimax(maxify, depth, bins):
    global choosenBin, copyBinAmount, tempBinAmount, binAmount, playerOne
    tempBinAmount = copyBinAmount.copy()
    
    if depth == 0:
        choosenBin = bins
        return diff()
    
    if maxify:
        best_score = 999
        for bins in range(7, 13, 1):
            tempBinAmount = binAmount.copy()
            tempBinAmount = player_one_stone_minimax_distribution(bins)
            copyBinAmount = tempBinAmount.copy()
            score = minimax(not maxify, depth-1, bins)
            best_score = min(best_score, score)
        return best_score
    
    else:
        best_score = -999
        for bins in range(0, 6, 1):
            tempBinAmount = player_ai_stone_minimax_distribution(bins)
            score= minimax(not maxify, depth-1, bins)
            best_score = max(best_score, score)
        return best_score


while (playing):
    terminal_message(messageCode, playerOne)
    messageCode = 0

    board()

    # choosenBin = 0
    if playerOne:
        userInput = input("Enter 'q' to end the game: ")
        choosenBin,messageCode,playing = player_one_user_input(userInput,messageCode,playing)
        if playing:
            tempBinAmount = binAmount.copy()
            tempBinAmount = player_one_stone_distribution(choosenBin)
            binAmount = tempBinAmount.copy()

    else: 
        tempBinAmount = binAmount.copy()
        copyBinAmount = binAmount.copy()
        minimax(True, 3,  int(choosenBin))

        for i in range(0, 35, 6):
            temp_diff_list.append(diff_list[i])

        min_not_ended_zero = True

        while(min_not_ended_zero):
            min_temp_diff_list = min(temp_diff_list)

            ai_choosen_bin = temp_diff_list.index(int(min_temp_diff_list))

            tempBinAmount = binAmount.copy()
            temp_bin_value_check = tempBinAmount[ai_choosen_bin + 7]
            if int(temp_bin_value_check) == 0:
                temp_diff_list[ai_choosen_bin] = 999
            else:
                tempBinAmount = player_ai_stone_distribution(ai_choosen_bin + 7)
                binAmount = tempBinAmount.copy()
                diff_list.clear()
                temp_diff_list.clear()
                min_not_ended_zero = False

        

    
    playing = end_game_check(playing)

# end of while loop
print("")
print("The Game is over!")
if int(binAmount[13]) < int(binAmount[6]):
    print("Player One has won the game!")
elif int(binAmount[13]) > int(binAmount[6]):
    print("Player Two has won the game!")
else:
    print("The game ended in a Tie!")

i = 0
for element in binAmount:
    binAmount[i] = int(binAmount[i])
    if int(binAmount[i] < 10):
        binAmount[i] = " " + str(binAmount[i])
    else:
        binAmount[i] = str(binAmount[i])
    i = i + 1
# end of for loop

print("")
print("+----+----+----+----+----+----+----+----+")
print("|    | " + binAmount[12] + " | " + binAmount[11] + " | " + binAmount[10] + " | " + binAmount[9] + " | " +
    binAmount[8] + " | " + binAmount[7] + " |    |")
print("| " + binAmount[13] + " |----+----+----+----+----+----| " + binAmount[6] + " |")
print("|    | " + binAmount[0] + " | " + binAmount[1] + " | " + binAmount[2] + " | " + binAmount[3] + " | " +
    binAmount[4] + " | " + binAmount[5] + " |    |")
print("+----+----+----+----+----+----+----+----+")