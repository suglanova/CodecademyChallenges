alphabet_caps = 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'
alphabet = ''.join([letter.strip() for letter in (alphabet_caps.lower()).split(',')])
length = len(alphabet)
n = 10
res_text = ''
text = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je t setu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
for symbol in text:
    index = alphabet.find(symbol)
    if index == -1:
        res_text += symbol
    else: 
        res_text += alphabet[(index + 10) % length]
#print(res_text)

text_my = 'glad to hear from you! how long have you been at home due to coronavirus?'
res_text_my = ''
for symbol in text_my:
    index = alphabet.find(symbol)
    if index == -1:
        res_text_my += symbol
    else:
        res_text_my += alphabet[(index - 10) % length]
#print(res_text_my)

def coder(message, offset):
    res_text = ''
    for symbol in message:
        index = alphabet.find(symbol)
        if index == -1:
            res_text += symbol
        else:
            res_text += alphabet[(index + offset) % length]
    return res_text
#print(coder('bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!', 14))

#def key_word_coder(message, key_word):
#    for n in range(len(message)):
#        if message[n] in alphabet:
    #print(coder('vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.', n))
#            print(alphabet.find(message[n]))
#        else:
#            print(message[n])
#    for m in range(len(key_word)):
#        if key_word[m] in alphabet:
#            print(alphabet.find(key_word[m]))
#        else:
#            print(key_word[m])
#print(key_word_coder('eoxum ov hnh gvb', 'dog'))


def translateMessage(message, key_word):
    keyIndex = 0
    translated = []
    for symbol in message:
        num = alphabet.find(symbol)
        if num != -1:
            num -= alphabet.find(key_word[keyIndex])
            num %= len(alphabet)
            translated.append(alphabet[num])
            keyIndex += 1
            if keyIndex == len(key_word):
                keyIndex = 0
        else:
            translated.append(symbol)
    return ''.join(translated)
print(translateMessage('dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!', 'friends'))

def codeMessage(message, key_word):
    keyIndex = 0
    translated = []
    for symbol in message:
        num = alphabet.find(symbol)
        if num != -1:
            num += alphabet.find(key_word[keyIndex])
            num %= len(alphabet)
            translated.append(alphabet[num])
            keyIndex += 1
            if keyIndex == len(key_word):
                keyIndex = 0
        else:
            translated.append(symbol)
    return ''.join(translated)
print(codeMessage('Hi dude, are you happy with my skill? So let us spot it!', 'friends'))

print(translateMessage('Hn uchr, djj pwy udhup emgk ed jsmyo? Sg qvb yf vhtk qx!', 'friends'))
            