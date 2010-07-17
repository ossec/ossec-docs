from paver.easy import *
import paver.doctools


options(
    sphinx=Bunch(
        builddir="_build",
        sourcedir="."
    )
)

@task
@needs('paver.doctools.html')
def html():
    builtdocs = path("docs") / options.sphinx.builddir / "html"
    destdir = path("docs") / "docs"
    destdir.rmtree()
    builtdocs.move(destdir)
