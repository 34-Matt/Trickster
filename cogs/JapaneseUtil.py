def vowalOffset(vo):
    '''Determines the offset for a hiragana "vowal" in unicode. Used in singleHiragana.
    vo is the "vowal" of the hiragana character

    Returns the offset associated with vo
    '''

    if vo == 'a':
        return 1
    elif vo == 'i':
        return 2
    elif vo == 'u':
        return 3
    elif vo == 'e':
        return 4
    elif vo == 'o':
        return 5
    else:
        return -1000

def conOffset(con):
    '''Determines the offset for a hiragana "consonant" in unicode. Used in singleHiragana.
    con is the "consonant" of the hiragana character

    Returns the offset associated with con
    '''

    if con == 'k':
        return 9,2
    elif con == 'g':
        return 10,2

    elif con == 's':
        return 19,2
    elif (con == 'z') or (con == 'j'):
        return 20,2

    elif con == 't':
        return 29,2
    elif con == 'd':
        return 30,2

    elif con =='n':
        return 41,1

    elif con == 'h':
        return 44,3
    elif con == 'b':
        return 45,3
    elif con == 'p':
        return 46,3

    elif con == 'm':
        return 61,1

    elif con == 'y':
        return 66,2

    elif con == 'r':
        return 72,1

    elif con == 'w':
        return 78,1

def singleChar(letter,katakana):
    '''Determines the unicode for the Japanese character.
    letter is the romanji of the hiragana character
    katakana is boolean for converting to Katakana (True) or Hiragana (False)

    Returns the unicode of letter
    '''

    letNum = len(letter)
    if katakana:
        output = 12448
    else:
        output = 12352

    if letNum == 1:
        if letter == 'n':
            output += 83
            output = chr(output)
        else:
            output += (2*vowalOffset(letter))
            output = chr(output)

    elif letNum == 2:
        vowalOff = vowalOffset(letter[1])
        conOff,multi = conOffset(letter[0])

        # Deal with lower case 'tsu'
        if ((letter[0] == 't') or (letter[0] == 'd')) and (vowalOff > 2):
            output += 1
        # No 'yi' or 'yo'
        if (letter[0] == 'y') and (vowalOff == 3):
            vowalOff = 2
        elif (letter[0] == 'y') and (vowalOff == 5):
            vowalOff = 3
        # No 'wi'
        if (conOff == 't') and (vowalOff > 2):
            output -= 1
        
        # Get character
        output += conOff + (multi * vowalOff)
        output = chr(output)

    elif letNum == 3:
        if letter[1] == 'y':
            output = singleChar(letter[0]+'i',katakana)
            output += chr(ord(singleChar(letter[1:]))-1,katakana)
        elif letter[0] == letter[1]:
            output = chr(ord(singleChar('tu'))-1,katakana)
            output += singleChar(letter[1:],katakana)
        else:
            output = singleChar(letter[0]+letter[2],katakana)

    #print(output)
    #print(letNum)
    return output