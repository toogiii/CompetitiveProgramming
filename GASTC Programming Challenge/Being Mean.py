from statistics import mean
from statistics import geometric_mean
dataset = sorted([int(i) for i in input("Enter the whole numbers for this data set (separate each number with a space): ").split(" ")])
am = mean(dataset)
gm = geometric_mean(dataset)
amCands = [abs(i - am) for i in dataset]
gmCands = [abs(i - gm) for i in dataset]
closestAm = dataset[amCands.index(min(amCands))]
closestGm = dataset[gmCands.index(min(gmCands))]

print("AM: {:0.2f} ({})".format(am, closestAm))
print("GM: {:0.2f} ({})".format(gm, closestGm))