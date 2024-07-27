from matplotlib import pyplot as p
import numpy as n
x=n.random.normal(180,5,200)
p.hist(x,color='k')
p.xlabel('height in cm')
p.ylabel('prople')
p.title('height of ppl')
p.show()