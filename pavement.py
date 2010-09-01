from paver.easy import *
import paver.doctools


import sys
sys.path.append("./")


options(
    incoming=Bunch(
        jrossi="http://bitbucket.org/jrossi/ossec-rules", 
        ddpbsd="http://bitbucket.org/ddpbsd/ossec-rules",
        oscar="http://bitbucket.org/oscarschneider/ossec-rules",
        xeno="http://bitbucket.org/XenoPhage/ossec-rules",
    ),
    tests=Bunch(
        tdir="./tests/",
    ),
    sphinx=Bunch(
        builddir="_build",
        sourcedir=".",
        destdir = path("docs") / "docs"
    ),
    ossec=Bunch(
        base="/var/ossec",
        version="2.4.1",
    )
)

@task 
def auto():
    """Auto load the ossec config if installed and readable"""
    p = path("/etc/ossec-init.conf")
    try:
        data = p.open().read()
    except IOError:
        return 

@task 
def incoming():
    """Check for incoming changes from known bitbucket forks"""
    for i in options.incoming.keys():
        results = sh("hg incoming %s"%(options.incoming[i]),ignore_error=True,capture=True)
        if "no changes found" in results:
            info("%s -> no changes found"%(i))
        else:
            error("%s -> changes found: \n %s"%(i, 
                "\n".join(["\t%s"%(x) for x in results.split("\n")])))


@task 
@cmdopts([("xunit", 'x', 'Create XUnit output files')])
def tests():
    """Run all tests on all rules that have them"""
    if options.xunit:
        sh("nosetests --with-xunit or_utils.runtests")
    else:
        sh("nosetests or_utils.runtests")


@task 
def fetch():
    """Pull updates from public repo"""
    sh("hg pull")
    sh("hg update")

@task 
def rules2rst():
    """Convert all rules in to rst pages to act as documations"""
    from or_utils import rules2rst 
    pass


@task 
@needs('paver.doctools.html')
def docs():
    pass 

@task
@needs('clean_docs', 'rules2rst', 'paver.doctools.html')
def html():
    """Generate Publishable HTML docs using sphinx"""
    builtdocs = path("docs") / options.sphinx.builddir / "html"
    builtdocs.move(options.sphinx.destdir) 

@task 
def clean_docs():
    """Clean up and remove all gerenated files"""
    options.sphinx.destdir.rmtree()


@task
def clean_tests():
    """Clean up and remove all temp files created during tests runs"""
    path("nosetests.xml").unlink() 


@task 
@needs('clean_docs', 'clean_tests')
def clean():
    """Clean up and remove all build and other non required files"""
    pass 


