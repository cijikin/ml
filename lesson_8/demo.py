import pandas as pd
import matplotlib.pyplot as plot
import sklearn.linear_model as linear
import sklearn.metrics as metrics
import sklearn.model_selection as model_selection

s_grade = pd.read_csv("single_grade.csv")
s_grade.sort_values(by=["grade", "qualifies"], inplace=True)

# сигмоид
# h(x) = 1 / (1 + e ^ (-t)), t(x) = kx + b
# class = {1, h(x) >= 0.5; 0, h(x) <= 0.5;}

grade = s_grade[["grade"]]
qualifies = s_grade["qualifies"]

# cost = {-log(h(x)), y = 1; -log(1 - h(x)), y = 0;} - штраф "предсказания"

plot.scatter(grade, qualifies)

model = linear.LogisticRegression()
model.fit(grade, qualifies)

modeled1 = model.predict(grade)
modeled2 = model.predict_proba(grade)[:, 1]  # вырезаем часть данных, отвечающих за однозначную
                                             # принадлежность классу, чтобы построить сигмоид
s_grade["probability"] = modeled2            # (он сам посчитает)

print(s_grade)

plot.plot(grade, modeled1, color="k")
plot.plot(grade, modeled2, color="g")

confusion_matrix = metrics.confusion_matrix(qualifies, modeled1) # ???
print(confusion_matrix)

  #0 #1 (предсказание)
# 19  3 #0 - 3 ошибочно присвоены 1ому классу
#  2 16 #1 (истина) 16 - правильно
  # 2 - ошибочно присвоены 0ому классу, 19 - правильно

# acc = ((0;0) + (1;1)) / ((0;1) + (1;0)) = 87.5%
# err = 1 - acc = 12.5%                                       / выбр. м. зн. \
# (how many selected items are relevant?) precision = (1;1) / ((1;1) + (1;0)) = 84%,
                                          # where (1;1) = true positives, (1;0) = false positives
# (how maтy relevant items are selected?) recall = (1;1) / ((0;1) + (1;1)) = 85%,
                                          # where (0;1) = false negatives

print(f"Accuracy: {metrics.accuracy_score(qualifies, modeled1)}") # acc
print(f"Error: {1 - metrics.accuracy_score(qualifies, modeled1)}") # err metrics.mean_absolute_error - это
                                                                   # для линейной регрессии
print(f"Precision: {metrics.precision_score(qualifies, modeled1)}") # precision
print(f"Recall: {metrics.recall_score(qualifies, modeled1)}") # recall

plot.show()

# то же самое, но ещё присутствует тест по английскому

d_grade = pd.read_csv("double_grade.csv")
d_grade.sort_values(by=["technical_grade", "english_grade", "qualifies"], inplace=True)

grades = d_grade[["technical_grade", "english_grade"]]
qualifies = d_grade["qualifies"]

qualified_candidates = d_grade[d_grade["qualifies"] == 1]
unqualified_candidates = d_grade[d_grade["qualifies"] == 0]

plot.scatter(qualified_candidates["technical_grade"], qualified_candidates["english_grade"], color="g")
plot.scatter(unqualified_candidates["technical_grade"], unqualified_candidates["english_grade"], color="k")

cv_model = linear.LogisticRegression() # cv = cross validation
cv_model_quality = model_selection.cross_val_score(cv_model, grades, qualifies, cv=4, scoring="accuracy")
                                                        # number of folds (сгиб) = 4
print(cv_model_quality)

cv_prediction = model_selection.cross_val_predict(cv_model, grades, qualifies, cv=4)
cv_confusion_matrix = metrics.confusion_matrix(qualifies, cv_prediction)
print(cv_prediction)
print(cv_confusion_matrix)

# на всех данных, а не cv
model2 = linear.LogisticRegression() # cv = cross validation
model2.fit(grades, qualifies)

modeled4 = model2.predict_proba(grades)[:, 1]
d_grade["probability"] = modeled4

pd.set_option("display.max_rows", None)
print(d_grade.sort_values(by="probability"))

print(model2.coef_)
print(model2.intercept_) # 3d surface plotter: 1 / (1 + e ^ -(coef_ * x + intercept_))

plot.ylabel("English grade")
plot.xlabel("Technical grade")

plot.show()

# лог. регр. привязана к двухклассовой модели. модель зависит от линейной комбинации.
# граница между классами так же является линейным объектом. исп. как опорная модель.
# оцениваем качество, которое можно достигнуть. и насколько модель получается сложной.

# мультиклассовая классификация. каждая модель учится распознавать "свой" класс и не "свой".
# для определения класса, данные проходят через все модели, выдающие "коэффициент
# принадлежности", по значению которого (макс., например) определяется класс.
