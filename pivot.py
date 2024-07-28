import pandas as p
t={
    'course':["py","jv","dbms","mma","mma"],
    'fee':[300,600,21,350,67],
    'complexity':[100,56,32,10,67]
}
d=p.DataFrame(t)
print(d)
print("\n",d.pivot(columns='course',values='complexity'))
print("\n",d.melt())
print("\n",d.melt())