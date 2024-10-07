import re
import string
import nltk
from collections import Counter
import csv

nltk.download('punkt')
def load_file(file_path):
    def preprocess(sentence):
        sentence=sentence.lower()
        sentence=sentence.translate(str.maketrans('', '', string.punctuation))
        return re.sub(r'[^\w\s]','',sentence)

    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
    parallel_sentences = []
    for i in range(0, len(lines), 2):
        english_sentence = preprocess(lines[i].strip())
        sinhala_sentence = preprocess(lines[i+1].strip())
          
        parallel_sentences.append((english_sentence,sinhala_sentence))

    csv_file_path = "sinhala_english_sentences.csv"
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(parallel_sentences)

    return parallel_sentences


   
def tokenize(sentences,language='english'):
    token=[]
    for sentence in sentences:
        if language=='english':
            token.append(nltk.word_tokenize(sentence))
        else:
            token.append(nltk.word_tokenize(sentence))

    return token
        
def word_frequency(tokens):
    flat_token=[]
    for sublist in tokens:
        for token in sublist:
            flat_token.append(token)
    return Counter(flat_token)