import webbrowser

def sendMail(email):
    webbrowser.open('mailto:' + email)

def googleSearch(query):
    webbrowser.open('https://www.google.com/search?q=' + query)

def youtubeSearch(query):
    webbrowser.open('https://www.youtube.com/results?search_query=' + query)
