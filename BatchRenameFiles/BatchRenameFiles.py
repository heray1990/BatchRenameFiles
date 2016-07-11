#!/usr/bin/python
#
#  BatchRenameFiles.py
#  Author: Sam Lin
#  Create: July 11, 2016
#
#  Batch renaming of files in a directory.
#
#  This example rename files, which are in 'HDCP' directory, from 'CtvHDCPKey_*.bin' to 'HDCP2_*.bin'.

import glob, os

def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        unchangePart = os.path.basename(pathAndFilename).split('_')[1]
        os.rename(pathAndFilename, os.path.join(dir, titlePattern + unchangePart))
        print('%s -> %s' % (os.path.basename(pathAndFilename), titlePattern + unchangePart))

def main():
    rename(os.path.join(os.getcwd(), 'HDCP'), r'*.bin', r'HDCP2_')

if __name__=='__main__':
    main()