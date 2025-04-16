import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 지도 유형 목록
map_types = {
    "행정구역": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/South_Korea_administrative_divisions_map.png/800px-South_Korea_administrative_divisions_map.png",
    "지형도": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/South_Korea_topographic_map_2.png/800px-South_Korea_topographic_map_2.png",
    "위성지도": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/South_Korea_satellite_map.png/800px-South_Korea_satellite_map.png",
}

# 스트림릿 제목
st.title("한반도 백지도 유형 선택")

# 지도 유형 선택
selected_map_type = st.selectbox("지도 유형을 선택하세요:", list(map_types.keys()))

# 선택된 지도 유형에 따라 이미지 표시
st.image(map_types[selected_map_type], caption=selected_map_type)
