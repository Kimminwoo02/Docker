from random import randint

min_number = int(input('Please enter the min number: '))
max_number = int(input('Please enter the max number: '))

if (max_number < min_number): 
  print('Invalid input - shutting down... Docker Rm Container'
  print('Docker -rm tag')
else:
  rnd_number = randint(min_number, max_number)
  print(rnd_number)

print('image check -> docker image inspect')
print('docker cp- 파일 복사 dummy에 있는 파일을 모두 복사한다.' )
print('docker cp dummy/.  컨테이너_이름:/컨테이너_내부경로(:/test)' )
print('docker cp 컨테이너_이름 로컬폴더')
print('위 커멘드로 컨테이너 내부를 확인해볼 수 있다. 구체적인 파일을 입력해도 된다.')

