from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
import mglearn
import matplotlib.pyplot as plt

x, y = make_blobs(random_state=1)
print(x)
agg = AgglomerativeClustering(n_clusters=3)
assignment = agg.fit_predict(x)


mglearn.discrete_scatter(x[:, 0], x[:, 1], assignment)
plt.legend(['cluster0', 'cluster1', 'cluster2'], loc='best')
plt.xlabel('attr0')
plt.ylabel('attr1')
plt.show()