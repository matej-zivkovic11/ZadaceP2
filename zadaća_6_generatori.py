def generiraj_parne_i_neparne(broj):
    print("Parni i neparni brojevi do", broj, ":")
    for i in range(broj+1):
        if i % 2 == 0:
            print(i, "- parni")
            yield i
        else:
            print(i, "- neparni")
            yield i

# Parametar za generator
n = 20

gen = generiraj_parne_i_neparne(n)
for broj in gen:
    pass 