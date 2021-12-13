#Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!

első = int(input("Írj be egy számot!"))
második = int(input("Írj be egy számot!"))

if első > második:
  print(első, 'nagyobb')
elif második > első:
  print(második, 'nagyobb')