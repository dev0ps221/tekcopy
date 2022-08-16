#!/usr/bin/env python3

def writeTo(file,lines):
    try:
        file.writelines(lines)
        return True
    except Exception as e:
        print(e.__CAUSE__,' is an exception')
        return False

def readFrom(file):
    return file.readlines()

def copy(src,dst):
    srcFile = open(src,'rb')
    dstFile = open(dst,'ab')
    lines = readFrom(srcFile)
    return writeTo(dstFile,lines)
    


copy('tekcopy.py','tekcopy2.py') 




