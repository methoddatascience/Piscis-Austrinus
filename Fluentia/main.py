import pandas as pd
from gmplot import gmplot

print 'Acknowledgement:'
print 'The credit of this project goes to Method Data Science, team Piscis Austrinus and involved client/s'
print '================\n'


def risk_metric(sc, season):
    #print sc, '::::', season
    #print (sc[0]*season[0])*100/(.7*41)
    return ((sc * season) * 100 / (.7 * 41))


def score(x, y):
    df = pd.read_csv('data/conf.csv')
    samelat = df['lat'] == x
    samelon = df['lon'] == y
    #print df[samelat & samelon]['score']
    return df[samelat & samelon]['score'].values


def seasonality(w):
    df = pd.read_csv('data/season.csv')
    sameweek = df['week'] == w
    #print df[sameweek]['max']
    return df[sameweek]['max'].values


#print seasonality(14)

#user input
w = raw_input('enter week number<int>: ')
w = int(w)
if w > 52:
    w = 52
elif w < 1:
    w = 1

#target zones
zfile = open('data/zfile.txt')
locs = []
for line in zfile:
    x = float(line.split()[0])
    y = float(line.split()[1])
    locs.append((x, y))

#mapping
gmap = gmplot.GoogleMapPlotter(34.730133, -86.614437, 13)

high = []
mod = []
low = []

#measure safety for each zone for week w
for p in locs:
    px = p[0]
    py = p[1]

    prediction = risk_metric(score(px, py), seasonality(w))

    #safety measure classification
    if prediction < 30:
        low.append((px, py))
    elif 30 <= prediction < 70:
        mod.append((px, py))
    else:
        high.append((px, py))

#gmap.scatter(risky_lats, risky_lons, color='red', size=500, marker=False)

#plot on google maps
try:
    highx, highy = zip(*high)
    gmap.scatter(highx, highy, color='red', size=500, marker=False)
except:
    pass

try:
    modx, mody = zip(*mod)
    gmap.scatter(modx, mody, color='blue', size=300, marker=False)
except:
    pass

try:
    lowx, lowy = zip(*low)
    gmap.scatter(lowx, lowy, color='yellow', size=150, marker=False)
except:
    pass

#output
gmap.draw('prediction_week' + str(w) + '.html')
