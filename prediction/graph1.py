from .models import data
# import matplotlib
# matplotlib.use('Agg')
from matplotlib import pyplot as plt

all_data = data.objects.all()

usd = []
predict = []
for data1 in all_data:
    usd.append(data1.usdnpr)
    predict.append(data1.predicate)
plt.plot(usd)
plt.plot(predict)
plt.show()