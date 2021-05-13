#!/usr/bin/python
#
#  BatchRenameFiles.py
#  Author: Sam Lin
#  Create: May 12, 2021
#
#  Batch renaming of files in a directory.
#
#  This example rename files, which are in 'HDCP' directory, from 'CtvHDCPKey_*.bin' to 'HDCP2_*.bin'.
#  And save new renamed files into 'Output' directory.

import re, os, sys
import shutil

HECTOR_FAIRPLAY_KEY_PREFIX = "FAIRPLAYMT9021000000HS"
HECTOR_WIDEVINE_KEY_PREFIX = "WIDEVNMTK90210000000HS"
OUTPUT_DIR_NAME = "Output"

def rename(inDir, outDir, keyType, strStartNum):
    #if keyType == 'fairplay':
    #    strRe = r'*fairplay*'
    #elif keyType == 'widevine':
    #    strRe = r'*widevine*'
    #else:
    #    print(r'Please confirm which kind of key you want to rename. Only support fairplay or widevine of Hector right.')
    #    sys.exit(1)

    intStartNum = int(strStartNum)
    for pathAndFilename in os.listdir(inDir):
        match = re.search(keyType, str(pathAndFilename))
        if not match:
            print("%s not match" % strRe)
            continue

        if intStartNum > 99999999:
            print(r'The number is out of range. It should be from 0 to 99999999.')
            sys.exit(1)

        shutil.copy(os.path.join(inDir, pathAndFilename), outDir)

        if len(str(intStartNum)) == 1:
            strStartNumTmp = '0000000' + str(intStartNum)
        elif len(str(intStartNum)) == 2:
            strStartNumTmp = '000000' + str(intStartNum)
        elif len(str(intStartNum)) == 3:
            strStartNumTmp = '00000' + str(intStartNum)
        elif len(str(intStartNum)) == 4:
            strStartNumTmp = '0000' + str(intStartNum)
        elif len(str(intStartNum)) == 5:
            strStartNumTmp = '000' + str(intStartNum)
        elif len(str(intStartNum)) == 6:
            strStartNumTmp = '00' + str(intStartNum)
        elif len(str(intStartNum)) == 7:
            strStartNumTmp = '0' + str(intStartNum)
        else:
            strStartNumTmp = str(intStartNum)

        if keyType == 'fairplay':
            strOutputFileName = HECTOR_FAIRPLAY_KEY_PREFIX + strStartNumTmp + r'.bin'
        elif keyType == 'widevine':
            strOutputFileName = HECTOR_WIDEVINE_KEY_PREFIX + strStartNumTmp + r'.bin'

        os.rename(os.path.join(outDir, pathAndFilename), os.path.join(outDir, strOutputFileName))
        intStartNum = intStartNum + 1
        print('%s -> %s' % (os.path.basename(pathAndFilename), strOutputFileName))

def main():
    if len(sys.argv) != 4:
        print(r'usage: python3 BatchRenameAmazonDRMKeys.py path (fairplay or widevine) "starting number".')
        sys.exit(1)

    if len(sys.argv[3]) > 8:
        print(r'The starting number should be from 0 to 99999999')
        sys.exit(1)

    inDir = sys.argv[1]
    outDir = os.path.join(os.getcwd(), OUTPUT_DIR_NAME)
    if os.path.exists(outDir):
        print("Output folder already exist. Delete it.")
        shutil.rmtree(outDir)

    print("Greate Output folder.")
    os.mkdir(outDir)

    rename(inDir, outDir, sys.argv[2], sys.argv[3])

if __name__=='__main__':
    main()