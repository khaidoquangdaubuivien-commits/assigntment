def acronym(phrase):
    words = phrase.split()
    result = ""

    for w in words:
        result += w[0].upper()

    return result
