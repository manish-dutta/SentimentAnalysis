def load_wordlist(filename):
    """
    This function should return a list or set of words from the given filename.
    """
    fh = open(filename, "r")
    data = fh.read().splitlines()

    return data


pWords = load_wordlist("C:\Masters\Spring 2019\BI\Topic 2/positive.txt")
print(pWords)
nWords = load_wordlist("C:\Masters\Spring 2019\BI\Topic 2/negative.txt")
print(nWords)
