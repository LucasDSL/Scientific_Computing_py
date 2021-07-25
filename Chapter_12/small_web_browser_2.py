# Counts the words in the poem 
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count_words = dict()
for line in fhand: 
    words = line.decode().split()
    for word in words: 
        count_words[word] = count_words.get(word, 0) + 1

# printing the words with they numbers of appearence
words_by_number_asc = list()
for k, v in count_words.items(): 
    words_by_number_asc.append((v, k))
words_by_number_asc = sorted(words_by_number_asc)
print(words_by_number_asc)