# -*- coding: cp1252 -*-
lines = ['<l n="11">Llyn bwrdd, llawen gwrdd, llawn ged &dash; llu�r Deau,</l>', '<l n="12">Llew�r barnau llawr Berned.</l>', '<l n="13">Llyna gapten Sain Bened</l>', '<l n="14">A llun crair meibion ll&ecirc;n Cred.</l>']

for i, other in enumerate(lines):
    print other,
    if i == len(lines) - 4:
        print "Fish sticks"
    else:
        print ""


