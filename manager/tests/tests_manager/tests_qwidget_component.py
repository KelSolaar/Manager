#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**tests_QWidget_component**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Defines units tests for :mod:`manager.QWidget_component` module.

**Others:**

"""

#**********************************************************************************************************************
#***	Future imports.
#**********************************************************************************************************************
from __future__ import unicode_literals

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import os
import sys
if sys.version_info[:2] <= (2, 6):
	import unittest2 as unittest
else:
	import unittest
from PyQt4.QtGui import QApplication

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
from manager.QWidget_component import QWidgetComponentFactory

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["RESOURCES_DIRECTORY", "UI_FILE" , "APPLICATION" , "TestQWidgetComponentFactory"]

RESOURCES_DIRECTORY = os.path.join(os.path.dirname(__file__), "resources")
UI_FILE = os.path.join(RESOURCES_DIRECTORY, "standard.ui")

APPLICATION = QApplication(sys.argv)

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
class TestQWidgetComponentFactory(unittest.TestCase):
	"""
	Defines :func:`manager.QWidget_component.QWidgetComponentFactory` factory units tests methods.
	"""

	def test_required_attributes(self):
		"""
		Tests presence of required attributes.
		"""

		required_attributes = ("name",
							"ui_file",
							"activated",
							"initialized_ui",
							"deactivatable")

		for attribute in required_attributes:
			self.assertIn(attribute, dir(QWidgetComponentFactory()))

	def test_required_methods(self):
		"""
		Tests presence of required methods.
		"""

		required_methods = ("activate",
						"deactivate",
						"initialize_ui",
						"uninitialize_ui")

		for method in required_methods:
			self.assertIn(method, dir(QWidgetComponentFactory()))

if __name__ == "__main__":
	import manager.tests.utilities
	unittest.main()
