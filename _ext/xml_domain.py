# -*- coding: utf-8 -*-


def setup(app):
    app.add_object_type('element', 'xml', '%s')
    app.add_object_type('attribute', 'xml', 'pair: %s; Attribute')
    app.add_object_type('intopt', 'OS','%s')
   
