import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정 (Windows, Mac, Linux)
plt.rcParams['font.family'] = "Malgun Gothic"  # Windows
# plt.rcParams['font.family'] = "AppleGothic"  # Mac
# plt.rcParams['font.family'] = "NanumGothic"  # Linux

# 데이터 불러오기
file_path = "Ecommerce_Consumer_Behavior_Analysis_Data.csv"  # 파일 경로를 맞춰줘!
df = pd.read_csv(file_path)

# 필요한 컬럼만 선택
selected_columns = ["Age", "Time_to_Decision"]
df_filtered = df[selected_columns].copy()

# NaN 값 제거
df_filtered = df_filtered.dropna()

# 연령대별 그룹화 (19세 이하, 20대, 30대, 40대, 50대)
bins = [0, 19, 29, 39, 49, 59]  # 60대 이상 제거
labels = ["19세 이하", "20대", "30대", "40대", "50대"]
df_filtered["Age_Group"] = pd.cut(df_filtered["Age"], bins=bins, labels=labels, right=True)

# 연령대별 Time_to_Decision 총합 계산 (각 연령대가 고민한 총 시간)
age_group_total = df_filtered.groupby("Age_Group")["Time_to_Decision"].sum().dropna()

# 전체 대비 연령대별 비율 계산
total_decision_time = age_group_total.sum()
age_group_ratio = age_group_total / total_decision_time  # 전체에서 차지하는 비율

# 1️⃣ 전체 비율을 나타내는 파이 차트
plt.figure(figsize=(8, 8))
explode = [0.05] * len(age_group_ratio)  # 모든 조각을 살짝 띄움

plt.pie(
    age_group_ratio, 
    labels=[f"{age}\n{ratio:.1%}" for age, ratio in age_group_ratio.items()], 
    autopct="%.1f%%", 
    startangle=90, 
    explode=explode, 
    wedgeprops={'width': 0.6},  # 도넛 형태로 만들기
    colors=sns.color_palette("pastel")
)

# 가운데 텍스트 추가
# plt.text(0, 0, "나이별 평균 구매 결정 시간", ha="center", va="center", fontsize=14, fontweight="bold")

# 타이틀 추가
plt.title("나이별 평균 구매 결정 시간 (전체 비율)", fontsize=16)

# 그래프 출력
plt.show()


# 각 나이 그룹에 대해 Time_to_Decision 평균값을 계산
age_group_distribution = df_filtered.groupby('Age_Group')['Time_to_Decision'].value_counts().unstack().fillna(0)

# 서브플롯 설정 (2행 3열로 설정, 나이대에 맞게 서브플롯 개수를 조정)
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()  # 2D 배열을 1D 리스트로 변환

# 각 나이대별로 분포를 그리기
for i, (age, distribution) in enumerate(age_group_distribution.iterrows()):
    max_time = distribution.idxmax()  # 제일 많이 고민한 시간이 무엇인지 찾기
    max_value = distribution.max()    # 제일 많이 고민한 시간에 해당하는 사람 수

    # 바 차트를 그리기 위해 각 시간에 대해 다른 색 지정
    bars = axes[i].bar(distribution.index, distribution.values, color="#ff9999")
    
    # 제일 많이 고민한 시간의 바는 다른 색으로 변경
    for bar in bars:
        if bar.get_x() + bar.get_width() / 2 == max_time:  # 가장 많이 고민한 시간이면
            bar.set_color("#ff5733")  # 다른 색으로 설정 (예: #ff5733)

    axes[i].set_title(f"{age} 나이대")
    axes[i].set_xlabel("생각한 시간 (일)")
    axes[i].set_ylabel("사람들의 수")
    axes[i].tick_params(axis='x', rotation=45)

# 불필요한 빈 서브플롯 제거
for j in range(len(age_group_distribution), len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()