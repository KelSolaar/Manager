#!/usr/bin/env python
# -*- coding: utf-8 -*-

#***********************************************************************************************
#
# Copyright (C) 2008 - 2011 - Thomas Mansencal - thomas.mansencal@gmail.com
#
#***********************************************************************************************
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#***********************************************************************************************
#
# The following code is protected by GNU GPL V3 Licence.
#
#***********************************************************************************************

"""
**testsUiComponent.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	UiComponent tests Module.

**Others:**

"""

#***********************************************************************************************
#***	Python begin.
#***********************************************************************************************

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
#***	Overall variables.
#***********************************************************************************************
RESOURCES_DIRECTORY = os.path.join(os.path.dirname(__file__), "resources")
UI_FILE = os.path.join(RESOURCES_DIRECTORY, "standard.ui")

APPLICATION = QApplication(sys.argv)

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************
class ComponentTestCase(unittest.TestCase):
	"""
	This class is the ComponentTestCase class.
	"""

	def testRequiredAttributes(self):
		"""
		This method tests presence of required attributes.
		"""

		uiComponent = UiComponent()
		requiredAttributes = ("name",
							"uiFile",
							"activated",
							"deactivatable",
							"ui")

		for attribute in requiredAttributes:
			self.assertIn(attribute, dir(uiComponent))

	def testRequiredMethods(self):
		"""
		This method tests presence of required methods.
		"""

		uiComponent = UiComponent()
		requiredMethods = ("_activate",
						"_deactivate",
						"_loadUi")

		for method in requiredMethods:
			self.assertIn(method, dir(uiComponent))

	def test_activate(self):
		"""
		This method tests the "uiComponent" class "_activate" method.
		"""

		uiComponent = UiComponent(uiFile=UI_FILE)
		uiComponent._activate()
		self.assertTrue(uiComponent.activated)

	def test_deactivate(self):
		"""
		This method tests the "uiComponent" class "_deactivate" method.
		"""

		uiComponent = UiComponent()
		uiComponent.activated = True
		uiComponent._deactivate()
		self.assertFalse(uiComponent.activated)

	def test_loadUi(self):
		"""
		This method tests the "uiComponent" class "_loadUi" method.
		"""

		uiComponent = UiComponent(uiFile=UI_FILE)
		self.assertTrue(uiComponent._loadUi())

if __name__ == "__main__":
	import tests.utilities
	unittest.main()

#***********************************************************************************************
#***	Python end.
#***********************************************************************************************
