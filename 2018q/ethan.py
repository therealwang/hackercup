# -*- coding: utf-8 -*-
"""
Created on Sun Jul 08 19:51:57 2018

@author: yuwan
"""

import sys

def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        word = sys.stdin.readline().strip()
        out = ethan(word)
        print 'Case #{}: {}'.format(case+1, out)
                    
                    
def ethan(word):
    for i in range(1,len(word)):
        if word[i] != word[0]:
            continue
        else:
            j = 1
            while i+j < len(word):
                if word[i+j] != word[j]:
                    return word[:i]+word
                else:
                    j += 1
    return 'Impossible'

main()