idlToPandas
===========

`idlToPandas` is a library to import a saved IDL structure and return it as a pandas DataFrame. 
Simply pass in the filename of the saved IDL structure, optionally specificy what variable 
in the IDL save file is the structure of interest using the `keyValue` optional argument, 
and the pandas DataFrame containing the IDL structure is returned with the IDL tags used
as column names in the pandas DataFrame.
