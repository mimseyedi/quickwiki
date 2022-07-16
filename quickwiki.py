"""
Quickwiki version 1.0.0

Quickwiki is a small and useful program for faster access to Wikipedia information.
This program with simple parameters can give you appropriate
and useful information about the subject you have chosen very quickly.

Quickwiki is open source under the MIT license and you can easily use it
and make any changes you like and share it with others.

Quickwiki github repository:
https://github.com/mimseyedi/quickwiki
"""


import os
import sys
import wikipedia
from rich.console import Console


def get_summary(subject, sentence="full"):
    if sentence == "full":
        try:
            return wikipedia.summary(subject)
        except wikipedia.exceptions.WikipediaException:
            suggest = wikipedia.search(subject)
            if len(suggest) > 0:
                return "cant find the subject in wikipedia!\ndid you mean?", suggest
            return "cant find the subject in wikipedia!"

    try:
        return wikipedia.summary(subject, sentences=int(sentence))
    except wikipedia.exceptions.WikipediaException:
        suggest = wikipedia.search(subject)
        if len(suggest) > 0:
            return "cant find the subject in wikipedia!\ndid you mean?", suggest
        return "cant find the subject in wikipedia!"


def main():
    console = Console()

    if len(sys.argv) == 1:
        console.print("You must using parameters!\nusing help parameter for guide.", style="red")

    elif len(sys.argv) == 2:
        if sys.argv[1] == "help":
            console.print("pattern: python quickwiki.py subject sentence\nexample: python quickwiki.py iran 3", style="green")
        else:
            result = get_summary(sys.argv[1])
            if type(result) == tuple:
                console.print(result[0], '\n'.join(result[1]))
            else:
                console.print(result)

    elif len(sys.argv) == 3 and sys.argv[2].isdigit():
        console.print(get_summary(sys.argv[1], sys.argv[2]))

    else:
        console.print("pattern: python quickwiki.py subject sentence\nexample: python quickwiki.py iran 3", style="green")


if __name__ == "__main__":
    main()