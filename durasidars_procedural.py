dars = ["Tahsin", "Nahwu", "Kajian Akidah", "Kajian Fiqih"]

durasi = 14
difficulties = 0


for lesson in dars:
  if lesson == "Nahwu":
      difficulties = difficulties + 4
  elif lesson == "Kajian Akidah":
      difficulties = difficulties + 3
  elif lesson == "Tahsin":
      difficulties = difficulties + 2
  elif lesson == "Kajian Fiqih":
      difficulties = difficulties + 1
      
for lesson in dars:
  meandurasi = 0
  
  if lesson == "Nahwu":
      meandurasi = 4 / difficulties * durasi 
  elif lesson == "Kajian Akidah":
      meandurasi = 3 / difficulties * durasi
  elif lesson == "Tahsin":
      meandurasi = 2 / difficulties * durasi 
  elif lesson == "Kajian Fiqih":
      meandurasi = 1 / difficulties * durasi
  
  
  print(f"{lesson} dilaksanakan selama {meandurasi} Jam")
  
