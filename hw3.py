def generate_phrase(characters, phrase):
    phrase_1 = {}
    for char in characters:
        if char in phrase_1:
            phrase_1[char] += 1
        else:
            phrase_1[char] = 1

    print(phrase_1)

    phrase_2 = {}
    for char in phrase:
        if char in phrase_2:
            phrase_2[char] += 1
        else:
            phrase_2[char] = 1

    print(phrase_2)

    for character, count in phrase_2.items():
        if not phrase_1.get(character) or count > phrase_1[character]:
            return False
    return True

print(generate_phrase('Lucymh19', 'mH1Lcu'))
