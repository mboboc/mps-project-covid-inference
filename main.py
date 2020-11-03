import pandas as pd
import sklearn as sk
import numpy as np
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
#from sklearn import preprocessing

#le = preprocessing.LabelEncoder()
#le.fit_transform()

col_names = ['instituția sursă', 'sex', 'vârstă', 'dată debut simptome declarate', 'simptome declarate', 'dată internare', 'simptome raportate la internare', 'istoric de călătorie', 'mijloace de transport folosite', 'confirmare contact cu o persoană infectată']
data = pd.read_excel (r'./mps.dataset.xlsx')
rezultat = pd.DataFrame(data, columns= ['rezultat testare'])
x = data[col_names]
y = rezultat
#df = pd.DataFrame(data, columns= ['sex'])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
x = x.fillna('nan')
for i in x.get('simptome raportate la internare'):
	if i != "nan":
		i = str(i).lower()
		i = i.strip()
		if "asim" not in i and not i.startswith("nu") and i != "-":
			print(i)

#clf = DecisionTreeClassifier()
#clf = clf.fit(x_train, y_train)

#y_pred=clf.predict(x_test)
#print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
