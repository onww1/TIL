/*
 *	mv.cpp
 *	> 파일을 해당 알고리즘 분류 폴더로 옮기고, commit.
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

const int SIZE = 50, CMD_LEN = 1000;
char file_name[SIZE], category[SIZE], language[SIZE], command[CMD_LEN];
int problem_number, command_length;

int main() {
	// EOF를 만날 때까지 입력을 받는다.
	while (scanf("%d %s %s", &problem_number, language, category) != -1) {
		// 공백 하나를 제거하고, 문제 제목을 한 번에 받아준다.
		getchar();
		fgets(file_name, sizeof(file_name), stdin);

		// git mv boj{problem_number}.{language} ../{category}/boj{probrem_number}_
		command_length = 0;
		command_length += sprintf(command + command_length, 
						  		  "git mv boj%d.%s ../%s/boj%d_", 
						          problem_number, language, category, problem_number);

		// filename의 공백을 _로 바꾸어서 입력
		for (int j = 0; filename[j]; ++j) {
			if (filename[j] == '\n') filename[j] = 0;
			else command_length += sprintf(command + command_length, "%c", 
										   file_name[j] == ' ' ? '_' : file_name[j]);
		}

		// .{language} && git commit -m "boj{problem_number} : {file_name} ({link})"
		command_length += sprintf(command + command_length, 
								  ".%s && git commit -m \"boj%d : %s (https://boj.kr/%d)\"\n", 
								  language, problem_number, file_name, problem_number);

		// command를 인자로 넘겨주면서 system 함수 실행
		int ret = system((const char *)command);
	}
	
	return 0;
}