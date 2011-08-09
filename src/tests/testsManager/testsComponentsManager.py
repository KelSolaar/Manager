#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**testsManager.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Manager tests Module.

**Others:**

"""

#***********************************************************************************************
#***	External imports.
#***********************************************************************************************
import os
import unittest

#***********************************************************************************************
#***	Internal imports.
#***********************************************************************************************
from manager.component import Component
from manager.componentsManager import Manager, Profile

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
COMPONENTS_DIRECTORY = os.path.join(RESOURCES_DIRECTORY, "components")
COMPONENTS = {"core":{"testsComponentA":"core/testsComponentA",
					"testsComponentB":"core/testsComponentB"},
			"addons":{"testsComponentC":"core/testsComponentC"}}
COMPONENTS_RANKING = ["core.testsComponentA", "core.testsComponentB", "addons.testsComponentC"]
STANDARD_PROFILE_CONTENT = {"name":"core.testsComponentA",
							"path":os.path.join(COMPONENTS_DIRECTORY, COMPONENTS["core"]["testsComponentA"]),
							"module":"testsComponentA",
							"object_":"TestsComponentA",
							"rank":"10",
							"version":"1.0",
							"author":"Thomas Mansencal",
							"email":"thomas.mansencal@gmail.com",
							"url":"http://www.hdrlabs.com/",
							"description":"Core tests Component A."}

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************
class ProfileTestCase(unittest.TestCase):
	"""
	This class is the **ProfileTestCase** class.
	"""

	def testRequiredAttributes(self):
		"""
		This method tests presence of required attributes.
		"""

		requiredAttributes = ("name",
							"path",
							"object_",
							"rank",
							"import_",
							"interface",
							"categorie",
							"module",
							"version",
							"author",
							"email",
							"url",
							"description")

		for attribute in requiredAttributes:
			self.assertIn(attribute, dir(Profile))

def testManagerCallback(profile):
	"""
	This definition is the Manager test callback.
	"""

	profile.callback = True

class ManagerTestCase(unittest.TestCase):
	"""
	This class is the **ManagerTestCase** class.
	"""

	def testRequiredAttributes(self):
		"""
		This method tests presence of required attributes.
		"""

		requiredAttributes = ("paths",
							"extension",
							"categories",
							"components",)

		for attribute in requiredAttributes:
			self.assertIn(attribute, dir(Manager))

	def testRequiredMethods(self):
		"""
		This method tests presence of required methods.
		"""

		requiredMethods = ("getProfile",
						"getComponents",
						"gatherComponents",
						"instantiateComponents",
						"reloadComponent",
						"filterComponents",
						"getInterface")

		for method in requiredMethods:
			self.assertIn(method, dir(manager))

	def testGetProfile(self):
		"""
		This method tests **Manager** class **getProfile** method.
		"""

		path = os.path.join(COMPONENTS_DIRECTORY, COMPONENTS["core"]["testsComponentA"], "testsComponentA.rc")

		manager = Manager()
		profile = manager.getProfile(path)
		self.assertIsInstance(profile, Profile)
		for attribute, value in STANDARD_PROFILE_CONTENT.items():
			self.assertIsInstance(getattr(profile, attribute), type(value))
			self.assertEqual(getattr(profile, attribute), value)

	def testGatherComponents(self):
		"""
		This method tests **Manager** class **gatherComponents** method.
		"""

		manager = Manager({item : os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS.keys()})
		manager.gatherComponents()
		self.assertIsInstance(manager.components, dict)
		for component in ("{0}.{1}".format(item, name) for item in COMPONENTS.keys() for name in COMPONENTS[item].keys()):
			self.assertIn(component, manager.components.keys())

	def testInstantiateComponents(self):
		"""
		This method tests **Manager** class **instantiateComponents** method.
		"""

		manager = Manager({item : os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS.keys()})
		manager.gatherComponents()
		manager.instantiateComponents()
		for component in manager.components.values():
			self.assertIsInstance(component.interface, Component)
		manager.clearComponents()
		manager.gatherComponents()
		manager.instantiateComponents(testManagerCallback)
		for component in manager.components.values():
			self.assertTrue(component.callback)

	def testDeleteComponents(self):
		"""
		This method tests **Manager** class **deleteComponents** method.
		"""

		manager = Manager({item : os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS.keys()})
		manager.gatherComponents()
		manager.instantiateComponents()
		for component in dict(manager.components).keys():
			self.assertTrue(manager.deleteComponent(component))
		self.assertTrue(not manager.components.keys())

	def testClearComponents(self):
		"""
		This method tests **Manager** class **clearComponents** method.
		"""

		manager = Manager({item : os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS.keys()})
		manager.gatherComponents()
		manager.instantiateComponents()
		manager.clearComponents()
		self.assertTrue(not manager.components.keys())

	def testReloadComponent(self):
		"""
		This method tests **Manager** class **reloadComponent** method.
		"""

		manager = Manager({item : os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS.keys()})
		manager.gatherComponents()
		manager.instantiateComponents()
		for component in manager.components.keys():
			manager.reloadComponent(component)

	def testGetComponents(self):
		"""
		This method tests **Manager** class **getComponents** method.
		"""

		manager = Manager({item : os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS.keys()})
		manager.gatherComponents()
		manager.instantiateComponents()
		components = manager.getComponents()
		self.assertIsInstance(components, list)
		self.assertListEqual(components, COMPONENTS_RANKING)

	def testFilterComponents(self):
		"""
		This method tests **Manager** class **filterComponents** method.
		"""

		manager = Manager({item : os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS.keys()})
		manager.gatherComponents()
		manager.instantiateComponents()
		components = manager.filterComponents("addons")
		self.assertIsInstance(components, list)
		self.assertListEqual(components, ["addons.testsComponentC"])

	def testGetInterface(self):
		"""
		This method tests **Manager** class **getInterface** method.
		"""

		manager = Manager({item : os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS.keys()})
		manager.gatherComponents()
		manager.instantiateComponents()
		for component in manager.components.keys():
			self.assertIsInstance(manager.getInterface(component), Component)

if __name__ == "__main__":
	import tests.utilities
	unittest.main()
