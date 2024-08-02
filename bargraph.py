from matplotlib import pyplot as p
pro_no=["intel","AMD","Snapdragon","Tensor"]
use=[200,100,250,50]
p.bar(pro_no,use,color='black',width=0.2)
p.xlabel("processors"),p.ylabel("no of users")
p.title("processor using in a community")
p.show()
