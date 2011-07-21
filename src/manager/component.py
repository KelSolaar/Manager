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
**component.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Component Module.

**Others:**

"""

#***********************************************************************************************
#***	Python Begin
#***********************************************************************************************

#***********************************************************************************************
#***	External Imports
#***********************************************************************************************
import logging

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
class Component(object):
	"""
	This Class Is The Component Class.
	"""

	@core.executionTrace
	def __init__(self, name=None):
		"""
		This Method Initializes The Class.
		
		@param name: Component Name. ( String )
		"""

		LOGGER.debug("> Initializing '{0}()' Class.".format(self.__class__.__name__))

		# --- Setting Class Attributes. ---
		self.__name = None
		self.name = name

		self.__activated = False
		self.__deactivatable = True

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

		@return: self.__activated. ( Boolean )
		"""

		return self.__activated

	@activated.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def activated(self, value):
		"""
		This Method Is The Setter Method For The _activated Attribute.
		
		@param value: Attribute Value. ( Boolean )
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

		@return: self.__deactivatable. ( Boolean )
		"""

		return self.__deactivatable

	@deactivatable.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def deactivatable(self, value):
		"""
		This Method Is The Setter Method For The _deactivatable Attribute.
		
		@param value: Attribute Value. ( Boolean )
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

	#***************************************************************************************
	#***	Class Methods
	#***************************************************************************************
	@core.executionTrace
	def _activate(self):
		"""
		This Method Sets Activation State.
		"""

		self.__activated = True

	@core.executionTrace
	def _deactivate(self):
		"""
		This Method UnSets Activation State.
		"""

		self.__activated = False

#***********************************************************************************************
#***	Python End
#***********************************************************************************************
