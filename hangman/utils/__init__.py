def game_over():
    return game_lose(tries) or game_won(letters)

def show_part (part, counter):
    return part <= counter

def game_lose(tries):
    return tries== constants.MAX_TRIES


def find_indexes_in_string(input, word):
    indexes = []
    word_length= len(word)
    if(letter == input):
        for index, letter in range(word_length):
            if word [index] == letter:
                indexes.append(index)
                return indexes

def update_letter (letters, find_indexes):
    for index in find_indexes:
        letters [index] = index
        return letters

def game_won(letters):
    return "_" not in letters



# TODO you should add and implemented other functions as well if necessary