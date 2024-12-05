import gensim.downloader as api
import pygame
import sys

def load_model():
    print("loading Word2Vec model...")
    return api.load("word2vec-google-news-300")  # downloads Google's pre-trained Word2Vec model

def calculate_similarity(model, word1, word2):
    try:
        similarity = model.similarity(word1, word2)
        return similarity
    except KeyError as e:
        return f'Error: "{e}" word not recognized'

model = load_model()

cont = input('hit enter to start')
while cont != 'q':

    word1 = input("\nfirst word: ").strip()
    word2 = input("second word: ").strip()

    similarity = calculate_similarity(model, word1, word2)
    print(f"similarity score between '{word1}' and '{word2}': {similarity*100:.5f}%") # 35% is similar for linxicon
    
    cont = input('hit enter to continue, [q] to quit')