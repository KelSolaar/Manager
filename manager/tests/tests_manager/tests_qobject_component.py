#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**tests_QObject_component**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines units tests for :mod:`manager.QObject_component` module.

**Others:**

"""

from __future__ import unicode_literals

import sys
if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

from manager.QObject_component import QObjectComponent

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["TestQObjectComponent"]

class TestQObjectComponent(unittest.TestCase):
    """
    Defines :class:`manager.QObject_component.QObjectComponent` class units tests methods.
    """

    def test_required_attributes(self):
        """
        Tests presence of required attributes.
        """

        required_attributes = ("name",
                            "activated",
                            "initialized",
                            "deactivatable")

        for attribute in required_attributes:
            self.assertIn(attribute, dir(QObjectComponent))

    def test_required_methods(self):
        """
        Tests presence of required methods.
        """

        required_methods = ("activate",
                        "deactivate",
                        "initialize",
                        "uninitialize")

        for method in required_methods:
            self.assertIn(method, dir(QObjectComponent))

if __name__ == "__main__":
    import manager.tests.utilities
    unittest.main()
