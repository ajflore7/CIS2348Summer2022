# Anthony Flores 1792816

word = input()

no_space = word.replace(' ', '')  # replaces the spaces with no spaces

if no_space == no_space[::-1]:  # [::-1] flips the string == checks if the flipped string matches the original string
    print(word, 'is a palindrome')
else:
    print(word, 'is not a palindrome')
