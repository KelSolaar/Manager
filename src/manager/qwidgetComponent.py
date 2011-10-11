#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**qwidgetComponent.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines the :class:`QWidgetComponent` class.

**Others:**

"""

#***********************************************************************************************
#***	External imports.
#***********************************************************************************************
import logging
import os
import sys
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#***********************************************************************************************
#***	Internal imports.
#***********************************************************************************************
import foundations.core as core
import foundations.exceptions
import foundations.ui.common
from manager.globals.constants import Constants

#***********************************************************************************************
#***	Module attributes.
#***********************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER", "QWidgetComponentFactory"]

LOGGER = logging.getLogger(Constants.logger)

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************
def QWidgetComponentFactory(uiFile=None, *args, **kwargs):
	"""
	This definition is a class factory creating :class:`QWidgetComponent` classes using provided ui file.

	:param uiFile: Ui file. ( String )
	:param \*args: Arguments. ( \* )
	:param \*\*kwargs: Keywords arguments. ( \* )
	"""

	class QWidgetComponent(foundations.ui.common.QWidgetFactory(uiFile=uiFile)):
		"""
		This class is the base class for **Manager** package QWidget Components.
		"""

		@core.executionTrace
		def __init__(self, parent=None, name=None, *args, **kwargs):
			"""
			This method initializes the class.
	
			:param parent: Object parent. ( QObject )
			:param name: Component name. ( String )
			:param \*args: Arguments. ( \* )
			:param \*\*kwargs: Keywords arguments. ( \* )
			"""

			LOGGER.debug("> Initializing '{0}()' class.".format(self.__class__.__name__))

			super(QWidgetComponent, self).__init__(parent, *args, **kwargs)

			# --- Setting class attributes. ---
			self.__name = None
			self.name = name

			self.__activated = False
			self.__deactivatable = True

		#***********************************************************************************************
		#***	Attributes properties.
		#***********************************************************************************************
		@property
		def name(self):
			"""
			This method is the property for **self.__name** attribute.
	
			:return: self.__name. ( String )
			"""

			return self.__name

		@name.setter
		@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
		def name(self, value):
			"""
			This method is the setter method for **self.__name** attribute.
	
			:param value: Attribute value. ( String )
			"""

			if value:
				assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("name", value)
			self.__name = value

		@name.deleter
		@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
		def name(self):
			"""
			This method is the deleter method for **self.__name** attribute.
			"""

			raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("name"))

		@property
		def activated(self):
			"""
			This method is the property for **self.__activated** attribute.
	
			:return: self.__activated. ( String )
			"""

			return self.__activated

		@activated.setter
		@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
		def activated(self, value):
			"""
			This method is the setter method for **self.__activated** attribute.
	
			:param value: Attribute value. ( String )
			"""

			if value:
				assert type(value) is bool, "'{0}' attribute: '{1}' type is not 'bool'!".format("activated", value)
			self.__activated = value

		@activated.deleter
		@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
		def activated(self):
			"""
			This method is the deleter method for **self.__activated** attribute.
			"""

			raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("activated"))

		@property
		def deactivatable(self):
			"""
			This method is the property for **self.__deactivatable** attribute.
	
			:return: self.__deactivatable. ( String )
			"""

			return self.__deactivatable

		@deactivatable.setter
		@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
		def deactivatable(self, value):
			"""
			This method is the setter method for **self.__deactivatable** attribute.
	
			:param value: Attribute value. ( String )
			"""

			if value:
				assert type(value) is bool, "'{0}' attribute: '{1}' type is not 'bool'!".format("deactivatable", value)
			self.__deactivatable = value

		@deactivatable.deleter
		@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
		def deactivatable(self):
			"""
			This method is the deleter method for **self.__deactivatable** attribute.
			"""

			raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("deactivatable"))

		#***********************************************************************************************
		#***	Class methods.
		#***********************************************************************************************
		@core.executionTrace
		def activate(self):
			"""
			This method sets Component activation state.
	
			:return: Method success. ( Boolean )
			"""

			self.__activated = True
			return True

		@core.executionTrace
		def deactivate(self):
			"""
			This method unsets Component activation state.
	
			:return: Method success. ( Boolean )
			"""

			self.__activated = False
			return True

	return QWidgetComponent
