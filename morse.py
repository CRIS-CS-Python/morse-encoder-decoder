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
morse.py <encode|decode> "<message>"

examples:
    morse.py encode "Hello World"
    .... . .-.. .-.. --- / .-- --- .-. .-.. -..

    morse.py decode ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    HELLO WORLD
'''

def warn(*args, **kwargs):
    '''print a string to stderr'''
    print(*args, file=sys.stderr, **kwargs)

def die(*args, **kwargs):
    '''print a string to stderr and exit 1'''
    warn(*args, **kwargs)
    sys.exit(1)

# Dictionary of English letters and their corresponding Morse encodings
alphabet = {
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

# dictionary using alphabet values as keys and vice-versa
inverse_alphabet = dict((v, k) for (k, v) in alphabet.items())

def morse_encode(msg):
    '''encodes a given English text message and returns Morse code sequences'''
    return 'TODO'

def morse_decode(msg):
    '''decodes a given Morse code message and returns English plain text'''
    return 'TODO'
    
if __name__ == '__main__':
    # print error and exit if not correct arguments
    if len(sys.argv) != 3:
        die(USAGE)

    # string containing command
    cmd = sys.argv[1]
    # English text or Morse sequences
    msg = sys.argv[2]

    # check for valid commands and call handler functions
    if cmd == 'encode':
        res = morse_encode(msg)
    elif cmd == 'decode':
        res = morse_decode(msg)
    else:
        warn(f"no such command: {cmd}\n")
        die(USAGE)

    # print results
    print(res)
