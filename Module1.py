# def moduleFunction():
# def moduleFunction():
# 	print "I AM from Module!"


# mystuff = {'Subject': "Java!"}

# a= " Ptyhon learning"

# # moduleFunction()


# def add(x,y):
#    return x + y

# # moduleFunction()

# mystuffList = ['Subject',"Java!","python"]

# def moduleExample():
# 	print "I AM from module!"


# print mystuff['Subject']

# # # #get X from Y

# stringModule = "This is inside Module.py"
# # print stringModule
# def sqr(n):
# 	print "I am from Module.py"
# 	return n+1
	
# def addtwo(n):
# 	return n+2
# When you run Python interactively the local __name__ variable is assigned a value of __main__. 
# Likewise, when you execute a Python module from the command line, rather than importing it into another module,
# its __name__ attribute is assigned a value of __main__, rather than the actual name of the module.
#  In this way, modules can look at their own __name__ value to determine for themselves how they are being used, 
# whether as support for another program or as the main application executed from the command line. 
# 
# if __name__ == "main": is used to execute some code only if the file was run directly, and not imported.
if (__name__ == '__main__'):
	print("Module.py is being run directly")
	def apple():
		print ("I AM APPLES!")
	mystuff = {'Subject': "Java!"}
	print (mystuff['Subject'])
	stringModule = "This is inside Module.py"
	print (stringModule)
	print ("success")

else:
	print("Module.py is being imported into another module")
	def sqr(n):
		print ("success")
		return n+1
	mystuff = {'Subject': "Scala!"}
	print (mystuff)

# mystuffoutside = {'Subject': "Scala1!"}
# print (mystuffoutside)

# TBD - how to make it available in both ways

# import vs from
# Waht's the difference between import and from in Python?

# Python's import loads a Python module into its own namespace, 
# so that you have to add the module name followed by a dot in front of references to any names from the imported module that you refer to:

# import us                                 # Access the whole module, us
# us_city = us.california("Sacramento")     # Qualify to reference
# from loads a Python module into the current namespace, 
# so that you can refer to it without the need to mention the module name again:

# from us import *                          # Copy name into my scope
# us_city = california("Sacramento")        # Use class name directly
# or
# from us import city
# us_city = california("Sacramento")
# Here is the summary:

# Can't I always use from?
# # If we are loading a lot of modules using from, we may have conflicts of names. 
# Though from is fine for a small program but for a big project, we would hit problems.
# Then, should we always use import?
# No, we should use import most of the time,
#  but we may want to use from if we want to refer to the members of a module lots of times in the calling code.
#   In that case, by using from, we can save ourselves.
