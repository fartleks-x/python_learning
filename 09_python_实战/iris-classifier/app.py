# 1. 调试技巧
import streamlit as st

# 打印调试信息（在终端查看）
print("调试信息")

# 使用st.write显示调试信息
st.write("变量值:", variable)

# 2. 性能监控
import time

start_time = time.time()
# 执行一些操作
st.write(f"执行时间: {time.time() - start_time:.2f}秒")

# 3. 错误处理
try:
    # 可能出错的代码
    result = 10 / 0
except Exception as e:
    st.error(f"发生错误: {str(e)}")