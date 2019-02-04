#!/usr/bin/env python

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

if __name__ == "__main__":

    words = full_text.split()
    words_vowel = [x for x in words if starts_w_vowel(x)]
    words_cons  = [x for x in words if ends_w_cons(x)]

    print("Word count:", len(words))
    print("Words that start with a vowel:", len(words_vowel))
    print("Words that end with a consonna:", len(words_cons))

