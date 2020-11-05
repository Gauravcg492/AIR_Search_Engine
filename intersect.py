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
                    ans.append((p1[i],pp1[x],ps))
                x += 1
            i += 1
            j += 1
        else:
            if p1[i][0] < p2[j][0]: 
                i += 1
            else:
                j += 1
    return list(map(lambda x:x[0],ans))

def posinter_over_invindex(invindex,query,k):
    d = {}
    N = 418
    for t in set(query.split()):
        d[t] = N//10**invindex[t][0]
    s = sorted(d)
    p1 = invindex[s[0]][1]
    for i in range(1,len(s)):
        p1 = posintersect(p1,invindex[s[i]][1],k)
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

def kgramintersect(kgramdict):
    itr = iter(kgramdict)
    res = kgramdict[next(itr)]
    for _ in range(len(kgramdict)-1):
        res = kgr(res,kgramdict[next(itr)])
    candlst=[]
    kgramlst = kgramdict.keys()
    for i in range(len(res)):
        f=1
        s = res[i]
        for kgram in kgramlst:
            if f:
                r = s.replace(kgram,"")
                if r==s:
                    f=0
                    break
                else:
                    s=r
        if f:
            candlst.append(res[i])
    return candlst
