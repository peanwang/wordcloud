# 一：Abstract
使用Python制作词云，需要wordcloud，PIL,numpy，matplotlib库。如果要制作中文词云，还需要jieba库。本篇blog介绍wordcloud库和英文词云，中文词云的制作。代码在[github](https://github.com/peanwang/wordcloud)上

# 二：	WordCloud
wordcloud库把词云当作一个WordCloud对象,制作词云并保存都需要WordCloud对象。我个人觉得需要设置的属性为：font_path,mask，background_color
```python
w = wordcloud.WordCloud()
width 宽度
height 高度
min_font_size 词云中字体最小字号
max_font_size  词云中字体最大字号
font_step    字体字号的步进间隔
font_path     字体文件路径
max_words     显示单词最大数量
stop_words   指定词云不显示了列表
mask        词云形状(后面介绍设置方法)
background_color  词云颜色
stopword 设置需要屏蔽的词，如果为空，则使用内置的STOPWORDS 其实是个set
repeat : bool, default=False   单词是否能重复直到满足max_word(显示单词最大数量)
```

# 三 生成词云函数
因为英文按照单词间的空格就可以分词，所以可以直接根据文本分词。但中文不行，所以要使用
jieba库先分词。所以我推荐英文词云使用w.generate函数，中文词云先用jieba分词，再构造单词频率字典，使用w.generate_from_frequencies函数。
```python
# 根据text生成词云
w.generate(text)
```

根据频率生成词云
```python
#frequencies是一个字典  {'word':出现次数}
w.generate_from_frequencies(frequencies) 
```

# 四：设置mask
mask需要一个ndarray对象
```python
import numpy as np
from PIL import Image
pic = np.array(Image.open('path'))
```

# 五：改变词云每个单词颜色
下面是根据图片颜色分布改变单词颜色
```python
# 按图片的颜色分布
from wordcloud import ImageColorGenerator

img = np.array(Image.open('path'))
# create coloring from image
img_color = ImageColorGenerator(img)

#recolor wordcloud
w.recolor(color_func=img_color) 
```
定制颜色(来自官网的例子)
```python
//灰色
def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)
    
 w.recolor(color_func=grey_color_func,random_state=3) 
```
还可以定制每个单词显示什么颜色，但是要写一个单词映射到颜色的类，官网有例子，我觉得太麻烦了，就没看
# 六：保存词云至文件
建议使用wordcloud的这个函数保存，而不是matplotlib库保存。因为matplotlib保存的图片会使图片模糊，清晰要设置参数，麻烦，wordcloud保存的是最清晰的。
```python
w.to_file(filename) 
```
# 七：中文词云
制作中文词云，一定要指定字体。
使用jieba分词得到的结果，可以直接构造单词频率字典，如下。再使用w.generate_from_frequencies,爽歪歪
```python
word_frequent = dict()
for str in jieba.lcut(text):
	if str in word_frequent:
		word_frequent[str] += 1
    else:
        word_frequent[str] = 1
w.generate_from_frequencies(word_frequent) 
```
# 八：英文词云
英文材料来自[heart attract](http://lunwendata.com/thesis/2008/21613.html)
```python
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
                    ")
    w.generate(text)
    #recolor wordcloud
    w.recolor(color_func=pic_color)     
    
    plt.figure() 
    plt.subplot(1,2,1)
    plt.imshow(pic)
    plt.subplot(1,2,2)
    plt.imshow(w, interpolation="bilinear")
    plt.show()

    w.to_file(os.path.join(d, 'fish.png'))



if __name__ == "__main__":
    __main__()
```
![fish.jpg](https://github.com/peanwang/wordcloud/blob/master/fish.jpg)
![fish.png](https://github.com/peanwang/wordcloud/blob/master/fish.png)
# 九：中文词云
中文材料来自[中国共产党第十九届中央纪律检查委员会第四次全体会议公报](http://fanfu.people.com.cn/n1/2020/0115/c64371-31550082.html)
```python
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

```
![cat.jpg](https://github.com/peanwang/wordcloud/blob/master/cat.jpg)
![cat.png](https://github.com/peanwang/wordcloud/blob/master/cat.png)
