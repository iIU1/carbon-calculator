import streamlit as st

st.title("我的第一个在线碳足迹计算器")

st.write("这是我用Python和Streamlit制作的网页！")

electricity = st.number_input(
    "请输入用电量（kWh）",
    min_value=0.0
)

factor = 0.55  # 教学假设排放因子
emission = electricity * factor

st.success(f"对应碳排放量：{emission:.2f} kg CO₂e")