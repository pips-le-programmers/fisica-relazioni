import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
import math as m
from colour import Color

class Measure:
    def __init__(self , measure:str) -> None:
        self.measure = measure.replace("," , ".").split("±")
        self.inc = float(self.measure[1])
        self.m = float(self.measure[0])

class Point:
    def __init__(self , x ,y , name , dist_x=0 , dist_y=0):
        self.x_measure = Measure(x)
        self.y_measure = Measure(y)
        self.x = self.x_measure.m
        self.y = self.y_measure.m
        self.inc_x = self.x_measure.inc
        self.inc_y = self.y_measure.inc
        self.name = name
        self.dist_x = dist_x
        self.dist_y = dist_y

def math_function(coeff , dati_x):
    f_fit = lambda x: coeff*x
    look_up_table = {dato.x:dato.inc_x for dato in dati}
    retta_fit_x = np.arange(0 , max(dati_x)+look_up_table[max(dati_x)] , 0.00000001)
    retta_fit_y = list(map(f_fit , retta_fit_x))
    return retta_fit_x , retta_fit_y






a1 = Point("0,000012	±	0,000001", "0,14	±	0,04","")
a2 = Point("0,000023	±	0,000001","0,30	±	0,04",'')
a3= Point('0,000035	±	0,000001','0,44	±	0,04','')
a4= Point('0,000046	±	0,000001','0,60	±	0,04','')
a5= Point('0,000058	±	0,000002','0,74 ±	0,04','')
a6= Point('0,000069	±	0,000002','0,88 ±	0,04','')
a7 = Point("0,000012	±	0,000001", "0,14	±	0,02","")
a8 = Point("0,000023	±	0,000001","0,29	±	0,02","")
a9= Point('0,000035	±	0,000001','0,45	±	0,02','')
a10= Point('0,000046	±	0,000001','0,61	±	0,02','')
a11= Point('0,000058	±	0,000002','0,75	±	0,02','')
a12= Point('0,000069	±	0,000002','0,90 ±	0,02','')
a13= Point("0,000012	±	0,000001", "0,11	±	0,02","")
a14= Point("0,000023	±	0,000001","0,21	±	0,02","")
a15= Point('0,000035	±	0,000001','0,31	±	0,02','')
a16= Point('0,000046	±	0,000001','0,40	±	0,02','')
a17= Point('0,000058	±	0,000002','0,51	±	0,02','')
a18= Point('0,000069	±	0,000002','0,61	±	0,02','')
a19= Point("0,000012	±	0,000001", "0,10	±	0,04"," ")
a20= Point("0,000023	±	0,000001","0,20	±	0,04"," ")
a21= Point('0,000035	±	0,000001','0,30	±	0,04','')
a22= Point('0,000046	±	0,000001','0,40	±	0,04','')
a23= Point('0,000058	±	0,000002','0,50	±	0,04','')
a24= Point('0,000069	±	0,000002','0,60	±	0,04','')
a25= Point("0,000012	±	0,000001", "0,12	±	0,04"," ")
a26= Point("0,000023	±	0,000001","0,26	±	0,04","")
a27= Point('0,000035	±	0,000001','0,38	±	0,04','')
a28= Point('0,000046	±	0,000001','0,50	±	0,04','')
a29= Point('0,000058	±	0,000002','0,62	±	0,04','')
a30= Point('0,000069	±	0,000002','0,74	±	0,04','')
a31= Point("0,000012	±	0,000001", "0,13	±	0,02"," ")
a32= Point("0,000023	±	0,000001","0,25	±	0,02","")
a33= Point('0,000035	±	0,000001','0,37	±	0,02','')
a34= Point('0,000046	±	0,000001','0,49	±	0,02','')
a35= Point('0,000058	±	0,000002','0,60	±	0,02','')
a36= Point('0,000069	±	0,000002','0,73	±	0,02','')


#plt.style.use("_mlp-gallery-nogrid")


#variabili
a = 0

dati = [a1, a2, a3, a4, a5, a6,a7,a8,a9,a10,a11,a12,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36]
dati_x = [h.x for h in dati]
dati_y = [h.y for h in dati]
inc_x_0 = [h.inc_x for h in dati]
inc_y = [h.inc_y for h in dati]

#fa i dati correlati+rumore

x=np.array(dati_x)
y=np.array(dati_y)

#plot
fig, ax = plt.subplots()

#divisione per colori delle batterie di misure
colors_pre = ['#16a7db','#0c22c9','#0be663','#46990f','#d40f0f','#e37210']

colors = []
for i,dato in enumerate(dati):
    a = Color(colors_pre[int(i/7)])
    a.set_luminance(Color(colors_pre[int(i/7)]).get_luminance()*dato.y)
    b = a.get_hex()
    colors.append(b)

print(colors)
ax.scatter(dati_x, dati_y, [inc_x*500000000 for inc_x in inc_x_0],c=np.array(colors))




#aggiunge etichetta ai punti
for h in dati:
    text = f'{h.name}'
    x = h.x
    y = h.y
    dist_x = h.dist_x
    dist_y = h.dist_y
    inc_y_int = h.inc_y
    p = 0
    if inc_y_int > 0.5:
        p = 10
    plt.annotate(text,(x+dist_x,y+dist_y),textcoords="offset points",xytext=(0,0),ha='center')

plt.show()
