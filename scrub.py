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

ROOTDIR = '.'
COM_SCRUB_TAGS = "exiftool -r -overwrite-original -all:all= %s"
COM_REMOVE_DUP_TAGS = "qpdf --linearize --replace-input %s"

def main():
        for subdir, dirs, files in os.walk( ROOTDIR ):
            for file in files:
                file_path = os.path.join( subdir, file )
                os.system( COM_SCRUB_TAGS % ( file_path ) )
                if( ".pdf" in file_path ):
                        os.system( COM_REMOVE_DUP_TAGS % ( file_path ) )
main()
