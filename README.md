#環境要求
- Unix/Linux系统
- python 2.7
- python包安装： keras,sklearn,gensim,jieba,h5py,numpy,pandas
```
sudo pip install -r requirements.txt
```
# 用法

## 使用SVM分類器進行情感分類：
```
python predict.py svm 這個手機質量很好，我很喜歡，不錯不錯

```
```
python predict.py svm 這書的印刷質量的太差了吧，還有缺頁，以後再也不買了

```

## 使用LSTM進行情感分類：
```
python predict.py lstm 酒店的環境不错，空間挺大的
```
```
python predict.py lstm 電腦散熱太差，偶爾還藍屏，送貨也太慢了吧
```
#程序
- code/Sentiment_lstm.py 使用word2vec和LSTM訓練和預測

- code/Sentiment_svm.py  使用word2vec和svm訓練和預測
- predict.py  調用Sentiment_lstm.py及Sentiment_svm.py進行預測

#數據
- ./data/ 原始數據文件夾
  - data/neg.xls 負樣本原始數據
  - data/pos.xls 正樣本原始數據

- ./svm_data/ svm數據文件夾
  - ./svm_data/\*.npy 處理後的訓練數據和測試數據
  - ./svm_data/svm_model/ 保存訓練好的svm模型
  - ./svm_data/w2v_model/ 保存訓練好的word2vec模型


- ./lstm_data/ lstm數據文件夾
  - ./lstm_data/Word2vec_model.pkl 保存訓練好的word2vec模型
  - ./lstm_data/lstm.yml  保存訓練網路的結構
  - ./lstm_data/lstm.h5  保存網路訓練到的權重
  
#詳細介紹

[购物评论情感分析的实现](http://buptldy.github.io/2016/07/20/2016-07-20-sentiment%20analysis/)
