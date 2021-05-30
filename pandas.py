#판다스 자료구조1
import pandas as pd
#print(pd.__version__) 버전 확인

data1 = ['a','b','c','d','e']
# print(data1)
# print("자료형: ",type(data1))


sr1 = pd.Series(data1)
# print("자료형: ",type(sr1))
# print(sr1)
# print(sr1.loc[0]) loc : 시리즈 객체의 원소를 추출함
# print(sr1.loc[1:3])

data2 = (1,2,3.14,100,-10)
sr2 = pd.Series(data2)
print(sr2) 