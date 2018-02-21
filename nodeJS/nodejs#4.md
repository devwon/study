
nodejs#4
--

[mongoDB연습]

CRUD, FIND, 

C
show dbs

mongo db는 data를 insert한 순간부터 db생성
-> createCollection은 먼저 collection 생성

$cls = clear
- 비교연산자



.count():
.limit():
.skip():
Remove
db.board.remove()
Update
순수 query문으로 돌리면 update시 나머지는 싹 다 사라짐!
mongoose(동적스키마인 mongodb의 스키마를 고정하기 위해 사용)는 안그래!

[Node.js]

stable보단 LTS가 안정적


javascript 모듈관리

가져올땐 require

//listen(3000)

console.log("hello nodejs");

//모듈 가져오기
var myvar = require('./myvar');
console.log(myvar.c,myvar.d);//a,b 모듈 가져오기

//함수 모듈 가져오기
//var setA = myvar.a();
//console.log(setA);//a,b 모듈 가져오기

//new키워드로 instance 생성
var setVar = new Myvar();
Console.log(setVar.name);

//웹서버 띄어보기
var http = require('http');

     http.createServer(function( request, response){
        response.writeHead(200,{'Content-Type':'text/plain'});
        response.write('hello nodejs');
        response.end();
     }).listen(3000);


*nodemon이 자동으로 서버를 내렸다가 재시작 해줌

-g로 설정하면 명령어로 사용가능 nodemon ~~이렇게


—save 하는 이유: package.json에 자동 반영되게




<정리>

- mongo db query문, collection
- node명령어로 서버에 띄우는거
- npm.js로가서 이미 만들어진 모듈을 사용할 수 있어(http는 내장모듈)

- express framework
-  —-save를 통해 package.json에 반영
- app.use <-url적으면 작동하는 미들웨어 나중에

- 폴더생성, 라우팅만드는거 연습
- npm 설치 
	- @로 버전 지정 가능
	- -g로 설치시 시스템에 설치해주는거
	- 소스 수정할때마다 서버에 올려주는게 nodemon
