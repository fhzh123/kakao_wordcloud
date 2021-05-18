import time
import argparse
from preprocessing import preprocessing
from generate_wordcloud import generate_wordcloud

def main(args):
    if args.preprocessing:
        preprocessing(args)
    
    generate_wordcloud(args)

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Kakaotalk Wordcloud Generator')
    parser.add_argument('--preprocessing', action='store_true')
    parser.add_argument('--data_path', default='./data', type=str,
                        help='Data path setting; Default is ./data')
    parser.add_argument('--data_name', default='2021_05_19', type=str,
                        help='Data name; Default is 2021_05_19')
    args = parser.parse_args()

    main(args)