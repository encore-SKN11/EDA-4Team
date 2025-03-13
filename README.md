# 🛒 전자상거래 가격대별 소비 분석


## **팀원** 

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/521e5f07-e343-44e9-95f1-62bdaab40583" width="100" height="100"><br>
      <b>김성지</b>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/8fc956a5-6e4f-4688-b241-94b71877fa73" width="100" height="100"><br>
      <b>이선호</b>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/1bc89a2d-508c-407c-ade6-fda48ee558fc" width="100" height="100"><br>
      <b>방성일</b>
    </td>
  </tr>
</table>



## 📌 프로젝트 개요  
전자상거래에서 소비자들이 **어떤 가격대의 상품을 주로 구매하는지** 분석하여,  
기업이 효과적인 **가격 전략**과 **마케팅 방향**을 수립할 수 있도록 돕는 것이 목표입니다.  

---

## 🎯프로젝트 목표  
✔ 특정 쇼핑몰에 효과적인 광고와 마켓팅의 예상

✔ 소비자층의 특징에 따른 소비 금액의 차이 분석

✔ 특정 소비자층의 소비 경향의 분석 

---

## 🔧 기술 스택

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">

<img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">

<img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=NumPy&logoColor=white">

---
# 1.데이터 로드
![image](https://github.com/user-attachments/assets/9a42c12c-7507-40cf-94b7-b4aeb7e2d344)

# 2.데이터 구조 및 통계
## 데이터 구조 확인 (info)
![image](https://github.com/user-attachments/assets/35817d1b-34b2-423b-9bf3-7dd1c0a97315)
## 📊 데이터 컬럼 설명

| 컬럼 이름              | 데이터 타입     | 설명                          |
|-----------------------|----------------|-----------------------------|
| Purchase_Amount       | object       | 소비자의 구매 금액           |
| Age                   | int64        | 소비자의 나이                |
| Gender                | object    | 소비자의 성별 (예: 남성, 여성)|
| Income_Level          | object    | 소비자의 소득 수준           |
| Marital_Status        | object    | 소비자의 결혼 상태 (예: 기혼, 미혼)|
| Education_Level       | object    | 소비자의 교육 수준 (예: 고졸, 대학졸)|
| Occupation            | object    | 소비자의 직업                |
| Purchase_Channel      | object    | 구매 채널 (예: 온라인, 오프라인)|
| Time_to_Decision      | int64        | 소비자가 구매 결정을 내리기까지의 시간 (분)|



## 데이터 구조 확인(describe)
<img src="https://github.com/user-attachments/assets/5ac17aef-98df-4029-a39e-04d78a594716" />

# 3. 데이터 전처리
![image](https://github.com/user-attachments/assets/ce36dcc0-60d3-4293-a304-f8181060092e)

![image](https://github.com/user-attachments/assets/28a45ff5-ef23-4aae-87e5-b060a191af11)

# 4.결측치, 이상치 탐색
<img width="1467" alt="스크린샷 2025-03-13 오후 8 00 11" src="https://github.com/user-attachments/assets/174ecb9f-22bc-43c6-8546-62d20dd4e535" />
<img width="732" alt="스크린샷 2025-03-13 오후 8 00 49" src="https://github.com/user-attachments/assets/79a7e87a-f1a5-419a-9e25-cb5052af8d22" />
<img width="985" alt="스크린샷 2025-03-13 오후 8 01 59" src="https://github.com/user-attachments/assets/c12bf498-7993-4b91-98dc-18e0d2b84fc7" />
<img width="982" alt="스크린샷 2025-03-13 오후 8 03 45" src="https://github.com/user-attachments/assets/3841d99c-598a-432a-92e1-96862b91deb2" />
<img width="786" alt="스크린샷 2025-03-13 오후 8 04 51" src="https://github.com/user-attachments/assets/70d71ae4-2fe6-4813-9ce9-bd85a3ce740e" />
<img width="977" alt="스크린샷 2025-03-13 오후 8 08 30" src="https://github.com/user-attachments/assets/0ebefe14-6e33-4cb6-a3cf-42a0b88fe59b" />


---




