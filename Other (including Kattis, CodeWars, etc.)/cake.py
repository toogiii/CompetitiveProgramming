width = input()
num_slices = input()
i = 0
slice_measures = []
for i in range(len(num_slices)):
    w_l_slices = input()
    dum_list = w_l_slices.split(" ")
    slice_measures.append(dum_list[0])
    slice_measures.append(dum_list[1])
    i += 1
