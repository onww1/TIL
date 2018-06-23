# Git .gitignore 적용하기



## .gitignore이란?

​	 Project에 원하지 않는 Backup File이나 Log File , 혹은 컴파일 된 파일들을 Git에서 제외시킬수 있는 설정 File이다.



### 1. .gitignore 파일 만들기😊

* 항상 최상위 Directory에 존재해야 한다.

* 예시

  ```markdown
  ## Algorithm Ignore File ##
  
  *
  
  !*.c
  !*.cpp
  !*.java
  !*.py
  !*.md
  !.gitignore
  
  !BOJ
  !CodeGround
  !CodingParty
  !ETC
  !SWExpert
  !TestDoc
  
  # report_card.pdf
  ```




- 문법 

  ```markdown
  # : comments
  
  # no .a files
  *.a
  
  # but do track lib.a, even though you’re ignoring .a files above
  !lib.a
  
  # only ignore the TODO file in the current directory, not subdir/TODO
  /TODO
  
  #ignore all files in the build/ directory
  build/
  
  # ignore doc/notes.txt, but not doc/server/arch.txt
  doc/*.txt
  
  # ignore all .pdf files in the doc/ directory
  doc/**/*.pdf
  ```



### 2. 적용하기😗

- .gitignore File을 같이 Push 

- 기존에 있던 Project에 .gitignore File이 적용이 안되는 경우에는 git Repository에서 적용해보고 다시 Push 

  ```shell
  git rm -r --cached .
  git add .
  git commit -m "fixed untracked files"
  ```



### 3. 확인해보기🤨

<img width="984" alt="4da18ab2-f00c-4178-846f-a3c05ff888c5" src="https://user-images.githubusercontent.com/34507372/41806842-36e6467c-7700-11e8-8b62-d7517a0ac861.png">



### 4. Reference😆

- <https://www.git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository>

- <https://www.gitignore.io/>
- <http://stackoverflow.com/questions/11451535/gitignore-not-working>



> 출처 : <https://nesoy.github.io/articles/2017-01/Git-Ignore> 
