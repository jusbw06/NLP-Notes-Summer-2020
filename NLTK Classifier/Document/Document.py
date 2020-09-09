

# I'm not sure yet that there is an advantage to using the object oriented approach,
# so stay posted on that, or please give me feedback if you know something better

# I would just say, use the "createOperand" and "compare" functions in
# your Knn code until I think this one all the way through
# I'm leaning towards a more simple class approach, but I don't know yet

# I am attempting to design the program so that a single switch in "SETTINGS.py"
# will cause your classifier to use either the graphical or vectorized 
# approach without altering your actual Knn code

# Parent
class Document:
	
	
    def __init__(self):
		pass
		
		
		
	def clean(self):
		pass
		
		
	def createOperand(self):
		pass
		
		
		
	def compare(self, op1, op2):
		pass

# Child
class DocumentVectorized:
	
	
    def __init__(self):
		pass
		
		
		
	def clean(self):
		pass
		
		
	# This creates a word frequency vector
	# One of two operands in a Knn distance comparison
	# This returns that operand
	def createOperand(self):
		pass
		
		
	# This function does the actual comparison of the two 
	# This returns the answer between 0 - 1
	def compare(self, op1, op2):
		pass
		
		
# Child
class DocumentGraph:
	
	
    def __init__(self):
		pass
		
		
		
	def clean(self):
		pass
		
		
	# This creates a graph from the document
	# One of two operands in a Knn distance comparison
	# This returns that operand

	def createOperand(self):
		pass
		
		
	# This function does the actual comparison of the two 
	# This returns the answer between 0 - 1
	def compare(self, op1, op2):
		pass
		
		
		
