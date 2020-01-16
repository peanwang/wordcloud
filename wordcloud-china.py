import numpy as np
import matplotlib.pyplot as plt
import wordcloud
from PIL import Image
import os
import jieba


def __main__():
    # 当前路径
    d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    #读文件
    with open(os.path.join(d, 'china.txt'),encoding='utf-8') as file:
        text = file.read()
    font_path = os.path.join(d, 'SIMYOU.TTF')
    pic = Image.open(os.path.join(d, 'cat.jpg'))
    mask = np.array(pic)

    word_frequent = dict()
    for str in jieba.lcut(text):
        if len(str) != 1:
            if str in word_frequent:
                word_frequent[str] += 1
            else:
                word_frequent[str] = 1
    
    w = wordcloud.WordCloud(font_path = font_path,background_color='white',mask=mask)
    w.generate_from_frequencies(word_frequent)
    
    plt.figure() 
    plt.subplot(1,2,1)
    plt.imshow(pic)
    plt.subplot(1,2,2)
    plt.imshow(w, interpolation="bilinear")
    plt.show()

    w.to_file(os.path.join(d, 'cat.png'))



if __name__ == "__main__":
    __main__()