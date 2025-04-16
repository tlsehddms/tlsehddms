import streamlit as st

# 저작권 걱정 없는 한반도 백지도를 위한 이미지 URL
map_types = {
    "행정구역": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/South_Korea_administrative_divisions_identity_map.svg/2000px-South_Korea_administrative_divisions_identity_map.svg.png",
    "지형도": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Topographic_Map_of_Korea.svg/2000px-Topographic_Map_of_Korea.svg.png",
    "위성지도": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/South_Korea_satellite_photo.png/800px-South_Korea_satellite_photo.png",
}

# 스트림릿 제목
st.title("한반도 백지도 유형 선택")

# 지도 유형 선택
selected_map_type = st.selectbox("지도 유형을 선택하세요:", list(map_types.keys()))

# 선택된 지도 유형에 따라 이미지 표시
st.image(map_types[selected_map_type], caption=selected_map_type)
