from sklearn.externals import joblib
from trained_model import *

print (1000)
classifier = joblib.load('model.pkl')
print(1)
predict = classifier.predict(msg_test)
print (2)
print (predict)
