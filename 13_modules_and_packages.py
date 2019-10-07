#
# MODULES and PACKAGES
#
#	Module:
#		- It's a file with '.py' or '.pyc' (compiled python) extension that haves
#		its own namespace with variables, functions, classes or even other modules
#
#		- Its purpose is to arrange and reuse the code
#		  Their imports should be written at the top of the file
#
#		- Import whole module: Syntax: 'import [module]'
#			By default, Python only searches in current directory, but you can search
#			in specified path under current directory specifying relative path
#				· import module_name
#				· import module_path (module_folder.module_name)
#			
#			Using this way, we have to use the 'module_path.module_name' notation
#			to use the module internals in our .py file. On the other hand, we can
#			add an alias and use 'alias.' notation to refer internal module parts
#				· import module_name as alias
#
#		- Import module parts. Syntax: 'from [module] import [parts]':
#			You can import one or several different parts
#				from package import module_part_1[, module_part_2, ...]
#			Even the whole module, using the '*' notation
#				form package import *
#			As before, you can also bind one or several aliases
#				from module_name import module_part_1 as alias_1[, module_part_2 as alias_2]
#
#	Package:
#		- It's a directory where related modules are (related '.py' or '.pyc' files)
#		  Its purpose is to arrange and reuse modules
#
#		- To build it, as simple as having a folder with an empty '__init__.py' file
#		  The 'init' file could contain arbitrary Python code
#
#		- You can create subpackages (directories into directories), each with its 'init'
#			Example:
#				package [/ __init__.py, module_1.py, subpackage [/__init__.py, module_2.py]]
#
#		- Import whole module. Syntax: 'from module_path import *'
#
#		- Import module parts. Syntax: 'from package import mod_1 as util[, mod_2 as pars, ...]'
#
#	Distributable package:
#		- It's a package you can distribute and send to third persons as they can
#		  install it on their machines and use it from anywhere. Two part-process:
#
#			1 First, you have to create the distributable package. You must start
#			  by creating a 'setup.py' file with package configuration in root path.
#			  Then, open a console and execute from root path 'python setup.py sdist'.
#
#			  This will create a 'distributable_package_name.egg-info' and 'dist' folders:
#			  the first one contains metadata (removable) and the second contains the
#			  distributable package as a '.tar.gz' file. The last one is the important.
#
#			2 Second, you have to install that '.tar.gz' file in your machine. Go to file
#			  location, open a console, and execute 'pip3 install package_name.tar.gz'.
#
#			  This will install the package and it will be available anywhere, regardless
#		  	  specific working directory path, and you'll be able to import it easily
#
#		- You can even uninstall Python packages you already have installed.
#		  As easy as open a console and execute from anywhere 'pip unistall package_name'
#
print("----------------------- Math functions ------------------------")

import modules.math_functions
modules.math_functions.subtract(5, 3)
print()

import modules.math_functions as math
math.sum(2, 3)
print()

from modules.math_functions import multiply
multiply(5, 3)
print()

from modules.math_functions import sum as my_sum, subtract as rest
my_sum(15, 8)
rest(2, 2)
print()

print("----------------------- General calculus ------------------------")

# these two last imports will work even if we remove 'package' folder, or any of
# its internal folders or files, because we have the dist-package installed
from package.general_calculus import divide, subtract
divide(10, 2)
subtract(5, 2)
print()

from package.subpackage.specific_calculus import round_num, sqrt_num
round_num(7.2)
sqrt_num(23)
print()