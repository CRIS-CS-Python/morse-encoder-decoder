'''
<Name>, <Grade> <Course>
Morse Code Sequence Encoder/Decoder

This program encodes a string of English text into a Morse sequence,
and vice-a-versa, decodes a Morse sequence into English text.

Morse Sequence Description:
  * Each English character is represented by a Morse sequence
    of dots and dashes having no spaces, for example:
      A =>  .-
  * Individual Morse sequences that represent a letter are separated by spaces.
  * Each space that seperates English words is represented by a slash: /
'''

import sys

USAGE = '''\
py morse.py <encode|decode> "<message>"

examples:
    py morse.py encode "Hello World"
    .... . .-.. .-.. --- / .-- --- .-. .-.. -..

    py morse.py decode ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    HELLO WORLD
'''

class MorseValueError(ValueError):
    '''Custom Exception class for Invalid Morse encode or decode input'''
    pass

def warn(*args, **kwargs):
    '''print a string to stderr'''
    print(*args, file=sys.stderr, **kwargs)

def die(*args, **kwargs):
    '''print a string to stderr and exit 1'''
    warn(*args, **kwargs)
    sys.exit(1)

# Dictionary of English letters and their corresponding Morse encodings
english_morse_map = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': '/',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    '0' : '-----',
    '.': '.-.-.-',
    ',': '--..--',
    ':': '---...',
    '?': '..--..',
    '\'': '.----.',
    '-': '-....-',
    '/': '-..-.',
    '@': '.--.-.',
    '=': '-...-'
}

# reverse of English to Morse dictionary
# having Morse codes as keys and English characters as values
morse_english_map = dict((v, k) for (k, v) in english_morse_map.items())

def encode(msg):
    '''encodes a given English text message and returns Morse code sequences'''
    return 'TODO'

def decode(msg):
    '''decodes a given Morse code message and returns English plain text'''
    return 'TODO'
    