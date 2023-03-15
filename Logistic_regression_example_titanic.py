import pandas as pd
import numpy as np

#사이킷런의 로지스틱 회귀 라이브러리
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv')

'''
데이터에 null이 포함되어 있는지 확인
null이 있으면 data를 제거 혹은은 평균값으로 채워준다.
data.isna().sum()
'''

#타겟 테이터 따로 저장
target = data['Survived']

#이름, 생존여부 삭제 아마?
data.drop(labels=['Name', 'Survived'], axis=1, inplace = True)

#성별 데이터를 숫자로 변환
data['Sex'] = data['Sex'].map({'male':0,'female':1})

#훈련 데이터와 테스트 데이터 분리
train_input, test_input, train_target, test_target = train_test_split(data, target, random_state=42)

#로지스틱 회귀 인스턴스 생성
lr = LogisticRegression()
#훈련 데이터로 모델 훈련
lr.fit(train_input, train_target)

'''
#변수 종류 출력
print(data.head(0))
#각 특징(변수, feature)들의 가중치
print(lr.coef_) # 절댓값이 높을 수록 더 큰 영향을 준 것
'''

#나의 상황을 예측해봄
pred = lr.predict([[2,0,23.0,1,0,30.5789]])

if(pred[0]==0):
    print('사망하실 것으로 예측됩니다.\n')
else:
    print('생존하실 것으로 예측됩니다.\n')

#음성 클래스 / 양성 클래스의 확률
print('양성 클래스 / 음성 클래스 : {} '.format(lr.predict_proba([[2,0,23.0,1,0,30.5789]])))

#참고 https://itstory1592.tistory.com/10
