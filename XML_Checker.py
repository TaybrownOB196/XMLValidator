#	XML documents must have a root element
#	XML elements must have a closing tag
#	XML tags are case sensitive
#	XML elements must be properly nested
#	XML attribute values must be quoted

class XML_Checker:
  """ This class contains all the static methods necessary to check the xml file"""
  
 
  current_tag = ""
  #This variable will be used as a dictionary to store the element names
  tag_list = {};
  
  #This static method checks the filename to see if it ends with a ".xml" exstension
  #If True, then the file is supposed to be an XML file
  #If False, then either the file's extension was not added or the file is not an XML file
  def xml_file_check(filename):
  	if filename[:-4] != ".xml":
  		return False
  	else
  		return True
  
  def xml_check_attrib():
	pass
    
  def xml_check_nest():
    pass
    
  def xml_check_case():
    pass
    
  def xml_root_check():
	pass
	  
  def xml_close_check():
    pass
