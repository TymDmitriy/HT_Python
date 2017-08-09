import string, pprint

with open(r"/Users/Wilson/Desktop/hhgttg.txt", "r+") as f:
    content = f.read().lower()

with open(r"/Users/Wilson/Desktop/skip_words.txt", "r+") as f:
    skip_words = f.read().lower().split()

list_words = content.split()
print(len(list_words))
print(len(skip_words))

word_stats = {}
for word in list_words:
    word = word.strip(string.punctuation)
    if word:
        if word in word_stats:
            word_stats[word] += 1
        else:
            word_stats[word] = 1


# pprint.pprint(word_stats)
for key in sorted(word_stats, key=word_stats.get, reverse=True):
    print("%s:\t%s" % (key, word_stats[key]))