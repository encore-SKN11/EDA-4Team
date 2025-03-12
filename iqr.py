import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm


df = pd.read_csv('Ecommerce_Consumer_Behavior_Analysis_Data.csv')
lst = ['Purchase_Amount','Age', 'Gender', 'Income_Level', 'Marital_Status', 'Education_Level', 'Occupation', 'Purchase_Channel', 'Time_to_Decision']
df = df.loc[:, lst]

print(df.info())
print(df.describe())

amount = df['Purchase_Amount']
amount = amount.str.replace('$', '')
amount = pd.to_numeric(amount)

# 정규분포표

mu = amount.sum() / len(amount)  # 평균
sigma = amount.std()  # 표준편차

# x 축의 값 범위 설정
x = np.linspace(0, 900, 100)

# 확률 밀도 함수 계산
y = norm.pdf(x, loc=mu, scale=sigma)
# y = amount

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', label='Normal Distribution')
plt.title('Normal Distribution')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()



#matplotlib 이용: box plot
# Q1 = amount.quantile(0.25)
# Q3 = amount.quantile(0.75)
# IQR = Q3 - Q1

# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR

# outliers = df[(amount < lower_bound) | (amount > upper_bound)]
# plt.figure(figsize=(10, 6))
# plt.boxplot(amount, vert=False)
# plt.title('Purchase Amount')
# plt.show()

#seabron 이용: box plot
box_plot = sns.boxplot(data=amount, palette='Set3')
for patch in box_plot.artists:
    r, g, b, a = patch.get_facecolor()
    patch.set_facecolor((r, g, b, .3))
    x = patch.get_x()
    y = patch.get_y