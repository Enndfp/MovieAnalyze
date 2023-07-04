## 项目名称

影视分析系统

## 项目简介

该项目是一个基于 Python 和 PyQt5 的影视作品分析应用程序。它提供了以下功能：加载电影数据、显示电影信息、生成词云图、显示热力图以及展示评分分布的饼状图。通过该应用程序，用户可以查看电影的基本信息、电影简介、评分情况以及进行数据可视化分析。

## 功能特点

- 加载电影数据：应用程序可以从预定义的数据文件加载电影数据，该数据包含电影的标题、年份、地区、评分、评价人数和电影简介等信息。
- 显示电影信息：应用程序提供一个下拉框，用户可以从中选择电影，然后显示选中电影的相关信息，包括年份、地区、评分、评价人数和电影简介等。
- 生成词云图：应用程序可以根据选中电影的简介生成词云图，使用结巴分词库对文本进行分词，并根据词频生成词云图展示。
- 显示热力图：应用程序可以生成电影数据的相关性矩阵，并以热力图的形式展示相关性。用户可以通过热力图了解电影数据中各个属性之间的相关程度。
- 展示评分分布的饼状图：应用程序可以统计电影数据中各个评分的数量，并以饼状图的形式展示评分分布情况，帮助用户了解电影评分的分布情况。

## 技术选型

- Python: 作为主要的编程语言，用于开发整个应用程序的逻辑和功能。
- PyQt5: 作为应用程序的图形用户界面框架，用于创建用户界面和交互。
- requests: 用于发送 HTTP 请求获取网页内容。
- re: 用于使用正则表达式匹配和提取电影信息。
- csv: 用于将电影数据存储到 CSV 文件中。
- pandas: 用于处理和分析电影数据。
- seaborn 和 matplotlib: 用于生成热力图和评分分布的饼状图。
- jieba 和 wordcloud: 用于生成电影简介的词云图。

## 项目展示

- **主页效果展示图**

![image-20230704191720361](https://enndfp-1317534445.cos.ap-guangzhou.myqcloud.com/img/image-20230704191720361.png)

- **电影数据信息图**

![image-20230704191818039](https://enndfp-1317534445.cos.ap-guangzhou.myqcloud.com/img/image-20230704191818039.png)

- **数据获取信息提示图**

![image-20230704191912748](https://enndfp-1317534445.cos.ap-guangzhou.myqcloud.com/img/image-20230704191912748.png)

- **相关性矩阵热力图**

![image-20230704191946721](https://enndfp-1317534445.cos.ap-guangzhou.myqcloud.com/img/image-20230704191946721.png)

- **《熔炉》电影词云图**

![image-20230704192032765](https://enndfp-1317534445.cos.ap-guangzhou.myqcloud.com/img/image-20230704192032765.png)

- **评分分布饼状图**

![image-20230704192056419](https://enndfp-1317534445.cos.ap-guangzhou.myqcloud.com/img/image-20230704192056419.png)

## 使用说明

​	1.安装所需依赖库：

```shell
pip install requests PyQt5 pandas seaborn matplotlib jieba wordcloud
```

2. 克隆或下载项目代码到本地。

3. 运行 `MainWindow.py` 文件启动应用程序。

4. 应用程序界面中，通过下拉框选择电影，查看电影信息和简介。

5. 点击 "显示词云图" 按钮生成选中电影的词云图。

6. 点击 "显示热力图" 按钮生成电影数据的相关性矩阵热力图。

7. 点击 "显示评分分布" 按钮生成评分分布的饼状图。

请注意：为了使应用程序正常运行，确保已准备好数据文件 "MoviesData.csv"（包含电影数据），以及字体文件 "SimHei.ttf"（用于词云图的中文字体显示）并放置在相应的文件路径下。

**注意：此处假设你已经准备好了数据文件和字体文件。**

## 示例代码

可以参考以下示例代码来使用项目中的功能：

```python
pythonCopy codefrom PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.load_data()
    window.populate_combo_box()
    app.exec_()
```

该代码片段创建了一个 `MainWindow` 对象并运行应用程序，加载电影数据并将电影选项添加到下拉框中，然后启动应用程序界面。

## 致谢

感谢使用影视作品分析应用程序！如有任何问题或反馈，请联系作者。

如果你喜欢这个项目，请给一个星星⭐支持并在GitHub上关注该项目。

欢迎访问 [GitHub 项目地址](https://github.com/Enndfp/MovieAnalyze) 获取最新代码和更多信息。

作者：Enndfp

邮箱：enndfp@163.com
