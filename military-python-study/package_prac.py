# package : 여러 모듈을 모아놓은 집합
# import travel.thailand # thailand 위치에 오는 것은 다른 모듈 or 패키지, class는 올 수 없음
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# __all__ : from 패키지명 import * 을 사용하기 위해 개발자가 모듈의 공개 범위를 설정하는 것. 각 모듈의 정상작동 하는지 확인할 때


# 패키지 & 모듈 위치 확인
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))


# pip install : 이미 만들어진 패키지 설치. 
# pypi : 패키지 탐색 사이트
# pip list : 다운된 패키지 확인
# pip install --upgrade 패키지명 : 특정 패키지 업데이트
# pip uninstall 패키지명 : 패키지 삭제


# 내장함수
# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# import random
# print(dir(random))
# lst = [1,2,3]
# print(dir(lst))
# etc..


# 외장함수
# random

# glob : 경로 내의 폴터 / 파일 목록 조회
# import glob
# print(glob.glob("*.py")) # 확장자자 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현제 디렉토리

# time : 시간 관련 함수
# import time
# print(time.strftime("%y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())
# timedelta : 두 날짜 사이 간격 측정
# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print(f"{today}의 100일 후는 {today + td}")