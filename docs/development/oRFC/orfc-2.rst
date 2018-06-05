==========================
oRFC: 2 Coding Style Guide
==========================

OSSEC Coding Style Guide

+-----------+--------------------------------------------------------+
| Name      | OSSEC Style Guide                                      |
+-----------+--------------------------------------------------------+
| Editor    | * Jeremy Rossi <jeremy at jeremyrossi dot com>         |
|           | * Christian Göttsche <cgzones at googlemail dot com>   |
+-----------+--------------------------------------------------------+
| State     | Draft                                                  |
+-----------+--------------------------------------------------------+
| Origin    | * http://zeromq.org/docs:style                         |
|           | * https://www.kernel.org/doc/Documentation/CodingStyle |
+-----------+--------------------------------------------------------+


--------
Language
--------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", 
"SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this 
document are to be interpreted as described in RFC 2119 [#]_.

------
Goals
------

The OSSEC Style Guide is meant to provide framework and guide of formating 
code contributor to OSSEC.  The overall goals are:

* Maximize Readability of code in OSSEC;
* Reduction in the number of bugs by removing ambiguity in code and logic flow;
* Be as minimally invasive as possible while achieving the stated goals; 
* Trust the contributor.

----------
Code Style
----------

Formatter
=========

* `Artistic Style`_ should be used to format the source code.



* Every code style should be achieved by a astyle command argument.

Indentation
===========

* 4 spaces shall be used per indentation level. *--indent=spaces=4*
* Switch and case blocks shall be indented. *--indent-switches*
* Preprocessor conditional statements shall be indeted to the same level as the source code. *--indent-preproc-cond*

File endings
============

* Every files shall end with a newline.
* Every files shall have linux like line endings (\\n). *--lineend=linux*

Breaking long lines and strings
===============================

Placing Braces and Spaces
=========================

* Braces shall be placed according to the stroustrup style. *--style=stroustrup*
* Operators shall be padded by a space. *--pad-oper*
* Every branch of conditional statements shall be surrounded by brackets. *--add-brackets*
* Pointer and reference operators shall be attached to the variable name. *--align-pointer=name*

Typedefs & Struct
=================

Naming
======

* Variables
* Functions
* Typedefs
* Structs


.. _Artistic Style: http://astyle.sourceforge.net/

----------
References
----------

.. [#] "Key words for use in RFCs to Indicate Requirement Levels" - http://tools.ietf.org/html/rfc2119 