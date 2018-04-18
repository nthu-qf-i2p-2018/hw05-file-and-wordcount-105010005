# -*- coding: utf-8 -*-
import json
import csv
import pickle
def main(filename):
    f=open(filename)
    lines=f.readlines()
    all_words=[]
    for line in lines:
        words=line.split()
        for word in words:
            import string
            word=word.strip(string.punctuation)
            if word:
                all_words.append(word)
    from collections import Counter
    counter=Counter(all_words)
    counter=Counter()
    counter.update(all_words)
    with open("wordcount.json",'w') as json_file:
        json.dump(counter.most_common(),json_file)
        json_file.close()
    with open("wordcount.csv",'w')as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(['word','count'])
        writer.writerow(counter.most_common())
        csv_file.close()
    with open("wordcount.pkl",'wb')as pkl_file:
        pickle.dump(counter,pkl_file)
        pkl_file.close()
    
        
    
        
        
    
        
if __name__ == '__main__':
    main('i_have_a_dream.txt')     
        
    
        
        
    
        
if __name__ == '__main__':
    main('i_have_a_dream.txt')