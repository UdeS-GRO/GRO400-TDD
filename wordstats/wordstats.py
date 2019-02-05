#!/usr/bin/env python

import string

full_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.
"""

def is_vowel(letter):
    assert(len(letter) == 1)
    return letter.lower() in ['a', 'e', 'i', 'o', 'u', 'y']

def starts_w_vowel(word):
    if is_vowel(word[0]):
        return True
    else:
        return False

def ends_w_cons(word):
    if is_vowel(word[-1]):
        return False
    else:
        return True

def clean_words(words):
    return ''.join([l for l in words if l.isalpha() or l.isspace()])

def words_start_w_vowel(words):
    return [x for x in words if starts_w_vowel(x)]

def words_end_w_cons(words):
    return [x for x in words if ends_w_cons(x)]

def split_text(text):
    text_clean = ''.join(l for l in text if l not in set(string.punctuation))
    return text_clean.split()

if __name__ == "__main__":

    words = split_text(full_text)
    words_vowels = words_start_w_vowel(words)
    words_cons   = words_end_w_cons(words)

    print("Word count:", len(words))
    print("Words that start with a vowel:", len(words_vowel))
    print("Words that end with a consonna:", len(words_cons))

