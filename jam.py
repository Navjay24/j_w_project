from bs4 import BeautifulSoup
import requests
from pathlib import Path
import plotly.express as px
import streamlit as st
import pandas as pd
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"

st.markdown("<head>IIT JAM 2025 MATHEMATICS RANK PREDICTOR AND MARKS CALCULATOR</head>"
            "<br>check validity of the response sheet link and then press confirm",unsafe_allow_html=True)

df=pd.read_csv('https://docs.google.com/spreadsheets/d/1SZG2rLsInIKdvUoX1Z-Ha-x5Evnaws8avNQd9PCsY_8/export?format=csv')

ul=df.to_dict()
ul=ul['url']
ul=list(ul.values())
ml=sorted(list(df.to_dict()['marksgroup'].values()))[::-1]

query_params = st.experimental_get_query_params()
url=query_params.get("link",[""])[0]

st.markdown(f'<form><input name="link" required><button type="submit">check validity of link</button></form>',unsafe_allow_html=True)

try:
    question_id_prefix='9536411'
    a_key=[
    'C',
    'B',
    'A',
    'A',
    'A',
    'D',
    'B',
    'C',
    'A',
    'A',
    'B',
    'B',
    'B',
    'C',
    'A',
    'B',
    'B',
    'D',
    'D',
    'A',
    'B',
    'C',
    'A',
    'C',
    'A',
    'B',
    'C',
    'B',
    'A',
    'C',
    'A;C;D',
    'A;B;C',
    'A;B;D',
    'B;D',
    'A;B',
    'A;C;D',
    'B;D',
    'B;C;D',
    'B;D',
    'C;D',
    [1.98, 2.02],
    [3.98, 4.02],
    [1.98, 2.02],
    [1.39, 1.43],
    [2.98, 3.02],
    [2, 2],
    [3.98, 4.02],
    [2.31, 2.35],
    [1, 1],
    [2.98, 3.02],
    [1.98, 2.02],
    [3, 3],
    [9, 9],
    [5.20, 5.24],
    [0.98, 1.02],
    [3.98, 4.02],
    [12.98, 13.02],
    [1, 1],
    [10, 10],
    [0, 0]]

    page=requests.get(url)
    soup=BeautifulSoup(page.text, "html.parser")
    p=str(soup)
    p=p.split('<div class="question-pnl"')
    p=p[1:]
    q_list=['']*60
    for i in p:
        t=i.find('<td class="bold">'+question_id_prefix)
        q_list[int(i[t+24:t+27])-141]=i
    nat_q_list=q_list[40:]
    q_list=q_list[:40]
    for i in range(len(q_list)):
        q_list[i]=q_list[i].split('class="menu-tbl"')
        q_list[i][0]=q_list[i][0].split('<td style="text-align: left;">')[1:]
    answered=['']*60
    c=0
    q_secb_list=q_list[30:]
    q_list=q_list[:30]
    for i in q_list:
        t=i[1].find('</td></table></td></tr></table></div>')
        if i[0][0][0]==i[1][t-1]:
            t2=i[0][0].find('.jpg')
            if (int(i[0][0][t2-3:t2])-2)%5==0:
                answered[c]=('A')
                c+=1
            elif (int(i[0][0][t2-3:t2])-3)%5==0:
                answered[c] = ('B')
                c += 1
            elif (int(i[0][0][t2-3:t2])-4)%5==0:
                answered[c] = ('C')
                c += 1
            elif (int(i[0][0][t2-3:t2])-5)%5==0:
                answered[c] = ('D')
                c += 1
        elif i[0][1][0] == i[1][t-1]:
            t2 = i[0][1].find('.jpg')
            if (int(i[0][1][t2 - 3:t2])-2) % 5==0:
                answered[c] = ('A')
                c += 1
            elif (int(i[0][1][t2 - 3:t2])-3) % 5==0:
                answered[c] = ('B')
                c += 1
            elif (int(i[0][1][t2 - 3:t2])-4) % 5==0:
                answered[c] = ('C')
                c += 1
            elif (int(i[0][1][t2 - 3:t2])-5) % 5==0:
                answered[c] = ('D')
                c += 1
        elif i[0][2][0] == i[1][t-1]:
            t2 = i[0][2].find('.jpg')
            if (int(i[0][2][t2 - 3:t2])-2) % 5==0:
                answered[c] = ('A')
                c += 1
            elif (int(i[0][2][t2 - 3:t2])-3) % 5==0:
                answered[c] = ('B')
                c += 1
            elif (int(i[0][2][t2 - 3:t2])-4) % 5==0:
                answered[c] = ('C')
                c += 1
            elif (int(i[0][2][t2 - 3:t2])-5) % 5==0:
                answered[c] = ('D')
                c += 1
        elif i[0][3][0] == i[1][t-1]:
            t2 = i[0][3].find('.jpg')
            if (int(i[0][3][t2 - 3:t2]) - 2) % 5==0:
                answered[c] = ('A')
                c += 1
            elif (int(i[0][3][t2 - 3:t2])-3) % 5==0:
                answered[c] = ('B')
                c += 1
            elif (int(i[0][3][t2 - 3:t2])-4) % 5==0:
                answered[c] = ('C')
                c += 1
            elif (int(i[0][3][t2 - 3:t2])-5) % 5==0:
                answered[c] = ('D')
                c += 1
        else:
            answered[c]='Not Answered'
            c+=1

    for i in q_secb_list:
        t=i[1].find('</td></table></td></tr></table></div>')
        j=1
        res=""
        while i[1][t-j]!='>':
            if i[1][t-j] in ['A','B','C','D']:
                res+=(i[1][t-j])
            j+=1
        a_res=""
        for j in res:
            if i[0][0][0]==j:
                t2=i[0][0].find('.jpg')
                if (int(i[0][0][t2-3:t2])-2)%5==0:
                    a_res+='A'
                elif (int(i[0][0][t2-3:t2])-3)%5==0:
                    a_res+='B'
                elif (int(i[0][0][t2-3:t2])-4)%5==0:
                    a_res+='C'
                elif (int(i[0][0][t2-3:t2])-5)%5==0:
                    a_res+='D'
            if i[0][1][0]==j:
                t2=i[0][1].find('.jpg')
                if (int(i[0][1][t2-3:t2])-2)%5==0:
                    a_res+='A'
                elif (int(i[0][1][t2-3:t2])-3)%5==0:
                    a_res+='B'
                elif (int(i[0][1][t2-3:t2])-4)%5==0:
                    a_res+='C'
                elif (int(i[0][1][t2-3:t2])-5)%5==0:
                    a_res+='D'
            if i[0][2][0]==j:
                t2=i[0][2].find('.jpg')
                if (int(i[0][2][t2-3:t2])-2)%5==0:
                    a_res+='A'
                elif (int(i[0][2][t2-3:t2])-3)%5==0:
                    a_res+='B'
                elif (int(i[0][2][t2-3:t2])-4)%5==0:
                    a_res+='C'
                elif (int(i[0][2][t2-3:t2])-5)%5==0:
                    a_res+='D'
            if i[0][3][0]==j:
                t2=i[0][3].find('.jpg')
                if (int(i[0][3][t2-3:t2])-2)%5==0:
                    a_res+='A'
                elif (int(i[0][3][t2-3:t2])-3)%5==0:
                    a_res+='B'
                elif (int(i[0][3][t2-3:t2])-4)%5==0:
                    a_res+='C'
                elif (int(i[0][3][t2-3:t2])-5)%5==0:
                    a_res+='D'
        if a_res=="":
            a_res="Not Answered"
        for i in sorted(a_res):
            answered[c]+=i+';'
        c+=1
        answered[c-1]=answered[c-1][:-1]

    for i in nat_q_list:
        t=i.find('Given Answer :<')
        if i[t+37]=='-':
            answered[c]='Not Answered'
            c+=1
        else:
            j=0
            a_res=''
            while i[t+68+j]!='<':
                a_res+=i[t+68+j]
                j+=1
            answered[c]=float(a_res)
            c+=1

    section_a1_attempted=0
    section_a2_attempted=0
    section_b_attempted=0
    section_c1_attempted=0
    section_c2_attempted=0
    section_a1_correct=0
    section_a2_correct=0
    section_a1_incorrect=0
    section_a2_incorrect=0
    section_b_correct=0
    section_c1_correct=0
    section_c2_correct=0
    for i in range(60):
        if i<=9:
            if answered[i]==a_key[i]:
                section_a1_correct+=1
                section_a1_attempted+=1
            elif answered[i]=='Not Answered':
                pass
            else:
                section_a1_incorrect+=1
                section_a1_attempted+=1
        elif i<=29:
            if answered[i]==a_key[i]:
                section_a2_correct+=1
                section_a2_attempted+=1
            elif answered[i]=='Not Answered':
                pass
            else:
                section_a2_incorrect+=1
                section_a2_attempted+=1
        elif i<=39:
            if answered[i]!='Not Answered':
                section_b_attempted+=1
                if answered[i]==a_key[i]:
                    section_b_correct+=1
        elif i<=49:
            if answered[i]!='Not Answered':
                section_c1_attempted+=1
                if (a_key[i][0]<=answered[i]) and (a_key[i][1]>=answered[i]):
                    section_c1_correct+=1
        elif i<=59:
            if answered[i]!='Not Answered':
                section_c2_attempted+=1
                if (a_key[i][0]<=answered[i]) and (a_key[i][1]>=answered[i]):
                    section_c2_correct+=1

    section_a1_marks=float(section_a1_correct+section_a1_incorrect*(-1/3))
    section_a2_marks=float(section_a2_correct*2+section_a2_incorrect*(-2/3))
    section_a_marks=section_a1_marks+section_a2_marks
    section_a1_accuracy=section_a1_correct*100/section_a1_attempted
    section_a2_accuracy=section_a2_correct*100/section_a2_attempted
    section_b_marks=float(section_b_correct*2)
    section_b_accuracy=section_b_correct*100/section_b_attempted
    section_c1_marks=float(section_c1_correct)
    section_c1_accuracy=section_c1_correct*100/section_c1_attempted
    section_c2_marks=float(section_c2_correct*2)
    section_c2_accuracy=section_c2_correct*100/section_c2_attempted
    section_c_marks=section_c1_marks+section_c2_marks
    section_a_correct=section_a1_correct+section_a2_correct
    section_c_correct=section_c1_correct+section_c2_correct
    total_correct=section_a_correct+section_b_correct+section_c_correct
    section_a_incorrect=section_a1_incorrect+section_a2_incorrect
    section_c_attempted=section_c1_attempted+section_c2_attempted
    total_incorrect=section_a_incorrect+section_b_attempted-section_b_correct+section_c_attempted-section_c_correct
    total_attempted=section_a1_attempted+section_a2_attempted+section_b_attempted+section_c_attempted
    total_accuracy=total_correct*100/total_attempted
    section_a_accuracy=section_a_correct*100/(section_a1_attempted+section_a2_attempted)
    section_c_accuracy=section_c_correct*100/section_c_attempted
    total_marks=section_a_marks+section_b_marks+section_c_marks
    section_b_incorrect=section_b_attempted-section_b_correct
    section_c1_incorrect=section_c1_attempted-section_c1_correct
    section_c2_incorrect=section_c2_attempted-section_c2_correct
    section_c_incorrect=section_c_attempted - section_c_correct

    if url not in ul:
        st.markdown(f'<form name="mark-form" method="post" action="https://script.google.com/macros/s/AKfycby3Rxsua58vvl-q_0ffriDxouPeSy6FCQKc160XUHGdruBaQ6gllca7_0VSdW7_emsy/exec">'
                f'<input type="hidden" name="url" value={url}><input type="hidden" name="marks" value={total_marks}><input type="hidden" name="marksgroup" value={round(total_marks)}>'
                '<input type="submit" value="Submit" id="submit"></form>'
                , unsafe_allow_html=True)

    st.markdown(
        f"<table><tr><th>sections:</th><th>A1</th><th>A2</th><th>A</th><th>B</th><th>C1</th><th>C2</th><th>C</th><th>Tot"
        f"al</th></tr><tr><th>incorrect:</th><td>{section_a1_incorrect}</td><td>{section_a2_incorrect}</td><td>{section_a_incorrect}</td>"
        f"<td>{section_b_incorrect}</td><td>{section_c1_incorrect}</td><td>{section_c2_incorrect}</td><td>{section_c_incorrect}</td>"
        f"<td>{total_incorrect}</td></tr><tr><th>correct:</th><td>{section_a1_correct}</td><td>{section_a2_correct}</td><td>{section_a_correct}</td>"
        f"<td>{section_b_correct}</td><td>{section_c1_correct}</td><td>{section_c2_correct}</td><td>{section_c_correct}</td>"
        f"<td>{total_correct}</td></tr><tr><th>attempted:</th><td>{section_a1_attempted}</td><td>{section_a2_attempted}</td><td>{section_a2_attempted+section_a1_attempted}</td>"
        f"<td>{section_b_attempted}</td><td>{section_c1_attempted}</td><td>{section_c2_attempted}</td><td>{section_c_attempted}</td>"
        f"<td>{total_attempted}</td></tr><tr><th>accuracy:</th><td>{(str(section_a1_accuracy)+"00000")[:5]}</td><td>{(str(section_a2_accuracy)+"00000")[:5]}</td><td>{(str(section_a_accuracy)+"00000")[:5]}</td>"
        f"<td>{(str(section_b_accuracy)+"00000")[:5]}</td><td>{(str(section_c1_accuracy)+"00000")[:5]}</td><td>{(str(section_c2_accuracy)+"00000")[:5]}</td><td>{(str(section_c_accuracy)+"00000")[:5]}</td>"
        f"<td>{(str(total_accuracy)+"00000")[:5]}</td></tr><tr><th>marks:</th><td>{(str(section_a1_marks)+"00000")[:5]}</td><td>{(str(section_a2_marks)+"00000")[:5]}</td><td>{(str(section_a_marks)+"00000")[:5]}</td>"
        f"<td>{(str(section_b_marks)+"00000")[:5]}</td><td>{(str(section_c1_marks)+"00000")[:5]}</td><td>{(str(section_c2_marks)+"00000")[:5]}</td><td>{(str(section_c_marks)+"00000")[:5]}</td>"
        f"<th>{(str(total_marks)+"00000")[:5]}</th></tr></table>"
        f"<br>total marks: {total_marks}"
        f"<br>expected rank: {round((ml.index(round(total_marks))+1)*15000/len(ml))} to {round(0.9*(ml.index(round(total_marks))+1)*15000/len(ml))}"
        f"<br>#based on {len(ml)} entries, assuming a total of 15000 students#",unsafe_allow_html=True)

except:
    st.markdown("enter a valid link")