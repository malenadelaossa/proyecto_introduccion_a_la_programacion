import hangman.config.constants as constants
import hangman.utils as utils


# TODO remember this when we will store word
def init_game_data(word):
    return {
        'errors': [],
        'tries': 0,
        'word': word,
        'utils': {
            'gameOver': utils.game_over,
            'gameLose': utils.game_lose,
            'showPart': utils.show_part
        },
        'display': constants.DISPLAY_MSG,
        'letters': "_" * len(word),
        'indexes': None
        # _ _ _ _

    }