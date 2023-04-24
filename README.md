# Paper/Report Summarzatoin Service


![header](https://capsule-render.vercel.app/api?type=rect&color=EFCFCC&height=200&section=header&text=Paper/Report%20Summarization&fontSize=50&fontColor=91342A&desc=%EA%B2%80%EC%83%89%20%EA%B2%BD%EC%9F%81%EB%A0%A5%20%ED%96%A5%EC%83%81%EC%9D%84%20%EC%9C%84%ED%95%9C%20%EB%85%BC%EB%AC%B8%2F%EB%A6%AC%ED%8F%AC%ED%8A%B8%20%EC%9A%94%EC%95%BD%20%EB%AA%A8%EB%8D%B8&descSize=20&descAlignY=72)


## Service Sample

![화면 캡처 2023-03-20 211918](https://user-images.githubusercontent.com/114756802/226337540-5838981b-d0a3-4fc6-94fe-503b4ec1542f.png)


- 본 서비스는 논문 및 레포트의 초록(1024자 이하)을 통해 주제문을 자동으로 요약/생성하는 서비스입니다.
- txt 파일의 요약문을 jupiter notebook 내에서 직접 확인하거나 excel 파일을 통해 확인하실 수 있습니다.


---


## **Generation Sample**
| | text |
|---|-----------------------------|
|text| 본 연구는 코로나19 이후 초등학생의 신체활동량과 신체적자기개념, 그리고 긍정심리자본의 관계를 탐색하고자 하였다. 구체적으로 운동참여가 긍정심리자본에 영향력을 행사하는 과정에서 신체적자기개념의 매개효과를 검증하고자 하였다. 이를 위해 초등학교 6학년에 재학 중인 97명의 학생들을 대상으로 주간운동빈도, 주간운동시간, 신체적자기개념, 긍정심리자본을 측정하는 설문조사를 실시하였고, 수집된 자료를 바탕으로 기술통계분석, 상관분석, 구조방정식 모형 검증을 실시하였다. 본 연구를 수행한 결과, 초등학생들의 운동참여수준(주간운동빈도, 주간운동시간) 은 신체적자기개념 및 긍정심리자본의 모든 하위요인들과 정적 상관관계가 나타났다. 또한 신체적자기개념은 운동참여수준과 긍정심리자본의 관계를 부분적으로 매개하는 것으로 나타났다. 본 연구의 결과를 통해 운동에 자주 참여하거나 운동에 참여하는 시간이 많은 학생일수록 자신의 신체에 대해서 긍정적으로 인식하고, 일상생활에서의 희망, 낙관성, 탄력성, 효능감을 가진다는 것을 확인하였으며, 초등학생들이 운동에 참여함으로써 향상된 신체적자기개념이 긍정심리자본의 향상으로 이어질 수 있다는 것을 실증적으로 규명하였다.|
|summary|코로나19 이후 초등학생의 신체활동량과 신체적자기개념, 그리고 긍정심리자본의 관계를 탐색하고자 운동참여가 긍정심리자본에 영향력을 행사하는 과정에서 신체적자기개념의 매개효과를 검증하고자 하였다.|


---

## **How to install**
```
$ git clone https://github.com/Jesimsim/ds-CP1-project
```
혹은 패키지 전체 다운로드(상단 초록색Code버튼 - Download .Zip)


## **Requirements**
- 파이썬 버전
```
python==3.6.9
```
파이썬은 다음과 같이 설치할 수 있습니다
```
$ conda create --name "가상환경이름" python=3.6.9"
$ conda activate "가상환경이름"
```
- 패키지 요구사항
```
pandas
openpyxl
torch==1.9.1
torchtext==0.10.1
torchvision==0.10.1
torchmetrics==0.5.1
transformers==4.8.2
streamlit==1.1.0
pyyaml==5.4.1
pytorch_lightning==1.5.2

```
요구조건은 다음과 같이 설치할 수 있습니다.
```
$ cd ds-CP1-project
$ pip install -r requirements.txt
```

## **How to Use**

- 폴더의 구조는 다음과 같습니다.
```
ds-CP1-project
├── data
│   └── sample0.txt    # 요약할 파일(논문/리포트.txt)의 위치
├── model              
├── utils              
├── result
│   └── summary.xlsx   # 생성된 요약문 excel파일의 위치
│
├── README.md          # 사용설명서
├── test.ipynb         # 서비스 실행 파일
└── requirements.txt   # 서비스 실행을 위한 필요조건

```
- data 폴더에 txt 파일(요약할 논문/리포트)을 넣습니다.
  - 파일은 txt 형태여야 합니다.
- test.ipynb를 열어 서비스를 실행합니다.
  - [파일 불러오기 및 전처리] 셀을 실행시킨 후, 원하는 결과 형태(직접 확인 혹은 파일 저장)에 따라 [요약문 생성 및 확인] 셀을 실행해주시기 바랍니다.
- 실행결과를 test.ipynb 파일 내에서, 혹은 result 폴더 내 excel 파일을 통해 확인하실 수 있습니다.
  - 파일이 한 개일 경우, [결과 확인하기] 셀을 통해 jupiter notebook 파일 내에서 바로 결과를 확인하실 수 있습니다.
    - 여러 개일 경우 첫번째 파일의 결과만 출력됩니다.
  - 파일이 여러 개일 경우, [액셀 파일로 저장하기] 셀 실행 시 result 폴더 내 excel 파일이 생성되며 결과를 확인하실 수 있습니다.
    - 단, excel 파일이 열려있으면 제대로 동작하지 않습니다. 실행 전 excel 파일이 열려있지 않은지 확인해주세요.
    - 파일이 한 개인 경우에도 excel 파일을 통해 결과를 저장하실 수 있습니다.
    
---

## **프로젝트 배경**

![image](https://user-images.githubusercontent.com/114756802/234034260-6637fe38-a0c7-4747-8869-68397b8efe1f.png)

### **프로젝트 목적 및 배경**
- 논문/리포트 플랫폼 서비스에서 검색 시 제목과 요약문을 함께 제공하기 위해, 논문/리포트 요약문 생성 모델 구축 및 배포

### 프로젝트 의의
- 논문제공자 - 요약 자동화를 통한 사용자 편의성 향상
- 논문독자 - 논문 내용을 살피는 단계(’검색화면’-’논문화면’ 2단계 > ‘검색화면’ 1단계)를 줄임으로써 논문 검색시간 단축, 타사에 비한 검색 경쟁력 향상

> 이후 키워드 추출 중심으로 모델을 바꿔, 검색 정확도를 향상시키는 모델로도 활용될 수 있을 것으로 보임


---

## 프로젝트 프로세스

![image](https://user-images.githubusercontent.com/114756802/234034444-c67514a9-2250-4497-805c-133b9abc390c.png)


---

## 데이터셋


---

## 모델 및 기법


---

## 프로젝트 결과

---

## 의의, 한계점 및 보완점
