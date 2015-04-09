import datetime, time
import sys

spd = float(60*60*24)

start = "2015-04-07-00h00m00s"
start = datetime.datetime.strptime(start, "%Y-%m-%d-%Hh%Mm%Ss")
last = ""

dayssince = []
pages = []

# the template already has 8 pages. thx reecer.
dayssince.append(0)
pages.append(8)

with open("pages.md") as file:
    for line in file.readlines():

        line = line.strip()
        if not line:
            continue
        if not line.count(" ") == 2:
            sys.exit("what the fuck")

        _, date, pagecount = line.split(" ")
        date = date.replace("[", "")
        date = date.replace("]", "")

        current = datetime.datetime.strptime(date, "%Y-%m-%d-%Hh%Mm%Ss")
        delta = current - start
        dayssince.append(delta.days + delta.seconds/spd)
        pages.append(int(pagecount))
        lasttime, lastpages = current, pagecount

import numpy as np
dayssince = np.array(dayssince)
pages     = np.array(pages)

from matplotlib import rcParams
rcParams["font.family"] = "sans-serif"
rcParams["font.sans-serif"] = ["Helvetica"]
rcParams["font.size"] = "20"
import matplotlib.pyplot as plt

now = datetime.datetime.now()
maxdayssince = (now - start).days + (now - start).seconds/spd

ax = plt.gca()
ax.xaxis.set_label_coords(0.67, -0.07)
ax.yaxis.set_label_coords(-0.10, 0.9)

# configure plot
plt.xlabel("Days since start (April 7, 2015)")
plt.ylabel("Pages")
plt.title("")
plt.text(0.8*maxdayssince, 1.22*max(pages), r"%s pages"   % (lastpages))
plt.text(0,                1.22*max(pages), r"Updated %s" % (lasttime))
plt.axis([-1, maxdayssince+1, 0, 1.2*max(pages)])
plt.grid(False)
plt.plot(dayssince, pages, "-")
plt.plot(dayssince, pages, "rd")
plt.fill_between(dayssince, 0, pages, facecolor='blue', interpolate=True)

# annotate
rcParams["font.size"] = "16"
ysep = 7

# thanksgiving
#days = (datetime.datetime.strptime("2014-11-27-00h00m00s", "%Y-%m-%d-%Hh%Mm%Ss") - start).days
#plt.text(days-6, 123+ysep, r"Thanks-")
#plt.text(days-4, 110+ysep, r"giving")
#plt.plot([days, days], [30, 110], "k-")


# guiding lines
#xsep = 4
#ysep = 25
#plt.plot([ 40,       25], [ 40,  50],      "w-") # gathering plots
#plt.plot([ 80+xsep,  80], [ 55,  55+ysep], "w-") # prospects
#plt.plot([ 87+xsep,  87], [ 85,  85+ysep], "w-") # taus, analysis
#plt.plot([ 93+xsep,  93], [115, 115+ysep], "w-") # LHC, ATLAS
#plt.plot([101+xsep, 101], [145, 145+ysep], "w-") # theory

# save
rcParams["font.size"] = "20"
plt.savefig("pages.png")
plt.savefig("pages.pdf")
