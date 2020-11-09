from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import mglearn
from sklearn.model_selection import KFold
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix, classification_report

# 1. sklearn datasets 에서 제공하는 iris 데이터를 읽어 온다
iris = load_iris()
#print(iris.data)
#print(iris.target)
#print(iris.target_names)

# 2. 읽어온 iris 데이터를 모델에 적용하기 위해 train_data와 test_data로 분류한다. 이때 데이터 비율은 train_data 80%, test_data 20%로 한다
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=0)
print('훈련 세트의 크기: {}  테스트 세트의 크기: {}'.format(X_train.shape[0], X_test.shape[0]))

# 3. RBF SVM 모델링을 하기 위해 2번에서 분류한 데이터를 스케일링 한다. 이때 코드에 스케일링할 때 사용한 scaler 기본 설명과 그 scaler를 선택한 이유를 주석으로 적는다.\

fig1, axes1 = plt.subplots(1, 2, figsize=(8, 4))
axes1[0].boxplot(X_train, manage_ticks=False)    # 박스 플롯으로 확인해보면 학습데이터는 4개의 attribute 으로 구성되어 있고 그 범위가 각각 틀리다. 특히 2번째 attr. 그 범위가 매우 좁아 스케일 조정이 필요하다

scaler = MinMaxScaler().fit(X_train)    # 스케일러는 원래 데이터 범위를 0~1로 바꿔주는 minmax scaler를 사용하였다. 그래프 참조
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
axes1[1].boxplot(X_train_scaled, manage_ticks=False)
#plt.show()

# 4. 3번에서 만든 데이터를 가지고 RBF SVM 모델에 적합한 매개 변수 C와 gamma 를 찾는다. 이때 5겹 계층별 교차 검증으로 GridSearchCV 객체를 생성하여 적용한다.
kfold = KFold(n_splits=5, shuffle=True, random_state=0)

param_grid = {'C':[0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50, 100],               # grid 파라미터 생성
              'gamma':[0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50, 100]}

grid_search = GridSearchCV(SVC(), param_grid, cv=kfold, return_train_score=True)
grid_search.fit(X_train_scaled, y_train)
#print('테스트 세트 점수: {:.2f}'.format(grid_search.score(X_test_scaled, y_test)))
print('최적 매개변수 :', grid_search.best_params_)
#print('최고 교차 검증 점수 : {:.2f}'. format(grid_search.best_score_))

# 5. y축을 꽃잎의 폭으로 x축을 꽃잎의 길이로 하여 SVM 모델 예측 값과 예측에 사용한 iris 데이터를 도식화한다. (iris 데이터는 산점도로 도식화한다)
svm = SVC(kernel='rbf', random_state=1, C=5, gamma=0.1)   # 최적의 파라미터를 이용하여 학습
svm.fit(X_train_scaled, y_train)
y_train_pred = svm.predict(X_train_scaled)

colormap = np.array(['tab:blue', 'tab:orange', 'tab:green'])
name1 = mpatches.Patch(color='tab:blue', label = iris.target_names[0])
name2 = mpatches.Patch(color='tab:orange', label = iris.target_names[1])
name3 = mpatches.Patch(color='tab:green', label = iris.target_names[2])
fig2, ax2 = plt.subplots(1, 2, figsize=(14, 6))
ax2[0].scatter(X_train[:, 2], X_train[:, 3], s=60, c=colormap[y_train], edgecolors='k')
ax2[0].set_title('Iris train data', fontsize=15)
ax2[0].set_xlabel('Sepal Length', fontsize=12)
ax2[0].set_ylabel('Sepal Width', fontsize=12)
ax2[0].legend(handles=[name1,name2,name3])
ax2[1].scatter(X_train[:, 2], X_train[:, 3], s=50, c=colormap[y_train_pred], edgecolors='k')
ax2[1].set_title('Iris predict data by SVM', fontsize=15)
ax2[1].set_xlabel('Sepal Length', fontsize=12)
ax2[1].set_ylabel('Sepal Width', fontsize=12)
ax2[1].legend(handles=[name1,name2,name3])

# 6. 1번 데이터를 이용하여  K-mean 군집 모델로 3개의 클러스터를 생성한다.
x, y = iris.data, iris.target
#print(x)
#print(y)

kmeans = KMeans(n_clusters=3, random_state=111)
kmeans.fit(x)
labels = kmeans.labels_
#print(y)
#print(labels)
labels1 = np.where(kmeans.labels_==1, 0, np.where(kmeans.labels_==0, 1, kmeans.labels_))   #클러스터링 되어 반환하는 값이 기존 데이터와 틀려 매칭하는 코드
#print(labels1)

# 7. 6번에서 클러스터한 데이터를 산점도로 도식화 한다.
fig3, ax3 = plt.subplots(1, 1, figsize=(7, 6))
ax3.scatter(x[:,2], x[:,3], c=colormap[labels1], marker='s', edgecolors='k', s=60)  #예측값
ax3.scatter(x[:,2], x[:,3], c=y, s=10)     #실제값
ax3.set_title('KMeans clustering (n=3)', fontsize=15)
ax3.set_xlabel('Sepal Length', fontsize=12)
ax3.set_ylabel('Sepal Width', fontsize=12)
ax3.legend(handles=[name1,name2,name3])

# 8. 6번에서 학습시킨 k-평균 군집 모델 예측 값과 정답 값을 이용하여 오차 행렬을 출력한다.
err_M = confusion_matrix(y, labels1)
print(err_M)
species = iris.target_names
fig4, ax4 = plt.subplots(1, 1, figsize=(7, 6))
im = ax4.imshow(err_M)
ax4.set_xticks(np.arange(len(species)))
ax4.set_yticks(np.arange(len(species)))
ax4.set_xticklabels(species)
ax4.set_yticklabels(species)

for i in range(len(species)):
    for j in range(len(species)):
        text = ax4.text(j, i, err_M[i, j],
                       ha="center", va="center", color="w")

ax4.set_title("Confusion metrix")
fig4.tight_layout()
print('\n', classification_report(y, labels1))
plt.show()
# 9. 코드에 주석으로 오차 행렬을 분석하고 그 내용을 적는다.
'''
- setosa 에 대한 정확도 및 재현율은 1로 매우 분류가 잘 되었다.
- versicolor 에 대한 정확도는 0.77이며, 재현율 0.96으로 재현율은 높은편이나 정확도는 낮은 수준이다. 개선이 필요
- virginica 에 대한 정확도는 0.95, 재현율은 0.72로 정확도는 높은편이나 재현률이 떨어짐, 
- versicolor 와 virginica의 분류에는 그래프 상 곂치는 구간이 있어 K-평균 분류에 한계점 존재
'''