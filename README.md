# study

[node.js로 구현하는 웹서비스 개발#1]

[왜 node.js인가]

- V8엔진 사용
- 비동기방식(non blocking IO)
- node.js 창시자는 js로 백엔드를 구현해보자고 만듦
- 강사님이 node.js 쓰는 이유는 프론트엔드와 궁합이 잘맞음(JSON데이터를 주고받는데 편리), 최근 서버사이드 플랫폼보다 프론트엔드의 변화의 속도가 더 빠르다

[css]
1. css 박스모델
padding vs. margin

- border 와 contents사이는 padding로 조절(padding-top,bottom,left,right,)
- content 와 다른 contents 사이는 margin으로 조절

2. css flat box
header>

3.  media query(반응형layout을 설정하는 방법)

@media(max-width: 600px){
	.width600{
		width: 100% !important;
		float: none;
	}
}

[bootstrap]
설정 link rel로 cdn으로 받아온다.
btn 종류 많다. btn bin-info…
layout
	col-sm-(1~12)->sm은 small device
	col-md
4. table table-bordered table-hover

5. bootstrap plugin

	ex)SB Admin, summernote(editor)
semantic ui, boot forest

6. navbar

상단 메뉴바

[node.js로 구현하는 웹서비스 개발#2]
1. javascript란?


여러 플랫폼 제작사에서 javascript 개발자를 끌어 안기위한 환경 조성
VS CODE, SLACK -made by js

2. 변수 선언

var 로 선언, 자바스크립트 변수는 기본자료형(undefined도 포함)과 객체형 두가지로 나뉜다.

var arr = new Array();

3. 객체형 

3-1. 리터럴 표현법(literal)(json과 비슷)

	var a = {
    numberVal : 111,
    arrayVal : "zzz",
    arrayList : [1,2,3],
    Speack : function(){
        consoloe.log("function");
    }
}
console.log(a);

=> object 출력

//멤버와 값을 출력
for(var propㅡㄱ시erty in a){
    console.log(   property + "/ " + a[property]);
}

public 변수
   함수내에서 this.name 멤버생성
private 변수
   함수내에서 var로 멤버생성


[jQuery]

1. jQuery란?
	자바스크립트 라이브러리

2. 셀렉터

3. css

4. 연습해보기

 1) 폼 검증 if(!emailInput.val()){}
 2) 댓글달기 input[name=comment]+val(‘’)로 입력창 비우기
 3) 스톱워치 slice(뒤에서 두자리까지만 잘라 012는 12초 08은 8초)와 append 주목!
 4) 이미지 슬라이더 slicker ,owl carousel 연습해보기
