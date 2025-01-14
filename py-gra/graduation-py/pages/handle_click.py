import streamlit as st

def handle_click():
    # 这里放置按钮点击后要执行的代码
    st.write("按钮已点击！")



def main():
    st.title("Streamlit 按钮示例")


    # 创建一个按钮，点击时调用 handle_click 函数
    if st.button("点击我"):
        handle_click()

if __name__ == "__main__":
    main()
