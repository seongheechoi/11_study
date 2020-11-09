from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

digits = load_digits()
y = digits.target == 9

x_train, x_test, y_train, y_test = train_test_split(digits.data, y, random_state=0)
logreg = LogisticRegression(C=0.1).fit(x_train, y_train)
pred_logreg = logreg.predict(x_test)
print('accuracy : {:.2f}'.format(logreg.score(x_test, y_test)))
print('\n', classification_report(y_test, pred_logreg, target_names=['9가 아님','9']))