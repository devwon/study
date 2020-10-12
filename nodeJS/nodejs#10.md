
[장바구니]
1. UI
form의 hidden에 개수,총가격 값을 담음

2. 장바구니 담기

  ex)
  cartList[10].amount
  cartList[10].cartNum

- 담기 액션

1. 기존 변수 가져오기 getCookie -> cartList 변수 셋팅 : *JSON.parse

2. cartList에 cartList[10] 추가

3. setCookie(cartList) : *JSON.stringify 

*자바스크립트로 객체를 파싱하고 한줄로 늘려주기위해

예시)
%7B%229%22%3A%7B%22number%22%3A%223%22%2C%22amount%22%3A%222700%22%2C%22thumbnail%22%3A%22products-1517830155901.jpeg%22%2C%22name%22%3A%221%uBC88%uC9F8%20%uC774%uBBF8%uC9C0%22%7D%7D

JSON.parse 하면 js 객체로 가져올 수 있음


[pagintate]

async 로 해서 동기식으로 처리

skip, offset

HW-메인에서 더보기 누르면 사진 더 나오는 거 

[장바구니]

- array like object
: object.keys(obj)

array.length prototype

- 실제 서비스에서는 logout하는 시점에 쿠키+id를 DB에 담는다. 쿠키는 비회원때문에

delete cartList[productId];  //지우는 부분//literal 객체에서 한 줄이 삭제됨


a = {1:{a,b},2:{c,d}}

delete a[1];// 1에 있는거 다 지워짐

[결제 기능]

   I’mport 사용(soCar 결제 구현 하신 분이 구현)

   아임포트로 결제정보보냄(우리서버)-> 아임포트에서 결제승인(아임포트측)->PG사에서 결제 승인->아임포트->DB업데이트(우리서버)

   아임포트로 정보를 보내는 부분 -> DB 업데이트 -> /checkout/success

   결제 정보를 요청전에 DB 담고 -> 아임포트로 쏘고 -> DB에 총가격 == 아임포트가격 일치하는지 확인 (amount 조작 가능성 있음)

[ngrok] 외부에서 local 도메인 접근 가능하게

   내 pc를 서버처럼 잠깐 띄어줄 수 있어

   주소 셀프로 입력 못하게: readonly
