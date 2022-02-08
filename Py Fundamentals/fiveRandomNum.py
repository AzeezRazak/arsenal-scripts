from random import randint
import datetime, time
import csv
import pandas as pd

def generateInteger():
    value = randint(0,500)
    return(value)

def generateNow():
    now = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    return(now)

df = pd.DataFrame({
    "time": generateNow(),
    "intVar1": [generateInteger()],
    "intVar2": [generateInteger()],
    "intVar3": [generateInteger()],
    "intVar4": [generateInteger()],
    })
df.to_csv('Names.csv', index=False)

while(1):
    df1 = pd.DataFrame({
    "time": generateNow(),
    "intVar1": [generateInteger()],
    "intVar2": [generateInteger()],
    "intVar3": [generateInteger()],
    "intVar4": [generateInteger()],
    })
    df1.to_csv('Names.csv', mode='a', header=False, index=False)
    time.sleep(15)

