from django.shortcuts import render
import operator
 
def home(request):
     return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    dictionary = {}

    for word in wordlist:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    sortedwords = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'worddict': sortedwords})

def letters(request):
    return render(request, 'letters.html')

def letterscounted(request):
    word = request.GET['fullword']
    dictionary = {}

    for letter in word:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

    letterssorted = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
  
    return render(request, 'letterscounted.html', {'word': word, 'wordlen': len(dictionary.items()), 'letterssorted': letterssorted})