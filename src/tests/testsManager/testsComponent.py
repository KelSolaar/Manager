#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**testsComponent.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines units tests for :mod:`manager.Component` module.

**Others:**

"""

#***********************************************************************************************
#***	External imports.
#***********************************************************************************************
import unittest

#***********************************************************************************************
#***	Internal imports.
#***********************************************************************************************
from manager.component import Component

#***********************************************************************************************
#***	Module attributes.
#***********************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["ComponentTestCase"]

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************
class ComponentTestCase(unittest.TestCase):
	"""
	This class defines :class:`manager.component.Component` class units tests methods.
	"""

	def testRequiredAttributes(self):
		"""
		This method tests presence of required attributes.
		"""

		requiredAttributes = ("name",
							"activated",
							"deactivatable")

		for attribute in requiredAttributes:
			self.assertIn(attribute, dir(Component))

	def testRequiredMethods(self):
		"""
		This method tests presence of required methods.
		"""

		requiredMethods = ("activate",
						"deactivate")

		for method in requiredMethods:
			self.assertIn(method, dir(Component))

	def testActivate(self):
		"""
		This method tests :meth:`manager.component.Component.activate` method.
		"""

		component = Component()
		component.activate()
		self.assertTrue(component.activated)

	def testDeactivate(self):
		"""
		This method tests :meth:`manager.component.Component.deactivate` method.
		"""

		component = Component()
		component.activated = True
		component.deactivate()
		self.assertFalse(component.activated)

if __name__ == "__main__":
	import tests.utilities
	unittest.main()
