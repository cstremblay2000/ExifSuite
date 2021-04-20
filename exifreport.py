"""
file: exifreport.py
author: ctremblay 
language: Python3 version 3.9.2
description:
        Searches a directory and generates a log file for each file type
        found in the directory. There will be a seperate report for all
        .pdf files, .png files, etc. It will create all log files
        in the current directory
usage:
        Make sure exifreport.py is in your current directory and run 
        
        python exifreport.py <scan_directory> <optional output file name>
        ex. python ./exifreport.py ./exifdata my_reports 

        This would generate file my_reports_pdf.txt, my_reports_png.txt, etc
        for all files
        -------------------
        If exifreport.py or the directoy is not in your current directory you
        can give the file path to it.
        
        ex. python /path/to/exifreport.py /path/to/directory my_reports 
"""

import sys
import os
from datetime import datetime

# Set that contains file extensions
FILE_EXTENSIONS = set()

# list that contails all file
FILES = list()

# Associates the file extension with the log file 
REPORTS_DICT = dict()

# temp file name
TEMP_FILE = "./.exifreport_temp"

# exiftool command
COMMAND = "exiftool -ee -u -P -z %s > %s"

def usage():
        """
        description:
                Print usage message
        returns:
                nothing
        """
        msg = "usage: python exiftool.py scan_directory [output_file_name]"
        print( msg )

def parse_files( scan_directory, prefix ):
        """
        scan_dir -> string, path to directory to be scanned
        prefix -> string, the prefix for the output files
        description:
                Populates FILES with all file paths and populates
                FILE_EXTENSIONS with all file extensions
        returns:
                nothing
        """
        for subdir, dirs, files in os.walk( scan_directory ):
                for file in files:
                        # add file path to FILES set
                        fp = os.path.join( subdir, file )

                        # get file extension
                        ext = file.split( "." )
                        if( len( ext ) == 2 ):
                                add_file( ext[1], prefix )
                                scrape_metadata( fp, ext[1] )

def scrape_metadata( fp, ext ):
        """
        fp -> string, file path to file to scan
        ext -> the extension of the file
        description:
                executes exiftool to scan the file for metadata
                then writes the output to the file in the dictionary
        returns:
                nothing
        """
        res = os.system( COMMAND % (fp, TEMP_FILE) )
        f = open( TEMP_FILE, "r" )
        for line in f:
                REPORTS_DICT[ext].write( line )
        
def add_file( ext, prefix ):
        """
        ext -> String, the file extension
        prefix -> String, the prefix for the file
        description:
                Checks to see if there is an entry for the extension
                in the dictionary before creating a new file
        returns:
                nothing
        """
        if not ext in REPORTS_DICT:
                f = open( "./"+prefix+"_"+ext+".txt", "w+" )
                REPORTS_DICT[ext] = f

def close_files():
        """
        description:
                Closes all files in the reports dictionary
        returns:
                nothing
        """
        for key in REPORTS_DICT:
                REPORTS_DICT[key].close()
        os.system( "rm %s" % TEMP_FILE )

def main():
        """
        """
        l = len( sys.argv )
        if( l < 1 ):
                usage()
                quit()

        scan_dir = sys.argv[1]
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("(%d-%b-%Y)_(%H:%M:%S.%f)")
        prefix = timestampStr
        if( l == 3 ):
                prefix = sys.argv[2] + "_" + prefix
        parse_files( scan_dir, prefix )
        close_files()
main()
