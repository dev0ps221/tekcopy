#!/usr/bin/env python3
from sys import argv

filename = (__file__.split('/')[-1])
argc = len(argv)

def get_args():
    args = argv
    idx = 0
    to_remove = []
    for elem in args:
        if filename in elem or 'python' in elem : to_remove.append(idx)
        idx+=1
    for idx in to_remove:
        del(args[idx])
    return args

print(get_args())

def writeTo(file,lines):
    try:
        file.writelines(lines)
        return True
    except Exception as e:
        print(e.__CAUSE__,' is an exception')
        return False

def readFrom(file):
    return file.readlines()

def tekcopy(src,dst):
    srcFile = open(src,'rb')
    dstFile = open(dst,'ab')
    lines = readFrom(srcFile)
    return writeTo(dstFile,lines)
    




