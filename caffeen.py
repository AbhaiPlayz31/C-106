import numpy as np 
import csv
import plotly.express as px

def getDataSource(dataPath):
    coffeeAmount = []
    sleep = []

    with open(dataPath) as file:
        df = csv.DictReader(file)

        for nou in df:
            coffeeAmount.append(float(nou['Coffee in ml']))
            sleep.append(float(nou['sleep in hours']))

    return  {'x': coffeeAmount, 'y': sleep}

def find(dataSource):
    correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print('Correlation between Coffee Consumption and slep: ', correlation[0,1])
    
def setup():
    dataPath = 'coffee.csv'
    dataSource = getDataSource(dataPath)
    find(dataSource)

setup()


