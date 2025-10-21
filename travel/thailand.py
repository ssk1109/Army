class ThailandPackage:
    def detail(self):
        print("[태국 3박 4일 50만원]")

if __name__ == "__main__":
    print("thailand 모듈을 직접 실행") # thailand.py에서 직접 실행 시 이 구문 출력
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("thailand 외부에서 모듈 호출") # name 정보를 사용하여 이 파일 내에서 사용하는 지 or 외부에서 사용하는 지 확인가능

