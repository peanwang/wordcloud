import numpy as np
import matplotlib.pyplot as plt
import wordcloud
import jieba
from PIL import Image
import os


def __main__():
    # 当前路径
    d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    #读文件
    with open(os.path.join(d, 'text.txt')) as file:
        text = file.read()

    w = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
#import matplotlib.pyplot as plt
#plt.imshow(wordcloud, interpolation='bilinear')
#plt.axis("off")

# lower max_font_size
#wordcloud = WordCloud(max_font_size=40).generate(text)
#plt.figure()
#plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")
#plt.show()



if __name__ == "__main__":
    __main__()