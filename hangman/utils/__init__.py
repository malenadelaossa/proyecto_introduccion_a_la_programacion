def game_over():
    # TODO function determine where game was won or lose
    pass


def game_lose(tries):
    return tries== constants.MAX_TRIES
    pass

def findIndexes(input, word):
    indexes = []
    for index, letter in enumerate(word[i]):
        if(letter == input):
            indexes.append(index)
    return indexes

def game_won(letters):
    return None not in letters
    pass


# TODO you should add and implemented other functions as well if necessary