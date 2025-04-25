dars = [("Tahsin","Membetulkan bacaan",2),
        ("Nahwu","Mendalami bahasa arab",4),
        ("Kajian Akidah","Majelis ilmu manhaj",3),
        ("Kajian Fiqih","Majelis ilmu fiqih",1)]

durasi = 60 * 14 #midurasi 14 jam

sum_difficulties = sum(difficulties for lesson, about, difficulties in dars)

for lesson, about, difficulties in dars:
    meandurasi = difficulties /  sum_difficulties * durasi
    print(f"Dars {lesson} mempelajari tentang {about} dilaksanakan selama {meandurasi} menit")