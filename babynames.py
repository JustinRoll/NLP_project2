#In the babynames.py file, implement the extract_names(filename) function which takes the filename of a baby1990.html file and returns the data from the file as a single list -- the year string at the start of the list followed by the name-rank strings in alphabetical order. ['2006', 'Aaliyah 91', 'Abagail 895', 'Aaron 57', ...]. Modify main() so it calls your extract_names() function and prints what it returns (main already has the code for the command line argument parsing). If you get stuck working out the regular expressions for the year and each name, solution regular expression patterns are shown at the end of this document.
import re
import os
import sys

def extract_names(fileName):
    with open(fileName) as f:
        fileText = f.read()
        babyDict = {}
        babyList = []
        match = re.search('Popularity in (\d\d\d\d)', fileText)
        year = match.groups()[0]
        f = open(fileName)
        for line in f:
            match = re.search('<.*><td>(\d*)</td><td>(\w*)</td><td>(\w*)', line)
            if match:
                rank = match.groups()[0]
                firstName = match.groups()[1]
                secondName = match.groups()[2]
                babyDict[firstName] = rank
                babyDict[secondName] = rank
                #print "rank: %s firstName: %s secondName %s\n" % rank, firstName, secondName
        #<h3 align="center">Popularity in 1990</h3>
        for key, value in babyDict.items():
            babyList.append(str(key))
        babyList.append("Mitt")
        babyList.append("Frodo") 
            #print key
        babyList.sort()
        babyList = babyList
        return babyList
