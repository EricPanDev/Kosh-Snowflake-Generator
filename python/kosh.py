# note that i compressed it, sorry for bad readability - eric
import turtle as m;d=input("Depth (1-5): ")
def k(t,n,l):
 if n==0:t.fd(l)
 else:
  for a in[60,-120,60,0]:k(t,n-1,l/3);t.lt(a)
w=m.Screen();w.title("von Koch snowflake Generator | Eric & Danny");p=m.Turtle();p.speed(0);p.hideturtle();p.pu();p.goto(-100,50);p.pd()
for _ in[0,1,2,3]:k(p,int(d),250);p.rt(120)
m.done()
