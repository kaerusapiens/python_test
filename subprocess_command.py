import subprocess

# 'ls' 명령어로 파일 목록을 출력하고, 그 결과를 'grep'을 사용하여 필터링
result = subprocess.run('ls -al | grep ".py"', shell=True, capture_output=True, text=True)

# 출력 확인
print(result.stdout)  # 명령어의 표준 출력
print()


#shell injection을 방어할수 있는방법
p1 = subprocess.Popen(['ls','-al'],stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep','.py'],stdin=p1.stdout,stdout=subprocess.PIPE) 

# p1의 표준 출력을 닫음 (p1의 출력 스트림을 더 이상 사용하지 않겠다고 알림)
p1.stdout.close()
output = p2.communicate()[0] #(stdout, stderr) 라서 표준을 추출하기 위한 방법
print(output)
