# pythonStudy26
파이썬기초(회원가입,성적,게시판,상품등)


python 3.11

LMS 개발순서
1. LMS 삭제 -> LMS폴더 생성 -> 각종 하위디렉토리 생성
2. domain에 객체 클래스 생성 -> member / score / board / item
3. service에 CRUD 클래스 생성 -> 회원가입,등등 세부
4. main.py 생성
5. __init__.py  패키징
6. service에 메서드 생성
7. main메

저장소를 만든다  : repository -> public -> readme.txt 생성
라이센스는 웹기반이면 아파치 / ai기반이면 mit를 선호함
만들어진 저장소에 readme.txt를 편집해본다. (프로젝트 별로 시그니쳐 기록)
깃허브 관리하는 프로그램 설시 (소스트리)
비트버킷 해제 -> git만 체크 -> 머큐리 체크해제 -> 설치진행
깃 -> 이메일 주소 입력 -> Hss안씀
소스트리와 깃허브 연동 -> 소스트리프로그램 -> 도구 -> 옵션 -> 인증 -> 추가 -> 호스팅서비스(github)  -> githuㅠ-> 우측상단 계정관리 -> setting 
-> 좌측하단 developer setting -> personal access tokens -> 토큰 classic -> generate new token -> 만료일 리밋없ㅇㅣ -> 모드 다 체크 (초보)
-> 하단 만들기 -> 16진수로 된 암호가 나옴 복사
소스트리 호스팅 서비스 : GitHub
선호 프로토콜 : HTTPS
인증 : personal Access Token 새로고침
암호에 발행한 토큰  발행된거 붙이기 -> 확인 -> 인증성공

# 내가 만든 프로젝트를 저장소에 업로드
#------------------깃과 바탕화면 동기화
new reporitory 생성
바탕화면에 github에 업로드 할 폴더를 생성 (git/pythonstudy)
소스 트리에서 new tab -> 원격 아이콘 클릭
본인의계정이 나오고 repos새로고침 -> 바로 전에 생성한 repository선택
repository아래 clone(복제)클릭 -> 클론 
첫번쨰줄 : 내 깃헙 주소
두번쨰줄 : 내 디스크 경로, 바탕화면/git/pythonstudy26
클론 버튼을 누르면 웹상에 있는 소스들이 바탕화면/git/pythonstudy26로 다운로드가 됨
(readme.md 수정했던 것들과 git에 관련된 환경설정이 내려옴)
.git 폴더같은것들이 숨겨져 있음
#------------------프로젝트 업로드
C:\pyton_study 안에 있을때 탐색기로 위치이동
폴더안에 모든것을 선택 , 주의사항 : 용량이 크면 안올라감 10MB이하
복사 바탕화면/git/pythonStudy26에 붙이기 (덮어쓰기)
소스트리에 가면 커밋에 빨간 아이콘이 보인다 -> 커밋 클릭
내가붙인 파일이 새로 만들어 졌거나 수정본이면 stage에 올리기
stage : github에 올리 준비하는 단계-> 검증단계(이전없던내용,새로생긴내용확인시켜줌)
하단에 커밋 메세지(추가수정된) 기록해야 버튼이 활성화됨 - >클릭
PUSH에 빨간아이콘 -> push에 가서 업로드를 진행함 (브랜치를 선택)
(브랜치: 소스코드의 백업레이어 ->조원명,메뉴기능추가 로 만들 수 있음)

