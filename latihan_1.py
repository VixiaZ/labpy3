print("=========== Latihan 2 Looping @Zulfikar.H ==========\n")
print(" ------ Program untuk menghasilkan nilai random dibawah 0.5 ------ \n\n")
from random import random

Jbil=int(input("Masukan Banyak data yang ingin di buat : "))


for i in range (Jbil):
	data=random()
	while data > 0.5:
		data=random()
	print("\ndata ke: ",i+1," => ",data)

end=input("\n======= Press Enter To Exit =======")
