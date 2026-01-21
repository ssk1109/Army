import streamlit as st
import pandas as pd

# 버튼 클릭
button = st.button('버튼을 눌러보세요')

if button:
    st.write(':blue[버튼]이 눌렸습니다 :sparkles:')

# 텍스트 입력
title = st.text_input(
    label='가고 싶은 여행지가 있나요?', 
    placeholder='여행지를 입력해 주세요'
)
st.write(f'당신이 선택한 여행지: :violet[{title}]')

# 텍스트 입력
title = st.text_input(
    label='API Key 입력', 
    type ='password'
)


# 파일 다운로드 버튼
# 샘플 데이터 생성
dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

# 다운로드 버튼 연결
st.download_button(
    label='CSV로 다운로드',
    data=dataframe.to_csv(), 
    file_name='sample.csv', 
    #mime='text/csv'
)

# 체크 박스
agree = st.checkbox('동의 하십니까?')

if agree:
    st.write('동의 해주셔서 감사합니다 :100:')

# 라디오 선택 버튼
mbti = st.radio(
    '당신이 좋아하는 음식은?',
    ('한식', '양식', '없음'))

if mbti == '한식':
    st.write('맛있는 :green[한식]')
elif mbti == '양식':
    st.write('고급진 :red[양식]')
else:
    st.write("더 고민해봐요")

# 선택 박스
food = st.selectbox(
	'당신이 좋아하는 음식은?',
	('한식', '양식', '없음'),
	index = 2    # 기본으로 설정할 선택지. 여기선 '없음'으로 선택됨.
)

if food == '한식':
	st.write('맛있는 :green[한식]')
elif food == '양식':
	st.write('고급진 :red[양식]')
else:
	st.write('더 고민해봐요')

# 다중 선택 박스
options = st.multiselect(
	'당신이 좋아하는 과일은?',
	['망고', '오렌지', '사과', '바나나'],
	['오렌지', '사과']
)

st.write(f'당신의 선택은: :orange[{options}] 입니다.')
