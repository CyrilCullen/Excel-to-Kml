import pandas as pd
import simplekml

df = pd.read_excel("����.xls").fillna('')

λ�ü��� = []
[λ�ü���.append(i) for i in list(df['λ��1']) if not i in λ�ü���]
kml = simplekml.Kml()
doc = kml.newdocument(name = '����λ��')
fld = []
pnt = []
for i in range(len(λ�ü���)):
    fld.append(doc.newfolder(name = λ�ü���[i]))

sharedstyle = simplekml.Style()
sharedstyle.labelstyle.scale = 0.85
sharedstyle.iconstyle.color = 'ff0000aa'
sharedstyle.iconstyle.scale = 0.7
sharedstyle.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
      

for j in range(len(df['����'])):
    pnt.append(fld[λ�ü���.index(df.ix[j]['λ��1'])].newpoint())
    pnt[j].name = df.ix[j]['����']
    pnt[j].description = df.ix[j]['����'] + ',' + df.ix[j]['λ��1'] + ',' + df.ix[j]['λ��2'] + ',' + df.ix[j]['λ��3'] + ',' + df.ix[j]['����'] 
    pnt[j].coords = [(df.ix[j]['����'], df.ix[j]['γ��'])]
    pnt[j].style = sharedstyle

kml.save('����.kml')