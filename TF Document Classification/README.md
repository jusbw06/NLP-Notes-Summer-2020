# TF Document Classification
This repository contains several different Tensorflow implementations of Document Classification using BERT. Can easily be modified for use with other transformer-based models.

**TF Keras**:  
Uses `tensorflow`, `keras`, and pretrained BERT layer from `tensorflow_hub` (TensorFlow Hub) to create BERT model for document classification. Most in depth of the models.

**TF HuggingFace**:  
Uses `tensorflow` and pretrained tokenizer and models from the `transformers` (HuggingFace) library to create document classifier. Medium complexity.


**TF KTrain**:  
Uses the `ktrain` library to greatly simplify the document classifier. Easiest.

*Note*:  
Transformer models like BERT can only process 512 token sequences which is not necessarily the length of the document being classified. Recommend using `TransformerXLM`.  

*Custom (BoW)*:
A custom bag-of-words implementation. It's not great but feel free to improve on it or create your own.