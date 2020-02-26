# подумать про отдельный словарь встречающихся в тексте почт, сайтов и номеров телефонов, так же возможно есть смысл
# их класифицировать, возможно стоит обратить внимание на наличие сайта/номер/почты и общее кол-во слов

from collections import defaultdict
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re


class calc_spam():
    def __init__(self):
        self.spam_dict = defaultdict(int)
        self.not_spam_dict = defaultdict(int)
        self.spam_letters_counter = 0
        self.not_spam_letters_counter = 0
        #self.letters_counter = self.spam_letters_counter + self.not_spam_letters_counter
        self.stopwords = set(stopwords.words("russian"))
        #self.P_spam = self.spam_letters_counter/self.letters_counter
        #self.P_not_spam = self.not_spam_letters_counter/self.letters_counter
        self.stemmer = PorterStemmer()
        
        
    def add_world(self, text, target_dict):
        pattern = r"[^\w]"
        text = re.sub(pattern, " ", text)
        text = text.split(" ")
        for world in text:
            if str(world) not in self.stopwords and world != '':
                world = world.lower()
                world = self.stemmer.stem(world)
                
                target_dict[world] +=1

    def calculate_word_frequencies(self,body, label):
        if label == "SPAM":
            self.spam_letters_counter+=1
            self.add_world(body, self.spam_dict)
        elif label == "NOT_SPAM":
            self.not_spam_letters_counter+=1
            self.add_world(body, self.not_spam_dict)
            
            
    def train(self, body, label):
        self.calculate_word_frequencies(body, label)
        if label == "SPAM":
            self.spam_letters_counter +=1
        elif label == "NOT_SPAM":
            self.not_spam_letters_counter +=1
    
    #вот тут не уверен что правильно понял задачу!
    def calculate_P_Bi_A(self, word, label):
        if label == "SPAM":
            P_Bi_A = (self.spam_dict[word] + 1)/(self.spam_dict[word] + 1 + self.not_spam_dict[word] + 1)
            
        elif label == "NOT_SPAM":
            P_Bi_A = (self.not_spam_dict[word] + 1)/(self.spam_dict[word] + 1 + self.not_spam_dict[word] + 1)
        print(P_Bi_A)
        return P_Bi_A
    
    def calculate_P_B_A(self, text, label):
        P_B_A = 1
        text = text.split(" ")
        for world in text:
            if str(world) not in self.stopwords:
                P_Bi_A = self.calculate_P_Bi_A(world, label)
                P_B_A = P_B_A*P_Bi_A
                #print(P_B_A)
        return P_B_A
    
    def classify(self, email):
        P_all_spam = self.spam_letters_counter/(self.spam_letters_counter+self.not_spam_letters_counter)
        P_spam = self.calculate_P_B_A(email, "SPAM")*P_all_spam
        P_not_spam = self.calculate_P_B_A(email, "NOT_SPAM")*(1-P_all_spam)
        print(P_spam)
        print(P_not_spam)
        if P_spam > P_not_spam:
            return "SPAM"
        else:
            return "NOT_SPAM"


