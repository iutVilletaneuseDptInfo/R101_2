import arrayNumbers.filter as f
import arrayNumbers.calculus as c
import arrayNumbers.inOut as io

t = [1, 2, 3, 4, 5, 6]
print("Somme =", c.array_sum(t))
print("Moyenne =", c.array_average(t))
print("Variance =", c.array_variance(t))

t2 = f.eltsLessThan(t, 5)
print(t2)

t2 = f.eltsBetween(t, 2, 3)
print(t2)

io.writeToFile(t2, "test.txt")
