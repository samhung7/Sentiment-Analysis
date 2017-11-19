# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 19:57:29 2016

@author: ldy
"""

import sys
sys.path.append("code")
from Sentiment_lstm import lstm_predict
argvs_lenght = len(sys.argv)
if argvs_lenght != 2:
    print('參數長度錯誤！')
argvs = sys.argv

sentence  = argvs[-1]
lstm_predict(sentence)
