<<<<<<< HEAD
__author__ = 'Seamus Donnellan | u/insane_playzYT'

=======
>>>>>>> 602de3dc6ab742db8e308ebfe16adef961ce8d3f
def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def user_crossword():
    user_input = input('> Put your crossword in here, letter by letter: ').split()

    looking_for = input('> What words are you looking for? (Separate with spaces) ')

    # print(user_input)
    # if user_input in english_words:
    #     print('YES')
    # else:
    #     print('NO')
    for word in user_input:
        for look in looking_for:
            print(word)
            print(look)
            if look in word:
                print('Found a bit of the word for you!')
        print(word)
        if looking_for in word:
            pass

if __name__ == '__main__':
    english_words = load_words()
    user_crossword()