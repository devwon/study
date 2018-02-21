# [로그인]

목차
- 모듈설치
- passport란
- app.js 설정
- router passport 적용
- 로그인 실패 flash 메시지 적용

세션: 사용자 이름,장바구니 정보등을 세션에 저장 요새는 세션보다 radis써서 따로 빼는 추세

#
serializeUser: 첫 로그인 성공시에만 호출
deserializeUser: 페이지를 이동할때마다 호출

facebook로그인
passport 이용해서 로그인!

분기는 2개 아이디가 있으면 바로 진행 없으면 db에 저장하고 진행

id는 fb_id로 받아오자
email을 아이디로 지정할 수 없음

github에 올릴때 dotenv로 막고나서 올리기
