
nodejs#3
--

[node.js]-1


1) 즉시실행익명함수(모듈작성패턴)

- 외부에서 내부 변수에 접근 못하게
- 내부에서 변수가 겹치지 않게
- 외부 변수에 영향을 받지 않음
	var test = 20;
	(function(){

   	var test = 10;
	console.log(test); // 10

	})();<-외부 변수에 영향을 받지 않는다!

- 함수 실행 후 return문으로 내가 원하는 변수만 제공 가능

		var test = (function(){
			var a= “1”;
			return{
				b : “2”;
				c : “3”;
			};
		})();
		console.log(test.a); // undefined
		console.log(test.b); // 2


		console.log(test); // 20
- 라이브러리를 만들경우, 모듈 작성 순서!
		
		(function(){
    			var test = 10;
    			window.test = test; //외부로 변수 출력
		})();
		console.log(test);

모듈 분리

변수 모듈에 영향을 안받아

2) 콜백 패턴

인자를 여러개 받고 싶으면 arguments변수 사용

3) 메서드 체이닝(함수가 이어져서 쏴지는 것)
	
	a().b();

4) prototype(js는 prototype기반 언어)

- 함수 생성시 같은 이름의 prototype 객체 생성

- 프로토타입은 함수 참조 계속해서 가르킨다. 서로 참조!

  *객체 생성시 생성자가 prototype 객체를 참조














== vs. ===

1 == “1” -> true (값만 비교)
1 === “1” -> false (값+형태까지 비교)

prototype은 공유하는 객체(유동적으로 바꿀 수 있어)

        function Car(){ }
        var myCar1 = new Car();
        var myCar2 = new Car();
        Car.prototype.color =“red”;//변수를 바꾸면 쳐다보고 있던 myCar1, myCar2의 color변수도 싹 바뀜
        console.log(myCar1.color);
        console.log(myCar2.color);
        Car.prototype.color ="blue";
        console.log(myCar1.color);
        console.log(myCar2.color);

        var test = { aa : 111 }; //리터럴로 객체생성
        test.prototype.bb = 222; //문법에러->test.bb=222;로 바꿔야해
        console.log(test.bb);  


- property 출력해보기

        function Car(){
            this.name = "첫번째";
            this.title = "타이틀"
        }
        Car.prototype.pro1 = "val1";//prototype변수
        Car.prototype.pro2 = "val2"; //prototype변수
        var myCar = new Car();
        var myCar = new Car();
        var prop;
        for(prop in myCar){
            if(myCar.hasOwnProperty(prop)){
                console.log(prop + " = "+ myCar[prop]);
            }
        }

#jQuery 플러그인 만들기
fn 하면 jQuery prototype에 접근 가능

<indexOf >

일치하는 index값이 있으면  위치값 반환
일치하는 index값이 없으면 -1


Object.create(): 인자를 prototype객체를 받는다.
java의 new와 비슷하게 구현(new가 더 빠름)

    function Car(){
        this.name = "내차";
        this.title = "타이틀"
    }
    Car.prototype.move = function(){
        console.log(this.name + " 이동" );
    };

    var myCar = Object.create(Car.prototype);
    myCar.move();  //undefined -> prototype이 object의 변수를 가져오지 못하므로 

- prototype이 변수도 가져올 수 있도록 두가지 방법
1. defineProperty로 변수 설정하거나
- set : 변수 바꾸거나 셋팅
- get : 변수 부르기
2. fn.call(객체명);<-object의 property를 다 가져옴!


<-prototype으로 객체 생성, prototype과 property구분하기위해서

[MongoDB]

JS와 잘 맞는 DB
- json-style의 document형태로 저장하는 오픈소스 NoSQL 데이터 베이스
- RDBMS VS. MongoDB

---
RDMS: MongoDB
Database: Database
---
- 하나하나가 문서형태(json)로 되있음
- NoSQL : 스키마 없이 사용가능
- 동적 스키마 : 필드에 맞추어서 넣지 않아도 되고, 입력시마다 필드를 추가 후 넣기 가능(RDBMS는 ALTER TABLE 해야되는데 이건 안해도 돼!)
- 단점: join시 코드가 복잡해짐
- 몇 억건일 경우 사용시 좋다.

- mongodb 모니터링 툴인 robo 3T사용!
