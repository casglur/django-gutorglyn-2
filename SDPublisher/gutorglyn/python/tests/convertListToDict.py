'''
Created on 12 Sep 2011

@author: lsrobert
'''
names = ["Jesus","Marc","Michal"]
places = ["Spain","USA","Poland","UK"]
# Use zip to combine 2 lists
combo = zip(names,places)
# Turn the resulting list into a dictionary
who = dict(combo)
print who
    