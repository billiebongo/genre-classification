#clean the restaurant names and reviews before indexing
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = stopwords.words('english')


#create the json and post

def clean_description(description):
	wordnet_lemmatizer = WordNetLemmatizer()
	tokens = word_tokenize(description) #by whitespace
	words = [word for word in tokens if word.isalpha()] #remove punctuation
	#lower
	words = [word.lower() for word in words]
	#stopw words: https://www.ranks.nl/stopwords
	words = [w for w in words if not w in stop_words]
	#porterstem
	#print(words)
	#stemmer2 = SnowballStemmer("english", ignore_stopwords=True)

	words = [wordnet_lemmatizer.lemmatize(w) for w in words]


	return cleaned_description
