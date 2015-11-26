import re

class PyImport():
	def __init__(self, line):
		#TODO, match "import X"
		
		#matching "from X import Y, Z..."
		m = re.match(r'''
					^(?:from)\s				#beginning, "from..."
					([A-Za-z]+)\s			#library name
					(?:import)\s			#"import"
					([A-Za-z]+)\s			#first module name (required)
					(,\s[A-Za-z]+)			#additional module names separated by comma
					''', line)
					
		if m:
			self.is_from = True
			self.lib_name = m.group(1)
			self.importModules(m)
			
			
	def importModules(self, m):
		index = 2
		module = m.group(2)
		self.modules = [module]
		while True:
			index += 1 				#go to next possible module
			try:
				module = m.group(index)
			except: 					#if no more modules, quietly return
				return
			module = module.split(',')[1].strip()	#get rid of leading ", "
			self.modules.append(module)
			
	def toJava(self):
		src = ""
		#TODO, "import X"
		
		#translating "from X import Y, Z"
		if self.is_from:
			for module in modules:
				src += "import " + self.lib_name + "." + module + "\n"
				
		return src