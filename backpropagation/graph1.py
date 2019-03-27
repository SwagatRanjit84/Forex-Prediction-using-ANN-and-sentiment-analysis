from .models import data1

# import matplotlib
# matplotlib.use('Agg')
from matplotlib import pyplot as plt

all_data = data1.objects.all()

usd = []
predict = []
for data1 in all_data:
    usd.append(data1.closea)
    predict.append(data1.predicatea)
plt.plot(usd)
plt.plot(predict)
plt.show()