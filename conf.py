# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath('_ext'))

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
    'xml_domain',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'conf.py.bak',
    '_templates/*.bak',
]

# Optional: Enable MyST extensions
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
]

# Paths for custom templates and static files
templates_path = ['_templates']
html_static_path = ['_static']

html_theme = "furo"

html_css_files = [
    'custom.css',
]

html_logo = "ossec_logo_bare_small.png"
