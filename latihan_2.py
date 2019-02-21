print("=========== Latihan 2 Looping @Zulfikar.H ==========\n")
print(" ------ Program Mencari Biangan terbesar dari bilangan yang di inputkan ------ \n\n")
indx=[]
Nilai=1

while Nilai != 0 :
    Nilai=int(input("Masukan Nilai = "))
    indx.append(Nilai)

print ("Nilai Terbesar dari semua bilangan di atas adalah = ", max(indx))

end=input("======== Press Enter to Exit ========")
