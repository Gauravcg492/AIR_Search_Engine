import nltk
import math

def posintersect(p1,p2):
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
                    if pp2[y]-pp1[x]==1:
                        l.append(pp2[y])
                    elif pp2[y]>pp1[x]:
                        break
                    y += 1
                while l and l[0]-pp1[x]>1:
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
    p1 = invindex[query[0]][index] if ('*' not in query[0]) else wildcard_index[query[0]][index]
    for i in range(1,len(query)):
        p3 =  invindex[query[i]][index] if ('*' not in query[i]) else wildcard_index[query[i]][index]
        print("p1 len and p3 len", len(p1), len(p3))
        p1 = posintersect(p1,p3)
    print("Returning Documents After Intersection")
    return list(map(lambda l:l[0],p1))
    
def merge_docs(inv_ind, terms, wildcard_index, champion_list = False):
    doc_set = set()
    index = 1
    if champion_list:
        index = 2
    for term in terms:
        if '*' in term:
            for doc_data in wildcard_index[term][index]:
                doc_set.add(doc_data[0])
        else:
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
            new_postings_list.append([doc_id, position_list, tf])
            i += 1
            j += 1
    while(i < t1_len):
        new_postings_list.append(term1_index[1][i])
        i += 1
    while(j < t2_len):
        new_postings_list.append(term2_index[1][j])
        j += 1
    sorted_list = sorted(new_postings_list, key=lambda x: x[2], reverse=True)
    new_champion_list = sorted(sorted_list[:20])
    df = len(new_postings_list)
    idf = math.log(N/df, 10)
    return (idf, new_postings_list, new_champion_list)     

def kgramintersect(kgramdict,orig,pref):
    itr = iter(kgramdict)
    res = kgramdict[next(itr)]
    for _ in range(len(kgramdict)-1):
        res = list(set(res) & set(kgramdict[next(itr)]))
    remlst = []
    for i in range(len(res)):
        if orig not in res[i] or (pref and orig != res[i][:len(orig)]) or (not pref and orig != res[i][-len(orig):]):
            remlst.append(res[i])
    for rem in remlst:
        res.remove(rem)
    del rem
    return res
