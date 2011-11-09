#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**testsQObjectComponent.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines units tests for :mod:`manager.qobjectComponent` module.

**Others:**

"""

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import unittest

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
from manager.qobjectComponent import QObjectComponent

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["QObjectComponentTestCase"]

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
class QObjectComponentTestCase(unittest.TestCase):
	"""
	This class defines :class:`manager.qobjectComponent.QObjectComponent` class units tests methods.
	"""

	def testRequiredAttributes(self):
		"""
		This method tests presence of required attributes.
		"""

		requiredAttributes = ("name",
							"activated",
							"deactivatable")

		for attribute in requiredAttributes:
			self.assertIn(attribute, dir(QObjectComponent))

	def testRequiredMethods(self):
		"""
		This method tests presence of required methods.
		"""

		requiredMethods = ("activate",
						"deactivate")

		for method in requiredMethods:
			self.assertIn(method, dir(QObjectComponent))

if __name__ == "__main__":
	import tests.utilities
	unittest.main()
