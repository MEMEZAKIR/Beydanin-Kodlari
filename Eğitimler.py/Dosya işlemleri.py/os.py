import os
#---Klasörün yerini gösterir

x = os.getcwd()
print(x) 

#*---Yeni Klasörler oluşturmanı sağlar

os.mkdir("Klasör/Alt_Klasör")

#---Bir Klasörün ismini değiştirir

os.rename("Klasör/Klasör_Yeni")

#---Klasörü silmeye yarar

os.rmdir( ) #klasörün ismi

#---Klasörün içersindeki dosyaları listeler
        #-Beydanın Kodları-#
y=("C:\\Users\\user\\Desktop\\Beydanın kodları")
z=os.listdir(y)
print(z)

#---uzantılı yapıları çalıştırmaya yarar

os.system("notepad.exe")

#---var olup olmadığına göre TRUE ya da FALSE değerlerini verir

os.path.exists("Beydanın kodları")

