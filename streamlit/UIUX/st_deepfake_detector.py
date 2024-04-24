#rev5. font(자간, 행간, 글씨체, 크기.. design)

import streamlit as st
from streamlit_option_menu import option_menu

#CSS클래스 정의
# 폰트 
font_dc = """
    <style>
    @font-face {
    font-family: 'Pretendard-Regular';
    src: url('https://cdn.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff') format('woff');
    font-weight: 400;
    font-style: normal;
    }
    </style>
    """

# 배경 이미지 CSS
page_bg_img_first = f"""
    <style>
    .stApp {{
        background-image: url("https://i.postimg.cc/jjVrkT31/Team-Detective-Garfield.png");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: local;
        color: #000000;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}
    </style>
"""

page_bg_img_second = f"""
    <style>
    .stApp {{
        background-image: url("https://i.postimg.cc/jqMxsLj0/circle-x.png"); 
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: local;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}
    </style>
"""



def main():
    st.set_page_config(initial_sidebar_state="expanded")
    #sidebar -> button 생성 
    with st.sidebar:
        choice = option_menu("MENU", ["Introduction", "Model-Description", "Model"],
                            icons=[	'caret-right-fill', 'caret-right-fill', 'caret-right-fill'],
                            menu_icon="card-text", default_index=0,
                            styles={
                                "container": {"padding": "4!important", "background-color": '#FFFFFF'},
                                "icon": {"color": "black", "font-size": "25px"},
                                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": '#FFFFFF'},
                                "nav-link-selected": {"background-color": "#72DDCE", "secondaryBackgroundColor":'#FFFFFF'}})
    

    #[Introduction]Tab 설정 v
    if choice == "Introduction":
        st.markdown(page_bg_img_first, unsafe_allow_html=True)
        st.markdown(font_dc+'<div style="font-family: Pretendard-Regular; font-size: 100px; font-weight: 900; color: #fafafa; line-height: 100px; letter-spacing: 5px">Deepfake</div>', unsafe_allow_html=True)
        st.markdown(font_dc+'<div style="font-family: Pretendard-Regular; font-size: 100px; font-weight: 900; color: #fafafa; line-height: 70px; letter-spacing: 5px">Detector</div>', unsafe_allow_html=True)
        st.markdown(font_dc+'<div style="font-family: Pretendard-Regular; font-size: 50px; color: #fafafa; letter-spacing: 2px">Mini Project2</div>', unsafe_allow_html=True)
        st.markdown(font_dc+'<div style="font-family: Pretendard-Regular; font-size: 20px; text-align:center; margin-top: 250px; color: #fafafa;">Team : Detective Garfield</div>', unsafe_allow_html=True)
        

    #[Model-Description]Tab 설정    background_gradient()
    elif choice == "Model-Description":
        st.markdown(font_dc+'<div style="font-family: Pretendard-Regular; font-size: 40px; font-weight: 900; color: #fafafa; line-height: 60px; letter-spacing: 2px">Summary</div>', unsafe_allow_html=True)
        
        #그래프 영역 layout 
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("정확도")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        with col2:
            st.header("재현성")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        with col3:
            st.header("F1-score")
            st.image("https://static.streamlit.io/examples/cat.jpg")
   
        st.markdown(font_dc+'<div style="font-family: Pretendard-Regular; font-size: 40px; font-weight: 900; color: #fafafa; line-height: 60px; letter-spacing: 5px">1</div>', unsafe_allow_html=True)

        st.markdown(page_bg_img_second, unsafe_allow_html=True)

    #[Model]Tab 설정 
    elif choice == "Model":  #가연's back-end area 
        st.markdown(font_dc+'<div style="font-family: Pretendard-Regular; font-size: 40px; font-weight: 900; color: #fafafa; line-height: 60px; letter-spacing: 2px">Model Implementation</div>', unsafe_allow_html=True)
        st.text_input(' ')
        st.file_uploader('🎞️ Upload your video 🎞️')
        st.markdown(page_bg_img_second, unsafe_allow_html=True)



if __name__ == '__main__':
    main()