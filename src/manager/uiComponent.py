#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**uiComponent.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Ui Component Module.

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

LOGGER = logging.getLogger(Constants.logger)

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************
class UiComponent(QWidget):
	"""
	This class is the UiComponent class.
	"""

	@core.executionTrace
	def __init__(self, name=None, uiFile=None):
		"""
		This method initializes the class.

		:param name: Component name. ( String )
		:param uiFile: Ui file. ( String )
		"""

		LOGGER.debug("> Initializing '{0}()' class.".format(self.__class__.__name__))

		QWidget.__init__(self)

		# --- Setting class attributes. ---
		self.__name = None
		self.name = name

		self.__uiFile = None
		self.uiFile = uiFile

		self.__activated = False
		self.__deactivatable = True

		self.__ui = None

	#***********************************************************************************************
	#***	Attributes properties.
	#***********************************************************************************************
	@property
	def name(self):
		"""
		This method is the property for the __name attribute.

		:return: self.__name. ( String )
		"""

		return self.__name

	@name.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def name(self, value):
		"""
		This method is the setter method for the __name attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("name", value)
		self.__name = value

	@name.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def name(self):
		"""
		This method is the deleter method for the __name attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("name"))

	@property
	def activated(self):
		"""
		This method is the property for the __activated attribute.

		:return: self.__activated. ( String )
		"""

		return self.__activated

	@activated.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def activated(self, value):
		"""
		This method is the setter method for the __activated attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) is bool, "'{0}' attribute: '{1}' type is not 'bool'!".format("activated", value)
		self.__activated = value

	@activated.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def activated(self):
		"""
		This method is the deleter method for the __activated attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("activated"))

	@property
	def deactivatable(self):
		"""
		This method is the property for the __deactivatable attribute.

		:return: self.__deactivatable. ( String )
		"""

		return self.__deactivatable

	@deactivatable.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def deactivatable(self, value):
		"""
		This method is the setter method for the __deactivatable attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) is bool, "'{0}' attribute: '{1}' type is not 'bool'!".format("deactivatable", value)
		self.__deactivatable = value

	@deactivatable.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def deactivatable(self):
		"""
		This method is the deleter method for the __deactivatable attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("deactivatable"))

	@property
	def uiFile(self):
		"""
		This method is the property for the __uiFile attribute.

		:return: self.__uiFile. ( String )
		"""

		return self.__uiFile

	@uiFile.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def uiFile(self, value):
		"""
		This method is the setter method for the __uiFile attribute.

		:param value: Attribute value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' attribute: '{1}' type is not 'str' or 'unicode'!".format("uiFile", value)
			assert os.path.exists(value), "'{0}' attribute: '{1}' ui file doesn't exists!".format("uiFile", value)
		self.__uiFile = value

	@uiFile.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def uiFile(self):
		"""
		This method is the deleter method for the __uiFile attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("uiFile"))

	@property
	def ui(self):
		"""
		This method is the property for the __ui attribute.

		:return: self.__ui. ( Object )
		"""

		return self.__ui

	@ui.setter
	def ui(self, value):
		"""
		This method is the setter method for the __ui attribute.

		:param value: Attribute value. ( Object )
		"""

		self.__ui = value

	@ui.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def ui(self):
		"""
		This method is the deleter method for the __ui attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("ui"))

	#***********************************************************************************************
	#***	Class methods.
	#***********************************************************************************************
	@core.executionTrace
	def _activate(self):
		"""
		This method sets activation state.
		"""

		self.__activated = True

		self._loadUi()

	@core.executionTrace
	def _deactivate(self):
		"""
		This method unsets activation state.
		"""

		self.__activated = False

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def _loadUi(self):
		"""
		This method loads the ui file.
		"""

		if self.__uiFile:
			self.__ui = uic.loadUi(self.__uiFile)
			if "." in sys.path:
				sys.path.remove(".")
			return True
		else:
			raise foundations.exceptions.ProgrammingError, "'{0}' Component ui file doesn't exists!".format(self.__name)

