# Named Entity Recognition Notes
General investigation into using NER on MS Dataset


## TF NER BERT -- Outline
An outline for creating a NER classifier TF  

Open `TF_NER_BERT.ipynb` and read description at top of notebook  

Alternative pre-trained option, see: [spaCy -- named entities](https://spacy.io/usage/linguistic-features#named-entities "spaCy")  


### Labeling Datasets:
**Doccano:**  
Free Tool for labeling NER datasets  

*Installation*:  
Follow instructions at [github.com/doccano/doccano](https://github.com/doccano/doccano "https://github.com/doccano/doccano")  
`git clone https://github.com/doccano/doccano.git`

*Preparing your data for input into Doccano*:  

- Combine all text files into one text file.
(Ex. `cat * > file.txt`).
- Separate all examples by a single newline character. See `example.txt`.
- Doccano will separate your data into separate training examples automatically and will allow you to create entity labels and label all of your training data through text highlighting. 
- Doccano will output files in `json` format, see `example.json`.
