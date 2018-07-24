# PyPretty-Table
A python script that takes in dictionaries and spits them out in visually organized table.

## Sample Output

## How to Install

Quite simple really. All of the code is in the `PrettyTable.py` file. If you wish you could just copy paste it directly.

###### Download the `PrettyTable.py` file

```
wget -O vfeed.db "https://raw.githubusercontent.com/advaitsaravade/PyPretty-Table/master/PrettyTable.py"
```
###### Import the file into your Python script
```
from PrettyTable import tablePrinter
```
###### Call the function
```
listOfDict = [ { "Name":"Advait", "Website": "link.org" } , { "Name":"Alice" } ]
tablePrinter(listOfDict)
```
