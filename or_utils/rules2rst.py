from xml.etree.ElementTree import parse , fromstring 
import sys 
from  paver.path import path 


rulesDir = path("rules")
docsDir = path("docs/rules")

full_tree = {} 
for aFile in rulesDir.walkfiles():
    if aFile.endswith("xml"):
        x = fromstring("<newroot>" + aFile.open().read() + "</newroot>")
        r = x.find("./newroot")
        

