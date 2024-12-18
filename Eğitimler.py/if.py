print("""1 den 1000 e kadar olan tek sayıları sıralamak için "1" çift sayıları sıralamak için "2"ye basınız""")
liste_çift=[]
liste_tek=[]
y=range(1,1001)
for i in y:
    if i%2==0:
        liste_çift.append(i)
    elif i%2!=0:
        liste_tek.append(i)
x=int(input())
if x==1:
    print(liste_tek)
elif x==2:
    print(liste_çift)