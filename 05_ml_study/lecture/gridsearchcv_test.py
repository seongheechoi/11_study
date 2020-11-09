from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.svm import SVC

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

param_grid = {'C':[0.001, 0.01, 0.1, 1 , 10, 100],
              'gamma':[0.001, 0.01, 0.1, 1 , 10, 100]}

grid_search = GridSearchCV(SVC(), param_grid, cv=5, return_train_score=True)
grid_search.fit(X_train, y_train)
'''
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
'''
print('테스트 세트 점수: {:.2f}'.format(grid_search.score(X_test, y_test)))
print('최적 매개변수 :', grid_search.best_params_)
print('최고 교차 검증 점수 : {:.2f}'. format(grid_search.best_score_))