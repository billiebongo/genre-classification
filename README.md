# Book Genre Classification
- Data (book_title, description, authors, popular shelves, pub_date) collected from Goodreads API and stored in MySQL in server
- Book description cleaned by removing common words in corpus and stopwords, then is preprocessed with Snowball / Porter lemmatizer
- word embeddings used: wiki-300d and GloVe
- EDA and models are on Jupyter Notebook
- Challenges: Imbalanced classes and 30 classes
- Tf-idf and countVectorizer with min df 2 and max df 0.85
- SVM and logistic regression models with parameters selected by GridSearchCV


***
- SVM and logistic regresison models ~65%
- LSTM - Work in Progress
