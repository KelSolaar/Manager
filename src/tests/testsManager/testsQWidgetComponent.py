#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**testsQWidgetComponent.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines units tests for :mod:`manager.qwidgetComponent` module.

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
from manager.qwidgetComponent import QWidgetComponent

#***********************************************************************************************
#***	Module attributes.
#***********************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["RESOURCES_DIRECTORY", "UI_FILE" , "APPLICATION" , "ComponentTestCase"]

RESOURCES_DIRECTORY = os.path.join(os.path.dirname(__file__), "resources")
UI_FILE = os.path.join(RESOURCES_DIRECTORY, "standard.ui")

APPLICATION = QApplication(sys.argv)

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************
class ComponentTestCase(unittest.TestCase):
	"""
	This class defines :class:`manager.qwidgetComponent.QWidgetComponent` class units tests methods.
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
			self.assertIn(attribute, dir(QWidgetComponent))

	def testRequiredMethods(self):
		"""
		This method tests presence of required methods.
		"""

		requiredMethods = ("activate",
						"deactivate",
						"loadUi")

		for method in requiredMethods:
			self.assertIn(method, dir(QWidgetComponent))

	def testActivate(self):
		"""
		This method tests :meth:`manager.qwidgetComponent.QWidgetComponent.activate` method.
		"""

		qwidgetComponent = QWidgetComponent(uiFile=UI_FILE)
		qwidgetComponent.activate()
		self.assertTrue(qwidgetComponent.activated)

	def testDeactivate(self):
		"""
		This method tests :meth:`manager.qwidgetComponent.QWidgetComponent.deactivate` method.
		"""

		qwidgetComponent = QWidgetComponent()
		qwidgetComponent.activated = True
		qwidgetComponent.deactivate()
		self.assertFalse(qwidgetComponent.activated)

	def testLoadUi(self):
		"""
		This method tests :meth:`manager.qwidgetComponent.QWidgetComponent.loadUi` method.
		"""

		qwidgetComponent = QWidgetComponent(uiFile=UI_FILE)
		self.assertTrue(qwidgetComponent.loadUi())

if __name__ == "__main__":
	import tests.utilities
	unittest.main()
