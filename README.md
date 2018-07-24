# PyPretty-Table
A python script that takes in dictionaries and spits them out in visually organized table.

## Sample Output

## How to Install

Quite simple really. All of the code is in the `PrettyTable.py` file. If you wish you could just copy paste it directly.

Download the `PrettyTable.py` file or [click here for a direct link to the raw file on GitHub](https://raw.githubusercontent.com/advaitsaravade/PyPretty-Table/master/PrettyTable.py). Save it using the same name in your project folder.
Once saved, just pass it a dictionary, or list of dictionaries like so:

###### Import the file into your Python script
```
from PrettyTable import tablePrinter
```
###### Call the function
```
listOfDict = [ {"Name":"Advait", "StackLink": ""} , {"Name":"Alice"} ]
tablePrinter(listOfDict)
```
