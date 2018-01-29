## 배운거
- 댓글구현
- validation 유효성 체크

댓글 process
댓글 내용 작성후 입력 버튼 클릭->댓글 ,product_id 라우팅으로 이동->라우팅에선 DB 삽입-> 성공메시지를 받아서 화면 갱신

*ajax는 기사더보기, 댓글 더보기에 많이 사용

### [PROCESS]

1) 댓글 작성

1. 댓글작성 + 댓글입력버튼 ( 이벤트 발생 )
2. ajax로 url을 호출( 라우팅을 호출 )
3. 라우팅 = DB insert구현
4. 라우팅 반환데이터 -> 원하는 위치에 append 

2) 댓글 삭제

1. a태그 클릭( .comment_delete ) -> 액션이 발생
2. ajax호출 -> url로 POST 요청
3. 라우팅 처리 ( DB에서 삭제 )
4. 해당 클릭했던 부분을 한줄 삭제

### [rest api]

GET /users -> 사용자 전체 리스트를 보는
POST /users -> 사용자를 추가
GET /users/:id -> 사용자 한명의 데이터
PUT /users/:id -> 사용자 한명 수정
DELETE /users/:id -> 사용자 한명 삭제
