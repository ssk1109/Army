# 모듈 파일 import하기
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# 모듈 파일 별명으로 import하기 
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# 모듈 파일 전체 import하기
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# 모듈 파일에서 원하는 method만 import하기
# from theater_module import price, price_morning
# price(5)
# price_morning(60)
# price_soldier(5) # soldier는 import하지 않았기 때문에 실행 x

# 원하는 method만 별명으로 import하기
from theater_module import price_soldier as ps
ps(8)