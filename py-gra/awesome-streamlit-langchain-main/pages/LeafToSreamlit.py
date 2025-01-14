import streamlit as st
import streamlit.components.v1 as components

# 读取本地HTML文件
def load_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# 主函数
def main():
    st.title('Streamlit HTML Embedding')

    # 指定本地HTML文件的路径
    html_file_path = './components/test.html'

    # 读取HTML文件
    html_content = load_html_file(html_file_path)

    # 将HTML内容嵌入到Streamlit页面中
    components.html(html_content,height=1000, scrolling=True)

if __name__ == "__main__":
    main()
