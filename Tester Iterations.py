problemSize = 100000
number = 0
print("%12s%15s" % ("Problem Size", "Iterations"))

while problemSize > 0:
    number += 1
    print("%12d%15d" % (problemSize, number))
    problemSize = problemSize // 2
    
