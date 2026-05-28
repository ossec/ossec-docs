# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OSSEC'
copyright = 'Atomicorp, Inc. 2025'
author = 'Atomicorp'
release = '4.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Optional: Enable MyST extensions
myst_enable_extensions = [
    "amsmath",         # Math support
    "colon_fence",     # ::: fenced blocks
    "deflist",         # Definition lists
    "fieldlist",       # Field lists for directives
    "html_admonition", # Admonitions
    "html_image",      # Render Markdown images
]

# Paths for custom templates and static files
templates_path = ['_templates']
html_static_path = ['_static']

# Not bad
html_theme = "furo"

html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

html_logo = "ossec_logo_bare_small.png"

