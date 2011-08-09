#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**testsUiComponent.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	UiComponent tests Module.

**Others:**

"""

#***********************************************************************************************
#***	External imports.
#***********************************************************************************************
import os
import sys
import unittest
from PyQt4.QtGui import QApplication

#***********************************************************************************************
#***	Internal imports.
#***********************************************************************************************
from manager.uiComponent import UiComponent

#***********************************************************************************************
#***	Module attributes.
#***********************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

RESOURCES_DIRECTORY = os.path.join(os.path.dirname(__file__), "resources")
UI_FILE = os.path.join(RESOURCES_DIRECTORY, "standard.ui")

APPLICATION = QApplication(sys.argv)

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************
class ComponentTestCase(unittest.TestCase):
	"""
	This class is the **ComponentTestCase** class.
	"""

	def testRequiredAttributes(self):
		"""
		This method tests presence of required attributes.
		"""

		requiredAttributes = ("name",
							"uiFile",
							"activated",
							"deactivatable",
							"ui")

		for attribute in requiredAttributes:
			self.assertIn(attribute, dir(UiComponent))

	def testRequiredMethods(self):
		"""
		This method tests presence of required methods.
		"""

		requiredMethods = ("_activate",
						"_deactivate",
						"_loadUi")

		for method in requiredMethods:
			self.assertIn(method, dir(UiComponent))

	def test_activate(self):
		"""
		This method tests **uiComponent** class **_activate** method.
		"""

		uiComponent = UiComponent(uiFile=UI_FILE)
		uiComponent._activate()
		self.assertTrue(uiComponent.activated)

	def test_deactivate(self):
		"""
		This method tests **uiComponent** class **_deactivate** method.
		"""

		uiComponent = UiComponent()
		uiComponent.activated = True
		uiComponent._deactivate()
		self.assertFalse(uiComponent.activated)

	def test_loadUi(self):
		"""
		This method tests **uiComponent** class **_loadUi** method.
		"""

		uiComponent = UiComponent(uiFile=UI_FILE)
		self.assertTrue(uiComponent._loadUi())

if __name__ == "__main__":
	import tests.utilities
	unittest.main()
