import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.savefig("plot.png")

# 가상환경 생성: python -m venv 가상환경명
# 가상환경 실행: 윈도우: 가상환경명\Script\activate.bat
#               리눅스/맥: source 가상환경명/bin/activate

# vs 내의 python script를 venv와 연결: view\command palette\python select interpreter 검색/설치한 가상환경 선택 or 가상환경 경로 입력

# codespace는 리눅스 + gui 부재로 matplotlib를 정상적으로 실행할 수 없기에 결과를 이미지로 저장하여 확인
