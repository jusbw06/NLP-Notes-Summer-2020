# TensorFlow Document Classification
This repository contains several different TensorFlow implementations of Document Classification using BERT. These notebooks can be easily modified for use with other transformer-based models.

**TF Keras**:  
Uses `tensorflow`, `keras`, and a pretrained BERT layer from `tensorflow_hub` (TensorFlow Hub) to create a BERT model for document classification. Most complex.

**TF HuggingFace**:  
Uses `tensorflow` along with a pretrained tokenizer and a pretrained model from the `transformers` (HuggingFace) library to create a BERT document classifier. Medium complexity.


**TF KTrain**:  
Uses the `ktrain` library to greatly simplify the document classification task. Easiest.

*Note*:  
Transformer models like BERT can only process 512 token sequences which is not necessarily the length of the document being classified. Recommend using the transformer model `XLM`.  

*Custom (BoW)*:
A custom bag-of-words implementation. It's not great, but feel free to improve on it or create your own.