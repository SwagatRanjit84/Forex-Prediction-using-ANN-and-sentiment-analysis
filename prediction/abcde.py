import matplotlib.pyplot as plt

x = [1,2,3]
y = ['aa','ads']
plt.plot(x, label = 'Actual price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Fundamental Analysis', )
plt.legend()
plt.show()

#
# import numpy as np
# import matplotlib.pyplot as plot
# import matplotlib.ticker as mticker
# from matplotlib import dates
# import datetime
#
# fig = plot.figure(1)
# DAU = (  2,  20,  25,  60, 190, 210,  18, 196, 212, 200, 160, 150, 185, 175, 316, 320, 294, 260, 180, 145, 135,  97,  84,  80,  60,  45,  37,  20,  20,  24,  39,  73,  99)
# WAU = ( 50, 160, 412, 403, 308, 379, 345, 299, 258, 367, 319, 381, 461, 412, 470, 470, 468, 380, 290, 268, 300, 312, 360, 350, 316, 307, 289, 321, 360, 378, 344, 340, 346)
# MAU = (760, 620, 487, 751, 612, 601, 546, 409, 457, 518, 534, 576, 599, 637, 670, 686, 574, 568, 816, 578, 615, 520, 499, 503, 529, 571, 461, 614, 685, 702, 687, 649, 489)
#
# firstDay = datetime.datetime(2012,1,15)     #15. Januar 2012
#
# dayArray = [firstDay + datetime.timedelta(days=i) for i in range(len(DAU))]
#
# ax = plot.subplot(111)
#
# line1 = ax.plot(dayArray, DAU, 'o-', color = '#336699')
# line2 = ax.plot(dayArray, WAU, 'o-', color = '#993333')
# line3 = ax.plot(dayArray, MAU, 'o-', color = '#89a54e')
#
# ax.xaxis.set_major_formatter(dates.DateFormatter('%m, %Y'))
# plot.show()

#
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array([0,1,2,3,123,123,123,12,312,3,12,31,23,123,12,3])
# my_xticks = ['John','Arnold']
# plt.xticks(x, my_xticks)
# plt.plot(x)
# plt.show()
#


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# time = pd.date_range('01/01/2014', '4/01/2014', freq='H')
# values = np.random.normal(0, 1, time.size).cumsum()
#
#
# fig, ax = plt.subplots()
# ax.plot_date(time, values, marker='', linestyle='-')
#
# fig.autofmt_xdate()
# plt.show()


import matplotlib.pyplot as plt
import pandas as pd

index = ["Jan 2,2012", "Jan 2,2012", "Jan 2,2012", "Jan 2,2012", "Jan 2,2012", "Jan 2,2012", "Jan 2,2012", "Jan 2,2012" , "Jan 2,2012", "Jan 2,2012", "Jan 2,2012", "Jan 2,2012", "Jan 2,2012", "Jan 2,2012"]
a = [1, 2, 3, 4,12,31,23,12,31,23,132,1,23,123]
df = pd.DataFrame(a, columns=["Value"], index=index)
ax = df.plot( rot=90)

threshold = 30
for t in ax.get_xticklabels():
    if len(t.get_text()) > threshold:
        t.set_rotation(90)

plt.tight_layout()
plt.show()

