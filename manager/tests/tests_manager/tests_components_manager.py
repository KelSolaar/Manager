#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**tests_components_manager.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Defines units tests for :mod:`manager.components_manager` module.

**Others:**

"""

from __future__ import unicode_literals

import os
import sys
if sys.version_info[:2] <= (2, 6):
	import unittest2 as unittest
else:
	import unittest

from manager.component import Component
from manager.components_manager import Manager
from manager.components_manager import Profile

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["RESOURCES_DIRECTORY",
			"SINGLE_COMPONENT",
			"COMPONENTS_DIRECTORY",
			"COMPONENTS",
			"COMPONENTS_NAMES",
			"COMPONENTS_DEPENDENCY_ORDER",
			"STANDARD_PROFILE_CONTENT",
			"managerCallback",
			"TestProfile",
			"TestManager"]

RESOURCES_DIRECTORY = os.path.join(os.path.dirname(__file__), "resources")
SINGLE_COMPONENT = ("core.tests_component_a", os.path.join(os.path.dirname(__file__),
                                                         "resources/components/core/tests_component_a/tests_component_a.rc"), Component)
COMPONENTS_DIRECTORY = os.path.join(RESOURCES_DIRECTORY, "components")
ALTERNATIVE_COMPONENTS_DIRECTORY = os.path.join(COMPONENTS_DIRECTORY, "extras", "addons")
COMPONENTS = {"core" : {"tests_component_a" : "core/tests_component_a",
					"tests_component_b" : "core/tests_component_b"},
			"addons" : {"tests_component_c" : "core/tests_component_c",
					"tests_component_d" : "core/tests_component_d"}}
COMPONENTS_NAMES = COMPONENTS_DEPENDENCY_ORDER = ["core.tests_component_a",
										"core.tests_component_b",
										"addons.tests_component_c",
										"addons.tests_component_d"]
COMPONENTS_DEPENDENTS = {"core.tests_component_a" : ["core.tests_component_b",
												"addons.tests_component_c",
												"addons.tests_component_d"],
						"core.tests_component_b" : ["addons.tests_component_c",
												"addons.tests_component_d"],
						"addons.tests_component_c" : ["addons.tests_component_d"],
						"addons.tests_component_d" :  []}
STANDARD_PROFILE_CONTENT = {"name" : "core.tests_component_a",
							"file" : os.path.join(COMPONENTS_DIRECTORY, COMPONENTS["core"]["tests_component_a"],
									"tests_component_a.rc"),
							"directory":os.path.join(COMPONENTS_DIRECTORY, COMPONENTS["core"]["tests_component_a"]),
							"title" : "Tests Component A",
							"package" : "tests_component_a",
							"attribute" : "TestsComponentA",
							"require" : [],
							"version" : "1.0",
							"author" : "Thomas Mansencal",
							"email" : "thomas.mansencal@gmail.com",
							"url" : "http://www.hdrlabs.com/",
							"description" : "Core tests Component A."}

def managerCallback(profile):
	"""
	Provides :class:`manager.components_manager.Manager` class test callback.
	"""

	profile.callback = True

class TestProfile(unittest.TestCase):
	"""
	Defines :class:`manager.components_manager.Profile` class units tests methods.
	"""

	def test_required_attributes(self):
		"""
		Tests presence of required attributes.
		"""

		required_attributes = ("name",
							"file",
							"directory",
							"attribute",
							"require",
							"module",
							"interface",
							"category",
							"title",
							"package",
							"version",
							"author",
							"email",
							"url",
							"description")

		for attribute in required_attributes:
			self.assertIn(attribute, dir(Profile))

	def test_required_methods(self):
		"""
		Tests presence of required methods.
		"""

		required_methods = ("initializeProfile",)

		for method in required_methods:
			self.assertIn(method, dir(Profile))

	def test_initialize_profile(self):
		"""
		Tests :meth:`manager.components_manager.Profile.initializeProfile` method.
		"""

		profile = Profile(file=STANDARD_PROFILE_CONTENT["file"])
		self.assertTrue(profile.initializeProfile())
		for attribute, value in STANDARD_PROFILE_CONTENT.iteritems():
			self.assertIsInstance(getattr(profile, attribute), type(value))
			self.assertEqual(getattr(profile, attribute), value)

class TestManager(unittest.TestCase):
	"""
	Defines :class:`manager.components_manager.Manager` class units tests methods.
	"""

	def test_required_attributes(self):
		"""
		Tests presence of required attributes.
		"""

		required_attributes = ("paths",
							"extension",
							"categories",
							"components",)

		for attribute in required_attributes:
			self.assertIn(attribute, dir(Manager))

	def test_required_methods(self):
		"""
		Tests presence of required methods.
		"""

		required_methods = ("__getitem__",
						"__iter__",
						"__contains__",
						"__len__",
						"register_components",
						"unregister_component",
						"register_components",
						"unregister_components",
						"instantiate_component",
						"instantiate_components",
						"reload_component",
						"list_components",
						"list_dependents",
						"filter_components",
						"get_profile",
						"get_interface",
						"get_component_attribute_name")

		for method in required_methods:
			self.assertIn(method, dir(Manager))

	def test__getitem__(self):
		"""
		Tests :meth:`manager.components_manager.Manager.__getitem__` method.
		"""

		manager = Manager([os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS])
		manager.register_components()
		manager.instantiate_components()
		for name, profile in manager:
			self.assertIsInstance(manager[name], Component)

	def test__iter__(self):
		"""
		Tests :meth:`manager.components_manager.Manager.__iter__` method.
		"""

		components_paths = [os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS]
		components_paths.append(ALTERNATIVE_COMPONENTS_DIRECTORY)
		manager = Manager(components_paths)
		manager.register_components()
		for name, profile in manager:
			self.assertIn(name, COMPONENTS_NAMES)
			self.assertIsInstance(profile, Profile)

	def test__contains__(self):
		"""
		Tests :meth:`manager.components_manager.Manager.__contains__` method.
		"""

		components_paths = [os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS]
		components_paths.append(ALTERNATIVE_COMPONENTS_DIRECTORY)
		manager = Manager(components_paths)
		manager.register_components()
		for component in COMPONENTS_NAMES:
			self.assertIn(component, manager)

	def test__len__(self):
		"""
		Tests :meth:`manager.components_manager.Manager.__len__` method.
		"""

		manager = Manager([os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS])
		manager.register_components()
		self.assertEqual(3, len(manager))

	def test_register_component(self):
		"""
		Tests :meth:`manager.components_manager.Manager.register_component` method.
		"""

		manager = Manager()
		self.assertTrue(manager.register_component(SINGLE_COMPONENT[1]))
		self.assertIn(SINGLE_COMPONENT[0], manager.components)

	def test_unregister_component(self):
		"""
		Tests :meth:`manager.components_manager.Manager.unregister_component` method.
		"""

		manager = Manager([os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS])
		manager.register_components()
		manager.instantiate_components()
		for component in dict(manager.components):
			self.assertTrue(manager.unregister_component(component))
		self.assertTrue(not manager.components)

	def test_register_components(self):
		"""
		Tests :meth:`manager.components_manager.Manager.register_components` method.
		"""

		components_paths = [os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS]
		components_paths.append(ALTERNATIVE_COMPONENTS_DIRECTORY)
		manager = Manager(components_paths)
		manager.register_components()
		self.assertIsInstance(manager.components, dict)
		for component in ("{0}.{1}".format(item, name) for item in COMPONENTS for name in COMPONENTS[item]):
			self.assertIn(component, manager.components)

	def test_unregister_components(self):
		"""
		Tests :meth:`manager.components_manager.Manager.unregister_components` method.
		"""

		manager = Manager([os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS])
		manager.register_components()
		manager.instantiate_components()
		manager.unregister_components()
		self.assertTrue(not manager.components)

	def test_instantiate_component(self):
		"""
		Tests :meth:`manager.components_manager.Manager.instantiate_component` method.
		"""

		manager = Manager()
		manager.register_component(SINGLE_COMPONENT[1])
		self.assertTrue(manager.instantiate_component(SINGLE_COMPONENT[0], managerCallback))
		self.assertIsInstance(manager.components.values()[0].interface, SINGLE_COMPONENT[2])

	def test_instantiate_components(self):
		"""
		Tests :meth:`manager.components_manager.Manager.instantiate_components` method.
		"""

		manager = Manager([os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS])
		manager.register_components()
		manager.instantiate_components()
		for component in manager.components.itervalues():
			self.assertIsInstance(component.interface, Component)
		manager.unregister_components()
		manager.register_components()
		manager.instantiate_components(managerCallback)
		for component in manager.components.itervalues():
			self.assertTrue(component.callback)

	def test_reload_component(self):
		"""
		Tests :meth:`manager.components_manager.Manager.reload_component` method.
		"""

		manager = Manager([os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS])
		manager.register_components()
		manager.instantiate_components()
		for component in manager.components:
			manager.reload_component(component)

	def test_list_components(self):
		"""
		Tests :meth:`manager.components_manager.Manager.list_components` method.
		"""

		components_paths = [os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS]
		components_paths.append(ALTERNATIVE_COMPONENTS_DIRECTORY)
		manager = Manager(components_paths)
		manager.register_components()
		manager.instantiate_components()
		components = manager.list_components()
		self.assertIsInstance(components, list)
		self.assertListEqual(components, COMPONENTS_DEPENDENCY_ORDER)
		self.assertListEqual(sorted(manager.list_components(dependency_order=False)), sorted(COMPONENTS_DEPENDENCY_ORDER))

	def test_list_dependents(self):
		"""
		Tests :meth:`manager.components_manager.Manager.list_dependents` method.
		"""

		components_paths = [os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS]
		components_paths.append(ALTERNATIVE_COMPONENTS_DIRECTORY)
		manager = Manager(components_paths)
		manager.register_components()
		manager.instantiate_components()
		for name, profile in manager:
			self.assertListEqual(sorted(COMPONENTS_DEPENDENTS[name]), sorted(manager.list_dependents(name)))

	def test_filter_components(self):
		"""
		Tests :meth:`manager.components_manager.Manager.filter_components` method.
		"""

		manager = Manager([os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS])
		manager.register_components()
		manager.instantiate_components()
		components = manager.filter_components("addons")
		self.assertIsInstance(components, list)
		self.assertListEqual(components, ["addons.tests_component_c"])

	def test_get_profile(self):
		"""
		Tests :meth:`manager.components_manager.Manager.get_profile` method.
		"""

		manager = Manager([os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS])
		manager.register_components()
		manager.instantiate_components()
		for component in manager.components:
			self.assertIsInstance(manager.get_profile(component), Profile)

	def test_get_interface(self):
		"""
		Tests :meth:`manager.components_manager.Manager.get_interface` method.
		"""

		manager = Manager([os.path.join(COMPONENTS_DIRECTORY, item) for item in COMPONENTS])
		manager.register_components()
		manager.instantiate_components()
		for component in manager.components:
			self.assertIsInstance(manager.get_interface(component), Component)

	def test_get_component_attribute_name(self):
		"""
		Tests :meth:`manager.components_manager.Manager.get_component_attribute_name` method.
		"""

		self.assertEquals(Manager.get_component_attribute_name("factory.componentsManagerUi"), "factoryComponentsManagerUi")
		self.assertEquals(Manager.get_component_attribute_name("addons.loggingNotifier"), "addonsLoggingNotifier")
		self.assertEquals(Manager.get_component_attribute_name("myComponent"), "myComponent")

if __name__ == "__main__":
	import manager.tests.utilities
	unittest.main()
