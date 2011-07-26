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
**manager.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Manager Module.

**Others:**

"""

#***********************************************************************************************
#***	Python begin.
#***********************************************************************************************

#***********************************************************************************************
#***	External imports.
#***********************************************************************************************
import inspect
import logging
import os
import sys
import re

#***********************************************************************************************
#***	Internal imports.
#***********************************************************************************************
import foundations.core as core
import foundations.exceptions
from foundations.parser import Parser
from foundations.walker import Walker
from manager.component import Component
from manager.globals.constants import Constants
from manager.uiComponent import UiComponent

#***********************************************************************************************
#***	Global variables.
#***********************************************************************************************
LOGGER = logging.getLogger(Constants.logger)

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************
class Profile(object):
	"""
	This Class Is The Profile Class.
	"""

	@core.executionTrace
	def __init__(self, name=None, path=None):
		"""
		This Method Initializes The Class.

		@param name: Name Of The Component. ( String )
		@param path: Path Of The Component. ( String )
		"""

		LOGGER.debug("> Initializing '{0}()' Class.".format(self.__class__.__name__))

		# --- Setting class attributes. ---
		self.__name = None
		self.name = name
		self.path = None
		self.__path = path

		self.__object_ = None
		self.__rank = None
		self.__import = None
		self.__interface = None
		self.__categorie = None

		self.__module = None
		self.__version = None
		self.__author = None
		self.__email = None
		self.__url = None
		self.__description = None

	#***********************************************************************************************
	#***	Attributes properties.
	#***********************************************************************************************
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
	def path(self):
		"""
		This Method Is The Property For The _path Attribute.

		@return: self.__path. ( String )
		"""

		return self.__path

	@path.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def path(self, value):
		"""
		This Method Is The Setter Method For The _path Attribute.

		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' Attribute: '{1}' Type Is Not 'str' or 'unicode'!".format("path", value)
			assert os.path.exists(value), "'{0}' Attribute: '{1}' Directory Doesn't Exists!".format("path", value)
		self.__path = value

	@path.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def path(self):
		"""
		This Method Is The Deleter Method For The _path Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("path"))

	@property
	def object_(self):
		"""
		This Method Is The Property For The _object_ Attribute.

		@return: self.__object_. ( String )
		"""

		return self.__object_

	@object_.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def object_(self, value):
		"""
		This Method Is The Setter Method For The _object_ Attribute.

		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' Attribute: '{1}' Type Is Not 'str' or 'unicode'!".format("object_", value)
		self.__object_ = value

	@object_.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def object_(self):
		"""
		This Method Is The Deleter Method For The _object_ Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("object_"))

	@property
	def rank(self):
		"""
		This Method Is The Property For The _rank Attribute.

		@return: self.__rank. ( String )
		"""

		return self.__rank

	@rank.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def rank(self, value):
		"""
		This Method Is The Setter Method For The _rank Attribute.

		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' Attribute: '{1}' Type Is Not 'str' or 'unicode'!".format("rank", value)
		self.__rank = value

	@rank.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def rank(self):
		"""
		This Method Is The Deleter Method For The _rank Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("rank"))

	@property
	def import_(self):
		"""
		This Method Is The Property For The _import_ Attribute.

		@return: self.__import. ( Module )
		"""

		return self.__import

	@import_.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def import_(self, value):
		"""
		This Method Is The Setter Method For The _import_ Attribute.

		@param value: Attribute Value. ( Module )
		"""

		if value:
			assert type(value) is type(sys), "'{0}' Attribute: '{1}' Type Is Not 'module'!".format("import", value)
		self.__import = value

	@import_.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def import_(self):
		"""
		This Method Is The Deleter Method For The _import_ Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("import"))

	@property
	def interface(self):
		"""
		This Method Is The Property For The _interface Attribute.

		@return: self.__interface. ( Object )
		"""

		return self.__interface

	@interface.setter
	def interface(self, value):
		"""
		This Method Is The Setter Method For The _interface Attribute.

		@param value: Attribute Value. ( Object )
		"""

		self.__interface = value

	@interface.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def interface(self):
		"""
		This Method Is The Deleter Method For The _interface Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("interface"))

	@property
	def categorie(self):
		"""
		This Method Is The Property For The _categorie Attribute.

		@return: self.__categorie. ( String )
		"""

		return self.__categorie

	@categorie.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def categorie(self, value):
		"""
		This Method Is The Setter Method For The _categorie Attribute.

		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' Attribute: '{1}' Type Is Not 'str' or 'unicode'!".format("categorie", value)
		self.__categorie = value

	@categorie.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def categorie(self):
		"""
		This Method Is The Deleter Method For The _categorie Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("categorie"))

	@property
	def module(self):
		"""
		This Method Is The Property For The _module Attribute.

		@return: self.__module. ( String )
		"""

		return self.__module

	@module.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def module(self, value):
		"""
		This Method Is The Setter Method For The _module Attribute.

		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' Attribute: '{1}' Type Is Not 'str' or 'unicode'!".format("module", value)
		self.__module = value

	@module.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def module(self):
		"""
		This Method Is The Deleter Method For The _module Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("module"))

	@property
	def version(self):
		"""
		This Method Is The Property For The _version Attribute.

		@return: self.__version. ( String )
		"""

		return self.__version

	@version.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def version(self, value):
		"""
		This Method Is The Setter Method For The _version Attribute.

		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' Attribute: '{1}' Type Is Not 'str' or 'unicode'!".format("version", value)
		self.__version = value

	@version.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def version(self):
		"""
		This Method Is The Deleter Method For The _version Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("version"))

	@property
	def author(self):
		"""
		This Method Is The Property For The _author Attribute.

		@return: self.__author. ( String )
		"""

		return self.__author

	@author.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def author(self, value):
		"""
		This Method Is The Setter Method For The _author Attribute.

		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' Attribute: '{1}' Type Is Not 'str' or 'unicode'!".format("author", value)
		self.__author = value

	@author.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def author(self):
		"""
		This Method Is The Deleter Method For The _author Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("author"))

	@property
	def email(self):
		"""
		This Method Is The Property For The _email Attribute.

		@return: self.__email. ( String )
		"""

		return self.__email

	@email.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def email(self, value):
		"""
		This Method Is The Setter Method For The _email Attribute.

		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' Attribute: '{1}' Type Is Not 'str' or 'unicode'!".format("email", value)
		self.__email = value

	@email.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def email(self):
		"""
		This Method Is The Deleter Method For The _email Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("email"))

	@property
	def url(self):
		"""
		This Method Is The Property For The _url Attribute.

		@return: self.__url. ( String )
		"""

		return self.__url

	@url.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def url(self, value):
		"""
		This Method Is The Setter Method For The _url Attribute.

		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' Attribute: '{1}' Type Is Not 'str' or 'unicode'!".format("url", value)
		self.__url = value

	@url.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def url(self):
		"""
		This Method Is The Deleter Method For The _url Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("url"))

	@property
	def description(self):
		"""
		This Method Is The Property For The _description Attribute.

		@return: self.__description. ( String )
		"""

		return self.__description

	@description.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def description(self, value):
		"""
		This Method Is The Setter Method For The _description Attribute.

		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' Attribute: '{1}' Type Is Not 'str' or 'unicode'!".format("description", value)
		self.__description = value

	@description.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def description(self):
		"""
		This Method Is The Deleter Method For The _description Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("description"))

class Manager(object):
	"""
	This Class Is The Manager Class.
	"""

	@core.executionTrace
	def __init__(self, paths=None, extension="rc", categories={ "default" : Component, "ui" : UiComponent }):
		"""
		This Method Initializes The Class.
		@param paths: Paths To Walk. ( Dictionary )
		@param extension: Extension To Look After. ( String )
		"""

		LOGGER.debug("> Initializing '{0}()' Class.".format(self.__class__.__name__))

		# --- Setting class attributes. ---
		self.__paths = None
		self.paths = paths
		self.__extension = None
		self.extension = extension
		self.__categories = None
		self.categories = categories
		self.__components = None

	#***********************************************************************************************
	#***	Attributes properties.
	#***********************************************************************************************
	@property
	def paths(self):
		"""
		This Method Is The Property For The _paths Attribute.

		@return: self.__paths. ( Dictionary )
		"""

		return self.__paths

	@paths.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def paths(self, value):
		"""
		This Method Is The Setter Method For The _paths Attribute.

		@param value: Attribute Value. ( Dictionary )
		"""

		if value:
			assert type(value) is dict, "'{0}' Attribute: '{1}' Type Is Not 'dict'!".format("paths", value)
			for path in value.values(): assert os.path.exists(path), "'{0}' Attribute: '{1}' Directory Doesn't Exists!".format("paths", path)
		self.__paths = value

	@paths.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def paths(self):
		"""
		This Method Is The Deleter Method For The _paths Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("paths"))

	@property
	def extension(self):
		"""
		This Method Is The Property For The _extension Attribute.

		@return: self.__extension. ( String )
		"""

		return self.__extension

	@extension.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def extension(self, value):
		"""
		This Method Is The Setter Method For The _extension Attribute.

		@param value: Attribute Value. ( String )
		"""

		if value:
			assert type(value) in (str, unicode), "'{0}' Attribute: '{1}' Type Is Not 'str' or 'unicode'!".format("extension", value)
		self.__extension = value

	@extension.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def extension(self):
		"""
		This Method Is The Deleter Method For The _extension Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("extension"))

	@property
	def categories(self):
		"""
		This Method Is The Property For The _categories Attribute.

		@return: self.__categories. ( Dictionary )
		"""

		return self.__categories

	@categories.setter
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def categories(self, value):
		"""
		This Method Is The Setter Method For The _categories Attribute.

		@param value: Attribute Value. ( Dictionary )
		"""

		if value:
			assert type(value) is dict, "'{0}' Attribute: '{1}' Type Is Not 'dict'!".format("categories", value)
		self.__categories = value

	@categories.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def categories(self):
		"""
		This Method Is The Deleter Method For The _categories Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("categories"))

	@property
	def components(self):
		"""
		This Method Is The Property For The _components Attribute.

		@return: self.__components. ( Dictionary )
		"""

		return self.__components

	@components.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def components(self, value):
		"""
		This Method Is The Setter Method For The _components Attribute.

		@param value: Attribute Value. ( Object )
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Read Only!".format("components"))

	@components.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def components(self):
		"""
		This Method Is The Deleter Method For The _components Attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' Attribute Is Not Deletable!".format("components"))

	#***********************************************************************************************
	#***	Class methods.
	#***********************************************************************************************
	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.FileStructureError)
	def getProfile(self, file):
		"""
		This Method Gets Provided Component Profile.

		@param file: File Path. ( String )
		@return: Profile. ( Profile )
		"""

		LOGGER.debug("> Building '{0}' Profile.".format(file))

		parser = Parser(file)
		parser.read() and parser.parse()

		if parser.sections:
			profile = Profile()
			profile.path = os.path.dirname(file)
			profile.name = parser.attributeExists("Name", "Component") and parser.getValue("Name", "Component") or None
			if not profile.name:
				raise foundations.exceptions.FileStructureError("'{0}' No '{1}' Attribute Found, File Structure Seems Invalid!".format(file, "Name"))
			profile.path = os.path.dirname(file)
			profile.module = parser.attributeExists("Module", "Component") and parser.getValue("Module", "Component") or None
			if not profile.module:
				raise foundations.exceptions.FileStructureError("'{0}' No '{1}' Attribute Found, File Structure Seems Invalid!".format(file, "Module"))
			profile.object_ = parser.attributeExists("Object", "Component") and parser.getValue("Object", "Component") or None
			if not profile.object_:
				raise foundations.exceptions.FileStructureError("'{0}' No '{1}' Attribute Found, File Structure Seems Invalid!".format(file, "Object"))
			profile.rank = parser.attributeExists("Rank", "Component") and parser.getValue("Rank", "Component") or None
			if not profile.rank:
				raise foundations.exceptions.FileStructureError("'{0}' No '{1}' Attribute Found, File Structure Seems Invalid!".format(file, "Rank"))
			profile.version = parser.attributeExists("Version", "Component") and parser.getValue("Version", "Component") or None
			if not profile.version:
				raise foundations.exceptions.FileStructureError("'{0}' No '{1}' Attribute Found, File Structure Seems Invalid!".format(file, "Version"))
			profile.author = parser.attributeExists("Author", "Informations") and parser.getValue("Author", "Informations") or None
			profile.email = parser.attributeExists("Email", "Informations") and parser.getValue("Email", "Informations") or None
			profile.url = parser.attributeExists("Url", "Informations") and parser.getValue("Url", "Informations") or None
			profile.description = parser.attributeExists("Description", "Informations") and parser.getValue("Description", "Informations") or None

			return profile
		else:
			raise foundations.exceptions.FileStructureError("'{0}' No Sections Found, File Structure Seems Invalid!".format(file))

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def gatherComponents(self):
		"""
		This Method Gather The Components.
		"""

		if self.paths:
			self.__components = {}
			walker = Walker()
			for path in self.paths.keys():
				walker.root = self.paths[path]
				walker.walk(("\.{0}$".format(self.__extension),), ("\._",))
				for component in walker.files.keys():
					LOGGER.debug("> Current Component: '{0}'.".format(component))
					profile = self.getProfile(walker.files[component])
					if profile:
						if os.path.isfile(os.path.join(profile.path, profile.module) + ".py"):
							self.__components[profile.name] = profile
						else:
							LOGGER.warning("!> {0} | '{1}' Has No Associated Module And Has Been Rejected!".format(self.__class__.__name__, component))
							continue
					else:
						LOGGER.warning("!> {0} | '{1}' Is Not A Valid Component And Has Been Rejected!".format(self.__class__.__name__, component))
		else:
			raise foundations.exceptions.ProgrammingError("'{0}' Has No Components Paths Defined!".format(self))

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError, ImportError)
	def instantiateComponents(self, callback=None):
		"""
		This Method Instantiates The Components.

		@param callback: Callback Object. ( Object )
		"""

		assert self.__components, "'{0}' Manager Has No Components!".format(self)

		for component in self.getComponents():
			profile = self.__components[component]
			callback and callback(profile)

			LOGGER.debug("> Current Component: '{0}'.".format(component))

			sys.path.append(profile.path)
			profile.import_ = __import__(profile.module)
			object_ = profile.object_ in profile.import_.__dict__ and getattr(profile.import_, profile.object_) or None
			if object_ and inspect.isclass(object_):
				for categorie, type in self.__categories.items():
					profile.categorie = categorie
					profile.interface = issubclass(object_, type) and object_ is not type and object_(name=profile.name) or None
					if profile.interface:
						LOGGER.info("{0} | '{1}' Component Has Been Instantiated!".format(self.__class__.__name__, profile.name))
						break
			else:
				LOGGER.error("{0} | '{1}' Component Has No Interface And Has Been Rejected!".format(self.__class__.__name__, profile.name))
				del(self.__components[component])

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def deleteComponent(self, component):
		"""
		This Method Removes The Provided Component.

		@param component: Component To Remove. ( List )
		@return: Deletion Success. ( Boolean )
		"""

		del(self.__components[component])
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def clearComponents(self):
		"""
		This Method Clears The Components.

		@return: Clearing Success. ( Boolean )
		"""

		self.__components.clear()
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, ImportError)
	def reloadComponent(self, component):
		"""
		This Method Reload The Provided Component.

		@param callback: Callback Object. ( Object )
		@return: Reload Success. ( Boolean )
		"""

		profile = self.__components[component]
		import_ = __import__(profile.module)
		reload(import_)
		object_ = profile.object_ in dir(import_) and getattr(import_, profile.object_) or None
		if object_ and inspect.isclass(object_):
			interface = issubclass(object_, self.__categories[profile.categorie]) and object_ is not self.__categories[profile.categorie] and object_(name=profile.name) or None
			if interface:
				LOGGER.info("{0} | '{1}' Component Has Been Reloaded!".format(self.__class__.__name__, profile.name))
				profile.import_ = import_
				profile.interface = interface

				return True

	@core.executionTrace
	def getComponents(self):
		"""
		This Method Gets The Components By Ranking.
		"""

		return [component[0] for component in sorted(((component, profile.rank) for component, profile in self.__components.items()), key=lambda x:(int(x[1])))]

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, AssertionError)
	def filterComponents(self, pattern, categorie=None):
		"""
		This Method Filters The Components Using The Provided Pattern.

		@param pattern: Regex Filtering Pattern. ( String )
		@param categorie: Categorie Filter. ( String )
		@return: Matching Items. ( List )
		"""

		assert self.__components is not None, "'{0}' Manager Has No Components!".format(self)
		matchingItems = []
		for component, profile in self.__components.items():
			if categorie:
				if profile.categorie != categorie:
					continue
			if re.search(pattern, component):
				matchingItems.append(component)
		return matchingItems

	@core.executionTrace
	def getInterface(self, component):
		"""
		This Method Gets The Component Interface.

		@param component: Component To Get The Interface.
		@return: Component Interface. ( Object )
		"""

		components = self.filterComponents("^" + component + "$")
		if components != []:
			return self.__components[components[0]].interface

#***********************************************************************************************
#***	Python end.
#***********************************************************************************************
