import torch
import torch.nn as nn
from shakespeareGPT import GPTLanguageModel
from shakespeareGPT import decode
import time

def print_text_animated(text):
    for char in text:
        print(char, end ="", flush=True)
        time.sleep(0.02)
device = 'cuda' #if torch.cuda.is_available() else 'cpu'

lm = GPTLanguageModel()
lm.to(device)
state_dict = torch.load('model.pt', map_location=device)
lm.load_state_dict(state_dict)
lm.eval()

context = torch.zeros((1, 1), dtype=torch.long, device=device)
#print(decode(lm.generate(context, max_new_tokens=500)[0].tolist()))
#open('more.txt', 'w').write(decode(lm.generate(context, max_new_tokens=10000)[0].tolist()))
print_text_animated(decode(lm.generate(context, max_new_tokens=500)[0].tolist()))

