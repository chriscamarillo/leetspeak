from random import choice
import sys

alpha = 'abcdefghijklmnopqrstuvwxyz'
leet = ['aA@4','bB','cC','dD','eE3','fF',
             'gG','hH','iI1!', 'jJ', 'kK', 'lL|',
             'mM', 'nN', 'oO0', 'pP', 'qQ', 'rR',
             'sS$5', 'tT', 'uU', 'vV', 'wW', 'xX',
             'yY', 'zZ']

leet_code = {k: v for k, v in zip(alpha, leet)}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py "<phrase>"')
        exit(1)
    print(''.join(choice(leet_code[w]) if w in leet_code else w for w in sys.argv[1]))