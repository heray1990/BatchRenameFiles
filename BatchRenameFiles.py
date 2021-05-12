#!/usr/bin/python
#
#  BatchRenameFiles.py
#  Author: Sam Lin
#  Create: July 11, 2016
#
#  Batch renaming of files in a directory.
#
#  This example rename files, which are in 'HDCP' directory, from 'CtvHDCPKey_*.bin' to 'HDCP2_*.bin'.
#  And save new renamed files into 'Output' directory.

import glob, os, shutil

def rename(outDir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(outDir, pattern)):
        unchangePart = os.path.basename(pathAndFilename).split('_')[1]
        os.rename(pathAndFilename, os.path.join(outDir, titlePattern + unchangePart))
        print('%s -> %s' % (os.path.basename(pathAndFilename), titlePattern + unchangePart))

def main():
    inDir = os.path.join(os.getcwd(), 'HDCP')
    outDir = os.path.join(os.getcwd(), 'Output')
    if os.path.exists(outDir):
        print("Output folder already exist. Delete it.")
        shutil.rmtree(outDir)

    print("Greate Output folder and copy files from Input to Output folder.")
    shutil.copytree(inDir, outDir)

    rename(outDir, r'*.bin', r'HDCP2_')

if __name__=='__main__':
    main()