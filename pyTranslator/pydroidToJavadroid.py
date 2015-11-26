import sys
from PyImport import *
            
class PyCode():
    def __init__(self, src):
        self.src = src
        self.statements = []
        self.parseStatementsFromSrc()
        
    def parseStatementsFromSrc(self):
        lines = self.src.split("\n")
        for line in lines:
            #TODO: condense multiple line statements (e.g. \, parens? etc?) to one line
            #TODO: separate lines by ';' into separate lines
			
			#match an import statement
            if re.match(r'^from ', line) or re.match(r'^import ', line):
                self.statements.append(PyImport(line))
                
            pass
        
    def ToJava_src(self):
        pass

def pyToJava_src(py_src):
    py_code = PyCode(py_src)
    return py_code.ToJava_src()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: Please specify a python source file to convert to java!")
        sys.exit(0)
    filename = sys.argv[1]
    
    with open(filename, 'r') as rf, open(filename+".java") as wf:
        py_src = rf.read()
        java_src = pyToJava_src(py_src)
        
        wf.write(java_src)