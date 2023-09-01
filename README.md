# BOK_TEAM_2

## 컨벤션
### Code Convention

- 클래스: `PascalCase`
- 변수명: `snake_case`
- 함수명: `snake_case`
- 상수: `SNAKE_CASE`
- 셀명: `# 약어(셀이름)` ex) # Mmpdc(MPB minutes pdf download code)

### Git Convention

기본 브랜치: `main`

<aside>
 `[프로젝트 협업 도구 할일 ID 넘버] COMMIT_TYPE: COMMIT_SUMMARY`

</aside>

- **BRANCH_TYPE**  
    - crawling : 크롤링
    - EDA : 전처리 및 EDA
    - make_dictionary : 감성 사전
    - modeling : 모델링

- **COMMIT_TYPE**
    - feat : 새로운 기능 추가
    - fix : 버그 수정
    - docs : 문서 추가 및 수정
    - refactor : 기존 코드 수정
    - style : 코드 포맷팅, 세미콜론 누락, 오타 수정 등
      
- **COMMIT_SUMMARY**
    - 영어로 작성
    - 마침표를 붙이지 않음
    - 50자를 넘기지 않음

(커밋 메세지 예시)

- `feat-crawling code-{상세 내용}` : crawling code 새 파일(or 기능) 추가
- `refactor-crawling code Mmpdc-{상세 내용}` : crawling code Mmpdc 셀 코드 수정
