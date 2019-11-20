# Analyzing Product Review System 
Analyzing product review system with BERT
<br><img src=https://user-images.githubusercontent.com/55969260/68922420-e8415d80-07be-11ea-8663-aad62b2003d2.png><br>

# Outline
Last october 2018, BERT (Bidirectional Encoder Representations from Transformers) achieved State of the art in the NLP (Natural
Language Processing) field. I used this and progressed Sentiment Analysis task. Through this, I would like to create a product
review analysis software that can be useful to companies.

# Research Goal
Sentiment Analysis using the existing BERT model, based on the result, it will check ther TF-IDF (Term Frequency-Inverse Document
Frequency) similarity between the reviews. The program displays the reviews that BERT is harsh criticism and outputs other reviews with similarities to the reviews on the screen through user input.

# Existing Research
## Transformers :
Transformer is a model derived from Google's 2017 paper, "Attention is all you need" which follows the existing encoder-decoder structure of seq2seq and implements only Attention as the name of the paper. This model has the advantage that the learning speed is much faster than the RNN by creating the encoder-decoder structure using only the attention without using the RNN. <br><img src = https://user-images.githubusercontent.com/55969260/68918325-02743f00-07b1-11ea-9f6e-724e96c5886b.png> <br>
The Transformer architecture itself can be understood as an iteration of the strucutre shown above. BERT is a model that uses only the left encoder.
## TF-IDF :
Usually used in Information retrieval or Textminig. Using TF-IDF, you can find out the importance of the entity. Because it describes how important a word is in a particular document. TF is a word frequency, which indicates how often a particular word appears in the document. Unsurprisingly, an Entity that appears frequently in documents can be expected to have a high value as an Entity. IDF is the inverse of the document frequency. The total number of documents is divided by the number of documents that contain the entity. This can be a measuer of the document characteristic. Consider the word 'bluetooth' often found in some documents. Perhaps this document group is likely to be a collection of electronics. This TF-IDF document similarity test will examine the simiarities of the reviews. <br><img src = https://user-images.githubusercontent.com/55969260/68918977-a65eea00-07b3-11ea-8ffc-71446e644f67.png><br>
## Product review sentiment analysis :
The current product review sentiment analysis codes were analyzed using models such as RNN (Recurrent Neural Networks), LSTM (Long Short-Term Memory), word2vec embedding, and SVM (Support Vector Machine). F1-score showed up to 80% on Amazon reviews data. In addition, research was stopped in sentiment analysis, and there were not many cases of using it meaningfully in real life. In thie project, I will use BERT to create software that analyzes sentiment and provides meaningful information through similarity test.

# Program progress
After sentiment analysis through a complex network of transfomer structures, their own embedding method, a BERT model using an activation function, harsh criticisms are printed on the screen. In addition, when a user (company) presses the criticism of the screen, the user can see a harsh criticisms similar to itself so that the user can know and develop for the defect of there product. <br><img src = https://user-images.githubusercontent.com/55969260/68919732-81b84180-07b6-11ea-96a7-57290b65e005.png><br>

# Training
A total of 4249 data were trained and tested with 1819 data. I used Amazon product review data, yelp and imdb data.
<br> ＊ train data <img src= https://user-images.githubusercontent.com/55969260/68920184-d60ff100-07b7-11ea-820a-dd902a9d2387.png><br>
The accuracy and f1 score are as follows<br>
<img src = https://user-images.githubusercontent.com/55969260/68920328-36069780-07b8-11ea-8b5a-d2b4eb9b07d9.png><br>

# Program execution
The review to analyze is the earphones sold by Amazon. The reviews on the earphones were as follows and the labels were all zeroed out and put in the BERT.
<br><img src =https://user-images.githubusercontent.com/55969260/68920775-b4b00480-07b9-11ea-86d1-580226ec01a7.png><br>
When the program is executed, it is displayed on the screen as follows. Here is part of the output
<br><img src=https://user-images.githubusercontent.com/55969260/68921825-4d944f00-07bd-11ea-9081-69472cc92307.png><br>
The result of pressing 113 index. Similarity is measured through ld (long description). Index 113 reviews the connection issues and the bad use of the earphones in the game (PUBG) , and shows similar descriptions.
<br><img src =https://user-images.githubusercontent.com/55969260/68921946-a368f700-07bd-11ea-8370-88fa5f5faa3b.png><br>

# References
- [1] Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova , 	BERT : Pre-training of Deep Bidirectional Transformers for Language Understanding									Network. arXiv:1810.04805
- [2] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin , 	Attention Is All You Need								Network. arXiv:1706.03762
- [3] https://nesoy.github.io/articles/2017-11/tf-idf
- [4] https://wikidocs.net/31379
