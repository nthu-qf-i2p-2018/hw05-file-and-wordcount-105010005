# -*- coding: utf-8 -*-
import csv
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
    with open("wordcount.csv",'w')as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(['word','count'])
        for vocabulary,number in counter.most_common():
            writer.writerow([vocabulary,str(number)])
        csv_file.close()    
        
    
        
        
    
        
if __name__ == '__main__':
    main('i_have_a_dream.txt')