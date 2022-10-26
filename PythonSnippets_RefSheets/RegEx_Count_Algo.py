#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 11:23:26 2022

@author: craigrupp
"""
import re

# =============================================================================
# The symbols .[....] are used to find expressions that allow any wildcard character
# amount when matching a string based on amount of period type characters used (see below examples)
# =============================================================================
text = "abc a c abbc ac adc"
res_1 = re.findall("a.c", text)
print(res_1)
text_2 = "arsl aeesl a  l as l arsenal"
res_2 = re.findall("a..l", text_2)
print(res_2)
text_3 = "caad cdcd cad ceed cfgrd cfad"
res_3 = re.findall("c..d", text_3)
print(res_3)



# More Flexible RegEx 
# Note : finall with wildcard (felexible armount) returns a list with one index that has all caught matches separated by a space (simple split gets you a list of all caught expression)
text_1 = "abc addc ac axc aOc aeeeb asssec"
result_1 = re.findall("a.*c", text_1)
print(result_1)
result_1[0].split(" ")


def wildcard(string, exp):
    """
    Parameters
    ----------
    string : str
        Like Text Values in Above commmit for string to search for count of returned matches.
    exp : str
        RegEx expression in mold of "a.[+]l" where the string (first argument) will return all matches with a known first character 
        and last character with 1 or more period wildcard characters in between
        Ex : "abc acb aeed adc" str with a RegEx of "a.c" would return the first and last values in the string

    Returns
    -------
    capturedexp : List
        A returned list of all caught expression in the string argument matching to the passed RegEx.

    """
    capturedexp = []
    while string.find(exp[0]) != -1:
        a_ind = string.find(exp[0])
        any_char_count = exp.count('.')
        end_char = string[-1]
        if string[a_ind + (any_char_count + 1)] == end_char and len(string[a_ind:]) > len(exp) + 1:
            end_char_index_inclusion = a_ind + (any_char_count + 1) + 1
            capturedexp.append(string[a_ind:end_char_index_inclusion])
            string = string[end_char_index_inclusion:]
            continue
        elif string[a_ind + (any_char_count + 1)] == end_char and len(string[a_ind:]) < len(exp) + 1:
            # End of String catch
            capturedexp.append(string[a_ind:])
            break
        else:
            string = string[a_ind+1:]
            continue
    return capturedexp
    

print(wildcard(text, "a.c"))
# ['abc', 'a c', 'adc']
print(wildcard(text_3, "c..d"))
# ['caad', 'cdcd', 'ceed', 'cfad']






