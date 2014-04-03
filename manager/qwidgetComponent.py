#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**qwidgetComponent.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Defines the :class:`QWidgetComponent` class.

**Others:**

"""

#**********************************************************************************************************************
#***	Future imports.
#**********************************************************************************************************************
from __future__ import unicode_literals

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
from PyQt4.QtCore import pyqtSignal

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
import foundations.exceptions
import foundations.verbose
import foundations.ui.common

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER", "QWidgetComponentFactory"]

LOGGER = foundations.verbose.installLogger()

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
def QWidgetComponentFactory(uiFile=None, *args, **kwargs):
	"""
	Defines a class factory creating :class:`QWidgetComponent` classes using given ui file.

	:param uiFile: Ui file.
	:type uiFile: unicode
	:param \*args: Arguments.
	:type \*args: \*
	:param \*\*kwargs: Keywords arguments.
	:type \*\*kwargs: \*\*
	:return: QWidgetComponent class.
	:rtype: QWidgetComponent
	"""

	class QWidgetComponent(foundations.ui.common.QWidgetFactory(uiFile=uiFile)):
		"""
		Defines the base class for **Manager** package QWidget Components.
		"""

		componentActivated = pyqtSignal()
		"""
		This signal is emited by the :class:`QObjectComponent` class when the Component is activated. ( pyqtSignal )
		"""

		componentDeactivated = pyqtSignal()
		"""
		This signal is emited by the :class:`QObjectComponent` class when the Component is deactivated. ( pyqtSignal )
		"""

		componentInitializedUi = pyqtSignal()
		"""
		This signal is emited by the :class:`QObjectComponent` class when the Component ui is initialized. ( pyqtSignal )
		"""

		componentUninitializedUi = pyqtSignal()
		"""
		This signal is emited by the :class:`QObjectComponent` class when the Component ui is uninitialized. ( pyqtSignal )
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

			super(QWidgetComponent, self).__init__(parent, *args, **kwargs)

			# --- Setting class attributes. ---
			self.__name = None
			self.name = name

			self.__activated = False
			self.__initializedUi = False
			self.__deactivatable = True

		#**************************************************************************************************************
		#***	Attributes properties.
		#**************************************************************************************************************
		@property
		def name(self):
			"""
			Property for **self.__name** attribute.
	
			:return: self.__name.
			:rtype: unicode
			"""

			return self.__name

		@name.setter
		@foundations.exceptions.handleExceptions(AssertionError)
		def name(self, value):
			"""
			Setter for **self.__name** attribute.
	
			:param value: Attribute value.
			:type value: unicode
			"""

			if value is not None:
				assert type(value) is unicode, "'{0}' attribute: '{1}' type is not 'unicode'!".format(
				"name", value)
			self.__name = value

		@name.deleter
		@foundations.exceptions.handleExceptions(foundations.exceptions.ProgrammingError)
		def name(self):
			"""
			Deleter for **self.__name** attribute.
			"""

			raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is not deletable!".format(
			self.__class__.__name__, "name"))

		@property
		def activated(self):
			"""
			Property for **self.__activated** attribute.
	
			:return: self.__activated.
			:rtype: unicode
			"""

			return self.__activated

		@activated.setter
		@foundations.exceptions.handleExceptions(AssertionError)
		def activated(self, value):
			"""
			Setter for **self.__activated** attribute.
	
			:param value: Attribute value.
			:type value: unicode
			"""

			if value is not None:
				assert type(value) is bool, "'{0}' attribute: '{1}' type is not 'bool'!".format("activated", value)
				self.componentActivated.emit() if value else self.componentDeactivated.emit()
			self.__activated = value

		@activated.deleter
		@foundations.exceptions.handleExceptions(foundations.exceptions.ProgrammingError)
		def activated(self):
			"""
			Deleter for **self.__activated** attribute.
			"""

			raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is not deletable!".format(
			self.__class__.__name__, "activated"))

		@property
		def initializedUi(self):
			"""
			Property for **self.__initializedUi** attribute.
	
			:return: self.__initializedUi.
			:rtype: bool
			"""

			return self.__initializedUi

		@initializedUi.setter
		@foundations.exceptions.handleExceptions(AssertionError)
		def initializedUi(self, value):
			"""
			Setter for **self.__initializedUi** attribute.
	
			:param value: Attribute value.
			:type value: bool
			"""

			if value is not None:
				assert type(value) is bool, "'{0}' attribute: '{1}' type is not 'bool'!".format("initializedUi", value)
				self.componentInitializedUi.emit() if value else self.componentUninitializedUi.emit()
			self.__initializedUi = value

		@initializedUi.deleter
		@foundations.exceptions.handleExceptions(foundations.exceptions.ProgrammingError)
		def initializedUi(self):
			"""
			Deleter for **self.__initializedUi** attribute.
			"""

			raise foundations.exceptions.ProgrammingError(
			"{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "initializedUi"))

		@property
		def deactivatable(self):
			"""
			Property for **self.__deactivatable** attribute.
	
			:return: self.__deactivatable.
			:rtype: unicode
			"""

			return self.__deactivatable

		@deactivatable.setter
		@foundations.exceptions.handleExceptions(AssertionError)
		def deactivatable(self, value):
			"""
			Setter for **self.__deactivatable** attribute.
	
			:param value: Attribute value.
			:type value: unicode
			"""

			if value is not None:
				assert type(value) is bool, "'{0}' attribute: '{1}' type is not 'bool'!".format("deactivatable", value)
			self.__deactivatable = value

		@deactivatable.deleter
		@foundations.exceptions.handleExceptions(foundations.exceptions.ProgrammingError)
		def deactivatable(self):
			"""
			Deleter for **self.__deactivatable** attribute.
			"""

			raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is not deletable!".format(
			self.__class__.__name__, "deactivatable"))

		#**************************************************************************************************************
		#***	Class methods.
		#**************************************************************************************************************
		@foundations.exceptions.handleExceptions(NotImplementedError)
		def activate(self):
			"""
			Sets Component activation state.
	
			:return: Method success.
			:rtype: bool
			"""

			raise NotImplementedError("{0} | '{1}' must be implemented by '{2}' subclasses!".format(
			self.__class__.__name__, self.activate.__name__, self.__class__.__name__))

		@foundations.exceptions.handleExceptions(NotImplementedError)
		def deactivate(self):
			"""
			Unsets Component activation state.
	
			:return: Method success.
			:rtype: bool
			"""

			raise NotImplementedError("{0} | '{1}' must be implemented by '{2}' subclasses!".format(
			self.__class__.__name__, self.deactivate.__name__, self.__class__.__name__))

		@foundations.exceptions.handleExceptions(NotImplementedError)
		def initializeUi(self):
			"""
			Initializes the Component ui.
			"""

			raise NotImplementedError("{0} | '{1}' must be implemented by '{2}' subclasses!".format(
			self.__class__.__name__, self.deactivate.__name__, self.__class__.__name__))

		@foundations.exceptions.handleExceptions(NotImplementedError)
		def addWidget(self):
			"""
			Adds the Component Widget ui.
			"""

			raise NotImplementedError("{0} | '{1}' must be implemented by '{2}' subclasses!".format(
			self.__class__.__name__, self.deactivate.__name__, self.__class__.__name__))

		@foundations.exceptions.handleExceptions(NotImplementedError)
		def removeWidget(self):
			"""
			Removes the Component Widget ui.
			"""

			raise NotImplementedError("{0} | '{1}' must be implemented by '{2}' subclasses!".format(
			self.__class__.__name__, self.deactivate.__name__, self.__class__.__name__))

		@foundations.exceptions.handleExceptions(NotImplementedError)
		def uninitializeUi(self):
			"""
			Uninitializes the Component ui.
			"""

			raise NotImplementedError("{0} | '{1}' must be implemented by '{2}' subclasses!".format(
			self.__class__.__name__, self.deactivate.__name__, self.__class__.__name__))

	return QWidgetComponent
