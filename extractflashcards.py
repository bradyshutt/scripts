#!/usr/bin/env python3

import sys

VERBOSE=False
filename_in = sys.argv[1]
filename_out = sys.argv[1].split('.')[0] + "_flashcards.txt"
terms = [] 
questions = []

def main():
    if len(sys.argv) > 2 and sys.argv[2] == "-v":
        VERBOSE=True

    if VERBOSE: 
        print( "Input File: " + filename_in )
        print( "Output File: " + filename_out )

    if VERBOSE: 
        print( "Scanning file..." )
    scan_file(filename_in) # terms and questions

    print("Word: Definition")
    for (w,d) in terms:
        print(w, ":\t ", d, sep="")


def scan_file(f_name):
    f_in = open(f_name, 'r')

    for line in f_in:
        if VERBOSE: 
            print(line)
        if "[#DEF]:" in line:
            print(line)
            splitline = line.replace('[#DEF]:', '|').split('|')
            terms.append( (splitline[1].strip(), splitline[2].strip()) )
        elif "[#Q]:" in line:
            print(line)
            splitline = line.split('[#Q]:')
            splitline = line.split('|')
            #questions.append( (splitline[0], splitline[1]) )
    f_in.close() 

def write_file(f_name, content):
    f_out = open(f_out, 'w')

if __name__ == "__main__":
    main()

# --------------------------
# EXAMPLE DOCUMENT TO PARSE
# --------------------------
#
# [#DEF]: Oreolization | The realization that oreos are still in your kitchen.
# 
#    * Oreolization was valued in western culture 
#    * Oreos actually cured canser
#    [#DEF]: Yuge |  A variation of the word HUGE commonly used by Donald Trump.
#    
#  [#Q]: Who frequently used the word Yuge, and what does it mean?
#        Donald Trump frequently used it, and it is just a variation of the word "Huge". Significance is unknown. 


