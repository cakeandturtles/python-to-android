from PyImport import PyImport

class PyProgram():
    def __init__(self, src):
        self.src = src
        self.statements = []
        self.parseStatementsFromSrc()
        
    def parseStatementsFromSrc(self):
        #need to look at indentation level
        #need to group function definitions and stuff as a single "program/statement" with its own statements?
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