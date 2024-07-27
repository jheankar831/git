from matplotlib import pyplot as p
x=[2,6,8,7,3,2,5]
y=[6,7,9,7,5,3,2]
c=['k','d']
p.scatter(x,y,label='value of x,y',color='k')
p.xlabel('x')
p.ylabel('y')
p.legend()
p.show()