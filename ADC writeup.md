**Automated Document Classification Design:**

*Problem*:  

The US Navy would like a way to automatically classify documents into their respective classification levels. This would entail starting with a random input document which could contain *unclassified*, *classified*, or *secret* information and correctly select the document's appropriate classification level.  

Note: This is before any classification markings are applied. (We cannot just look for a classifaction stamp.) This is meant to be a tool for the Navy personnel responsible for classifying documents into their appropriate classification levels.  

*Background Information*:  

Documents take on the classification level of the highest level of classified information contained within the document. For example, a document which contains a single piece of *secret* information while the rest of the document contains all *unclassified* information retains the classification level: *secret*. If a document denoted *classified* is comprised completely of *classified* information, it does not assume a higher classification level.  

Document classification is determined by a program's classification guide. For example, a project code-named *ORANGE*\* (this is fake, don't go looking it up) will have its own classification guide. This guide will have certain rules. It may say information denoting the location of related military installations is classified as *secret*. It may also say system-level descriptions of the equipment at those locations is *unclassified*. This could be the reverse with the former *unclassified* and the latter *secret*. These guides can have many, many rules.

Just to reiterate, a document that includes **any** information in the first category (*secret*) from the previous paragraph will be considered *secret* while a document containing information in the latter category (*unclassified*) with **no other information from a higher classification level** will retain an *unclassified* classification.  

*special kudos to whoever gets the reference 


*General Approach*:  

Because the classification of a document is largely determined by the document's parent program, we see automated document classification as a two step process.  

First, we must correctly select the documents classification guide. This entails using a document classifier to select the document's correct program name. From the program name, we shall be able to select the programs corresponding classification guide for use in the classifier. The team had considered several different approaches to accomplishing the task but have largely agreed on persuing methods implementing ML/NLP Transformer base models such as BERT.

Second, using the selected classification guide we must be able to find any classified information within the selected document. This entails using a method that can "understand" English language, be familiar with Navy terminology, and demonstrate basic reasoning skills. This suggests that we must use machine learning/artificail intelligence models for this task. The goal of this task is to be able to pick out and highlight (if need be) any classified information held within a specific document

*Layer 1 -- Document Categorical Classification*  

In trying to accomplish the first task of simple document classification, the team had considered many different options ranging from non-ML "bag-of-words" approaches to ML/AI approaches. The approaches that had shown the most promise were those involving ML Transformer-based NLP models. The team had written several scripts proving capability of using the method to classify documents into predetermined categories using both PyTorch and TensorFlow. The team currently believes that using a Transformer-based model built specifically for document classification such as `TransformerXLM` is the best way to accomplish this task.  

This will require access to several real Navy datasets from different Navy programs in order to train our neural network models. This will also require access to larger computing resources than we have available at present.  


*Layer 2 -- Finding Classified Information*  

In order to classify the documents, we need to find classified information within the documents. Most of the rules within the classifcation guides cannot be answered using simple pattern recognition. For example, one cannot simply say "just find units of measurement, for those signify qualities of the system which should all be classified". Rules often take the form of something more like this, "all descriptions of system-level components are to be considered classified". Teaching a computer to follow a rule such as that is no easy task. The most promising method proposed by one of the members of the team was using a hypothesis-prediction method on a transformer-based model somewhat resembling work done on the SQuAD dataset. The SQuAD BERT model takes in two sequences, a question and a prompt containing the answer. What we propose is something a little bit different. We propose giving the BERT model the specific classification rule as the first sequence and the contents of the document as the second sequence. If the contents of the document satisfy the hypothesis given by the rule, then the model will have found classified information.  

In order to implement this, the team is again going to need access to a large dataset from a particular Navy program and personel with experience using these Transformer NLP models.  




