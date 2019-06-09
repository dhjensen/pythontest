#!/usr/bin/env python3
""" Retrieve and print words from a URL

Usage: 
    
    py words.py <URL>

Example: 
    py words.py 'http://sixty-north.com/c/t.txt'
"""

import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.
    
    Args:
        url: The URL of a UTF-8 text document.

    Returns: 
        A list of strings containing words from 
        the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        return story_words


def print_items(items):
    """ Print items one per line
    
    Args:
        items: An interable seriest of printable items
    """
    for item in items:
        print(item)


def main(url):
    """ Print each words from a text document from a URL 
    
    Args:
        url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)

if __name__ == "__main__":
    main(sys.argv[1]) # The 0th argument is the module filename