from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import mglearn
import matplotlib.pyplot as plt

digits = load_digits()

x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=0)
logreg = LogisticRegression(C=0.1).fit(x_train, y_train)
pred_logreg = logreg.predict(x_test)
print('accuracy : {:.2f}'.format(logreg.score(x_test, y_test)))
print('\n', classification_report(y_test, pred_logreg))

scores_image = mglearn.tools.heatmap(
    confusion_matrix(y_test, pred_logreg), xlabel='predict label', ylabel='target label',
    xticklabels=digits.target_names, yticklabels=digits.target_names, cmap=plt.cm.gray_r, fmt='%d')
plt.title('error matrix')
plt.gca().invert_yaxis()
plt.show()