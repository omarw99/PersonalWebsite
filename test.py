def hello(listOfVars):
	list1 = []

	for i in listOfVars:
		list1.append(type(i).__name__)

	return ' '.join(list1)