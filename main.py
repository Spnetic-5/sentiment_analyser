import string
# print(string.punctuation)
from collections import Counter  
import matplotlib.pyplot as plt
# read the text from file
text = open('read.txt',encoding='utf-8').read()
#print(text)


#lowering all letters

lc = text.lower()
#print(lc)

# removing punctuation
# str.maketrans('<Text which is to be replaced>','<replaced text>','<text which is to be deleted>')
clean_text = lc.translate(str.maketrans("","",string.punctuation))
#print(clean_text)

# Tokenization #listing words in sentence
tokenized_words = clean_text.split()
#print(tokenized_words)

# removing unnecessary words
scrap_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own",  "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []


for word in tokenized_words:
    if word not in scrap_words:
        final_words.append(word)
#print(final_words)

emotion_lst = []

with open('emotion.txt','r') as file:
    for i in file:
        clean_line = i.replace('\n','').replace(',','').replace("'",'').strip() #removing new lines
        word, emotion = clean_line.split(":")
        #print("Word=", word,"Emotion=", emotion)
        if word in final_words:
            #print(word)
            emotion_lst.append(emotion)
#print(emotion_lst)
w = Counter(emotion_lst)
plt.bar(w.keys(),w.values())
plt.show()
print(w)