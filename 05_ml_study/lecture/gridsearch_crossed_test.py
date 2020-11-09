from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
import numpy as np

iris = load_iris()
X_trainval, X_test, y_trainval, y_test = train_test_split(iris.data, iris.target, random_state=0)
X_train, X_valid, y_train, y_valid = train_test_split(X_trainval, y_trainval, random_state=1)
print('훈련 세트의 크기: {}   검증 세트의 크기: {}   테스트 세트의 크기: {}'.format(X_train.shape[0], X_valid.shape[0], X_test.shape[0]))

best_score = 0

for gamma in [0.001, 0.01, 0.1, 1 , 10, 100]:
    for C in [0.001, 0.01, 0.1, 1 , 10, 100]:
        svm = SVC(gamma=gamma, C=C)
        #svm.fit(X_train, y_train)

        scores = cross_val_score(svm, X_trainval, y_trainval, cv=5)
        score = np.mean(scores)

        if score > best_score:
            best_score = score
            best_parameters = {'C': C, 'gamma': gamma}    #딕셔너리 타입

svm = SVC(**best_parameters)
svm.fit(X_trainval, y_trainval)
test_score = svm.score(X_test, y_test)
print('검증 세트에서 최고 점수 : {:.2f}'.format(best_score))
print('최적 파라미터 :', best_parameters)
print('최적 파라미터에서 테스트 세트 점수 : {:.2f}'. format(test_score))