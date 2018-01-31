[xss&csrf]

1) xss: cross site scripitng

악의적인 공격, 글 등록시 <script>location.href</script> 와 같이 페이지를 이동하게 하거나 매 초마다 목표사이트를 공격하게 하는 스크립트 삽입, 또는 사이트 쿠키를 가로채고 전송

1-2) 방어법
	
	-DB에 저장 전 특수문자를 필터링한다. <, >, 을 html 특수문자 코드로 변환한다그 밖의 문자열은 지운다. 
	- nodejs-> npm install xss

2) csrf: Cross-Site Request forgery

	옥션 해킹에도 사용된 기법
2-2) 방어법
	- 목표 사이트를 정하고 aciton의 위치로 필드명만 일치한 폼을 전송
	- 우리 사이트에서 작성됬다는 증거로 토큰을 발행,확인
	- nodes -> nom install csurf


[cookie-parser]

browser cookie에 id,pw 암호화해서 저장-> 나중에 자동로그인 가능

[미들웨어middleware]

중간에 요청을 가로채는거 (로그인 같은 거 필요시 다음 콜백함수 대신 가로챔)

    function loginRequired(req,res,next){
	    console.log(‘작동’);
	    next();
    }

            router.get(‘/products', loginRequired , function (req, res) {
                ProductsModel.find(function(err, products){//인자는 에러와 products
                    res.render('admin/products',//views의 위치
                        { products : products}//두번째 products가 위의 인자
                        //DB에서 받은 products를 products변수명으로 내보냄
                    );
                });
            });

POST에서 csrfProtection 미들웨어: 토큰을 확인하고 DB에 저장

[파일업로드]

multer 사용

[적용순서]
- DB에 저장될 필드 수정(PostModel) : thumbnail(파일 경로)을 schema에 추가
- npm install –save multer
- uploads 폴더 생성: 정적 폴더(static folder) 지정
- router 처리 ( write, edit - post ): 파일 업로드 지정
- view 처리 ( detail ) : 뿌려주기

[파일 업로드 흐름]
- 폼 데이터 서버로 전송
- destination에 저장될 위치로 지정
- filename으로 파일명을 받아서 DB에 저장


파일 삭제
unlinkSync 내장 모듈 사용!

*ajax같은 경우 form으로 매번 문서를 만들기 귀찮으므로 postman이용해서 데이터를 쏴줌


[회원가입]
passport사용!

회원가입 적용순서

- UserModel 구현
- accounts router 작성
- 회원가입 폼작성
- 로그인 폼작성
- 암호화 모듈 작성


회원가입시 암호화해서 저장, 로그인시 암호화된 거랑 DB에 저장된 거랑 비교
암호 까먹을시 암호화된 임시 비밀번호를 주고 rainbow attack:쉬운 비밀번호를 암호화된 결과값으로 돌려봄

pw 암호화 crypto 모듈 사용
1234

[암호화 기법]

Ciper(복원불가능)
<->Hmac방식 (복원 불가능)

form 에서 입력된 정보 + salt 로 아무 의미 없는 문자를 더한 후
를 sha512라는 암호화 기법으로 해시로 만들어서 제공한다.
ex) 1234 + fastcampus -> sha512 -> hash -> base64인코딩

