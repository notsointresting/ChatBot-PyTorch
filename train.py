import json
from nltk_utils import tokenizer,stem,bag_of_words
import numpy as np
import torch
import torch.nn as nn 
from torch.utils.data import Dataset,DataLoader
from model import NeuralNet


with open('intents.json','r') as f:
    intents = json.load(f)


all_words = []
tags = []
xy = []


for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intent['patterns']:
        w = tokenizer(pattern)
        all_words.extend(w)
        xy.append((w,tag))


ignore_words = ['!','.',',','?','@','#','$','%','^','&','*','(',')','_','-','+','=','<','>','/','\\','|','[',']','{','}',';',':','"','\'','`','~','1','2','3','4','5','6','7','8','9','0']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

X_train = []
Y_train = []

for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tags.index(tag)
    Y_train.append(label) # CrossEntropyLoss

X_train = np.array(X_train)
Y_train = np.array(Y_train)




class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = Y_train

    # dataset[idx]
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    def __len__(self):
        return self.n_samples

# Hyperparameters
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(X_train[0])


dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset,
                        batch_size=batch_size,
                        shuffle=True,
                        num_workers=2)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)
model = NeuralNet(input_size,hidden_size,output_size)