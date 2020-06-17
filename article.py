# ARTICLE - last updated for NodeBox 1rc7
# Author: Tom De Smedt <tomdesmedt@organisms.be>
# See LICENSE.txt for details.

# Based on the Ruby Linguistics module by Michael Granger:
# http://www.deveiate.org/projects/Linguistics/wiki/English

import re

article_rules = [        

    [re.compile("euler|hour(?!i)|heir|honest|hono"), "an"],       # exceptions: an hour, an honor

    # Abbreviations
    # Strings of capitals starting with a vowel-sound consonant
    # followed by another consonant,
    # and which are not likely to be real words.
    [re.compile("(?!FJO|[HLMNS]Y.|RY[EO]|SQU|(F[LR]?|[HL]|MN?|N|RH?|S[CHKLMNPTVW]?|X(YL)?)[AEIOU])[FHLMNRSX][A-Z]"), "an"],
    [re.compile("^[aefhilmnorsx][.-]"), "an"],
    [re.compile("^[a-z][.-]"), "a"],

    [re.compile("^[^aeiouy]"), "a"],                              # consonants: a bear
    [re.compile("^e[uw]"), "a"],                                  # eu like "you": a european
    [re.compile("^onc?e"), "a"],                                  # o like "wa": a one-liner
    [re.compile("uni([^nmd]|mo)"), "a"],                          # u like "you": a university
    [re.compile("^u[bcfhjkqrst][aeiou]"), "a"],                   # u like "you": a uterus
    [re.compile("^[aeiou]"), "an"],                               # vowels: an owl
    [re.compile("y(b[lor]|cl[ea]|fere|gg|p[ios]|rou|tt)"), "an"], # y like "i": an yclept, a year
    [re.compile(""), "a"]                                         # guess "a"

]

def article(word):
    
    """ Returns the indefinite article for a given word.
    
    For example: university -> a university.
    
    """

    for pattern, article in article_rules:
        if pattern.search(word) is not None:
            return article + " " + word

def a(word): 
    return article(word)

def an(word):
    return article(word)

#print article("hour")        
#print article("FBI")
#print article("bear")
#print article("one-liner")
#print article("european")
#print article("university")
#print article("uterus")
#print article("owl")
#print article("yclept")
#print article("year")
