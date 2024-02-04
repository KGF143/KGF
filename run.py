import os, platform

bit = platform.architecture()[0]
if "32bit" in bit:
    __import__("kgf32")
elif "64bit" in bit:
    __import__("kgf64")
else:
    exit()
