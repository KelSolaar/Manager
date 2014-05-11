#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**tests_component_b.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Defines the :class:`TestsComponentB` Component Interface class.

**Others:**

"""

from __future__ import unicode_literals

import foundations.exceptions
import foundations.verbose
from manager.component import Component

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER", "TestsComponentB"]

LOGGER = foundations.verbose.install_logger()

class TestsComponentB(Component):
	"""
	Defines the :mod:`tests.tests_manager.resources.components.core.tests_component_b.tests_component_b`
	Component Interface class.
	"""

	def __init__(self, name=None):
		"""
		Initializes the class.

		:param name: Component name.
		:type name: unicode
		"""

		LOGGER.debug("> Initializing '{0}()' class.".format(self.__class__.__name__))

		Component.__init__(self, name=name)

		# --- Setting class attributes. ---
		self.deactivatable = True

		self.__container = None

	@property
	def container(self):
		"""
		Property for **self.__container** attribute.

		:return: self.__container.
		:rtype: QObject
		"""

		return self.__container

	@container.setter
	@foundations.exceptions.handle_exceptions(foundations.exceptions.ProgrammingError)
	def container(self, value):
		"""
		Setter for **self.__container** attribute.

		:param value: Attribute value.
		:type value: QObject
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "container"))

	@container.deleter
	@foundations.exceptions.handle_exceptions(foundations.exceptions.ProgrammingError)
	def container(self):
		"""
		Deleter for **self.__container** attribute.
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "container"))
	def activate(self, container):
		"""
		Activates the Component.

		:param container: Container to attach the Component to.
		:type container: QObject
		:return: Method success.
		:rtype: bool
		"""

		LOGGER.debug("> Activating '{0}' Component.".format(self.__class__.__name__))

		self.__container = container

		self.activated = True
		return True

	def deactivate(self):
		"""
		Deactivates the Component.

		:return: Method success.
		:rtype: bool
		"""

		LOGGER.debug("> Deactivating '{0}' Component.".format(self.__class__.__name__))

		self.__container = None

		self.activated = False
		return True

	def initialize(self):
		"""
		Initializes the Component.

		:return: Method success.
		:rtype: bool
		"""

		LOGGER.debug("> Initializing '{0}' Component.".format(self.__class__.__name__))

		self.initialized = True
		return True

	def uninitialize(self):
		"""
		Uninitializes the Component.

		:return: Method success.
		:rtype: bool
		"""

		LOGGER.debug("> Uninitializing '{0}' Component.".format(self.__class__.__name__))

		self.initialized = False
		return True

