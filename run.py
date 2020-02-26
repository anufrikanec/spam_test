from application import app
from spam_classifer import calc_spam

spam_class = calc_spam()

train_data = [  
    ['Купите новое чистящее средство', "SPAM"],   
    ['Купи мою новую книгу', "SPAM"],  
    ['Подари себе новый телефон', "SPAM"],
    ['Добро пожаловать и купите новый телевизор', "SPAM"],
    ['Привет давно не виделись', "NOT_SPAM"], 
    ['Довезем до аэропорта из пригорода всего за 399 рублей', "SPAM"], 
    ['Добро пожаловать в Мой Круг', "NOT_SPAM"],  
    ['Я все еще жду документы', "NOT_SPAM"],  
    ['Приглашаем на конференцию Data Science', "NOT_SPAM"],
    ['Потерял твой телефон напомни', "NOT_SPAM"],
    ['Порадуй своего питомца новым костюмом', "SPAM"]
]

for info in train_data:
    spam_class.train(info[0], info[1])
