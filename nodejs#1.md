# nodejs#1
[왜 node.js인가]
- V8엔진 사용(V8이란 크롬에 탑재된 자바스크립트 엔진)
- node.js의 특징
 1) 이벤트기반: 사용자가 웹페이지 요청, 데이터 입력 같은 이벤트시에만 작동
 2) 싱글스레드: 모든 요청 및 응답을 하나의 스레드에서 담당
 3) 비동기방식(non blocking IO): 하나의 요청과 응답이 마무리 되지 않아도 다음 요청 처리!(python asyncio도 비동기방식)<->Blocking IO
	- 비동기 방식의 단점은 하나의 스레드가 모든 요청을 처리하므로 긴요청이 걸리는 작업이 있으면 다음 작업처리에 대기하게된다-> 웹서버등의 DB호출등에 최적화
- node.js 창시자는 front언어로 유명한 js로 백엔드를 구현해보자고 만듦
- 강사님이 node.js 쓰는 이유는 프론트엔드와 궁합이 잘맞음(JSON데이터를 주고받는데 편리), 최근 서버사이드 플랫폼보다 프론트엔드의 변화의 속도가 더 빠르다

[웹접근성]
- 간단히 말하면 브라우저에 상관없이 같은 내용을 보여주는 것!(웹표준에 맞게 작성해서)ex) 눈이 안보이는 사람은 스크린리더기(alt태그 사용)로, 인터넷 속도가 느린 사람은 css를 끄고도 정보를 습득가능하게

[HTML5]
IE8이하에서 HTML5태그 쓰는법

[css]
*class 는 . /id는 #
1. 우선순위(모든걸 우선하는 !important)
id>>class이고 1. style선언 2. <style></style> head 안 선언 3. 외부 link선언 
2. css 박스모델

Padding vs. Margin

	- border 와 content사이는 padding로 조절(padding-top/bottom/left/right)
	- element 와 다른 element 사이는 margin으로 조절(margin-top/bottom/left/right)





3. background
<div style="background:url('https://nodejs.junyoung.me/demo/images/1.jpg’) 0 0 no-repeat; color:#fff; width:200px; height:300px;">
    첫번째
</div>

4. css float box: 주로 상단 네비게이션 만들때나 레이아웃을 만들 때 많이 쓰임
			<html><body>
				<div>
			<img src="http://nodejs.junyoung.me/demo/images/2.jpg" style="float: right; " alt="강아지">
			    플로트연습
			</div>
			</body>	
			</html>

5.  media query(반응형layout을 설정하는 방법)

		@media(max-width: 600px){//브라우저의 창사이즈가 최대 600px일때
			.width600{
			width: 100% !important;
			float: none;
			}
		}

[bootstrap]
설정 link rel로 cdn으로 받아온다.
- btn 종류 많다.
btn btn-default, btn-primary, btn-danger, btn-info, btn-warning
layout
	col-sm-(1~12)->sm은 small device
	col-md
- table
table: tr간의 구분
table-bordered: 양옆의 구분선
table-hover: 마우스 올릴시 배경색

- bootstrap plugin
ex)SB Admin(관리자 페이지), summernote(에디터)
semantic ui, boot forest

- navbar

상단 메뉴바
