def word_count(x):
    x.lower()
    y = []
    y = x.split()
    dictwords = {}
    count = 0
    for word in y:
      if word in dictwords:
        dictwords[word] += 1
      else:
        dictwords[word] = 1
    return (dictwords)

word_count("I am that I am")
