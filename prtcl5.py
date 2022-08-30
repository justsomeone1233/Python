import operator
A={1:20,3:40,2:50,4:70}
print(A)
a=sorted(A.items(),key=operator.itemgetter(0))
print('In ascending order=',a)
a=sorted(A.items(),key=operator.itemgetter(0),reverse=True)
print('In descending order=',a)
