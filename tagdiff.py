"""
file: tagdiff.py
author: ctremblay
language: Python3
descirption:
        opens two tag files and compares which ones
        are there and which ones aren't 
"""

import sys

def main():
        if( len( sys.argv ) != 3 ):
                print( "Usage: python tagdiff.py unscrubbed_tag_file srubbed_tag_file" )
                quit()
        unscrubbed_tag_file = open( sys.argv[1], "r" )
        scrubbed_tag_file = open( sys.argv[2], "r" )

        scrubbed_tags = set()
        for line in scrubbed_tag_file:
                for tag in line.split(","):
                        scrubbed_tags.add( tag )

        tags_gone = list()
        for line in unscrubbed_tag_file:
                for tag in line.split(","):
                        if( not tag in scrubbed_tags ):
                                tags_gone.add( tag )

        print( tags_gone )
        tags_gone.sort()
        for tag in tags_gone:
                if( tag == tags_gone[-1] ):
                        print( tag, end='' )
                else:
                        print( tag, end=', ' )

main()
