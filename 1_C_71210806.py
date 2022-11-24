print("Menu")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")

b1=int(input("Masukan Angka Pertama:"))
b2=int(input("Masukan Angka Kedua:"))
a=int(input("Pilihan Anda:"))

#rumus
tambah=b1+b2
kurang=b1-b2
kali=b1*b2
bagi=b1/b2

if a==1:
    print("Hasil:",tambah)
elif a==2:
    print("Hasil:",kurang)
elif a==3:
    print("Hasil:",kali)
else:
    print("Hasil",bagi)
