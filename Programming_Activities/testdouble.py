def twoWords(word1, word2):
    letters1 = list(word1)
    letters2 = list(word2)

    letters1.sort()
    letters2.sort()

    return letters1 == letters2


# test the function
print(twoWords("lead", "dale"))   # True
print(twoWords("gong", "long"))   # False