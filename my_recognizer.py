import warnings
from asl_data import SinglesData


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    # TODO implement the recognizer

    for testing_word, (X, l) in test_set.get_all_Xlengths().items():
      best_score = float("-inf")
      best_guess = ''
      prob = {}

      for train_word, model in models.items():
        try:
          Lprob = model.score(X, l)
          prob[train_word] = Lprob
        except Exception as e:
          prob[train_word] = float("-inf")

        if best_score < Lprob:
          best_score = Lprob
          best_guess = train_word

      probabilities += [prob]
      guesses += [best_guess]

    return probabilities, guesses
