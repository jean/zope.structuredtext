##############################################################################
#
# Copyright (c) 2001 Zope Corporation and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################
"""
Consider the following example::

  >>> from structuredtext.stng import structurize
  >>> from structuredtext.document import DocumentWithImages
  >>> from structuredtext.html import HTMLWithImages
  >>> from structuredtext.docbook import DocBook

  We first need to structurize the string and make a full-blown
  document out of it:

  >>> struct = structurize(structured_string)
  >>> doc = DocumentWithImages()(struct)

  Now feed it to some output generator, in this case HTML or DocBook:
  
  >>> output = HTMLWithImages()(doc, level=1)
  >>> output = DocBook()(doc, level=1)

$Id: __init__.py,v 1.1 2004/02/19 19:46:31 philikon Exp $
"""
