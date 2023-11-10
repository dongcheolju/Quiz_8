import pandas
import numpy

my_index = numpy.array([1,2,3])
data = ['a','b','c']
my_series = pandas.Series(data, index=my_index)
print(my_series)


import pandas as pd
# pandas Series
data = pd.Series([10,20,30,40,50,])
# Series
print(data)

#데이터 호출
data = pd.Series([10,20,30,40,50], index=['A','B','C','D','E'])
#데이터 호출
value_B = data['B']
value_E = data['E']

#호출된 데이터 출력
print("Value at index 'B':", value_B)
print("Value at index 'E':", value_E)


import pandas as pd

data = {
    '이름' : ['엘리스', '밥', '칼린', '데이비드']
    '나이' : [25,30,35,28]
    '성별' : ['여','남','남','여']
}
my_index = ['1','2','3','4']
df = pd.DataFrame(data, index=my_index)
print(df)

import numpy
my_index = ['1','2','3','4']
my_columns =['이름','나이','성별']
my_data = numpy.array([['엘리스', '밥', '칼린', '데이비드'],
                       [25,30,35,28], ['여','남','남','여']]).transpose()
df = pd.DataFrame(my_data, index=my_index, columns=my_columns)
print(df)


import pandas as pd

dir="/Users/judongcheol/Library/Mobile Documents/com~apple~CloudDocs/대학교/2학년 2학기/프로그래밍 2/코딩 파일/dongcheolju_Quiz_8/data/"
filename = "08_pima-indians-diabetes.data.csv"
filename = dir + filename

data_columns = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv(filename, names=data_columns)
print(data.head(5))

data.describe().to_csv("./data/pima_describe.csv")
