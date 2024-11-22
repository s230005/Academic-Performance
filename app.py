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
with col1:
      st.subheader('데이터시각화1')
      st.image('시각화2.png' )
with col2:
      st.subheader('데이터시각화2')
      st.image('시각화3.png' )

# 4. 모델 활용
