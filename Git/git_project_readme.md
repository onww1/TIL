# Git 프로젝트 소개 글 작성하기 (README.md 작성하기)

* [awesome-readme](https://github.com/matiassingers/awesome-readme)에서 우수한 ***README*** 를 큐레이션했다. 

  이 중 몇 가지 모범 예제를 참고해 스스로 목차를 만들어보자.

* ***README.md*** 파일은 [마크다운 문법](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#lines)으로 작성한다.

* ***README.md*** 파일에는 기본적으로 다음 내용들을 포함해야 한다.

  * 프로젝트명
  * 프로젝트 소개
  * 설치 방법
  * 사용 예제
  * 개발 환경 설정 방법
  * 기여 방법
  * 변경 로그
  * 라이센스 및 작성자 정보

* 예시 Template

------

## Project title
A little info about your project and/ or overview that explains **what** the project is about.

## Motivation
A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.

## Build status
Build status of continus integration i.e. travis, appveyor etc. Ex. - 

[![Build Status](https://travis-ci.org/akashnimare/foco.svg?branch=master)](https://travis-ci.org/akashnimare/foco)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/akashnimare/foco?branch=master&svg=true)](https://ci.appveyor.com/project/akashnimare/foco/branch/master)

## Code style
If you're using any code style like xo, standard etc. That will help others while contributing to your project. Ex. -

[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)

## Screenshots
Include logo/demo screenshot etc.

## Tech/framework used
Ex. -

<b>Built with</b>
- [Electron](https://electron.atom.io)

## Features
What makes your project stand out?

## Code Example
Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

## Installation
Provide step by step series of examples and explanations about how to get a development env running.

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests
Describe and show how to run the tests with code examples.

## How to use?
If people like your project they’ll want to learn how they can use it. To do so include step by step guide to use your project.

## Contribute

Let people know how they can contribute into your project. A [contributing guideline](https://github.com/zulip/zulip-electron/blob/master/CONTRIBUTING.md) will be a big plus.

## Credits
Give proper credits. This could be a link to any repo which inspired you to build this project, any blogposts or links to people who contrbuted in this project. 

#### Anything else that seems useful

## License
A short snippet describing the license (MIT, Apache etc)

MIT © [Yourname]()

------



### 1. 프로젝트 제목

* 제목만으로도 어떤 기술을 사용하여 무슨 프로젝트를 만들었는지 상대방이 이해할 수 있게 **직관적으로** 작성한다.
* **프로젝트 소개 웹 사이트**도 추가한다.
  (**heroku, surge.sh, gh-pages** 등 무료 호스팅 서비스가 많으니 적극 활용한다.)
  (특히 **gh-pages** 는 마크다운으로 정적페이지를 만들어주니 꼭 사용해보자.)
* 프로젝트에 사용한 **기술, 분야, 주제 등 태그도 추가**해 프로젝트 메인 페이지를 풍성하게 만든다.



### 2. 프로젝트 내용

* **짧은 소개 문구**와 한 문단 분량의 **프로젝트 내용**을 적는다.
* 프로젝트의 **목적과 동기, 주요 기능**이 잘 드러나있어야 한다.
* 사용자에게 프로젝트 실제 **데모를 보여주는 것이 중요**하다.
* 배포를 하거나 설치가 필요한 프로그램이라면 반드시 데모를 추가하자.
* 스크린 캡쳐 프로그램으로 스크린 녹화를 하고 ***gif*** 파일로 변환한다.
* 영상이 필요하면 **YouTube**에 올리고 링크를 건다.
* (Option)  [shields.io](https://shields.io/)에서 뱃지를 선택해 패키지, 배포, 소셜 네트워크, 코드 커버리지, 다운로드 수, 버전 등을 명시해 좀더 시각적으로 표현할 수 있다.



### 3. 설치 방법

* 실력과 관계없이 누구나 개발 환경을 설치할 수 있어야 한다.
* 사용자가 설치 과정 중 좌절하지 않게 **최대한 자세하고 친절하게 작성**한다.
* **운영체제 별(OS X/Linux/Windows 등) 설치 방법**도 작성한다.
* 가능한 사용자가 간단한 명령어로 설치를 끝내도록 **설치 과정을 간결하게** 만드는 것이 좋다.



### 4. 코드 예제

* 설치 이후 **실제 사용 방법 가이드**를 작성한다.
* **코드 예제**와 **실제 적용 사례**를 보여준다.



### 5. 개발 환경 설정 방법

* 잠재적인 Contributor가 프로젝트에 기여할 수 있도록 **명확한 가이드를 제시**한다.
* **개발 의존성 설치**와 **자동 테스트 슈트를 실행**해 사용자가 개발 환경을 올바르게 설정했는지 확인할 수 있게 한다.
* 신규 버전 소프트웨어를 빌드하고 릴리스하는 방법도 작성한다.



### 6. 기여 방법

* 누구나 소스 코드를 다운받아 개발환경을 구축할 수 있고 개선시킬 수 있다.
* 나의 프로젝트에 관심을 가진 누군가 직접 기여할 수 있다.
* 따라서 **개발 프로세스와 기여 방법에 관한 명확한 지침을 제공**해야 한다.



### 7. 로그 변경

* 사용자는 마지막 버전과 비교하여 어떤 변경 사항이 있었는지 확인할 수 있어야 한다.
* **기능 개선과 수정 내역을 함축적으로 정리**하여 **로그 변경 히스토리를 관리**한다.



### 8. 크레딧

* 오픈 소스 프로젝트를 사용해 만들었거나, 누군가로부터 큰 도움을 받았거나, 크게 기여한 사람이 있다면 잊지 않고 꼭 언급하자.



### 9. 라이센스

* 라이센스를 명시하고 디렉터리에 ***LICENSE.txt*** 를 포함시키자.
*  [오픈 소스 라이센스(영문)](http://choosealicense.com/), [오픈소스 SW 라이센스 종합시스템(국문)](https://olis.or.kr/license/licenseGuide.do) 라이센스 목록을 확인할 수 있다.
* 가장 많이 쓰는 라이센스는 MIT 라이센스, Apache 2.0 라이센스, ISC 라이센스, BSD 라이센스다.



### 10. 연락처

* 연락처는 프로젝트 신뢰성을 뒷받침해준다.
* 프로젝트 담당자 또는 팀원들의 깃허브 프로필 링크, 트위터, 이메일 등 연락처 정보를 기입한다.
* 별도로 전문적이고 공식적인 트위터를 만들고 프로젝트 진행 상황과 업데이트 소식을 알리며 적극적으로 내 프로젝트를 홍보하자.





> 출처 : https://sujinlee.me/professional-github/