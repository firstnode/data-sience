from app import app
import csv

@app.route('/<name>')
def home(name):
        with open(name+'.csv', 'r') as csvFile:
            return datas(csvFile)
 



def datas(x):
    body='<html><table>'
    reader = csv.DictReader(x)
    for i,row in enumerate(reader):
        rows=''            
        for j,cell in enumerate(row):
            if(i==0):
                rows +='<th>'+cell+'</th>'
            else:
                rows +='<td>'+row[cell]+'</td>'
        body += '<tr>'+rows+'</tr>'
    body +='</table></html>'   
    return body
