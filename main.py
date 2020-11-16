import pandas as pd
import sklearn as sk
import numpy as np
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
#from sklearn import preprocessing

#le = preprocessing.LabelEncoder()
#le.fit_transform()

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

col_names = ['sex', 'vârstă', 'simptome declarate', 'simptome raportate la internare', 'confirmare contact cu o persoană infectată']
data = pd.read_excel (r'./mps.dataset.xlsx')
rezultat = pd.DataFrame(data, columns= ['rezultat testare'])
x = data[col_names]
y = rezultat


i=0
sex_column = {}
for sex in x.get("sex"):
	if sex == "FEMININ":
		sex = 0
		sex_column[i] = sex
		i=i+1
	else:
		sex = 1
		sex_column[i] = sex
		i=i+1

i=0
age_column = {}
for age in x.get("vârstă"):
	if isinstance(age, int):
		age_column[i] = age
		i=i+1
	else:
		age = 0
		age_column[i] = age
		i=i+1

symptoms = readFile("./simptome_unice")
symp_column = {}
j=0

for symp in x.get("simptome declarate"):
	symp = str(symp).lower()
	symp = symp.replace(",", " ")
	symp = symp.replace(".", " ")
	symp = symp.replace("-", " ")
	split_symp = symp.split(" ")
	i=0
	for word in split_symp:
		if word in symptoms:
			i = i + 1
	symp_column[j] = i
	j = j + 1
	
#print(symp_column)


reported_column = {}
j=0

for symp in x.get("simptome raportate la internare"):
	symp = str(symp).lower()
	symp = symp.replace(",", " ")
	symp = symp.replace(".", " ")
	symp = symp.replace("-", " ")
	split_symp = symp.split(" ")
	i=0
	for word in split_symp:
		if word in symptoms:
			i = i + 1
	reported_column[j] = i
	j = j + 1

i=0
contact_column = {}
for answer in x.get("confirmare contact cu o persoană infectată"):
	answer = str(answer).lower()
	if answer[0] == "d" or answer[0] == "c":
		contact_column[i] = 1
		i=i+1
	else:
		contact_column[i] = 0
		i=i+1
	

i=0
result_column = {}
for result in y.get("rezultat testare"):
	result = str(result).lower()
	if result == "pozitiv":
		result_column[i] = 2
		i=i+1
	elif result == "negativ":
		result_column[i] = 0
		i=i+1
	else:
		result_column[i] = 1
		i=i+1
#print(y)



#print("\nArray after insertion : \n", a) 


Matrix = [[0 for x in range(5)] for y in range(len(contact_column))] 

for i in range(len(contact_column)):
	Matrix[i][0] = sex_column[i]
	Matrix[i][1] = age_column[i]
	Matrix[i][2] = symp_column[i]
	Matrix[i][3] = reported_column[i]
	Matrix[i][4] = contact_column[i]


x_train, x_test, y_train, y_test = train_test_split(Matrix, result_column, test_size=0.3, random_state=1)

clf = DecisionTreeClassifier()
clf = clf.fit(x_train, y_train)

y_pred=clf.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
