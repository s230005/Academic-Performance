# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model.pkl')
# 2. 모델 설명
st.title('학업성취도 예측 지능 에이전트')
st.subheader('모델 설명')
st.write(' - 기계학습 알고리즘 : 선형 회귀 ')
st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
st.write(' - 훈련    데이터 : 364건')
st.write(' - 테스트 데이터 : 156건')
st.write(' - 인공지능 모델 정확도 : 0.12')

# 3. 데이터시각화
col1, col2 = st.columns(2)
with col1:
      st.subheader('데이터시각화1')
      st.image('시각화2.png' )
with col2:
      st.subheader('데이터시각화2')
      st.image('시각화3.png' )

# 4. 모델 활용
st.subheader('모델 활용')
st.write('**** 다음을 입력하세요 **** 인공지능이 당신의 학업성취도를 1~5사이의 값으로 예측해드립니다!')
a = st.number_input(' 지난 일주일간 평균 수면의 질을 1~5 사이의 값으로 평가한다면 몇입니까? ', value=0)      #초기값은 0
b = st.number_input(' 지난 일주일간 평균 두통 횟수를 입력하세요. ', value=0)     # 초기값은 0.0
c = st.number_input(' 당신의 공부량을 1~5 사이의 값으로 평가한다면 몇입니까? ', value=0)
d = st.number_input(' 일주일에 몇번정도 학교외에 추가적인 활동을 하시나요? ex.운동, 학원 ', value=0)
e = st.number_input(' 당신의 스트레스 지수를 1~5사이의 값으로 평가한다면 몇입니까? ', value=0)
if st.button('학업성취도 예측'):            # 사용자가 '점수예측' 버튼을 누르면
        input_data = [[a,b,c,d,e]]     # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model.predict(input_data)         # model이 예측한 값을 p에 저장한다
        st.write('인공지능의 예측 학업성취도는', p)
st.write('당신의 정보는 오로지 점수 예측에만 사용되며, 암호화되어 서버에 저장됩니다.')
