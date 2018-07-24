import pprint

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def tablePrinter(listofDicts, colList=None):
    try:
        if str(type(listofDicts)) == "<type 'dict'>":
            listofDicts = [listofDicts]
        columnNames = []
        for iDictionary in listofDicts:
            for columnName in iDictionary:
                if not columnName in columnNames:
                    columnNames.append(columnName)
        lengthofColumns = len(columnNames)
        header = ""
        columnWidth = 3 + len(max(columnNames, key=len)) + 3
        for columnName in columnNames:
            header = header + color.PURPLE + "| " + color.END + color.BOLD + ( ("{:<" + str(columnWidth) + "}").format(columnName) ) + color.END
        header = header + color.PURPLE + "| " + color.END
        print header
        for iDictionary in listofDicts:
            lengthOfDict = len(iDictionary)
            currentIndex = 0
            row = ""
            for columnName in columnNames:
                try:
                    columnValue = iDictionary[columnName]
                    try:
                        columnValue = str(repr(columnValue))
                    except:
                        columnValue = str(type(columnValue))
                    if len(columnValue) > columnWidth:
                        columnValue = columnValue[0:(columnWidth-3)]+"..."
                    row = row  + color.PURPLE + "| " + color.END + ( ("{:<" + str(columnWidth) + "}").format(columnValue) )
                except:
                    # Not found
                    row = row  + color.PURPLE + "| " + color.END + ( ("{:<" + str(columnWidth) + "}").format(" ") )
            row = row + color.PURPLE + "| " + color.END
            print row
    except:
        pp = pprint.PrettyPrinter(indent=1)
        pp.pprint(listofDicts)
