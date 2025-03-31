import base64
import streamlit as st

def sidebar_bg(side_bg):
 
   side_bg_ext = 'png'
 
   st.markdown(
      f'''
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      ''',
      unsafe_allow_html=True,
      )
 
#调用
sidebar_bg('background1.jpg')

def main_bg(main_bg):
    main_bg_ext = "png"
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
 
#调用
main_bg('b2.jpg')
page = st.sidebar.title('电子相册')
page = st.sidebar.radio('',['首页','活动合影'])

def page1():
    st.title("首页")
    st.subheader("电子相册(2027级二班)")
    st.write("")
    st.write("")
    st.write('''
                 时光的胶片在此定格，将欢笑、汗水、成长的痕迹编织成独属于我们的璀璨星河。教室里的奋笔疾书，操场上的肆意奔跑，试卷上晕开的墨迹，运动会上震耳的呐喊……每一帧都是青春最鲜活的注脚。

                 感谢这场盛大的相遇，让我们成为彼此青春的主角。那些共度的晨昏、分享的秘密、碰撞的梦想，早已化作心底最温柔的锚点。纵使未来山海相隔，请记得：你曾是被全班撑腰的少年，是某段故事里不可替代的光。

                 愿此去乘风破浪，仍葆今日赤子热忱；纵踏荆棘之路，亦有同窗岁月熨帖心魂。我们的故事永不写就“终章”，因为每一次奔赴星辰大海的旅程，都是对青春盟约的盛大重逢。''')
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("文段创编：Deepseek")
    st.write("编程实现：马一航")
    st.write("2025 /03 /31")

def page2():
    st.title("活动合影")
    st.subheader("电子相册(2027级二班)")
    st.write("")
    st.write("")
    st.header("初一篮球联赛合影")
    st.subheader("男队(图片)")
    st.write("")
    st.write("")
    st.image("2.jpg")
    st.image("6.jpg")
    st.image("7.jpg")
    st.image("8.jpg")
    st.image("10.jpg")
    st.image("11.jpg")
    st.image("14.jpg")
    st.image("17.jpg")
    st.image("21.jpg")
    st.image("23.jpg")
    st.image("28.jpg")
    st.image("29.jpg")
    st.image("36.jpg")
    st.image("38.jpg")
    st.image("40.jpg")
    st.image("45.jpg")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.subheader("女队(图片)")
    st.image("1.jpg")
    st.image("3.jpg")
    st.image("25.jpg")
    st.image("32.jpg")
    st.image("41.jpg")
    st.image("44.jpg")
    st.image("46.jpg")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("摄影录制：陆星云")
    st.write("图片处理：马一航")
    st.write("编程实现：马一航")
    st.write("2025 /03 /31")
    
    
    
    

    

if page == "首页":
    page1()

if page == "活动合影":
    page2()