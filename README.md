# 처음 배우는 데이터과학

역자 최근우

## 기본 안내

이 코드를 실행하려면 아래 도구를 사용할 줄 알아야합니다. 
 - 아이파이썬 노트북
 - 터미널 (명령행)
 - 깃
 - pip, pip3 (파이썬 패키지 설치)

## 설치

### 소스 다운로드
터미널에서 다운로드를 원하는 위치로 간 뒤 아래 명령어를 실행합니다.
```
$ git clone https://github.com/keunwoochoi/data-science-handbook.git
```
### 실행
설치가 끝나면 해당 폴더로 이동하고 아이파이썬 노트북을 실행합니다.
```
$ cd data-science-handbook
$ ipython3 notebook
```

### 파이썬3용 아이파이썬 노트북
```
$ sudo pip3 install ipython[all]
```
### 그 외에 필요한 파이썬 패키지
```
$ pip3 install -r requirements.txt
```
를 실행하면 아래 패키지를 설치합니다.
```
numpy>=1.9.1
scipy>=0.17.1
pandas>=0.21.1
matplotlib>=2.1.1
scikit-learn>=0.19.1
statsmodels>=0.8.0
```

추가적으로, 24장 예제 코드는 아래 코드를 실행하세요.
```
$ pip3 install -r requirements_24.txt
```
24장 예제 코드는 아래 패키지가 필요합니다.
```
keras>=2.1.2
pymc>=2.3.6
tensorflow>=1.4.1
```

