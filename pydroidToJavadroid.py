import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: Please specify a python source file to convert to java!")
        sys.exit(0)
    filename = sys.argv[1]
    
    with open(filename, 'r') as rf, open(filename+".java") as wf:
        py_source = rf.read()
        
        index = 0
        while True:
            py_statement = readStatement(py_source, index)
            java_statement = pyToJava(py_statement)
            wf.write(java_statement)