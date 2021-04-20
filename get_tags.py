"""
file: get_tags.py
author: ctremblay
language: python3
description:
        enumerates working directory recursively calling 
        exiftool to get tag names and dumps them out to a file called
        tags.out
"""

import os
import sys

ROOTDIR = '.'
COMMAND = "exiftool -s %s > ./.tmp"

def main():
        if( len( sys.argv ) != 2 ):
                print( "Usage: python get_tags.py output_file" )
                quit()

        OUTFILE = sys.argv[1]
        tags = set()

        for subdir, dirs, files in os.walk( ROOTDIR ):
            for file in files:
                file_path = os.path.join( subdir, file )
                os.system( COMMAND % ( file_path ) )
                tmp = open( "./.tmp", "r" )
                for line in tmp:
                        tag_val = line.split(":")
                        if( len(tag_val) == 2 ):
                                tag = tag_val[0].strip()
                                if( tag == "Error" ):
                                        break
                                if( not tag in tags ):
                                        tags.add( tag )


        tags_list = list( tags )
        tags_list.sort()
        tmp = open( OUTFILE, "w" )
        for tag in tags_list:
                if( tag == tags_list[-1] ):
                        tmp.write( tag )
                else:
                        tmp.write( tag + ", " )

main()
