entries = os.listdir('F:\\IMDB_Cleaned\IMDB\divide')
p=0
for entry in entries:
    f=open(os.path.join('F://IMDB_Cleaned/IMDB/divide',entry),'r',encoding='UTF-8')
    print(entry+'start')
    print(p)
    s=f.read().split('\n')
    data=[]
    print('file readed succesfully')
    for i in s:
        text="".join(i)
        text=text.split('\t')
        data.append(text)
    data=pd.DataFrame(data) 
    print('converted to dataframe')
    for column in data.columns:
        data[column] = data[column].str.replace(r"\[\"", "")
        data[column] = data[column].str.replace(r"\"\]", "")
        data[column]=  data[column].str.replace(r"\\N.*","")
    print('data cleaning done')
    print(data.head())
    data.to_csv(os.path.join('F://IMDB_Cleaned/IMDB/conq/',str(p)+'.csv'),index=False,header=False,encoding='utf-8-sig')
    p+=1
    print(str(p)+'.csv'+' succesfully')
    f.close()