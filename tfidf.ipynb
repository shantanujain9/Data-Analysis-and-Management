import re
import math
def tfidf(f):
    numberofdocs = 0
    nesteddict = {}
    idf = {}
    tfidfdict = {}
    for file in open(f):
        frequencies = {}
        termfrequencies = {}
        for line in open(file.strip()):
            writefile = open('preproc_'+file.strip(),'a')
            if line.isalnum() == False:
                pattern = r'[^\w\s]'
                newline = re.sub(pattern,'',line)
                line = newline
            line = re.sub(" +"," ",line)
            line = re.sub(r'http\S+','',line)
            line = re.sub(r'https\S+','',line)
            line = line.lower()
            stopwords = []
            with open('stopwords.txt','r') as stopfile:
                for word in stopfile:
                    stopwords.append(word.strip())
            linelist = line.split()
            for x in stopwords:
                if x in linelist:
                    for i in range(0,len(linelist)):
                        if linelist[i] == x:
                            linelist[i] = ""
            line = ' '.join(str(x) for x in linelist if x!='')
            linelist2 = line.split()
            for x in linelist2:
                if x[-3:] == 'ing' and x[-5:] != 'nning':
                    linelist2[linelist2.index(x)] = x[:-3]
                if x[-3:] == 'ing' and x[-5:] == 'nning':
                    linelist2[linelist2.index(x)] = x[:-4]
                if x[-2:] == 'ly' or x[-3:] == 'lly':
                    linelist2[linelist2.index(x)] = x[:-2]
                if x[-4:] == 'ment':
                    linelist2[linelist2.index(x)] = x[:-4]
            line = ' '.join(str(x) for x in linelist2)
            writefile.write(line.rstrip('\n'))
            writefile.write(" ")
            linelist3 = line.split()
            for x in linelist3:
                if x in frequencies:
                    frequencies[x] += 1
                else:
                    frequencies[x] = 1
        sumofwords = 0
        for keys in frequencies:
            sumofwords += frequencies[keys]
        for keys in frequencies:
            termfrequencies[keys] = frequencies[keys] / sumofwords
        nesteddict[file.strip()] = termfrequencies
        numberofdocs += 1
    wordfoundin = {}

    for keys in nesteddict:
        for x in nesteddict[keys]:
            if x in wordfoundin:
                wordfoundin[x] += 1
            else:
                wordfoundin[x] = 1
    for keys in nesteddict:
        idf[keys] = {}
        for x in nesteddict[keys]:
            if wordfoundin[x] != 0:
                idf[keys][x] = math.log(numberofdocs / wordfoundin[x])
            else:
                idf[keys][x] = 0
                idf[keys][x] += 1
    for keys in idf:
        for x in idf[keys]:
            idf[keys][x] += 1
    for keys in idf:
        tfidfdict[keys] = {}
        for x in idf[keys]:
            score = nesteddict[keys][x] * idf[keys][x]
            score = round(score,2)
            tfidfdict[keys][x] = score
    for keys in tfidfdict:
        lis = [(k, v) for k,v in tfidfdict[keys].items()]
        tfidfdict[keys] = lis
    for keys in tfidfdict:
        tfidfdict[keys] = sorted(tfidfdict[keys],key = lambda x: x[1],reverse = True)
    for keys in tfidfdict:
        for i in range(0, len(tfidfdict[keys])):
            for j in range(i+1,len(tfidfdict[keys])):
                temp = ''
                if tfidfdict[keys][i][1] == tfidfdict[keys][j][1] and tfidfdict[keys][i][0] > tfidfdict[keys][j][0]:
                    temp = tfidfdict[keys][i]
                    tfidfdict[keys][i] = tfidfdict[keys][j]
                    tfidfdict[keys][j] = temp
    for file in open(f):
        filew = open('tfidf_'+file.strip(),'a')
        if len(tfidfdict[file.strip()]) >= 5:
            filew.write("[")
            for x in range(0,4):
                filew.write(str(tfidfdict[file.strip()][x]))
                filew.write(", ")
            filew.write(str(tfidfdict[file.strip()][4]))
            filew.write("]")
        else:
            filew.write("[")
            for x in range(0,len(tfidfdict[file.strip()]) - 1):
                filew.write(str(tfidfdict[file.strip()][x]))
                filew.write(", ")
            filew.write(str(tfidfdict[file.strip()][len(tfidfdict[file.strip()]) - 1]))
            filew.write("]")
        filew.close()
tfidf('tfidf_docs.txt')
