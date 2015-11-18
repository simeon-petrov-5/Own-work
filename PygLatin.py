# PygLatin
# Pig Latin is a language game in which words in English are altered. The objective is to conceal the meaning of the words from others not familiar with the rules.

pyg = 'ay'
original =input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print (original)
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print (new_word)
else:
    print ('empty')