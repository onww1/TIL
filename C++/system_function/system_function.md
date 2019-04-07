## C++ system 함수로 터미널 커맨드 실행하기



Library : `stdlib.h`

Prototype : `int system(const char* command);`

* Parameter : const형 char 배열 (`command`)
* Return Value : `command` 를 실행시켰을 때의 리턴값



### Example code

```c++

*#include* <stdio.h>

*#include* <stdlib.h>

int main(int argc, char *argv[]) {

​    int ret = system("ls -a");

​    return 0;

}

```

