import psycopg2
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# db에서 데이터 추출
hostname = 'localhost'
database = 'jeongbinheo'
username = 'jeongbinheo'
pwd = 'wilshere10'
port_id = 5432

conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = pwd,
    port = port_id)

cur = conn.cursor()

cur.execute("SELECT * FROM pants p ;")

data = cur.fetchall()

columns = ['id', 'height', 'weight', 'color', 'fit', 'size']
df = pd.DataFrame(data, columns = columns)

# 선형 회귀를 통해 키와 몸무게에 따른 바지 사이즈를 예측
model = LinearRegression()

X_train = df[['height', 'weight']]
y_train = df[['size']]

model.fit(X_train, y_train)

# 테스트 데이터로 키 180, 몸무게 70을 삽입 -> 소수점 아래는 반올림해서 처리
X_test = [[180, 70]]
y_pred = model.predict(X_test)
answer = round(y_pred[0][0])

print(f'키 = {X_test[0][0]}, 몸무게 = {X_test[0][1]} 일 떄 최적의 바지 사이즈 = {answer}')

# 모델을 피클링
with open('model.pkl', 'wb') as pickle_file :
    pickle.dump(model, pickle_file)