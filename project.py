import random
import re
import numpy as np

def count_nwords(s, n = 1):
    '''
    count the number of occurance of n-words in a string
    Input: 
        s: a string
        n: the size of n-words to count
    Return: 
        counts: a dictionary keyed by n-words whose values are number of occurance in s
    '''
    counts = {}
    words = s.split()
    for i in range(len(words) - n + 1):
        nwords = tuple(words[i:(i+n)])
        if nwords in counts:
            counts[nwords] += 1
        else:
            counts[nwords] = 1
    return counts

def is_special_ending(ending):
    '''
    Check if an ending is a special ending: -es, -ed, -e (except -le)
    Input: 
        ending: a string with a length of 2
    Return: 
        A logical value indicating if the ending is a special ending
    '''
    # check if it is "es"
    is_es = (ending[0] == "e") and (ending[1] == "s")
    # check if it is "ed"
    is_ed = (ending[0] == "e") and (ending[1] == "d")
    # check if it is -e but not "le"
    is_e_not_le = (ending[1] == "e") and (ending[0] != "l")
    return (is_es or is_ed or is_e_not_le)

def rm_special_endings(word):
    '''
    Takes a word as input and removes the special ending if there's any
    Input: 
        word: a string
    Return: 
        new: a string
    '''
    # extract the last two characters
    ending = word[-2:]
    # set new to be word
    new = word
    # check if it is a special ending
    if is_special_ending(ending):
        # remove the last char if it's -e
        if ending[1] == "e":
            new = word[:-1]
        # remove the last two chars if it's other special endings
        else:
            new = word[:-2]
    return new

def count_syllables(word):
    '''
    Count the syllables of a word.
    Input: 
        word: a string
    Return: 
        syllables: an integer
    '''
    # count the syllable as 1 if the length of the word is less or equal to 3
    if len(word) <= 3:
        syllables = 1
    else:
        # remove the special ending
        new_word = rm_special_endings(word)
        # sum of vowel
        sum_of_vowels = sum([i in ["a", "e", "i", "o", "u", "y"] for i in new_word])
        # check if each character in word is a vowel
        word_vowels = [i in ["a", "e", "i", "o", "u", "y"] for i in new_word]
        # get the indices of True values
        index = [i for i, val in enumerate(word_vowels) if val]
        # sum of consecutive vowels
        sum_of_consecutive = sum(np.diff(index) == 1)
        # number of syllables
        syllables = sum_of_vowels - sum_of_consecutive  
    return syllables

def reading_ease_score(s):
    '''
    Compute the Flesch reading ease score for the input text.
    Input:
        s: a string
    Return:
        RE, a float number representing the reading ease score of s
    '''
    # ending punctuations
    sentenceEnders = re.compile('[.!?:;]')
    # split the text to sentences
    sentences = sentenceEnders.split(s)
    # convert all to lowercase
    sentences = [i.lower() for i in sentences]
    # remove the punctuations
    sentences = [re.sub('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', "", i) for i in sentences]
    # remove the empty string
    sentences = [i for i in sentences if len(i) > 0]
    
    # words
    # split the sentences into words
    words = [i.split() for i in sentences]
    # flaten the list of lists
    words = [item for sublist in words for item in sublist]
    
    # total syllables
    syllables = sum([count_syllables(i) for i in words])
    
    # compute the score using formula
    RE = 206.835 - (1.015 * (len(words) / len(sentences))) - (84.6 * (syllables / len(words)))
    
    return RE

class MarkovText():
    def __init__(self, text, n, length, seed):
        '''
        Initialize all the variables
        '''
        self.text = text
        self.n = n
        self.length = length
        self.seed = seed
        # check the type of the input seed
        try:
            self.seed.split()
        except AttributeError:
            print("The seed should be a string.")

    def markov_text_word(self):
        '''
        Generate fake text with words as units.
        Args:
            None
        Returns:
            fake: a string, the fake text
        '''  
        # test the input
        if self.n > len(self.seed.split()):
            raise ValueError("n has to be smaller or equal to the number of words in seed.")
 
        # initialize
        word_dict = count_nwords(self.text, self.n + 1)
        fake = self.seed
        
        while len(fake.split()) < self.length:
            previous = tuple(fake.split()[(-self.n):])

            # filter dict to keep only matching grams
            sub = {}
            for key in word_dict:
                if key[:self.n] == previous:
                    sub[key] = word_dict[key]
            
            # convert to lists for use with random.choices
            choices = list(sub.keys())
            weights = [sub[key] for key in choices]

            # make choice
            # if no possible choice could be found, try to decrease n by 1.
            try:
                new_nword = random.choices(choices, weights)[0]
            except IndexError:
                if self.n > 1:
                    self.n -= 1
                    print("cannot find matching words, trying n-1 =", self.n)
                    return self.markov_text_word()
                else:
                    print("Please try another seed.")
                    return

            # add to s
            new_word = new_nword[-1]
            fake += " " + new_word
    
        return fake
    
    def make_a_sentence(self):
        '''
        Generate one sentence. Prompt the user to choose whether to 
        generate this sentence by characters or by words.
        Arg:
            None
        Return:
            s: string, a sentence
        '''
        sentenceEnders = re.compile('[.!?:;]')
        s = self.markov_text_word()
        s = sentenceEnders.split(s)[0]
        return s
    
    def reading_ease_score(self):
        '''
        Print the Flesch reading ease score of the generated text and original text.
        Arg:
            None
        Return:
            None
        '''
        fake_text = self.markov_text_word()
        fake_text_score = round(reading_ease_score(fake_text), 2)
        start = random.randint(0, len(self.text) - len(fake_text))
        original_text = self.text[start:(start + len(fake_text))]
        original_text_score = round(reading_ease_score(original_text), 2)
        print("RE for original text: " + str(original_text_score) + "\n", 
              "RE for fake text: " + str(fake_text_score))
        
        
