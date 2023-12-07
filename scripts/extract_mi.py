import nltk
from collections import Counter

def get_target_mi(ids, target, topn=20, mincount=5):
    vocab_counter = Counter() # initiate an empty counter of words - we will feed it iterarively on the go by all words we meet
    target_sents = [] # initiate an empty list of sentences containing the target word
    for id in ids: # for each work ID from our subset of IDs
        # based on the ID, open the file containing the lemmatized sentences and load its content as a list of lists
        with open("../data/large_data/sents_lemmata/{}.txt".format(str(id)), "r") as f:
            sents_lemmata = [sent.strip().split() for sent in f.readlines()]
        # based on the ID, open the file containing POS tags of the sentences and load its content as a list of lists
        # (this object should have the same structure as the previous one, what allows us to do a sort of filtering based on selected POS tags
        with open("../data/large_data/sents_pos/{}.txt".format(str(id)), "r") as f:
            sents_pos = [sent.strip().split() for sent in f.readlines()]
        sents_n = len(sents_lemmata) # count the number of sentences within the document
        lemmata = [l for s in sents_lemmata for l in s] # represent the whole work as one continuous list of words
        word_counts = dict(nltk.FreqDist(lemmata).most_common()) # count all words within the lemmata list
        vocab_counter.update(word_counts) # update the counter by these words
        sents_lemmata_filtered = [] # initiate a new empty list for sentence lemmata filtered by POS tags
        for n in range(len(sents_lemmata)):
            try:
                pos_indices = [t[0] for t in enumerate(sents_pos[n]) if t[1] in ["PROPN", "NOUN","VERB", "ADJ"]]
            except:
                pos_indices = []
            sent = sents_lemmata[n]
            try:
                sent_filtered = [sent[i] for i in pos_indices]
            except:
                sent_filtered = []
            #sent_filtered = [el for el in sent_filtered if len(el) > 2]
            sent_filtered = [el for el in sent_filtered if len(el) > 2]
            sents_lemmata_filtered.append(sent_filtered)
        target_sents_local = [sent for sent in sents_lemmata_filtered if target in sent]
        target_sents.extend(target_sents_local)
    target_sents = [[t for t in sent if vocab_counter[t] >= mincount] for sent in target_sents] # include only words appearing at least five times in the IDs texts
    target_coocs_counts = dict(nltk.FreqDist([t for s in target_sents for t in s]).most_common())
    target_coocs_n = sum(target_coocs_counts.values())
    target_coocs_freqs = dict([(tup[0], tup[1] / target_coocs_n) for tup in target_coocs_counts.items()])
    words_n = sum(vocab_counter.values())
    words_freqs = dict([(tup[0], tup[1] / words_n) for tup in vocab_counter.items()])
    target_coocs_freqs_weighted = {}
    for key in target_coocs_freqs.keys():
        target_coocs_freqs_weighted[key] = np.log((target_coocs_freqs[key])**2 / (words_freqs[key] * words_freqs[target]))
    target_coocs_topN = list(sorted(target_coocs_freqs_weighted.items(), key=lambda x:x[1], reverse=True))[1:topn +1]
    target_coocs_topN = [(tup[0], tup[1], vocab_counter[tup[0]], target_coocs_counts[tup[0]]) for tup in target_coocs_topN]
    return target_coocs_topN