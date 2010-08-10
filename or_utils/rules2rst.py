from xml.etree.ElementTree import parse , fromstring 
import sys 
from  paver.path import path 


def indent(elem,level=1):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

rulesDir = path("rules")
decoderDir = path("./decoders/")

rst_rulesDir = path("docs/rules/rules")
rst_decoderDir = path("docs/rules/decoders/")

rule_header = path("docs") / path("header.template.rst")
rh_data = rule_header.bytes()
rule_footer = path("docs") / path("footer.template.rst")
rf_data = rule_footer.bytes()

full_tree = {} 
for aFile in rulesDir.walkfiles():
    if aFile.endswith("xml"):
        x = fromstring("<newroot>" + aFile.bytes() + "</newroot>")
        r = x
        rstFile = rst_rulesDir / "{0}.rst".format(aFile.name )
        f = rstFile.open(mode="w")
        f.write(rh_data.format({"title":aFile.name, "filename":aFile}))
        if r:
            for i in r.findall("./group"):
                f.write("\n\n.. describe:: groups {0}\n".format(i.get("name")))
                if i:
                    for a in i.findall("./rule"):
                        #f.write("\n\nRule ID: {0}\n^^^^^^^^^^^^^^^^^^^^^^\n\n".format(a.get("id")))
                        f.write("\n\n.. describe:: rule-id-{0}\n\n".format(a.get("id")))
                        for z in a.findall("./description"):
                            f.write("\n\n{0}\n\n".format(z.text))
        
        f.write(rf_data.format({"title":aFile.name, "filename":aFile}))
        f.write(".. code-block:: xml\n")
        f.write("   :linenos:\n\n")
        for i in aFile.lines():
            f.write("    " + i)
        f.close()

x = """"
for aFile in decoderDir.walkfiles():
    if aFile.endswith("xml"):
        print aFile.bytes()
        try:

            x = fromstring("<newroot>" + aFile.bytes() + "</newroot>")
        except:
            continue
        r = x
        rstFile = rst_decoderDir / "{0}.rst".format(aFile.name ) 
        f = rstFile.open(mode="w")
        f.write(rh_data.format({"title":aFile.name, "filename":aFile}))
        if r:
            for i in r.findall("./group"):
                f.write("\n\n.. describe:: groups {0}\n".format(i.get("name")))
                if i:
                    for a in i.findall("./rule"):
                        #f.write("\n\nRule ID: {0}\n^^^^^^^^^^^^^^^^^^^^^^\n\n".format(a.get("id")))
                        f.write("\n\n.. describe:: rule-id-{0}\n\n".format(a.get("id")))
                        for z in a.findall("./description"):
                            f.write("\n\n{0}\n\n".format(z.text))
        
        f.write(rf_data.format({"title":aFile.name, "filename":aFile}))
        f.write(".. code-block:: xml\n")
        f.write("   :linenos:\n\n")
        for i in aFile.lines():
            f.write("    " + i)
        f.close()

"""
