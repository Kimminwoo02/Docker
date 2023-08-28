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