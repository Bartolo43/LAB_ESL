#This file contains few tests made throughout reading introduction
#Other files are tests taken from introduction itself

from myhdl import block, Signal, delay,always, now, instances

from ClkDriver import ClkDriver
from Hello import Hello

@block
def Greetings():

    clk1 = Signal(0)
    clk2 = Signal(0)

    clkdriver_1 = ClkDriver(clk1)
    clkdriver_2 = ClkDriver(clk=clk2, period=19)
    hello_1 = Hello(clk=clk1)
    hello_2 = Hello(to="MyHDL", clk=clk2)

    return clkdriver_1, clkdriver_2, hello_1, hello_2

inst = Greetings()
inst.run_sim(50)


@block
def top():

    clk1 = Signal(0)
    clk2 = Signal(0)

    instance_1 = ClkDriver(clk1)
    instance_2 = ClkDriver(clk=clk2, period=19)
    instance_3 = Hello(clk=clk1)
    instance_4 = Hello(to="MyHDL", clk=clk2)

    return instances()

#inst2 = top()
#inst2.run_sim(50)

