/*
 *	rm.cpp
 *	> 같은 문제에 대한 여러 파일을 가장 마지막 것만 남기고 모두 지워주는 프로그램
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

const int SIZE = 50, CMD_LEN = 1000;
char language[SIZE], command[CMD_LEN];
int problem_number, version, command_length;

int main() {
    // EOF를 만날 때까지 입력을 받는다.
    while (~scanf("%d %d %s", &problem_number, &version, language) != -1) {
        // git rm boj{problem_number}.{language} && 
        // git mv boj{problem_number}_{version}.{language} boj{problem_number}.{language}
        command_length = 0;
        command_length += sprintf(command + command_length, 
                                  "git rm boj%d.%s && git mv boj%d_%d.%s boj%d.%s", 
                                  problem_number, language, problem_number, 
                                  version, language, problem_number, language);

        // version이 2보다 크면 그 사이에 있는 것들을 모두 지우는 커맨드를 추가한다.
        if (version > 2) {
            for (int ver = 2; ver < version; ++ver) {
                command_length += sprintf(command + command_length, 
                                          " && git rm boj%d_%d.%s", 
                                          problem_number, ver, language);
            }
        }

        // 줄바꿈 문자를 넣어주고 system 함수에 command를 넘겨주어 실행한다.
        command_length += sprintf(command + command_length, "\n");
        int ret = system((const char *)command);
    }

    return 0;
}
