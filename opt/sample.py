#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys
# import subprocess
import pandas as pd
import MeCab

MECAB_DIC_PATH = '/var/lib/mecab/dic/ipadic-utf8'
USER_MECAB_DIC_PATH = '/root/opt/dic/rule.dic'

# /usr/lib/mecab/mecab-dict-index -d /var/lib/mecab/dic/ipadic-utf8 -u rule.dic -f utf8 -t utf8 /root/opt/rule.csv
mecab_instance = MeCab.Tagger(f'-d {MECAB_DIC_PATH} -u {USER_MECAB_DIC_PATH}')

def mecab(character):
  return mecab_instance.parse(character)

def get_xlsx():
  excel = pd.ExcelFile('/root/opt/text_data.xlsx')
  sheet_df = excel.parse('Sheet1')
  df = pd.DataFrame(sheet_df, columns = ['text', 'speaker'])
  first_text = df['text'][0]
  print(mecab(first_text))
  # for i in df.index:
  #   print(df['speaker'][i])
  #   print(df['text'][i])

  return 'hoge'

def main():
  get_xlsx()
  # char = mecab('すもももももももものうち')
  # print(char)

if __name__ == "__main__":
  main()