# Import modules
import os
import re
import pandas as pd
from tqdm import tqdm

from utils import time_return

def main(args):
    with open(os.path.join('C:/Users/fhzh/Desktop/', 'kakao_text.txt'), 'r', encoding='utf8') as f:
        kakao_text = f.readlines()

    for i, text in enumerate(tqdm(kakao_text)):
        if i == 0:
            year, month, day = re.findall('\d+', text)
            author, hour, minute, text_list = list(), list(), list(), list()
            text_dat = pd.DataFrame({
                'year': [],
                'month': [],
                'day': [],
                'author': [],
                'hour': [],
                'minute': [],
                'text': []
            })
        if text[:15] == '---------------':
            year, month, day = re.findall('\d+', text)
            year_list = [year for _ in range(len(text_list))]
            month_list = [month for _ in range(len(text_list))]
            day_list = [day for _ in range(len(text_list))]
            new_dat = pd.DataFrame({
                'year': year_list,
                'month': month_list,
                'day': day_list,
                'author': author,
                'hour': hour,
                'minute': minute,
                'text': text_list
            })
            text_dat = pd.concat([text_dat, new_dat], axis=0)
            author, hour, minute, text_list = list(), list(), list(), list()
        elif text[:5] == '[야놀자]' or text[:6] == '[1벌구성]':
            author.append(text_split[0])
            hour.append(h)
            minute.append(m)
            text_list.append(text.replace('\n', '').strip())
        elif text[0] == '[':
            text_split = [x.replace('[', '').strip() for x in text.split(']')]
            author.append(text_split[0])
            h, m = time_return(text_split[1])
            hour.append(h)
            minute.append(m)
            text_list.append(text_split[2].replace('\n', '').strip())
        elif text == '':
            continue
        elif text[0] != '[' and text[0] != '-':
            author.append(text_split[0])
            hour.append(h)
            minute.append(m)
            text_list.append(text.replace('\n', '').strip())

    text_dat.index = range(len(text_dat))
    # emo_ix = text_dat[text_dat['text'] == '이모티콘'].index.tolist()
    emo_ix = set()
    picture_ix = text_dat[text_dat['text'] == '사진'].index.tolist()
    text_dat = text_dat.iloc[list(set(text_dat.index) - set(emo_ix) - set(picture_ix))]
    text_dat.index = range(len(text_dat))

    text_dat.to_csv(os.path.join('C:/Users/fhzh/Desktop/', 'kakao_text.csv'), index=False)