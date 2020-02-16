"""This program is to fetch the words from an url online.

Example:
$python words.py "http://sixty-north.com/c/t.txt"
"""
import sys
from urllib.request import urlopen


# Do Something nice: 
def fetch_words(uri):
    story = urlopen(uri)
    story_words = []

    for line in story:
        for word in line.split():
            story_words.append(word.decode("utf-8"))

    story.close()
    return story_words


def print_items(items):
    for item in items:
        print(item)


if __name__ == "__main__":
    print_items(fetch_words(sys.argv[1]))
