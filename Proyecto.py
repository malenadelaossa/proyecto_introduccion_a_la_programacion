from flask import Flask, make_response, redirect, request, jsonify, render_template
from flask_cors import CORS
from hangman import init_game_data
import hangman.config.constants as constants
import hangman.utils as utils
import hangman.validations as validations
from config.db import DB
from config.api import WordApi


app = Flask(__name__)  # referencing current file
CORS(app)

db_instance = DB(app)

crud_methods = ['GET', 'POST']
Word = db_instance.models['word']
WORD = WordApi.get_word()
print(WORD)



GAME_DATA = init_game_data(WORD)


#url sin ningún parámetro
@app.route('/', methods=crud_methods)
def index():
    print('estoy en home')
    global WORD
    if request.method == 'POST':
        req = request.form
        game_finished= utils.game_over (
            GAME_DATA ['letters'], GAME_DATA ['tries'])
    #
    if (find_indexes):
        GAME_DATA ['letters'] = utils.update_letter(
            GAME_DATA ['letters'], find_indexes)
        game_finished= utils.game_over(
            GAME_DATA ['letters'], GAME_DATA ['tries'])
        if game_finished:
            word.add_word(WORD, redirect('/'))
        elif (GAME_DATA['tries'] <= constants.MAX_TRIES):
            GAME_DATA['tries'] +=1
    else:
        GAME_DATA ['errors']. append('digite una letra válida')
        return redirect ('/')
    else:
        GAME_DATA ['words']= Word.get_played_words()
        GAME_DATA ['words'] = Word.get_played_words()
        return render_template(
            'index.html',
            intructions= constants.INSTRUCTIONS,
            game=GAME_DATA)


        print(GAME_DATA['tries'])
        GAME_DATA['tries'] = GAME_DATA['tries'] + 1
        # TODO handle game logic functionality different
        # handle different scenarios
        # handle errors
        # handle tries
        #if (utils.valid)
        input = req['letter']
        #
        GAME_DATA['indexes'] = utils.findIndexes(input, WORD)

        print(input)
        # if input in GAME_DATA['letters']:

        Word.add_word(input, redirect('/'))
        return redirect('/')
    else:
        GAME_DATA['words'] = Word.get_played_words()
        return render_template(
            'index.html',
            instructions=constants.INSTRUCTIONS,
            game=GAME_DATA)

@app.route('/restart', methods=['GET'])
def restart():
    global WORD, GAME_DATA
    WORD= WordApi.get_word()
    GAME_DATA = init_game_data(WORD)
    return redirect('/')
    print('estoy en restart')

if __name__ == '__main__':
    db_instance.init_db()
    app.run(debug=True)
