#rev5-1.chart_hist / tab4(final area) add 

#필요한 모듈 
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import altair as alt
import plotly.express as px 

#csv file load
model1 = pd.read_csv('C:/ChatGPT/0422_pro2_deepfake/history1.csv', index_col=0)
model2 = pd.read_csv('C:/ChatGPT/0422_pro2_deepfake/history2.csv', index_col=0)
model3 = pd.read_csv('C:/ChatGPT/0422_pro2_deepfake/history3.csv', index_col=0)
model4 = pd.read_csv('C:/ChatGPT/0422_pro2_deepfake/history4.csv', index_col=0)
model5 = pd.read_csv('C:/ChatGPT/0422_pro2_deepfake/history5.csv', index_col=0)


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



def main():
    st.set_page_config(initial_sidebar_state="expanded")
    #sidebar -> button 생성 
    with st.sidebar:
        choice = option_menu("MENU", ["Introduction", "Description", "Detector"],
                            icons=[	'caret-right-fill', 'caret-right-fill', 'caret-right-fill'],
                            menu_icon="card-text", default_index=0,
                            styles={
                                "container": {"padding": "4!important", "background-color": '#FFFFFF'},
                                "icon": {"color": "black", "font-size": "25px"},
                                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": '#FFFFFF'},
                                "nav-link-selected": {"background-color": "#72DDCE", "secondaryBackgroundColor":'#FFFFFF'}})
    

    #[Introduction]Tab 설정 
    if choice == "Introduction":
        st.markdown(page_bg_img_first, unsafe_allow_html=True)
        st.markdown(font_dc+'<div style="font-family: Pretendard-Regular; font-size: 100px; font-weight: 900; color: #fafafa; line-height: 100px; letter-spacing: 5px">Deepfake</div>', unsafe_allow_html=True)
        st.markdown(font_dc+'<div style="font-family: Pretendard-Regular; font-size: 100px; font-weight: 900; color: #fafafa; line-height: 70px; letter-spacing: 5px">Detector</div>', unsafe_allow_html=True)
        st.markdown(font_dc+'<div style="font-family: Pretendard-Regular; font-size: 50px; color: #fafafa; letter-spacing: 2px">Mini Project2</div>', unsafe_allow_html=True)
        st.markdown(font_dc+'<div style="font-family: Pretendard-Regular; font-size: 20px; text-align:center; margin-top: 250px; color: #fafafa;">Team : Detective Garfield</div>', unsafe_allow_html=True)
        

    #[Model-Description]Tab 설정
    elif choice == "Description":
        st.markdown(font_dc+'<div style="font-family: Pretendard-Regular; font-size: 40px; font-weight: 900; color: #04B8C4; line-height: 60px; letter-spacing: 2px">Summary</div>', unsafe_allow_html=True)
  
        col1, col2 = st.columns(2)
        with col1:
            data_th = {'Model_No' : ['1', '2', '3', '4', '5'],
                'Accuracy' : ['1.00000', '0.99900', '0.99900', '0.99450', '0.99178'],
                'F1-score' : ['1.00000', '0.99902', '0.99901', '0.99455', '0.99144'],
                'Recall' : ['1.00000', '0.99902', '1.00000', '1.00000', '0.99775']}
            df = pd.DataFrame(data_th)
            st.dataframe(data_th)
    
        with col2:
            # 숫자열로 변환
            df[['Accuracy', 'F1-score', 'Recall']] = df[['Accuracy', 'F1-score', 'Recall']].apply(pd.to_numeric)
            
            hist_fig = plt.figure(figsize=(8,7))
            hist_ax = hist_fig.add_subplot(111)
            sub_df = df[['Accuracy', 'F1-score', 'Recall']]
            sub_df.plot.bar(alpha = 0.8, ax = hist_ax, title = 'chart', color=('skyblue', 'lightgreen', 'salmon'))
            hist_ax.set_xticklabels(['no1', 'no2', 'no3', 'no4', 'no5'])  # x 축 레이블 설정
            hist_ax.set_ylim(0.98, 1.0)  # y 축 범위 설정
            hist_ax.set_yticks([0.98, 1.0])  # y 축 눈금 설정
            st.pyplot(hist_fig)        
        
        #chart별 tab 분리 
        tab1, tab2, tab3 = st.tabs(['History', 'Confusion matrix', 'Final'])

        #[line_chart]
        with tab1:
            st.subheader('Model1')
            st.line_chart(pd.DataFrame(model1, columns=['loss', 'accuracy', 'val_loss', 'val_accuracy']))
            st.subheader('Model2')
            st.line_chart(pd.DataFrame(model2, columns=['loss', 'accuracy', 'val_loss', 'val_accuracy']))
            st.subheader('Model3')
            st.line_chart(pd.DataFrame(model3, columns=['loss', 'accuracy', 'val_loss', 'val_accuracy']))
            st.subheader('Model4')
            st.line_chart(pd.DataFrame(model4, columns=['loss', 'accuracy', 'val_loss', 'val_accuracy']))
            st.subheader('Model5')
            st.line_chart(pd.DataFrame(model5, columns=['loss', 'accuracy', 'val_loss', 'val_accuracy']))

        #[confusion_matrix]
        with tab2:
            #model1,2의 confusion matrix 
            col3, col4 = st.columns(2)  

            with col3:
                st.subheader('Model1')
                conf_matrix = np.array([[1021, 0],
                                        [0, 979]])
                plt.figure(figsize=(6, 6)) #그림size
                sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False, square=True)  #annot: 숫자 표시, fmt=d: 정수표현, cbar: 측면에 나타나는 colorbar, square: 행,열 크기비례
                plt.title('Confusion Matrix')
                plt.xlabel('Predicted')
                plt.ylabel('Actual')
                st.pyplot(plt)
 
            with col4:
                st.subheader('Model2')
                conf_matrix = np.array([[981, 1],
                                        [1, 1017]])
                plt.figure(figsize=(6, 6))
                sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False, square=True)
                plt.title('Confusion Matrix')
                plt.xlabel('Predicted')
                plt.ylabel('Actual')
                st.pyplot(plt)

            #model3,4의 confusion matrix 
            col5, col6 = st.columns(2)  

            with col5:
                st.subheader('Model3')
                conf_matrix = np.array([[985, 2],
                                        [0, 1013]])
                plt.figure(figsize=(6, 6))
                sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False, square=True)  
                plt.title('Confusion Matrix')
                plt.xlabel('Predicted')
                plt.ylabel('Actual')
                st.pyplot(plt)
    
            with col6:
                st.subheader('Model4')
                conf_matrix = np.array([[986, 11],
                                        [0, 1003]])
                plt.figure(figsize=(6, 6))
                sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False, square=True)
                plt.title('Confusion Matrix')
                plt.xlabel('Predicted')
                plt.ylabel('Actual')
                st.pyplot(plt)

            #model5의 confusion matrix 
            col7, col8 = st.columns(2)  

            with col7:
                st.subheader('Model5')
                conf_matrix = np.array([[4331, 60],
                                        [9, 3994]])
                plt.figure(figsize=(6, 6)) 
                sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False, square=True)  
                plt.title('Confusion Matrix')
                plt.xlabel('Predicted')
                plt.ylabel('Actual')
                st.pyplot(plt)
 
        with tab3:
            st.subheader('History')
            st.line_chart(pd.DataFrame(model1, columns=['loss', 'accuracy', 'val_loss', 'val_accuracy']))
            st.subheader('Confusion matrix')
            conf_matrix = np.array([[1021, 0],
                                    [0, 979]])
            plt.figure(figsize=(6, 6)) #그림size
            sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False, square=True)  #annot: 숫자 표시, fmt=d: 정수표현, cbar: 측면에 나타나는 colorbar, square: 행,열 크기비례
            plt.xlabel('Predicted')
            plt.ylabel('Actual')
            st.pyplot(plt)
            st.subheader('Grad-CAM')
            st.text('patch-size=20')
            st.image('C:/ChatGPT/0422_pro2_deepfake/all_patchsize20.png', use_column_width = True)
            st.text('patch-size=50')
            st.image('C:/ChatGPT/0422_pro2_deepfake/crop_patchsize50.png', use_column_width = True)
            


    #[Model]Tab 설정 
    elif choice == "Detector":  #가연's back-end area 
        st.markdown(font_dc+'<div style="font-family: Pretendard-Regular; font-size: 40px; font-weight: 900; color: #04B8C4; line-height: 60px; letter-spacing: 2px">Deepfake Detector</div>', unsafe_allow_html=True)
        st.text_input(' ')
        st.file_uploader('🎞️ Upload your video 🎞️')
    

if __name__ == '__main__':
    main()