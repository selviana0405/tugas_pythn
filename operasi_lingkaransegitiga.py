from modul import lingkaran, segitiga

cek = input("pilih lingkaran/segitiga (1/2)")

if cek == "1":
    jari = int(input("masukan jari-jari : "))
    lingkaran(jari)
elif cek== "2":
    a = int(input("masukan alas : "))
    t = int(input("masukan tinggi : "))
    segitiga(a,t)