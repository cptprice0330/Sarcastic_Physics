import plotly

a = 154516873219
b = 624954654657
c = 954687651
m = 1457698563589

y =(a*(b+c)) %m
yx = [y]
x= [0]
for i in range (0, 100):
    c = yx[i]/56
    yx.append((a*(b+c))%m)
    x.append(i)
print(yx)
trace = plotly.graph_objs.Scatter(x =x, y = yx)
data = [trace]
plotly.offline.plot(data, filename= 'SudoRandom.html')