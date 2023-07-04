import os
import jieba
from wordcloud import WordCloud, STOPWORDS
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QTextEdit, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DATA_FILE_PATH = "data/MoviesData.csv"
FONT_PATH = "fonts/SimHei.ttf"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.movies = []  # 存储电影数据的列表
        self.current_movie = None  # 当前选中的电影

        self.setWindowTitle("影视作品分析")
        self.setGeometry(650, 200, 600, 700)

        # 创建下拉框
        self.combo_box = QComboBox(self)
        self.combo_box.currentIndexChanged.connect(self.on_movie_selected)
        self.combo_box.setGeometry(20, 20, 300, 30)

        # 创建文本编辑框
        self.text_reviews = QTextEdit(self)
        self.text_reviews.setGeometry(20, 70, 560, 150)
        self.text_reviews.setReadOnly(True)

        # 创建按钮 - 显示热力图
        self.button_heatmap = QPushButton("显示热力图", self)
        self.button_heatmap.setGeometry(20, 260, 120, 30)
        self.button_heatmap.clicked.connect(self.show_heatmap)

        # 创建按钮 - 显示词云图
        self.button_wordcloud = QPushButton("显示词云图", self)
        self.button_wordcloud.setGeometry(250, 260, 120, 30)
        self.button_wordcloud.clicked.connect(self.show_wordcloud)

        # 创建按钮 - 显示评分分布
        self.button_pie_chart = QPushButton("显示评分分布", self)
        self.button_pie_chart.setGeometry(460, 260, 120, 30)
        self.button_pie_chart.clicked.connect(self.show_pie_chart)

        # 创建标签 - 图像展示区域
        self.label_visualization = QLabel(self)
        self.label_visualization.setGeometry(20, 320, 560, 360)
        self.label_visualization.setAlignment(Qt.AlignCenter)

        self.show()

    def load_data(self):
        # 从文件加载数据
        with open(DATA_FILE_PATH, "r", encoding="UTF-8") as file:
            data = file.readlines()

        # 解析数据行并存储到movies列表中
        for line in data[1:]:
            line = line.strip().split(",")
            movie = {
                "title": line[0],
                "year": line[1],
                "region": line[2],
                "score": float(line[3]),
                "num_of_ratings": int(line[4]),
                "summary": line[5][:-1]
            }
            self.movies.append(movie)

    def populate_combo_box(self):
        # 向下拉框添加电影选项
        for movie in self.movies:
            self.combo_box.addItem(movie["title"])

    def on_movie_selected(self, index):
        # 当下拉框的选项改变时触发该函数
        self.current_movie = self.movies[index]
        self.show_reviews()
        self.label_visualization.hide()

    def show_reviews(self):
        # 显示电影的相关信息和简介
        movie = self.current_movie
        review_text = f"年份: {movie['year']}\n地区: {movie['region']}\n评分: {movie['score']}\n" \
                      f"评价人数: {movie['num_of_ratings']}\n电影简介: {movie['summary']}"
        self.text_reviews.setPlainText(review_text)

    def show_wordcloud(self):
        # 显示电影的词云图
        movie = self.current_movie
        summary = movie["summary"]
        word_list = jieba.lcut(summary)  # 使用结巴分词库进行分词

        # 创建词云对象
        wordcloud = WordCloud(
            font_path=FONT_PATH,
            width=600,
            height=400,
            background_color="white",
            stopwords=STOPWORDS,
            repeat=True,
            max_words=32
        ).generate(" ".join(word_list))

        # 保存词云图
        folder_path = "wordcloud"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, f"{movie['title']}.png")
        wordcloud.to_file(file_path)

        # 显示词云图
        pixmap = QPixmap(file_path)
        self.label_visualization.setPixmap(pixmap)
        self.label_visualization.setScaledContents(True)
        self.label_visualization.show()

    def show_heatmap(self):
        # 显示热力图
        # 设置中文字体为SimHei
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 显示负号
        plt.rcParams['axes.unicode_minus'] = False

        # 设置图形大小
        plt.figure(figsize=(4, 4))

        # 创建DataFrame对象
        df = pd.DataFrame(self.movies)

        # 删除非数值列
        df_numeric = df.drop(['title', 'region', 'summary'], axis=1)
        df_numeric = df_numeric.rename(columns={'year': '年份', 'score': '评分', 'num_of_ratings': '评价人数'})
        df_corr = df_numeric.corr()

        # 绘制相关性矩阵热力图
        sns.heatmap(df_corr, annot=True, cmap='coolwarm')
        plt.title('相关性矩阵热力图')
        # 保存热力图
        folder_path = "heatmap"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, "heatmap.png")
        plt.savefig(file_path)
        plt.clf()

        # 显示热力图
        pixmap = QPixmap(file_path)
        self.label_visualization.setPixmap(pixmap)
        self.label_visualization.setScaledContents(True)
        self.label_visualization.show()

    def show_pie_chart(self):
        # 显示评分分布的饼状图
        # 设置中文字体为SimHei
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 统计评分的数量
        rating_counts = {}
        for movie in self.movies:
            rating = movie['score']
            if rating in rating_counts:
                rating_counts[rating] += 1
            else:
                rating_counts[rating] = 1

        # 绘制饼状图
        labels = list(rating_counts.keys())
        counts = list(rating_counts.values())

        plt.figure(figsize=(4, 4))
        plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
        plt.title('评分分布')

        # 保存饼状图
        folder_path = "pie_chart"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, "pie_chart.png")
        plt.savefig(file_path)
        plt.clf()

        # 显示饼状图
        pixmap = QPixmap(file_path)
        self.label_visualization.setPixmap(pixmap)
        self.label_visualization.setScaledContents(True)
        self.label_visualization.show()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.load_data()
    window.populate_combo_box()
    app.exec_()
