#!/usr/bin/env python
'''Ultra simple summarizer'''

# Algorithm:
# 1. For each word, caluclate it's frequency in the document
# 2. For each sentence in the document
#       score(sentence) = sum([freq(word) for word in sentence])
# 3. Print X top sentences such that their size < MAX_SUMMARY_SIZE
# See http://en.wikipedia.org/wiki/Sentence_extraction for more



from collections import defaultdict
import re

MAX_SUMMARY_SIZE = 5
finalP = "/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/papers/"
finalA = "/home/palash/Downloads/7th-Sem/NLP/datasets/NIPS-Papers/final/attempt1-baseline/"



def tokenize(text):
    '''Very simple white space tokenizer, in real life we'll be much more
    fancy.
    '''
    return text.split()


def split_to_sentences(text):
    '''Very simple spliting to sentences by [.!?] and paragraphs.
    In real life we'll be much more fancy.
    '''
    sentences = []
    start = 0

    # We use finditer and not split since we want to keep the end
    for match in re.finditer('(\s*[.!?]\s*)|(\n{2,})', text):
        sentences.append(text[start:match.end()].strip())
        start = match.end()

    if start < len(text):
        sentences.append(text[start:].strip())

    return sentences


def token_frequency(text):
    '''Return frequency (count) for each token in the text'''
    frequencies = defaultdict(int)
    for token in tokenize(text):
        frequencies[token] += 1

    return frequencies


def sentence_score(sentence, frequencies):
    l = tokenize(sentence)
    ans = sum((frequencies[token] for token in l))
    return ans*1.0/len(l)


def create_summary(sentences, max_length):
    summary = []
    size = 0
    for sentence in sentences:
        summary.append(sentence)
        size += 1
        if size >= max_length:
            break

    # summary = summary[:max_length]
    return '\n'.join(summary)


def summarize(text, max_summary_size=MAX_SUMMARY_SIZE):
    frequencies = token_frequency(text)
    sentences = split_to_sentences(text)
    sentences.sort(key=lambda s: sentence_score(s, frequencies), reverse=1)
    summary = create_summary(sentences, max_summary_size)

    return summary



def main(argv=None):
    D = 1886
    for num in range(1,D+1):
        print num
        pFile = finalP + "p" + str(num) + ".txt"
        f= open(pFile, "r")
        text = f.read()
        try:
            a = summarize(text, 10)
        except:
            continue
        aFile = finalA + "a" + str(num) + "-baseline.txt"
        f1 = open(aFile, "w")
        f1.write(a)
        f1.close()
    


if __name__ == '__main__':
    main()