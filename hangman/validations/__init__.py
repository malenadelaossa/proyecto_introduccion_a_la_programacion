def valid_letter(letter):
    letter=letter.lower()
    if len(letter) != 1:
        print ('Inserte solo 1 letra a la vez')
    elif letter not in 'abcdefghijklmnopqrstuvwxyz':
        print ('Solo se pueden insertar letras válidas del abecedario')
    else:
        return letter

    # Make function to validate if input is a letter
    return True


#meter letra repetida