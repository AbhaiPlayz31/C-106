import numpy as np 
import csv
import plotly.express as px

def getDataSource(dataPath):
    studentMark = []
    studentPresent = []

    with open(dataPath) as file:
        df = csv.DictReader(file)

        for yes in df:
            studentMark.append(float(yes['Marks In Percentage']))
            studentPresent.append(float(yes['Days Present']))

    return  {'x': studentMark, 'y': studentPresent}

def find(dataSource):
    correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print('Correlation between Student Marks and Student Present: ', correlation[0,1])
    
def setup():
    dataPath = 'stinky.csv'
    dataSource = getDataSource(dataPath)
    find(dataSource)

setup()


