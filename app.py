import streamlit as st    
import requests    
import jieba    
from collections import Counter    
from pyecharts import options as opts    
from pyecharts.charts import WordCloud, Line, Bar, Scatter, Pie  
  
# 设计文本输入框, 用户输入文章URL    
url = st.text_input('请输入文章URL')    
  
# 请求URL抓取文本内容    
response = requests.get(url)    
content = response.text    
  
# 对文本分词, 统计词频    
seg_list = jieba.cut(content)    
word_count = Counter(seg_list)    
  
# 展示词频排名前20的词汇    
top20_words = word_count.most_common(20)    
st.write('词频排名前20的词汇：')    
for word, freq in top20_words:    
    st.write(f'{word}: {freq}')    
  
# 使用pyecharts绘制词云    
words = [('word', freq) for word, freq in word_count.items()]    
wordcloud = (    
    WordCloud()    
    .add("", words, word_size_range=[20, 100], shape='triangle')    
    .set_global_opts(title_opts=opts.TitleOpts(title="文章词云"))    
)    
st.write(wordcloud)    
  
# 构建 streamlit 的 st.sidebar 进行图型筛选, 至少7种图型   
chart_type = st.sidebar.selectbox('图型筛选', ['词云图', '折线图', '柱状图', '散点图', '饼图', '地图', '其他图型'])    
  
if chart_type == '折线图':    
    # 绘制折线图的代码    
    line_chart = Line()  
    line_chart.add_xaxis(['周一', '周二', '周三', '周四', '周五', '周六', '周日'])  
    line_chart.add_yaxis('销售额', [120, 200, 150, 80, 70, 110, 130])  
    line_chart.set_global_opts(title_opts=opts.TitleOpts(title="折线图示例"))  
    st.write(line_chart)  
      
elif chart_type == '柱状图':    
    # 绘制柱状图的代码    
    bar_chart = Bar()  
    bar_chart.add_xaxis(['水果', '数量'])  
    bar_chart.add_yaxis('苹果', [5, 20, 36, 10, 75, 90])  
    bar_chart.add_yaxis('橙子', [15, 30, 46, 20, 65, 80])  
    bar_chart.set_global_opts(title_opts=opts.TitleOpts(title="柱状图示例"))  
    st.write(bar_chart)  
      
elif chart_type == '散点图':    
    # 绘制散点图的代码    
    scatter_chart = Scatter()  
    scatter_chart.add_xaxis([1, 2, 3, 4, 5])  
    scatter_chart.add_yaxis('销售额', [200, 150, 300, 250, 180])  
    scatter_chart.set_global_opts(title_opts=opts.TitleOpts(title="散点图示例"))  
    st.write(scatter_chart)  
      
elif chart_type == '饼图':    
    # 绘制饼图的代码    
    pie_chart = Pie()  
    pie_chart.add("", [("苹果", 30), ("橙子", 20), ("香蕉", 15), ("葡萄", 25), ("其他", 20)])  
    pie_chart.set_global_opts(title_opts=opts.TitleOpts(title="饼图示例"))  
    st.write(pie_chart)  
      
