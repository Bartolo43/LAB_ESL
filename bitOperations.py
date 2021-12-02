from myhdl import intbv,bin,modbv,Signal

test = intbv(25, min = 0, max = 31)
print(test.min)
print(test.max)
print(len(test))

print(test[0])
print(test[1])
print(test[2])
print(test[3])
print(test[4])

print(bin(test[4:1]))
print(bin(test[5:2]))

count = Signal(modbv(0, min=0, max=2**8))
print(count)
count.next = count + 1
print(count.next)