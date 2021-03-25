#Penginputan usia dan kelulusan hasil ujian kualifikasi
usia = int(input("Berapakah usia anda ? = "))
ujian = input("Apakah anda lulus ujian kualifikasi (Y/T) ? = ")

#Syarat diperbolehkan mendaftar kursus
syarat_usia = (usia >= 21)
syarat_ujian = (ujian == "Y", ujian == "y")

#Menampilkan output
if syarat_usia and syarat_ujian :
    print("Anda dapat mendaftar kursus")
else: print("Anda tidak dapat mendaftar kursus")