def read(filename):
    '''
    Reads the CSV file and returns a 2D list of the data
    :param filename: Name of file or absolute path to file
    :type filename: String
    :return: CSV Data
    :rtype: 2D Nested List
    '''
    file = open(filename).read().split('\n')
    data = []
    for line in file:
        data.append(line.split(','))
    return data

def write(filename, data):
    '''
    Takes filename/path, and 2D list of data to be written and writes it as a CSV file

    :param filename: Name of file or absolute path to file
    :param data: 2D Nested List of CSV Data
    '''
    text = ""
    for line in data:
        l = ""
        for item in line:
            l += item+','
        l = l.strip(',')
        text += l + '\n'
    text = text.strip('\n')

    file = open(filename,'w')
    file.write(text)
    file.close()


def sort(file = None, column = 0):
    '''
    Sorts the CSV file based on the values of the given column
    :param file: Either file/filepath or CSV Data from 2D Nested List
    :param column: Column that value should be sorted by -- VALUE MUST BE UNIQUE
    :return: Sorted 2D Nested List
    '''
    data = []
    if type(file) == type("String"):
        data = read(file)
    else:
        data = file[:]
    keys = []
    keyedData = {}

    for element in data:
        key = element[column]
        keys.append(key)
        keyedData[key] = element

    keys.sort()

    sortedData = []

    for key in keys:
        sortedData.append(keyedData[key])

    return sortedData