# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:52:14 2017

@author: vase_
"""

import operator


file = open("tweetsCounted.txt", "r") 
i = 0
for line in file: 
    i += 1
print i
file.close()

w, h = 2, i
table = [['' for x in range(w)] for y in range(h)]

file = open("tweetsCounted.txt", "r") 
j=0
for line in file: 
    if line[len(line)-2].isdigit():
        if line[len(line)-3].isdigit():
            if line[len(line)-4].isdigit():
                if line[len(line)-5].isdigit():
                    if line[len(line)-6].isdigit():
                        table[j][1] = int(line[len(line)-6:len(line)-1])
                        table[j][0] = line[1:len(line)-8]
                    else:
                       table[j][1] = int(line[len(line)-5:len(line)-1])
                       table[j][0] = line[1:len(line)-7]
                else:
                    table[j][1] = int(line[len(line)-4:len(line)-1])
                    table[j][0] = line[1:len(line)-6]
            else:
               table[j][1] = int(line[len(line)-3:len(line)-1])
               table[j][0] = line[1:len(line)-5]
        else:
            table[j][1] = int(line[len(line)-2])
            table[j][0] = line[1:len(line)-4]
    #table[j][0] = line[:line[len(line)-5]]
    j += 1

file.close()


sorted_table = sorted(table, key=operator.itemgetter(1), reverse=True)

