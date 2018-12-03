
import random as rand
import os
import webbrowser

rand.seed(a=os.urandom(256),version=2)
url = "https://xkcd.com/{}/".format(rand.randrange(1, 2079, 1))
print(url)
webbrowser.open(url)