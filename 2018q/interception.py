# -*- coding: utf-8 -*-
"""
Created on Sun Jul 08 19:47:26 2018

@author: yuwan
"""

import sys

def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        parity = int(sys.stdin.readline())
        for _ in range(parity+1):
            sys.stdin.readline()
        if parity%2 == 1:
            print 'Case #{}: {}'.format(case+1, 1)
            print 0
        else:
            print 'Case #{}: {}'.format(case+1, 0)
        
main()
        