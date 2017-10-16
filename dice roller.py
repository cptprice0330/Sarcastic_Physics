from random import randint

import plotly

print("Rolling a D6 4 million times ")

x= [0]
y=[0]
axis = [0]
doubleCount = 0
for i in range (1,2000000):
    x.append(randint(1,6))
    y.append(randint(1,6))
    axis.append(i)
    if x[i] == 6 and y[i]== 6:
        doubleCount += 1

trace = plotly.graph_objs.Scatter(x =axis,y = x)
trace1 = plotly.graph_objs.Scatter(x = axis,y = y)
data = [trace,trace1]
print("Double six is rolled ",doubleCount," times.")
#plotly.offline.plot(data,filename = 'Dice.html')

z = [x + y for x, y in zip(x, y)]
Dice_1 = plotly.graph_objs.Histogram(x =x, opacity = 0.75,histnorm = 'probability',xbins=dict(start=1.5,end=6.5,size=1),name ='Dice 1')
Dice_2 = plotly.graph_objs.Histogram(x =y, opacity = 0.25,histnorm = 'probability',xbins=dict(start=1.5,end=6.5,size=1),name ='Dice 2')
Cumulative_Dice = plotly.graph_objs.Histogram(x =z, opacity = 0.75,histnorm = 'probability',xbins=dict(start=1.5,end=13.5,size=1),name ='Cumulative')
data=[Dice_1,Dice_2,Cumulative_Dice]
layout = plotly.graph_objs.Layout(title = 'Dice roll histogram',xaxis = dict(title = 'Diceroll'),yaxis = dict(title = 'probablity'), bargap = 0.2,)
fig = plotly.graph_objs.Figure(data=data,layout = layout)
plotly.offline.plot(fig,filename='DiceHistogramme.html')
doublePercent = (doubleCount/2000000)*100
print("%Double Six: ",doublePercent)
