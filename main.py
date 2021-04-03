# Import modules
import os
import numpy as np
from PIL import Image
from tqdm import tqdm
from collections import Counter
from wordcloud import WordCloud
#
from khaiii import KhaiiiApi
from konlpy.tag import Mecab, Okt, Hannanum
#
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
plt.rcParams["font.family"] = 'NanumGothic'

def main(args):
    text_dat = pd.read_csv('./kakao_text2.csv')
    text_dat = text_dat.dropna()

    mecab = Mecab()
    okt = Okt()
    h = Hannanum()
    api = KhaiiiApi()

    counter = Counter()
    for i, text in enumerate(tqdm(text_dat['text'])):
        text = text.replace('이모티콘','따룽해')
        text = text.replace('?','')
        text = text.replace('!','')
        text = text.replace('.','')
        text = text.replace('ㅋ','')
        text = text.replace('ㅎ','')
        text = text.replace('ㅠ','')
        text = text.strip()
        if text != '':
            for word in api.analyze(text):
                counter.update([word.lex])

    vocab_list = list()
    count_list = list()

    for k, v in counter.items():
        vocab_list.append(k)
        count_list.append(v)

    count_dat = pd.DataFrame({
        'vocab': vocab_list,
        'count': count_list
    })

    wordcloud_dat = count_dat[count_dat['count'] >= 200]
    wordcloud_dat2 = wordcloud_dat.head(50)

    keywords = dict()
    for i in range(len(wordcloud_dat2)):
        keywords[wordcloud_dat2.iloc[i]['vocab']] = wordcloud_dat2.iloc[i]['count']

    wordcloud = WordCloud()
    wordcloud = wordcloud.generate_from_frequencies(keywords)

    array = wordcloud.to_array()

    wordcloud = WordCloud(
        font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf',
        width = 1200,
        height = 1200,
        mask = np.array(Image.open('./heart7.jpg')),
        background_color='white',
        colormap='spring'
    )
    wordcloud = wordcloud.generate_from_frequencies(keywords)
    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.savefig('./test.jpg')
    plt.axis("off")
    plt.show()