[CRUD 구현]
[Mongoose]

Mongoose라는 패키지로 스키마 없는 MONGODB의 스키마 사용하기! 
1. MODELS 폴더 안에 사용자는 어떤 필드를 받는다는걸 기술해놓을 수 있다.
2. VALIDATION 유효성 체크를 위한 MONGOOS 검증 코드에 한 줄만 추가하면 됨.

mongoose.model(‘ collection명’,


[MODEL]
----
DB관련

identitycounters collection에는 기준이 되서 count할 수 있게 해줌

findOne 한 row만 가져옴

[VIEWS]-템플릿을 넣는 곳
----
HTML
view engine 뷰엔진
확장자 .ejs

[CONTROLLER]
----
*router 잘 정리하자!
GET /admin/products

admin.js

view/admin/products

GET /admin/products/write

views/admin/form.ejs

res.direct

res.render는 뿌려줘
res.redirect( /admin/products)<- 저장되고나서

//강사님 메모
GET /admin/products
admin.js
views/admin/products.ejs
GET /admin/products/write
views/admin/form.ejs
POST /admin/products/write
res.redirect(  /admin/products )
res.render( 템플릿위치 , 변수들  )
템플릿 불러오기 include
router.메서드( URL , 콜백함수 );

코드가 더러워지지 않게 가상변수!

[POSTMAN]

[homework]

MVC

모델작성Model 
models/ContactsModel.js

라우팅Controller
routes/contacts.js

뷰폴더View
views/contacts/list.ejs
views/contacts/form.ejs
URL
/contacts  글리스트
/contacts/write 글작성
/contacts/detail/:id  상세글보기
/contacts/edit/:id 글수정하기
/contacts/delete/:id 글삭제하기
