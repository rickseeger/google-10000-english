#!/usr/bin/python

# encode/decode base-58 string as sequence of words

base58 = 'abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789'
fp = open('dict.txt')
i = 0
dict = [ ] 
rdict = { }
for word in fp:
    w = word.strip()
    dict.append(w)
    rdict[w] = i 
    i += 1
fp.close()


# encode
test = '1NSCyJfx7F5L66c6XtPPGXigtUHuq1GWEn'
print '\n' + test + '\n'

phrase = []
for i in range(0,len(test),2):
    lo = base58.index(test[i])
    hi = base58.index(test[i+1])
    idx = (hi*64)+lo
    word = dict[idx]
    print i, test[i:(i+2)], lo, hi, idx, word
    phrase.append(word)

print '\n' + ' '.join(phrase) + '\n'

# decode
test = 'sides happen drama reach dental smooth cure doug giving gang kenya issue modes scott temp legacy custom'
words = test.split(' ')
print words
code = ''
for w in words:
    idx = rdict[w]
    hi = (idx/64)
    lo = idx % 64
    print w, rdict[w], lo, hi, base58[lo], base58[hi]
    code += base58[lo] + base58[hi]
    
print '\n' + code + '\n'
