#clean the restaurant names and reviews before indexing
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = stopwords.words('english')


#create the json and post





def clean_description(description):

	try:
		#wordnet_lemmatizer = WordNetLemmatizer()
		stemmer = SnowballStemmer("english", ignore_stopwords=True)
		tokens = word_tokenize(description) #by whitespace
		words = [word for word in tokens if word.isalpha()] #remove punctuation
		#lower
		words = [word.lower() for word in words]
		#stopw words: https://www.ranks.nl/stopwords
		words = [w for w in words if not w in stop_words]
		#porterstem
		#print(words)
		#stemmer2 = SnowballStemmer("english", ignore_stopwords=True)

		words = [stemmer.stem(w) for w in words]
		stitched = " ".join(words)

	except Exception as e:
		# empty after cleaning, err: expected string or bytes like object
		print("issue")
		print(e)
		return ""
	return stitched


def tfidf():
	pass

