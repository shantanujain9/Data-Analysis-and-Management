import csv
def covidtasks(f):
    with open(f) as covidtrain:
        with open('covidResult.csv','w') as outfile:
            reader = csv.reader(covidtrain)
            lis = list(reader)
            writer = csv.writer(outfile,delimiter =',')
            latlist = {}
            longlist = {}
            citylist = {}
            symptomlist = {}
            provincessymptom = {}
            provincescity = {}
            for i in range(1,len(lis)):
                if "-" in lis[i][1]:
                    first, second = lis[i][1].split("-")
                    avg = round((int(first)+int(second))/2)
                    lis[i][1] = str(avg)
                d1,m1,y1 = lis[i][8].split(".")
                lis[i][8] = m1 + "." + d1 + "." + y1
                d2,m2,y2 = lis[i][9].split(".")
                lis[i][9] = m2 + "." + d2 + "." + y2
                d3,m3,y3 = lis[i][10].split(".")
                lis[i][10] = m3 + "." + d3 + "." + y3
            for i in range(1,len(lis)):
                if lis[i][6] != 'NaN':
                    if lis[i][4] in latlist:
                        latlist[lis[i][4]].append(lis[i][6])
                    else:
                        latlist[lis[i][4]] = [lis[i][6]]
            for i in range(1,len(lis)):
                if lis[i][7] != 'NaN':
                    if lis[i][4] in longlist:
                        longlist[lis[i][4]].append(lis[i][7])
                    else:
                        longlist[lis[i][4]] = [lis[i][7]]
            for i in range(1,len(lis)):
                if lis[i][6] == 'NaN':
                    latsum = 0
                    for elem in latlist[lis[i][4]]:
                        latsum += float(elem)
                    avglat = latsum/len(latlist[lis[i][4]])
                    avglat = round(avglat,2)
                    lis[i][6] = str(avglat)
                if lis[i][7] == 'NaN':
                    longsum = 0
                    for elem in longlist[lis[i][4]]:
                        longsum += float(elem)
                    avglong = longsum/len(latlist[lis[i][4]])
                    avglong = round(avglong,2)
                    lis[i][7] = str(avglong)
            for i in range(1,len(lis)):
                if lis[i][4] in citylist and lis[i][3] != 'NaN':
                    citylist[lis[i][4]].append(lis[i][3])
                elif lis[i][3] != 'NaN':
                    citylist[lis[i][4]] = [lis[i][3]]
            for keys in citylist:
                provincescity[keys] = {}
            for keys in citylist:
                for x in citylist[keys]:
                    if x.strip() in provincescity[keys]:
                        provincescity[keys][x.strip()] += 1
                    else:
                        provincescity[keys][x.strip()] = 1
            for keys in provincescity:
                temp1 = provincescity[keys]
                sorted_temp1 = sorted(temp1.items(),key = lambda x:x[1],reverse = True)
                provincescity[keys] = sorted_temp1
            for keys in provincescity:
                for i in range(0, len(provincescity[keys])):
                    for j in range(i+1,len(provincescity[keys])):
                        temp2 = ''
                        if provincescity[keys][i][1] == provincescity[keys][j][1] and provincescity[keys][i][0] > provincescity[keys][j][0]:
                            temp2 = provincescity[keys][i]
                            provincescity[keys][i] = provincescity[keys][j]
                            provincescity[keys][j] = temp2
            for i in range(1,len(lis)):
                if lis[i][3] == 'NaN':
                    popularcity = provincescity[lis[i][4]][0][0]
                    lis[i][3] = str(popularcity)
            for i in range(1,len(lis)):
                if lis[i][4] in symptomlist:
                    x = lis[i][11].split(";")
                    for elem in x:
                        elem = elem.strip()
                        if elem != 'NaN':
                            symptomlist[lis[i][4]].append(elem)
                else:
                    x = lis[i][11].split(";")
                    for elem in x:
                        elem = elem.strip()
                    symptomlist[lis[i][4]] = [x[0]]
                    for i in range(1,len(x)):
                        if x[i] != 'NaN':
                            symptomlist[lis[i][4]].append(x[i])
            for keys in symptomlist:
                provincessymptom[keys] = {}
            for keys in symptomlist:
                for x in symptomlist[keys]:
                    if x.strip() in provincessymptom[keys]:
                        provincessymptom[keys][x.strip()] += 1
                    else:
                        provincessymptom[keys][x.strip()] = 1
            for keys in provincessymptom:
                temp = provincessymptom[keys]
                sorted_temp = (sorted(temp.items(),key = lambda x: x[1], reverse = True))
                provincessymptom[keys] = sorted_temp
            for keys in provincessymptom:
                for i in range(0, len(provincessymptom[keys])):
                    for j in range(i+1,len(provincessymptom[keys])):
                        temp = ''
                        if provincessymptom[keys][i][1] == provincessymptom[keys][j][1] and provincessymptom[keys][i][0] > provincessymptom[keys][j][0]:
                            temp = provincessymptom[keys][i]
                            provincessymptom[keys][i] = provincessymptom[keys][j]
                            provincessymptom[keys][j] = temp
            for i in range(1,len(lis)):
                if lis[i][11] == 'NaN':
                    popularsymptom = provincessymptom[lis[i][4]][0][0]
                    lis[i][11] = popularsymptom
            writer.writerows(lis)
    covidtrain.close()
    outfile.close()
covidtasks('covidTrain.csv') 


        
