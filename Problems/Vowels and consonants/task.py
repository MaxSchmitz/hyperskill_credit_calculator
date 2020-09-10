user_input = str(input())
for letter in user_input:
    if letter in 'aeiou':
        print('vowel')
    elif letter in 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM':
        print('consonant')
    else:
        break
