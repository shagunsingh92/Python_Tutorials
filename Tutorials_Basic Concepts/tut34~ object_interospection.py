'''
1. Object introspection is the way to know more about an object
2. if we want to know the object's class then we can call type function on that object
3. id function if run on the object will return the id of that object.
4. if we run dir function on an object then all the methods of that particular object are returned in a list format
5. inspect module - need to import the module in order to run inspect.getmembers() function on the object of interest.
inspect.getmembers() will return all the attributes of that particular object.
6. __dict__ after the object name will return all the variables of it's class in a dictionary format.
'''