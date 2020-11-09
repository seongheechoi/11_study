from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import mglearn
import matplotlib.pyplot as plt

x, y = make_moons(random_state=0, n_samples=200, noise=0.05)

scaler = StandardScaler()
scaler.fit(x)
x_scaled = scaler.transform(x)

dbscan = DBSCAN(eps=0.5)
clusters = dbscan.fit_predict(x_scaled)
plt.scatter(x_scaled[:, 0], x_scaled[:, 1], c=clusters, cmap=mglearn.cm2, s=60, edgecolors='black')
plt.xlabel('attr0')
plt.ylabel('attr1')
plt.show()