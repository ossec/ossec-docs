# -*- coding: utf-8 -*-
"""
    sphinx.ext.oldcmarkup
    ~~~~~~~~~~~~~~~~~~~~~


    :copyright: Copyright 2007-2010 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from docutils.parsers.rst import directives

from sphinx.util.compat import Directive

_warned_oldcmarkup = False

class OldCDirective(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'noindex': directives.flag,
        'module': directives.unchanged,
    }

    def run(self):
        env = self.state.document.settings.env
        if not env.app._oldcmarkup_warned:
            env.warn(env.docname, WARNING_MSG, self.lineno)
            env.app._oldcmarkup_warned = True
        newname = 'xml:' + self.name[1:]
        newdir = env.lookup_domain_element('directive', newname)[0]
        return newdir(newname, self.arguments, self.options,
                      self.content, self.lineno, self.content_offset,
                      self.block_text, self.state, self.state_machine).run()


def old_crole(typ, rawtext, text, lineno, inliner, options={}, content=[]):
    env = inliner.document.settings.env
    newtyp = 'xml:' + typ[1:]
    newrole = env.lookup_domain_element('role', newtyp)[0]
    return newrole(newtyp, rawtext, text, lineno, inliner, options, content)


def setup(app):
    app._oldcmarkup_warned = False
    app.add_directive('element', OldCDirective)
    app.add_directive('attrubute', OldCDirective)
    app.add_role('element', old_crole)
    app.add_role('attrubute', old_crole)
