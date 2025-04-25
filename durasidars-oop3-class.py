
class dars:
    def __init__(self, name, about, difficulties):
        self.name = name
        self.about = about
        self.difficulties = difficulties

listdars = [dars("Tahsin","Membetulkan bacaan",2), 
               dars("Nahwu","Mendalami bahasa arab",4), 
               dars("Kajian Akidah","Majelis ilmu manhaj",3), 
               dars("Kajian Fiqih","Majelis ilmu fiqih",1)]

durasi = 60 * 14 #midurasi 14 jam

sum_difficulties = sum(lesson.difficulties for lesson in listdars)

for lesson in listdars:
    meandurasi = lesson.difficulties /  sum_difficulties * durasi
    print(f"Dars {lesson.name} mempelajari tentang {lesson.about} dilaksanakan selama {meandurasi} menit")