import pandas as pd

#Lösung 1
print("Hallo Welt")
number = [1,2,3,4,5,6,9.87654321]

print(sum(number)/len(number))

#Lösung 2
daten = {'Werte': [1,2,3,4,5,6,9.87654321]}
df = pd.DataFrame(daten)

mittelwert = df['Werte'].mean()

print("Der Mittelwert ist:", mittelwert)

