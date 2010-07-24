import ConfigParser
import subprocess 
import os 
import sys
import os.path 
#import unittest
#import exception
import nose 

class LogtestError(Exception):
    pass 

def runTest(log, rule, alert, decoder, section, name, negate=False):
    formated = "%s:%s:%s"%(rule,alert,decoder)
    p = subprocess.Popen(['sudo', '/var/ossec/bin/ossec-logtest', '-U',formated],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.PIPE,
            shell=False)
    std_out = p.communicate(log)[0]
    if (p.returncode != 0 and not negate) or (p.returncode == 0 and negate):
        msg = "\n" 
        msg += "Failed: Exit code = %s\n"%(p.returncode) 
        msg += "        Alert     = %s\n"%(alert) 
        msg += "        Rule      = %s\n"%(rule)
        msg += "        Decoder   = %s\n"%(decoder)
        msg += "        Section   = %s\n"%(section)
        msg += "        line name = %s\n"%(name)
        msg += " " 
        raise LogtestError(msg) 
    else:
        return True

def test_generator(tpath="./tests"):
    for aFile in os.listdir(tpath):
        aFile = os.path.join(tpath, aFile)
        print "- [ File = %s ] ---------"%(aFile)
        if aFile.endswith(".ini"):
            tGroup = ConfigParser.ConfigParser()
            tGroup.read([aFile])
            tSections = tGroup.sections()
            for t in tSections:
                sectionCount = 0 
                sectionPass = 0
                rule = tGroup.get(t, "rule")
                alert = tGroup.get(t, "alert")
                decoder = tGroup.get(t, "decoder")
                for (name, value) in tGroup.items(t):
                    if name.startswith("log "):
                        if name.endswith("pass"):
                            neg = False 
                        elif name.endswith("fail"):
                            neg = True
                        else:
                            neg = False 
                        
                        yield runTest, value, rule, alert, decoder, t, name, neg


#if __name__ == "__main__":
#    run()
