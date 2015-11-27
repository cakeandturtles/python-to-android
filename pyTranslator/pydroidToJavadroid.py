import sys
from PyProgram import PyProgram
from PyImport import *

def pyToJava_src(py_src):
    py_prog = PyProgram(py_src)
    return py_prog.ToJava_src()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: Please specify a python source file to convert to java!")
        sys.exit(0)
    filename = sys.argv[1]
    
    with open(filename, 'r') as rf, open(filename+".java") as wf:
        py_src = rf.read()
        java_src = pyToJava_src(py_src)
        
        wf.write(java_src)