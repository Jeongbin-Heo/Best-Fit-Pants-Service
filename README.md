# 완벽한 슬랙스 핏을 찾는 당신을 위하여
* **개요** : 키와 몸무게를 입력하면 최적의 바지 사이즈를 추천해주는 서비스 개발
* **진행 기간** : 2022. 04. 18 ~ 2022. 04. 22
* **사용 스킬** : `Requests` `BeautifulSoup` `DBeaver` `PostgreSQL` `Pandas` `Numpy` `Scikit-learn` `Metabase` `Flask` `Heroku`


### &nbsp;

## :file_folder: 파일 설명
* **tablecreate.py** : 사이즈 후기 데이터들이 들어갈 테이블 설계
* **datapull.py** : 추출한 데이터들을 테이블에 저장
* **modeling.py** : 사이즈 추천 모델로 사용할 선형 회귀 모델 학습
* **model.pkl** : 부호화하여 저장한 사이즈 추천 모델
* **flask_app** : 서비스 홈페이지 제작

### &nbsp;

## :computer: 사용 Skill
* **VSCode**
* **Python 3.8**
  * SQL 데이터베이스 연동 : psycopg2, requests, bs4
  * 모델 설계 : pandas, numpy, sklearn, pickle
* **ML Model**
  * Linear Regression
* **DBeaver, PostgreSQL**
* **Flask**
* **Heroku**
* **Metabase**

### &nbsp;

## :pushpin: Contents
* :one: **서비스 소개**
* :two: **서비스 설계 과정**
* :three: **서비스 시연**


### &nbsp;

## :one: 서비스 소개
### 서비스 설계 배경
* 슬랙스를 비롯한 하의는 체형을 잘 타는 편이며 온라인으로 구매하고 사이즈가 안맞는 경우가 많음
* 하지만 근처에 오프라인 매장이 없거나, 옷을 사러갈 시간이 부족한 사람들이 존재
* 위와 같이 부득이하게 온라인으로 구매를 해야하는 사람들을 위해 키와 몸무게를 입력하면 본인의 체형에 적절한 바지 사이즈를 추천하는 서비스를 개발

### &nbsp;

## :two: 서비스 설계 과정
### 파이프라인 구성
<img width="887" alt="스크린샷 2022-09-09 오후 6 17 08" src="https://user-images.githubusercontent.com/97662174/189316176-99056e1f-42e1-4260-9ef6-ae64480b7a68.png">


### 사이즈 후기 데이터 수집 및 데이터베이스 저장
<img width="401" alt="스크린샷 2022-09-09 오후 5 54 46" src="https://user-images.githubusercontent.com/97662174/189312844-5558cfb3-418f-49bb-93ba-18cfc6a2d943.png">

* 데이터 출처 : [무신사 스탠다드 - 테아퍼드 히든 밴딩 크롭 슬랙스](https://www.musinsa.com/app/goods/1149328)
* 데이터 설명 : 해당 제품을 구매한 유저들의 `키` `몸무게` `구매 색상` `구매 사이즈` `후기(큼, 적당함, 작음)` 데이터

<img width="531" alt="스크린샷 2022-09-09 오후 6 04 34" src="https://user-images.githubusercontent.com/97662174/189313822-bf127fd4-8800-467b-99b9-d4822c16ae21.png">

* 해당 데이터를 requests, beautifulsoup을 이용하여 추출
* 해당 데이터를 PostgreSQL 데이터베이스에 저장

### 사이즈 예측 모델 설계
* PostgreSQL 데이터베이스에서 `키` `몸무게` `구매 사이즈` 특성만 추출
* `키` `몸무게`를 바탕으로 `구매 사이즈`를 예측하는 선형 회귀 모델 학습
* 학습을 마친 모델을 재학습 없이 사용할 수 있도록 부호화(피클링)하여 저장

### 서비스 구현 홈페이지 설계
* 저장한 모델을 복호화(역피클링)하여 Flask, HTML을 통해 서비스를 이용할 수 있는 홈페이지 구성
* Heroku를 이용하여 배포

### 대시보드 제작
<img width="547" alt="스크린샷 2022-09-09 오후 6 23 03" src="https://user-images.githubusercontent.com/97662174/189317396-e909ae8d-a312-4461-b554-caf35f819968.png">

* PostgreSQL 데이터베이스에서 추출하여 Metabase를 이용하여 제작
* 키/체중별 평균 구매 사이즈, 유저들의 사이즈 후기(큼/적당함/작음) 비율 확인 가능


### &nbsp;

## :three: 서비스 시연
### 홈페이지 접속
<img width="953" alt="스크린샷 2022-09-09 오후 7 22 10" src="https://user-images.githubusercontent.com/97662174/189328842-d24d819e-35e0-4eeb-b8fa-000312503972.png">



* [완벽한 슬랙스 핏을 찾는 당신을 위하여](https://bestfitpants.herokuapp.com/)
* 홈페이지에 접속 후 `측정하러 가기` 버튼 클릭

### 사이즈 측정
<img width="941" alt="스크린샷 2022-09-09 오후 7 22 17" src="https://user-images.githubusercontent.com/97662174/189328861-2393acb4-027c-44aa-8b97-c96199e921b1.png">



* `키를 입력하세요` `몸무게를 입력하세요`에 본인의 키와 몸무게를 입력
* `바지 사이즈 찾기!` 버튼 클릭

### 측정 결과
<img width="912" alt="스크린샷 2022-09-09 오후 7 22 24" src="https://user-images.githubusercontent.com/97662174/189328931-21e414be-0347-4b85-9f2d-b4888004ce97.png">




* 입력한 키와 몸무게를 바탕으로 사이즈 예측 모델을 통해 최적의 사이즈를 추천
* 하단 `쇼핑하러 가기` 링크를 통해 최적 사이즈 슬랙스를 쇼핑 
