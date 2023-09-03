print('Volume')
print('이미지는 Read-only 이다. 실행 중인 애플리케이션은 편집할 수 없다.')
print('영구적인 데이터를 실행중인  컨테이너에서 가져와서 저장해야한다. 이럴 때 볼륨을 사용한다.')

print('볼륨은 하드 드라이브에 존재하여 사용가능하거나 컨테이너로 매핑되는 것을 의미한다. 즉 볼륨은 도커가 인식하는 컴퓨터에 있는 폴더')


print('볼륨의 종류')
print('익명의 볼륨')
print('named 볼륨')
print('익명의 볼륨은 컨테이너가 존재하는 동안에만 실제로 존재한다. 즉 컨테이너가 종료되면 데이터가 사라진다.')
print('named 볼륨은 컨테이너가 종료되어도 제거되지 않는다. 즉 영구적인 데이터나 중요한 데이터를 저장하는데 적합하다.')
print('사용방법: docker run 의 옵션으로 이름:볼륨의 경로')

print('익명의 볼륨은 하나의 컨테이너와 밀접하게 연관되었다.')
print('named 볼륨은 하나의 컨테이너에만 연결되지는 않는다.')

print('바인드 마운트')
print('도커애 의해 관리되는 볼륨의 위치, 즉 호스트 머신의 파일 시스템 상의 볼륨이 어디에 있는지 실제로 알지 못하지만 바인드 마운트의 경우 그 위치를 알고 있다.')
print('그래서 영구적이고 편집 가능한 데이터에 적합하다. ')
print('named볼륨의 경우 호스트 머신의 어디에 저장되는지 모르기 때문에 편집에 적합하지 않다.')
print('run 옵션으로 절대경로를 입력한다.')
print('익명 볼륨과 바인드 마운트는 하나의 핵심 개념을 공유한다')

print('바인드 마운트의 경우 로컬환경에서 데이터의 변경이 있으면 바로 컨테이너에 반영된다.')
# 정리
print('익명의 볼륨 : 컨테이너에 연결된 볼륨으로 컨테이너가 제거되면 같이 제거된다. 따라서 컨테이너 간의 데이터를 공유할 수 없다.')
print('하지만 도커파일의 볼륨으로 생성되거나 -v로 생성된 익명 볼륨은 컨테이너에 존재하는 특정 데이터를 잠그는데 유용하다. 즉 데이터가 다른 모듈에 의해 덮어쓰여지는 것을 방지, 시간을 절약하는데 유용' )

print('Named 볼륨')
print('-v 이후에 이름을 지정한다. 특정 컨테이너에 연결되어 있지 않다. 여러 컨테이너 간의 데이터 공유가 가능하다. ')

print('바인드 마운트')
print('특정 컨테이너에 국한되지 않는다.')


print(' 읽기전용 볼륨')
print(' 바인드 마운트는 로컬의 데이터를 컨테이너 내부에서 변경할 수 없도록 해야한다. 이를 위해 옵션으로 ro를 줄 수 있다.')

print(' 바인드 마운트는 로컬의 데이터를 컨테이너 내부에서 변경할 수 없도록 해야한다. 이를 위해 옵션으로 ro를 줄 수 있다.')


print('docker volume inspect feedback 을 통해 볼륨의 정보를 볼 수 있다. 또한 volume rm 을 통해 볼륨을 제거할 수 있다.')


print('DockerFile은 git과 마찬가지로 ignore가 존재하고 컨테이너화를 원치 않는 요소를 추가할 수 있다.')

# 인수와 환경변수
print('ENV를 통한 환경변수 주입이 가능하다. ENV PORT 80 과 같은 형식으로 환경변수 셋팅이 가능하다.')
print('ARG를 통해서 동적으로 환경변수를 설정할 수 있다.')

print('코드내에서  localhost 를 도커가 이해할 수 있는 특별한 도메인으로 대체해야한다.')
print('host.docker.internal 이 도메인은 도커에 의해 인식된다. 도커가 이해하고 있고 도커 컨테이너 내부에서 호스트 머신의 IP 주소로 변환된다.') 
print('내부적으로 이 명령은 로컬 호스트 머신의 IP주소로 변환된다.')