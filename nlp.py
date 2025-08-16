import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger_eng')

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def natural_language_processing(worf_quote):
    stop_words = set(stopwords.words("english"))
    words_in_quote = word_tokenize(worf_quote)
    
    filtered_words = [word for word in words_in_quote if word.casefold() not in stop_words]
        
    lemmatizer = WordNetLemmatizer()

    pos_tags = nltk.pos_tag(filtered_words) 
    
    lemmatized_words = [
        lemmatizer.lemmatize(word, get_wordnet_pos(tag))
        for word, tag in pos_tags
    ]
    return lemmatized_words

