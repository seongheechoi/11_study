import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np



url = 'https://library.busan.go.kr/gsmbooks/member/loginProc'
ids = ['next450', 'isaiah496', 'gaeul1113', 'mekim0924', 'mjchoi0902']
df_tot = pd.DataFrame(index=range(0), columns=['No', '책제목', '도서관', '코드', '대출일자', '반납일자'])
for id in ids:
    data = {
        "return_url": "",
        "id": id,
        "password": "sktkrkwk51!"
    }

    with requests.Session() as s:
        response = s.post(url, data=data)
        soup = bs(response.text, "html.parser")
        tag = soup.find("a", {"href":"javascript:goMenu('Y', '/gsmbooks/member/mylibrary/loanDetailsConfirm', '');"})
        result = s.get('https://library.busan.go.kr/gsmbooks/member/mylibrary/loanDetailsConfirm')
        soup2 = bs(result.text, 'html.parser')
        tag2 = soup2.find("section")
    #tds = list(tag2.find_all("td"))
        columns = tag2.select('tbody > tr')
        columnlist = []
        for column in columns:
            columnlist.append(column.text)
        df = pd.DataFrame(columns = columnlist)
        contents = tag2.select('tbody')
        dfcontent=[]
        alldfcontents=[]

        for content in contents:
            tds = content.find_all("td")
            for td in tds:
                dfcontent.append(td.text)
            alldfcontents.append(dfcontent)
            dfcontent=[]

    N_component = np.shape(alldfcontents)[1]
    if N_component == 1:
        continue
    N_index = int(np.shape(alldfcontents)[1]/8)
    df = pd.DataFrame(index = range(0, N_index), columns=['No', '책제목', '도서관', '코드', '대출일자', '반납일자'])

    no = []
    Title = []
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []

    for i in range(0,N_component):
        if i%8 == 0:
            no.append(alldfcontents[0][i])
        elif i%8 == 1:
            Title.append(alldfcontents[0][i])
        elif i%8 == 2:
            a.append(alldfcontents[0][i])
        elif i%8 == 3:
            b.append(alldfcontents[0][i])
        elif i%8 == 4:
            c.append(alldfcontents[0][i])
        elif i%8 == 5:
            d.append(alldfcontents[0][i])

    df.No = no
    df['책제목'] = Title
    df['도서관'] = a
    df['코드']= b
    df['대출일자'] = c
    df['반납일자'] = d
    df_tot = pd.concat([df_tot, df], axis=0)

print(df_tot)
df_tot.to_excel('도서대출목록.xlsx', index=False)
df_tot.to_html("도서목록.html")