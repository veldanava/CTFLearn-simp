flag = 0

# include data.dat
with open("data.dat") as f:
    for line in f.readlines():
        if line.count('0') % 3 == 0 or line.count('1') % 2 == 0:
            flag += 1
print(flag)
