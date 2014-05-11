#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**QObject_component.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Defines the :class:`QObjectComponent` class.

**Others:**

"""

from __future__ import unicode_literals

from PyQt4.QtCore import QObject
from PyQt4.QtCore import pyqtSignal

import foundations.exceptions
import foundations.verbose

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER", "QObjectComponent"]

LOGGER = foundations.verbose.install_logger()

class QObjectComponent(QObject):
	"""
	Defines the base class for **Manager** package QObject Components.
	"""

	component_activated = pyqtSignal()
	"""
	This signal is emited by the :class:`QObjectComponent` class when the Component is activated.
	"""

	component_deactivated = pyqtSignal()
	"""
	This signal is emited by the :class:`QObjectComponent` class when the Component is deactivated.
	"""

	component_initialized = pyqtSignal()
	"""
	This signal is emited by the :class:`QObjectComponent` class when the Component is initialized.
	"""

	component_uninitialized = pyqtSignal()
	"""
	This signal is emited by the :class:`QObjectComponent` class when the Component is uninitialized.
	"""

	def __init__(self, parent=None, name=None, *args, **kwargs):
		"""
		Initializes the class.

		:param parent: Object parent.
		:type parent: QObject
		:param name: Component name.
		:type name: unicode
		:param \*args: Arguments.
		:type \*args: \*
		:param \*\*kwargs: Keywords arguments.
		:type \*\*kwargs: \*\*
		"""

		LOGGER.debug("> Initializing '{0}()' class.".format(self.__class__.__name__))

		QObject.__init__(self, parent, *args, **kwargs)

		# --- Setting class attributes. ---
		self.__name = None
		self.name = name

		self.__activated = False
		self.__initialized = False
		self.__deactivatable = True

	@property
	def name(self):
		"""
		Property for **self.__name** attribute.

		:return: self.__name.
		:rtype: unicode
		"""

		return self.__name

	@name.setter
	@foundations.exceptions.handle_exceptions(AssertionError)
	def name(self, value):
		"""
		Setter for **self.__name** attribute.

		:param value: Attribute value.
		:type value: unicode
		"""

		if value is not None:
			assert type(value) is unicode, "'{0}' attribute: '{1}' type is not 'unicode'!".format("name", value)
		self.__name = value

	@name.deleter
	@foundations.exceptions.handle_exceptions(foundations.exceptions.ProgrammingError)
	def name(self):
		"""
		Deleter for **self.__name** attribute.
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "name"))

	@property
	def activated(self):
		"""
		Property for **self.__activated** attribute.

		:return: self.__activated.
		:rtype: bool
		"""

		return self.__activated

	@activated.setter
	@foundations.exceptions.handle_exceptions(AssertionError)
	def activated(self, value):
		"""
		Setter for **self.__activated** attribute.

		:param value: Attribute value.
		:type value: bool
		"""

		if value is not None:
			assert type(value) is bool, "'{0}' attribute: '{1}' type is not 'bool'!".format("activated", value)
			self.component_activated.emit() if value else self.component_deactivated.emit()
		self.__activated = value

	@activated.deleter
	@foundations.exceptions.handle_exceptions(foundations.exceptions.ProgrammingError)
	def activated(self):
		"""
		Deleter for **self.__activated** attribute.
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "activated"))

	@property
	def initialized(self):
		"""
		Property for **self.__initialized** attribute.

		:return: self.__initialized.
		:rtype: bool
		"""

		return self.__initialized

	@initialized.setter
	@foundations.exceptions.handle_exceptions(AssertionError)
	def initialized(self, value):
		"""
		Setter for **self.__initialized** attribute.

		:param value: Attribute value.
		:type value: bool
		"""

		if value is not None:
			assert type(value) is bool, "'{0}' attribute: '{1}' type is not 'bool'!".format("initialized", value)
			self.component_initialized.emit() if value else self.component_uninitialized.emit()
		self.__initialized = value

	@initialized.deleter
	@foundations.exceptions.handle_exceptions(foundations.exceptions.ProgrammingError)
	def initialized(self):
		"""
		Deleter for **self.__initialized** attribute.
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "initialized"))

	@property
	def deactivatable(self):
		"""
		Property for **self.__deactivatable** attribute.

		:return: self.__deactivatable.
		:rtype: bool
		"""

		return self.__deactivatable

	@deactivatable.setter
	@foundations.exceptions.handle_exceptions(AssertionError)
	def deactivatable(self, value):
		"""
		Setter for **self.__deactivatable** attribute.

		:param value: Attribute value.
		:type value: bool
		"""

		if value is not None:
			assert type(value) is bool, "'{0}' attribute: '{1}' type is not 'bool'!".format("deactivatable", value)
		self.__deactivatable = value

	@deactivatable.deleter
	@foundations.exceptions.handle_exceptions(foundations.exceptions.ProgrammingError)
	def deactivatable(self):
		"""
		Deleter for **self.__deactivatable** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is not deletable!".format(
		self.__class__.__name__, "deactivatable"))

	@foundations.exceptions.handle_exceptions(NotImplementedError)
	def activate(self):
		"""
		Sets Component activation state.

		:return: Method success.
		:rtype: bool
		"""

		raise NotImplementedError("{0} | '{1}' must be implemented by '{2}' subclasses!".format(
		self.__class__.__name__, self.deactivate.__name__, self.__class__.__name__))

	@foundations.exceptions.handle_exceptions(NotImplementedError)
	def deactivate(self):
		"""
		Unsets Component activation state.

		:return: Method success.
		:rtype: bool
		"""

		raise NotImplementedError("{0} | '{1}' must be implemented by '{2}' subclasses!".format(
		self.__class__.__name__, self.deactivate.__name__, self.__class__.__name__))

	@foundations.exceptions.handle_exceptions(NotImplementedError)
	def initialize(self):
		"""
		Initializes the Component.
		"""

		raise NotImplementedError("{0} | '{1}' must be implemented by '{2}' subclasses!".format(
		self.__class__.__name__, self.deactivate.__name__, self.__class__.__name__))

	@foundations.exceptions.handle_exceptions(NotImplementedError)
	def uninitialize(self):
		"""
		Uninitializes the Component.
		"""

		raise NotImplementedError("{0} | '{1}' must be implemented by '{2}' subclasses!".format(
		self.__class__.__name__, self.deactivate.__name__, self.__class__.__name__))

