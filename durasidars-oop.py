dars = [("Tahsin",2),  ("Nahwu",4), ("Kajian Akidah",3), ("Kajian Fiqih",1)]

durasi = 60 * 14 #midurasi 14 jam

sum_difficulties = sum(difficulties for lesson, difficulties in dars)

for lesson, difficulties in dars:
    meandurasi = difficulties /  sum_difficulties * durasi
    print(f"{lesson} dilaksanakan selama {meandurasi} menit")