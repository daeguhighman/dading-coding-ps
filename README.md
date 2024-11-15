# 🎯 Dading Coding Problem Solving Study

## 📅 Study Period
- 스터디 기간: 2023년 11월 17일 - 12월 19일 (35일)

## 👥 Members & Goals
| 이름 | 목표 진행률 | 목표 문제 수 |
|------|------------|-------------|
| 동현 | 70% | 25문제 |
| 소연 | 20% | 7문제 |
| 나리 | 50% | 18문제 |
| 경륜 | 50% | 18문제 |
| 윤서 | 40% | 14문제 |

## 📊 Progress Tracking
현재 진행 상황은 [여기](progress.md)에서 확인할 수 있습니다.

## 🚀 Getting Started

### 1. Repository Setup
1단계: 브랜치 생성
```bash
# 메인 저장소 클론
git clone https://github.com/yoondh1215/dading-coding-ps.git
cd dading-coding-ps

# 본인의 이름으로 브랜치 생성
git checkout -b [본인이름]
# 예: git checkout -b donghyun
```

2단계: 원격 브랜치 설정
```bash
git push -u origin [본인이름]
```

### 2. File Structure
파일은 다음과 같은 구조로 정리됩니다:
```
dading-coding-ps/
├── Chapter11/
│   ├── 윤동현/
│   ├── 정소연/
│   └── ...
├── Chapter12/
└── ...
```

#### 파일 이름 규칙
이것이 코딩테스트다 문제:
```
pfct_[문제번호].py    # 예시: pfct_13.py
```

백준 문제:
```
boj_[문제번호].py     # 예시: boj_134.py
```

### 3. 문제 풀이 제출 방법

#### 1단계: 변경사항 추가 및 커밋
```bash
# 변경사항 추가
git add .

# 설명적인 메시지와 함께 커밋
git commit -m "solve: 12장 1번 문제 - 이진 탐색"
```

#### 2단계: 브랜치에 푸시
```bash
git push  # 본인 브랜치에 푸시
```

#### 3단계: Pull Request 생성
- GitHub에서 본인 브랜치에서 main으로 Pull Request 생성
- PR은 매일 문제 해결 후 생성 가능
  ```
  예시: 월요일에 1문제, 화요일에 2문제를 풀었다면
  - 월요일: 1개의 PR 생성
  - 화요일: 1개의 PR 생성
  ```
- **주의사항**: 일주일에 최소 1회는 리뷰어를 지정하여 PR 생성
  ```
  예시: 이번 주에 5개의 PR을 생성한다면
  - 4개는 리뷰어 지정 없이 PR 생성 가능
  - 1개는 반드시 리뷰어를 지정하고 코드 리뷰 요청
  ```

### Pull Request 종류
1. **일반 PR**
   - 리뷰어 지정 없이 생성
   - 바로 main 브랜치에 병합하기
   - 매일 문제 해결 후 생성

2. **리뷰 요청 PR**
   - 일주일에 최소 1회
   - 리뷰어(챕터 담당자) 지정 필수
   - PR 템플릿에 따라 자세한 설명 작성
   - 목요일 오후 12시까지 생성

## 📝 코드 리뷰 프로세스

### 주간 요구사항
1. **리뷰 할당량**
   - 모든 스터디원은 주당 최소 1개의 문제에 대해 리뷰를 요청해야합니다.
     - 리뷰를 요청할 때는 아래의 템플릿에 따라 작성해주세요.
   - 챕터 담당자는 최소 2개의 문제를 리뷰해야 합니다

2. **마감기한**
   - 목요일 오후 12시까지 리뷰 요청 제출
   - 주간 미팅 전까지 리뷰 완료

3. **리뷰어 지정**
   - 챕터 담당자를 리뷰어로 지정
   - GitHub의 리뷰 요청 기능 사용

### Pull Request 템플릿
```
## 📌 문제 정보
- 챕터: [번호]
- 문제: [번호]
- 제목: [문제 제목]

## 💡 풀이 방법
- 사용한 알고리즘:
- 시간복잡도:
- 공간복잡도:

## 🔍 구현 설명
[풀이 방법에 대한 간단한 설명]

## ✨ 질문사항 
```


## ⏰ 주요 일정

### 주간 일정
- **목요일 오후 12시**: 리뷰 제출 마감
- **주간 미팅**: 챕터 발표 및 토론

## 🔍 추가 자료
### 📚 교재 및 소스코드
- [이것이 취업을 위한 코딩 테스트다 with Python (GitHub)](https://github.com/ndb796/python-for-coding-test)

### 📺 강의 자료

- [이것이 취업을 위한 코딩 테스트다 with Python ()](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)

- [바킹독의 실전 알고리즘(Youtube) ](https://youtube.com/playlist?list=PLtqbFd2VIQv4O6D6l9HcD732hdrnYb6CY&si=UKB2gLI3iXaL6bxl)
