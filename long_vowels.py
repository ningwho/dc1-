word = 'good'
result = ''

for i in range(len(word)):
    twoletters = word[i : i+2]
    if twoletters == 'oo':
        result += 'oooo'
    elif twolettters == 'ee':
        result += 'eeee'
    else:
        result += word[i]
print result
