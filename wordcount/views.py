from django.http import HttpResponse
from django.shortcuts import render
import operator
"""Esto es para poder importar documentos html"""


"""Se define una funcion para la pagina principal"""
def homepage(request):

    return render(request, 'home.html', {'texto':'this is me', 'hola':'mundo'})
    """Recibe dos parametros el request y el nombre de la pagina"""

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
                worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddictionary':sortedwords})

def about(request):
    return render(request, 'about.html')