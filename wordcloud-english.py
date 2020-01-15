import numpy as np
import matplotlib.pyplot as plt
import wordcloud
from PIL import Image
import os



def __main__():
    # 当前路径
    d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    #读文件
    with open(os.path.join(d, 'English.txt'),encoding='utf-8') as file:
        text = file.read()
    font_path = os.path.join(d, 'GABRWFFR.TTF')
    pic = Image.open(os.path.join(d, 'fish.jpg'))
    mask = np.array(pic)
    # create coloring from image
    pic_color = wordcloud.ImageColorGenerator(mask)

    w = wordcloud.WordCloud(font_path = font_path,background_color='white',mask=mask,
                    contour_width=3, contour_color="blue")
    w.generate(text)
    #recolor wordcloud
    w.recolor(color_func=pic_color)     
    
    plt.figure() 
    plt.subplot(1,2,1)
    plt.imshow(pic)
    plt.subplot(1,2,2)
    plt.imshow(w, interpolation="bilinear")
    plt.show()

    w.to_file(os.path.join(d, 'pic.png'))



if __name__ == "__main__":
    __main__()