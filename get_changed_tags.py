"""
file: get_changed_tags.py
author: ctremblay
language: Python3
description:
        Sorts the output of a diff -c command
"""

import sys 

def main():
        if( len( sys.argv ) != 2 ):
                print( "Usage: python get_changed_tags.py diff_file" )

        unchanged_tags = set()
        changed_tags = set()
        diff_file = open( sys.argv[1], "r" )
        for line in diff_file:
                tag = line.split( ":" ) 
                if( len( tag ) != 2 ):
                        continue
                if( tag[0][0] == "-" ):
                        changed_tags.add( (tag[0][1:]).strip() )
                else:
                        unchanged_tags.add( (tag[0][1:]).strip() )
        
        unchanged_list = list( unchanged_tags )
        changed_list = list( changed_tags )
        unchanged_list.sort()
        changed_list.sort()

        print( "Unchanged", len( unchanged_list ) )
        for tag in unchanged_list:
                print( tag )
        
        print( "\nChanged", len( changed_list ) )
        for tag in changed_list:
                print( tag )
main()
