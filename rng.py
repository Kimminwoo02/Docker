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


print('docker run --name 을 통한 컨테이너 이름 지정')
print('docker name:tag'    ,' 태그에는 버전이나 다른 구성이 있는경우 이름과 태그를 결합할 수 있다.')

print('도커파일 공유 방법 : 도커허브에 직접 만든 도커파일을 업로드하여 공유할 수 있다. 이렇게 사용하면 빌드할 필요가 없다. ')
print('Dockerfile Push : docker push IMAGE_NAME      이미지는 로컬에 존재하지 않는 저장소를 참조하고 있을 경우, 이미지에 이름을 지정하면 된다.')
print('docker tag node-demo:latest acdemind/node-hello-world     : tag 뒤에는 이전에 사용한 이름:태그 도커아이디/사용할_이름' )
print('Dockerfile Pull : docker pull IMAGE_NAME ')