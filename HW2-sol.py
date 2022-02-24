import random
import string

def count_characters(s):
    """
    Count the number of occurrences of each character in a string. 
    s: str, the string in which to count. 
    return counts, a dict keyed by character whose values are the number of occurrences in s
    """
    
    # create an empty dictionary
    counts = {}
    
    # loop through the input string, 
    # creating and incrementing counts
    for i in range(len(s)):
        l = s[i]
        if l in counts:
            counts[l] += 1
        # if it's a new key
        else:
            counts[l] = 1
            
    return counts

def count_ngrams(s, n=1):
    """
    Count the number of occurrences of n-grams in a string. 
    s: str, the string in which to count. 
    n: the size of n-grams to count. 
    return counts, a dict keyed by n-grams whose values are the number of occurrences in s
    """
    
    # initialize an empty dictionary
    counts = {}
    
    # loop through substrings of length n of 
    # the input string, updating counts as before
    for i in range(len(s)-n+1):
        gram = s[i:(i+n)]
        if gram in counts:
            counts[gram] += 1
        else:
            counts[gram] = 1

    return counts


def markov_text(s, n, length = 100, seed = "Emma Woodhouse"):
    """
    Generate fake text according to an n-th order Markov model, with data from a user-supplied corpus. 
    s: the text from which to learn grams
    n: the order of the Markov model. 
    length: the number of synthetic characters to generate. The length of the output string will be equal to this plus the length of the seed string. 
    seed: the initial string.
    """
    counts = count_ngrams(s, n+1)
    
    # initialize
    fake = seed
    for i in range(length):
        previous = fake[(-n):]
        
        # filter dict to keep only matching grams
        sub = {}
        for key in counts:
            if key[:-1] == previous:
                sub[key] = counts[key]
        
        # slightly simpler, if you know dictionary comprehensions (not discussed in class)
        # sub = {key : counts[key] for key in counts if key[:-1] == previous}
        
        # convert to lists for use with random.choices
        choices = list(sub.keys())
        weights = [sub[key] for key in choices]
          
        # make choice 
        new_gram = random.choices(choices, weights)[0]
        
        # add to s
        new_char = new_gram[-1]
        fake += new_char
    
    return fake
