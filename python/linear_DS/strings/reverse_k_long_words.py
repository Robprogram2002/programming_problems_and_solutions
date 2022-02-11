# 8._ Write a function that takes in a string of one or more words, and returns the same string, but with all five or
# more letter words reversed. Strings passed in will consist of only letters and
# spaces.

def spin_words(sentence):
    # using pythonian syntax
    # return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
    words = sentence.split(' ')
    for k in range(len(words)):
        if len(words[k]) >= 5:
            words[k] = words[k][::-1]

    return ' '.join(words)
