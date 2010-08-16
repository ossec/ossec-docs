# -*- coding: utf-8 -*-


def setup(app):
    app.add_object_type('element', 'xml', '%s')
    app.add_object_type('attrubute', 'xml', 'pair: %s; Attrubute')
    app.add_object_type('intopj', 'obj','%s')
   
