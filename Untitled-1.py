bands = [("Bayu", 5), ("Deri", 3), ("Joni", 3), ("Yoyok",3), ("Edi", 2)] 
honor = 45000000 
sum_ranking = sum(ranking for nama, ranking in bands) 
for nama, ranking in bands:
    share = ranking / sum_ranking * honor        
    print(f"{nama} dapat honor {share} Rupiah.")

