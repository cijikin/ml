import pandas as pd
import matplotlib.pyplot as plot
import sklearn.linear_model as linear
import sklearn.metrics as metrics
import sklearn.model_selection as model_selection

lvl = pd.read_csv("linear_vs_logistic.csv")
lvl.sort_values(by=["grade", "qualifies"], inplace=True)

grade = lvl[["grade"]]
qualifies = lvl["qualifies"]

plot.scatter(grade, qualifies)

model = linear.LogisticRegression()
model.fit(grade, qualifies)

modeled1 = model.predict(grade)
modeled2 = model.predict_proba(grade)[:, 1]

plot.scatter(grade, qualifies)
model2 = linear.LinearRegression()
model2.fit(grade, qualifies)
modeled3 = model2.predict(grade)

plot.plot(grade, modeled3, label="grade", color="b")

lvl["logistic probability"] = modeled2
lvl["linear probability"] = modeled3

print(lvl)

plot.plot(grade, modeled1, color="r")
plot.plot(grade, modeled2, color="g")

confusion_matrix = metrics.confusion_matrix(qualifies, modeled1) # ???
print(confusion_matrix)

print(f"Accuracy: {metrics.accuracy_score(qualifies, modeled1)}")
print(f"Error: {1 - metrics.accuracy_score(qualifies, modeled1)}")

print(f"Precision: {metrics.precision_score(qualifies, modeled1)}")
print(f"Recall: {metrics.recall_score(qualifies, modeled1)}")

plot.show()