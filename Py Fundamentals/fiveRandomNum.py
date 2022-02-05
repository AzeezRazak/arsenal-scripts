from random import randint
import datetime
import csv
import pandas as pd

def generateInteger():
    value = randint(0,500)
    return(value)

now = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
"""
df=pd.DataFrame(
    columns=['time','intVar1','intVar2','intVar3', 'intVar4']
)
"""
df = pd.DataFrame({
    "time": now,
    "intVar1": [generateInteger()],
    "intVar2": [generateInteger()],
    "intVar3": [generateInteger()],
    "intVar4": [generateInteger()],
    })
df.to_csv('Names.csv')

while(1):
    df1 = pd.DataFrame({
    "time": now,
    "intVar1": [generateInteger()],
    "intVar2": [generateInteger()],
    "intVar3": [generateInteger()],
    "intVar4": [generateInteger()],
    })
    df1.to_csv('Names.csv', mode='a', header=False)


"""
randomNumberDict = {
    "time": now,
    "intVar1": generateInteger(),
    "intVar2": generateInteger(),
    "intVar3": generateInteger(),
    "intVar4": generateInteger(),
}

randomNumberDict={}
df = pd.DataFrame(randomNumberDict, columns= ['time', 'intVar1', 'intVar2', 'intVar3', 'intVar4'])
while(1):
    randomNumberDict = {
    "time": now,
    "intVar1": generateInteger(),
    "intVar2": generateInteger(),
    "intVar3": generateInteger(),
    "intVar4": generateInteger(),
    }
    df.to_csv('Names.csv', index=False)
#df = pd.DataFrame(randomNumberDict, columns= ['time', 'intVar1', 'intVar2', 'intVar3', 'intVar4'])
"""