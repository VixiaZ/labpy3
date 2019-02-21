print("=========== Tugas Praktikum 3 Looping @Zulfikar.H ==========")
print(" Program Menghitung Laba dalam 8 bulan terakhir \n\n")

print("Modal awal = 100.000.000\n\n")
modal=100000000

for l in range(1,9):
	if (l >= 1 and l <= 2):
		l1=modal*0
		print("Laba bulan ke -",l,"sebesar =",l1,"= 0%")
	if (l > 2 and l <= 4):
		l2=modal*0.1
		print("Laba bulan ke -",l,"sebesar =",l2,"= 1%")
	if (l > 4 and l <= 7):
		l3=modal*0.5
		print("Laba bulan ke -",l,"sebesar =",l3,"= 5%")
	if (l > 7):
		l4=modal*0.2
		print("Laba bulan ke -",l,"sebesar =",l4,"= 2%")

total=[l1,l2,l2,l3,l3,l3,l4]
hasil = sum(total)

print("\nTotal Laba dalam 8 Bulan Terkahir =",hasil)
end=input("-------- Press Enter to Exit ------")


