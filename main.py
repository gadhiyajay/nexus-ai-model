import datetime, os
import wikipedia
from nexus import say, listen
from browser import browseropen
import time
from google import search

def mfx(fx):
    def ifx():
        say("Welcome Sir!")
        fx()
        say("Thank You Sir!")
        return ifx()


# @mfx
def main():
    print("Search on Internet\n"
          "Open and search on Browser\n"
          "Search a Wikipedia Article\n"
          "Open a Application\n"
          "Give you time\n"
          "Play music for you!")

    task = listen()
    if "browser" in task:
        result = browseropen(task)
        say(result)
    elif "time" in task:
        dt = datetime.datetime.now().strftime("%H Hours and %M Minutes ")
        print(dt)
        say(dt)
    elif "wikipedia" in task:
        task = task.replace("wikipedia", "")
        result = wikipedia.summary(task)
        print(result)
        say(result)
    elif "search" in task:
        result = search(task)
        print(result)
        say(result)
main()