#!/usr/bin/env python3
from sys import argv

filename = (__file__.split('/')[-1])
argc = len(argv)
cmdargs = []

def get_args():
    args = argv.copy()
    idx = 0
    to_remove = []
    for elem in args:
        if idx in ([0,1] if 'python' in str(args) else [0]):
            if filename in elem or 'python' in elem : to_remove.append(idx)
        idx+=1
    for x in to_remove:
        del(args[x])
    return args

cmdargs = get_args()

def missing_arg():
    print('utilisation : ')
    print(argv[:-len(cmdargs)])

if cmdargs:
    if len(cmdargs) < 2:
        missing_arg()
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
    




