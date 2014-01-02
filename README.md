XMLTool
============

The XML Tool will be an application written in Python that can read and validate XML files as well as XSD schema files. It
will also allow for XML files to be validated against XSD schema.

Part 1.
  The XML Validator
    >This portion of the application will read and make sure that the input file is indeed a XML document and it is
    "well formed," i.e. it meets the following requirements:
      >> XML documents must have a root element
      >> XML elements must have a closing tag
      >> XML tags are case sensitive
      >> XML elements must be properly nested
      >> XML attribute values must be quoted
Part 2.
  The XSD Validator
    >This portion of the application will read and make sure that the input file is indeed a XSD schema file and it
    follows the W3 standard.
Part 3.
  The XML vs XSD Validation
    >This portion of the application will read in two files, first a XSD schema and secondly a XML file that will first be
    put through the XML Validator and then it will be validated against the loaded schema.
    
(Optional)
  >Add a text editor feature so the XML and XSD files can be written and automatically edited as the user types them.
    
