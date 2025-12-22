import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('Winter_Food_and_Beverages-Cleaned.csv')

# CLEAN DATA
#Tổng dữ liệu bị null
print(df.isnull().sum()) # Cột Calories là 75, Cột Rating là 73

#Điền dữ liệu ở cột Calories và Rating bằng trung bình
df['Calories'].fillna(df['Calories'].mean().__round__(0),inplace=True)

df['Rating'].fillna(df['Rating'].mean().__round__(1),inplace=True)

df.to_csv('Winter_Food_and_Beverages-Cleaned.csv',index=False)
# Hiển thị 10 dòng đầu tiên
print(df.head(10))

# Hiển thị thông tin file csv
print(df.info())

print(df.describe())

#Tính toán giá trị trung bình, lớn nhất, nhỏ nhất của cột Calories và Price(USD) bằng mảng.
mang=np.array([df['Calories'].max(),df['Calories'].min(),df['Calories'].mean(),
               df['Price(USD)'].max(),df['Price(USD)'].min(),df['Price(USD)'].mean()])
print(mang)

#Lọc danh sách các món ăn thuộc loại Drink có giá Price(USD) lớn hơn 10.
a2=df[(df['Price(USD)']>10)&(df['Type']=='Drink')]
print(a2)

#Nhóm dữ liệu theo Origin (Quốc gia) để tính trung bình cộng Rating và Popularity_Score.
a3=df.groupby('Origin')[['Rating','Popularity_Score']].mean()
print(a3)

# Vẽ biểu đồ cột (Bar chart) thể hiện số lượng món ăn theo từng Type và biểu đồ tròn (Pie chart) cho cột Season.
a4=df['Type'].value_counts()
plt.bar(a4.index,a4.values,color='skyblue', edgecolor='navy', width=0.6)
plt.title('Bieu do the hien so luong mon an theo tung kieu')
plt.xlabel('Type')
plt.ylabel('So luong')
plt.savefig('Biêu đồ thể hiện số lượng món ăn theo kiểu ăn')

a5=df['Season'].value_counts()
plt.pie(a5.values,labels=a5.index, autopct='%1.1f%%', startangle=140)
plt.savefig('Biểu đồ thể hiện cơ cấu giữa món ăn và mùa')
