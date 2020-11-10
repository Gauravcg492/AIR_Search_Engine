import nltk
import math

def posintersect(p1,p2,k):
    ans=[]
    i = 0
    j = i
    lp1 = len(p1)
    lp2 = len(p2)
    while i<lp1 and j<lp2:
        if p1[i][0] == p2[j][0]:
            l=[]
            x=0
            y=x
            pp1 = p1[i][1]
            pp2 = p2[j][1]
            lpp1 = len(pp1)
            lpp2 = len(pp2)
            while x<lpp1:
                while y<lpp2:
                    if abs(pp1[x]-pp2[y]) <=k:
                        l.append(pp2[y])
                    elif pp2[y]>pp1[x]:
                        break
                    y += 1
                while l and abs(l[0]-pp1[x])>k:
                    l.pop(0)
                for ps in l:
                    ans.append((p1[i][0],ps))
                x += 1
            i += 1
            j += 1
        else:
            if p1[i][0] < p2[j][0]: 
                i += 1
            else:
                j += 1
    nans = []
    for t in ans:
        lgth = len(nans)
        i=0
        for nt in nans:
            if t[0] == nt[0]:
                if t[1] not in nt[1]:
                    nt[1].append(t[1])
                    break
            else:
                i += 1
        if i == lgth:
            nans.append((t[0],[t[1]]))
    del ans
    return nans

def posinter_over_invindex(invindex,query, wildcard_index, champion =True):
    index = 2 #champion
    if not champion :
        index = 1
    d = {}
    tokens = nltk.word_tokenize(query)
    q = []
    itr = 0
    enum = list(query.split())
    for token in tokens:
        while itr < len(enum):
            if token == enum[itr]:
                q.append((token,itr))
                itr += 1
                break
            else:
                itr += 1
    for t in q:
        d[t] = len(invindex[t[0]])
    s = sorted(d,key=lambda x:d[x])
    del q
    del d
    p1 = invindex[s[0][0]][index] if ('*' not in s[0][0]) else wildcard_index[s[0][0]][1]
    for i in range(1,len(s)):
        p3 =  invindex[s[i][0]][index] if ('*' not in s[i][0]) else wildcard_index[s[i][0]][1]
        k = abs(s[i][1] - s[i-1][1])
        p1 = posintersect(p1,p3,k)
    return list(set(map(lambda l:l[0],p1)))
    
def merge_docs(inv_ind, terms, champion_list = False):
    doc_set = set()
    index = 1
    if champion_list:
        index = 2
    for term in terms:
        for doc_data in inv_ind[term][index]:
            doc_set.add(doc_data[0])
    return sorted(doc_set)

def merge_terms(term1_index, term2_index):
    new_postings_list = []
    i = j = 0
    t1_len = len(term1_index[1])
    t2_len = len(term2_index[1])
    N = 94858
    while(i < t1_len and j < t2_len):
        if term1_index[1][i][0] < term2_index[1][j][0]:
            new_postings_list.append(term1_index[1][i])
            i += 1
        elif term1_index[1][i][0] > term2_index[1][j][0]:
            new_postings_list.append(term2_index[1][j])
            j += 1
        else:
            doc_id = term1_index[1][i][0]
            position_list = sorted(term1_index[1][i][1] + term2_index[1][j][1])
            tf = 1 + math.log(len(position_list), 10)
            new_postings_list.append(doc_id, position_list, tf)
    sorted_list = sorted(new_postings_list, key=lambda x: x[2], reverse=True)
    new_champion_list = sorted(sorted_list[:20])
    df = len(new_postings_list)
    idf = math.log(N/df, 10)
    return (idf, new_postings_list, new_champion_list)     

def kgr(kg1,kg2):
    ans = []
    for term in kg1:
        if term in kg2:
            ans.append(term)
            kg2.remove(term)
    for term in kg2:
        if term in kg1:
            ans.append(term)
            kg1.remove(term)
    return ans

def kgramintersect(kgramdict,pref):
    itr = iter(kgramdict)
    res = kgramdict[next(itr)]
    for _ in range(len(kgramdict)-1):
        res = kgr(res,kgramdict[next(itr)])
    itr = iter(kgramdict)
    orig = next(itr)
    for _ in range(len(kgramdict)-2):
        orig += next(itr)[1]
    remlst = []
    for i in range(len(res)):
        if orig not in res[i] or (pref and orig != res[i][:len(orig)]) or (not pref and orig != res[i][-len(orig):]):
            remlst.append(res[i])
            continue
    for rem in remlst:
        res.remove(rem)
    del rem
    return res
