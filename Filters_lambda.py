pos=lambda n:n>0
neg=lambda n:n<0
lst=[-35,-87,65,98,34,-62]
pres=filter(pos,lst)
nres=filter(neg,lst)
poslst=set(pres)
neglst=list(nres)
print("Given values")
print("positive values ",poslst)
print("negitive values",neglst)