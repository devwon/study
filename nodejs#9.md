### promise 연습: reserve, reject

[1초 뒤에 숫자 출력하는 예제]

        function printLater(number) {
            setTimeout(
                function() { 
                    console.log(number); 
                },
                1000
            );
        }

        printLater(1);
- promise.all -> array로



내가 사용할 시점에 reserve로 받는다.

[콜백헬 개선]

함수명 앞에 *를 붙인다. 호출 시에는 함수명을 부르고 next-> yield있는 만큼 출력: generator(함수를 반복가능한 객체로 만든다.)

    function* iterFunc() {//함수를 여러번 호출할 수 있게

        yield console.log("첫번째 출력");
        yield console.log("두번째 출력");
        yield console.log("세번째 출력");
        yield console.log("네번째 출력");

    }

    var iter = iterFunc();
    iter.next();   // 첫번째 출력
    iter.next();   // 두번째 출력

-> 만들어진 함수 co

비슷한 기능[async await]-> router에 한 줄씩 실행할 수 있다.

    co(function*()) ——> async()=> yield 대신 await

    router.get('/products/detail/:id' , async(req,res)=>{
        try{
            const product = await ProductsModel.find().exec();
            const comments = await CommentsModel.find().exec();
            res.render(  , { product: product,comments : comments });
        }catch{
        }
    });

try , catch 로 에러처리 권장


[위지윅 에디터]-summernote
cf) ckeditor, naver editor

 ### <%= vs. <%-
- <%= 는 html 태그가 그대로
- <%- 는 html 태그 인식해서

summernote에서 file upload

1. front-end : ajax 로 파일을 전송->new FormData()->

2. POST /admin/products/ajax_summernote
multer로 이미지 업로드 걸어주고
-> return: 이미지 업로드 url

3. ajax로 받은 결과를 editor 삽입


[장바구니]
1. UI
form의 hidden에 개수,총가격 값을 담음

2. 장바구니 담기 기능

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

*JSON.parse 하면 

*js 객체로 가져올 수 있음
