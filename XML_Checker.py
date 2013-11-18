class XML_Validator(object):
    """
    This class contains all the static methods necessary to check an XML file's validation.
    #XML documents must have the version number 
    #and the language encoding on the first line
    #XML documents must have a root element
    #XML elements must have a closing tag
    #XML tags are case sensitive
    #XML elements must be properly nested
    #XML attribute values must be quoted
    """

    #This static method checks the filename to see if it ends with a ".xml" exstension.
    #If True, then the file is supposed to be an XML file.
    #If False, then either the file's extension was not added or the file is not an XML file.
    def xml_file_check(self, filename):#Finished
        if filename[-4:] != ".xml":
            return False
        else:
            return True
        
    #
    def __init__(self, filename):#Finished
        if self.xml_file_check(filename):
            #This variable will hold the object that reads through the XML file.
            self.xml_file = open(filename, "r")
            #This variable will be used as a dictionary to store the element names.
            self.tag_list = {}
            #This variable will store the string name of the current tag that the file stream is on.
            self.current_tag = ""
            #
            self.version = ""
            #
            self.declaration = ""
            #
            self.encoding = ""

    

    #This method is used to fill the tag list with an element tag from the XML that we are
    #currently looking at. The tag list will be a ditionary that holds the name of the 
    #element and its nest level in the XML file.
    def fill_tag_list(self, tag_name, level):
        self.tag_list[tag_name] = level

    #This method will be used to check to make sure that the first line in the XML file is
    #the version number and language encoding.
    def check_for_declaration(self):#Finished
        self.xml_file.seek(0)
        firstline = self.xml_file.readline()
        if firstline[:2] != "<?":
            return False
        num = firstline.find("?>", 0, len(firstline))
        if num == -1:
            return False
        self.declaration = firstline[:num+2]
        return True

    #
    def get_version(self):#Finished
        test = self.declaration.find("\"", 2, len(self.declaration))
        if test == -1:
            return False
        if self.declaration[test+1:test+3] != "1.":
            return False
        return self.declaration[test+1:self.declaration.find("\"", test+3, len(self.declaration))]
    
    #
    def print_file(self):#Finished
        #self.check_for_declaration()
        #print self.xml_file.seek(len(self.declaration))
        for line in self.xml_file:
            print line

    #
    def xml_check_attrib(self):
        pass
    
    #
    def xml_check_nest(self):
        self.check_for_declaration()
        self.xml_file.seek(len(self.declaration))
        firstline = self.xml_file.readline()
        
        #self.print_file()
        
    #
    def xml_close_check(self):#Finished
        if self.xml_file.closed():
            True
        else:
            False

    
    #
    def xml_file_close(self):#Finished
        self.xml_file.close()
