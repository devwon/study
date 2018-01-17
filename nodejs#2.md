
nodejs#2
--
[javascript]
1. javascript란?


- 여러 플랫폼 제작사에서 javascript 개발자를 끌어 안기위한 환경 조성
- VS CODE, SLACK -made by js

2. 변수

*동적언어이므로 자료형 선언할 필요없이 var 로 선언

	var arr = new Array(“1번째”,”2번째”);//array 0부터 시작
	
*자바스크립트 변수는 기본자료형(undefined도 포함)과 객체형 두가지로 나뉜다.
- 기본자료형

기본 자료형	설명
- Boolean	논리적인 요소를 나타내고, (true 와 false)
- Null		객체 값이 존재하지 않는다는 것을 의미
- Undefined	값을 할당하지 않음
- Number	숫자형
- String	문자형
- Symbol	ECMAScript 6 에서 추가, 유일하고 변경 불가

*배열 출력시 IE9부터 사용가능한 forEach 사용법

	forEach( ! IE9부터 사용가능
		arr.forEach(function(value){
    		console.log(value);
		});

- 객체형

2-1) 리터럴 표현법(literal)(JSON과 비슷)
var로 변수선언
멤버간에는 ,로 구분
생성과 동시에 객체를 생성

	var a = {
    		numberVal : 111,
    		arrayVal : "zzz",
    		arrayList : [1,2,3],
    		Speack : function(){
        	consoloe.log("function");
    		}
	}
	console.log(a);
	//멤버와 값을 출력
=> object 출력
- 추가하려면 a.addNumber = 222;

2-2) 함수표현법

- 어떤 일정한 틀을 만들어 놓고 생성, 내부가 어떻게 구현되었나 생각하지 않고 제공되는 함수와 변수를 사용

function test(name, title){
    this.name = name;
    this.title = title;
}
var myTest = new test( "park" , "jjjj")
console.log(myTest.name);

2-2-1) public 변수
   함수내에서 this.name 멤버생성
2-2-2) private 변수
   함수내에서 var로 멤버생성
   
	function test(name, title){
		this.name = name;//public variable
		this.title = title;
		var private = “private variable”;//private variable
	}
	var myTest = new test(“park”, “jjjj”);
	console.log(myTest.private);//undefined 에러발생(내부에서만 접근가능)
	//해결법
	function test(name, title){
		this.name = name;//public variable
		this.title = title;
		var privateVal = “private variable”;
		this.privatePrint = privateVal;//접근할 공용변수 생성
	}
	var myTest = new test(“park”, “jjjj”);
	console.log(myTest.privatePrint);/

Global variable 전역변수
	- var 없이 선언
	- 글로벌 변수로 선언시 
3. 상속
  - ECMAScript5에서 Object.creat(): 인자로 prototype을 넘긴다.
  - ECMA6 에서 extends
  
	    class Dog extends Animal {
  		     speak() {
    			console.log(this.name + ' barks.');
  			}
		}
	
Global 변수(전역변수)
	- var 없이 선언
	- 글로벌 변수로 선언시 window객체의 멤버가 됨(window.variable)
	

[jQuery]

1. jQuery란?

	- 자바스크립트 라이브러리
	- DOM을 컨트롤하거나 소스를 짧고 직관적으로 작성가능
	- https://code.jquery.com/ 에서 head사이에 삽입
	- vscode에서 document.ready 단축키: jqdoc+tab

2. 셀렉터

	- $(‘#id’)//id검색
	- $(‘.class’)//class검색
	- $(‘.a_id input[name=abc]’)//a_id다음 abc 선택가능
3. css
	- css 속성지정
	
		$(‘#actionDiv’).click(function(){
			$(this).css(‘color’,’red’);
		});

		- 클래스가 존재하면 removeClass 없으면 addClass 작동 
			$(document).ready(function() {
  				  $('#actionDiv').click(function(){
        					$(this).toggleClass('color_red');
   				});
			});

4. 연습해보기

 1) 폼 검증 if(!emailInput.val()){}
 2) 댓글달기 input[name=comment]+val(‘’)로 입력창 비우기
 3) 스톱워치 slice(뒤에서 두자리까지만 잘라 012는 12초 08은 8초)와 append 주목!
 4) 이미지 슬라이더 slicker ,owl carousel 연습해보기
