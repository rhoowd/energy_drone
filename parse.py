
f = open("../energy/data1.log")
try:
    for line in f:
        # a = json.loads(line.split()[3])
        print line.split()[3]
        # for n in line.split():
        #     print n

finally:
   f.close()