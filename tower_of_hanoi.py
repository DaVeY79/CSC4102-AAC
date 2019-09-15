def toh(n,from_tower,aux_tower,to_tower):
    if n>0:
        toh(n-1,from_tower,to_tower,aux_tower)
        print("Moving disc from {} --> {}".format(from_tower,to_tower))
        toh(n-1,aux_tower,from_tower,to_tower)

toh(3,"A","B","C")
