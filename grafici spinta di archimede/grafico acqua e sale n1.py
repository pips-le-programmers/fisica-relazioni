import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
import math as m

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






a1 = Point("0,000012	±	0,000001", "0,14	±	0,02","1cm")
a2 = Point("0,000023	±	0,000001","0,29	±	0,02","2cm")
a3= Point('0,000035	±	0,000001','0,45	±	0,02','3cm')
a4= Point('0,000046	±	0,000001','0,61	±	0,02','4 cm')
a5= Point('0,000058	±	0,000002','0,75	±	0,02','5 cm')
a6= Point('0,000069	±	0,000002','0,90 ±	0,02','6 cm')
plt.style.use("ggplot")

#variabili
a = 0

dati = [a1, a2, a3, a4, a5, a6]
dati_x = [h.x for h in dati]
dati_y = [h.y for h in dati]
inc_x_0 = [h.inc_x for h in dati]
inc_y = [h.inc_y for h in dati]
fig, ax = plt.subplots()

ax.plot(dati_x , dati_y , 'b.' , label="valore medio dato")
for count in range(len(dati_x)):
    x = dati_x[count]
    y = dati_y[count]
    width = inc_x_0[count]*2
    height = inc_y[count]*2
    if(not a):
        ellipse = Ellipse((x,y) , width , height , fill=False , color="c",label="incertezza dato")
        a = 1
    else:
        ellipse = Ellipse((x,y) , width , height , fill=False , color="c")
    ax.add_artist(ellipse)



#mouse 
coeff_1 = 0

def onclick(event):
    global coeff_1
    coeff = event.ydata / event.xdata
    if coeff_1 != 0:
        coeff_med= (coeff_1+coeff)/2
        retta_fit= math_function(coeff_med, dati_x)
        plt.plot(retta_fit[0] , retta_fit[1], color="#e3098c", label='retta di fit' )
        print(coeff)
        print(coeff_1)
        print(f"{coeff_med} ± {abs(coeff_1-coeff)/2}")
        plt.legend(loc="upper left")
    coeff_1 = coeff
    retta = math_function(coeff, dati_x)
    plt.plot(retta[0] , retta[1], "--", color='#0c9126', label="rette di max e min pendenza")


cid = fig.canvas.mpl_connect('key_press_event', onclick)

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


plt.xlim(0 , 10**-4 )
plt.ylim(0 , 1 )


plt.show()
