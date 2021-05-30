#판다스 자료구조1
import pandas as pd
#print(pd.__version__) 버전확인

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
# print(sr2) 

dict_data = {'c0':sr1, 'c1':sr2}
df1 = pd.DataFrame(dict_data)
# print(df1)
# print(type(df1))
# print(df1.columns) 열 이름
df1.columns = ['string','number']
# print(df1)
df1.index = ['r0','r1','r2','r3','r4']
print(df1 )
