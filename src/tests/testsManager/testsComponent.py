#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**testsComponent.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Component tests Module.

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

		component = Component()
		requiredAttributes = ("name",
							"activated",
							"deactivatable")

		for attribute in requiredAttributes:
			self.assertIn(attribute, dir(component))

	def testRequiredMethods(self):
		"""
		This method tests presence of required methods.
		"""

		component = Component()
		requiredMethods = ("_activate",
						"_deactivate")

		for method in requiredMethods:
			self.assertIn(method, dir(component))

	def test_activate(self):
		"""
		This method tests **Component** class **_activate** method.
		"""

		component = Component()
		component._activate()
		self.assertTrue(component.activated)

	def test_deactivate(self):
		"""
		This method tests **Component** class **_deactivate** method.
		"""

		component = Component()
		component.activated = True
		component._deactivate()
		self.assertFalse(component.activated)

if __name__ == "__main__":
	import tests.utilities
	unittest.main()

