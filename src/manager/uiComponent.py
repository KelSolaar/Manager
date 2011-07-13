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
# The Following Code Is Protected By GNU GPL V3 Licence.
#
#***********************************************************************************************

"""
************************************************************************************************
***	uiComponent.py
***
***	Platform:
***		Windows, Linux, Mac Os X
***
***	Description:
***		Ui Component Module.
***
***	Others:
***
************************************************************************************************
"""

#***********************************************************************************************
#***	Python Begin
#***********************************************************************************************

#***********************************************************************************************
#***	External Imports
#***********************************************************************************************
import logging
import os
import sys
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#***********************************************************************************************
#***	Internal Imports
#***********************************************************************************************
import foundations.core as core
import foundations.exceptions
from manager.globals.constants import Constants

#***********************************************************************************************
#***	Global Variables
#***********************************************************************************************
LOGGER = logging.getLogger(Constants.logger)

#***********************************************************************************************
#***	Module Classes And Definitions
#***********************************************************************************************
class UiComponent(QWidget):
	"""
	This Class Is The UiComponent Class.
	"""

	@core.executionTrace
	def __init__(self, name=None, uiFile=None):
		"""
		This Method Initializes The Class.
		
		@param name: Component Name. ( String )
		@param uiFile: Ui File. ( String )
		"""

		LOGGER.debug("> Initializing '{0}()' Class.".format(self.__class__.__name__))

		QWidget.__init__(self)

		# --- Setting Class Attributes. ---
		self.__name = None
		self.name = name

		self.__uiFile = None
		self.uiFile = uiFile

		self.__activated = False
		self.__deactivatable = True

		self.__ui = None

	#***************************************************************************************
	#***	Attributes Properties
	#***************************************************************************************
	@property
	def name(self):
		"""
		This Method Is The Property For The _name Attribute.

		@return: self.__name. ( String )
		"""

		return self.__name

	@name.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def name(self, value):
		"""
		This Method Is The Setter Method For The _name Attribute.
		
		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' Attribute: '{1}' Type Is Not 'str' or 'unicode'!".format("name", value)
		self.__name = value

	@name.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def name(self):
		"""
		This Method Is The Deleter Method For The _name Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("name"))

	@property
	def activated(self):
		"""
		This Method Is The Property For The _activated Attribute.

		@return: self.__activated. ( String )
		"""

		return self.__activated

	@activated.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def activated(self, value):
		"""
		This Method Is The Setter Method For The _activated Attribute.
		
		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) is bool, "'{0}' Attribute: '{1}' Type Is Not 'bool'!".format("activated", value)
		self.__activated = value

	@activated.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def activated(self):
		"""
		This Method Is The Deleter Method For The _activated Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("activated"))

	@property
	def deactivatable(self):
		"""
		This Method Is The Property For The _deactivatable Attribute.

		@return: self.__deactivatable. ( String )
		"""

		return self.__deactivatable

	@deactivatable.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def deactivatable(self, value):
		"""
		This Method Is The Setter Method For The _deactivatable Attribute.
		
		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) is bool, "'{0}' Attribute: '{1}' Type Is Not 'bool'!".format("deactivatable", value)
		self.__deactivatable = value

	@deactivatable.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def deactivatable(self):
		"""
		This Method Is The Deleter Method For The _deactivatable Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("deactivatable"))

	@property
	def uiFile(self):
		"""
		This Method Is The Property For The _uiFile Attribute.

		@return: self.__uiFile. ( String )
		"""

		return self.__uiFile

	@uiFile.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def uiFile(self, value):
		"""
		This Method Is The Setter Method For The _uiFile Attribute.
		
		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' Attribute: '{1}' Type Is Not 'str' or 'unicode'!".format("uiFile", value)
			assert os.path.exists(value), "'{0}' Attribute: '{1}' ui File Doesn't Exists!".format("uiFile", value)
		self.__uiFile = value

	@uiFile.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def uiFile(self):
		"""
		This Method Is The Deleter Method For The _uiFile Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("uiFile"))

	@property
	def ui(self):
		"""
		This Method Is The Property For The _ui Attribute.

		@return: self.__ui. ( Object )
		"""

		return self.__ui

	@ui.setter
	def ui(self, value):
		"""
		This Method Is The Setter Method For The _ui Attribute.
		
		@param value: Attribute Value. ( Object )
		"""

		self.__ui = value

	@ui.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def ui(self):
		"""
		This Method Is The Deleter Method For The _ui Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("ui"))

	#***************************************************************************************
	#***	Class Methods
	#***************************************************************************************
	@core.executionTrace
	def _activate(self):
		"""
		This Method Sets Activation State.
		"""

		self.__activated = True

		self._loadUi()

	@core.executionTrace
	def _deactivate(self):
		"""
		This Method UnSets Activation State.
		"""

		self.__activated = False

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def _loadUi(self):
		"""
		This Method Loads The Ui File.
		"""

		if self.__uiFile:
			self.__ui = uic.loadUi(self.__uiFile)
			if "." in sys.path:
				sys.path.remove(".")
			return True
		else:
			raise foundations.exceptions.ProgrammingError, "'{0}' Component Ui File Doesn't Exists!".format(self.__name)

#***********************************************************************************************
#***	Python End
#***********************************************************************************************
