# input
word_list = ['hello','world','my','name','is','Anna']
charm = 'o'

def find_word_by_char(li,char):
    new_li = []
    for word in li:
        for letter in word:
            if letter==char:
                new_li.append(word)
    print new_li
    return new_li
find_word_by_char(word_list, charm)