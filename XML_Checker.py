#   XML documents must have the version number 
#    and the language encoding on the first line
#	XML documents must have a root element
#	XML elements must have a closing tag
#	XML tags are case sensitive
#	XML elements must be properly nested
#	XML attribute values must be quoted

class XML_Checker(object):
	""" This class contains all the static methods necessary to check an XML file's validation"""

  	def __init__(self, filename):
  		if __xml_file_check(filename):
  			#This variable will hold the object that reads through the XML file
  			self.xml_file = open(filename, "r")
  			#This variable will be used as a dictionary to store the element names
  			self.tag_list = {}
  			#This variable will store the string name of the current tag that the file stream is on
  			self.current_tag = ""
  			#
  			self.version = ""
  			#
  			self.declaration = ""
  			
  	#This static method checks the filename to see if it ends with a ".xml" exstension
  	#If True, then the file is supposed to be an XML file
  	#If False, then either the file's extension was not added or the file is not an XML file
	def __xml_file_check(filename):
		if filename[-4:] != ".xml":
  			return False
  		else:
  			return True
  
  	#This method is used to fill the tag list with an element tag from the XML that we are
  	#currently looking at. The tag list will be a ditionary that holds the name of the 
  	#element and its nest level in the XML file
	def __fill_tag_list(tag_name, level):
 		self.tag_list[tag_name] = level
 	
 	#This method will be used to check to make sure that the first line in the XML file is
 	#the version number and language encoding.
 	def check_for_declaration():
 		self.xml_file.seek(0)
 		firstline = self.xml_file.readline()
 		if firstline[:2] != "<?":
 			return False
 		num = firstline.find("?>", 0, len(firstline))
 		if num == -1:
 			return False
 		self.declaration = firstline[:num+2]
 		return True
 		
 	def get_version():
 		self.declaration.find("version", 2, len(self.declaration)
 		
	def xml_check_attrib():
		pass
    
	def xml_check_nest():
    	pass
    
	def xml_check_case():
    	pass
    
	def xml_root_check():
		pass
	  
	def xml_close_check():
    	self.xml_file.close()
