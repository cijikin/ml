import pandas as pd
import matplotlib.pyplot as plot
import sklearn.linear_model as linear
import numpy as np
import sklearn.metrics as metrics
import sklearn.model_selection as model_selection
from scipy.stats import pearsonr


# subs = pd.read_csv("subscribers_from_ads.csv")
#
# print(subs)
# plot.scatter(subs[["promotion_budget"]], subs[["subscribers"]])
#
# pb = subs[["promotion_budget"]]
# s = subs[["subscribers"]]
#
# regression = linear.LinearRegression()
# regression.fit(pb, s)
#
# #y=kx + b
#
# print(regression.coef_) #k
# print(regression.intercept_) #b
#
# regression_line_points = regression.predict(pb)
# plot.plot(pb, s)
# plot.plot(pb, regression_line_points)
#
# plot.show()

###############################################

def model_to_string(model, labels, precision=4):
    model_str = "{} = ".format(labels[-1])
    for z in range(len(labels) - 1):
        model_str += "{} * {} + ".format(round(model.coef_.flatten()[z], precision), labels[z])
    model_str += "{}".format(round(model.intercept_[0], precision))
    return model_str


def train_linear_model(X, y):
    regression = linear.LinearRegression()
    regression.fit(X, y)
    return regression


def get_MSE(model, X, y):
    y_redicted = model.predict(X)
    MSE = metrics.mean_squared_error(y, y_redicted)
    return MSE


adv = pd.read_csv("advertising.csv", index_col=0)
print(adv)

ad_data = adv[["TV", "radio", "newspaper"]]
sales_data = adv[["sales"]]

regression2 = linear.LinearRegression()
lasso_regression = linear.Lasso()  # l1
ridge_regression = linear.Ridge()  # l2

regression2.fit(ad_data, sales_data)
lasso_regression.fit(ad_data, sales_data)
ridge_regression.fit(ad_data, sales_data)

X_train, X_test, y_train, y_test = model_selection.train_test_split(ad_data, sales_data, shuffle=True)

regression2 = train_linear_model(X_train, y_train)
# print("MSE = {}".format(get_MSE(regression2, X_test, y_test)))
# print("MSE_train = {}".format(get_MSE(regression2, X_train, y_train)))

labels = adv.columns.values

print("Linear regression.\n" + model_to_string(model=regression2, labels=labels), end="\n")
print("Ridge regression (L2).\n" + model_to_string(model=ridge_regression, labels=labels), end="\n")
print("Lasso regression (L1).\n" + model_to_string(model=lasso_regression, labels=labels), end="\n")
print()

for z in range(len(labels) - 1):
    feature_name = labels[z]
    print("{} removed:".format(feature_name))

    X_train_2_features = X_train.drop(feature_name, axis=1)
    X_test_2_features = X_test.drop(feature_name, axis=1)
    # print(X_test_2_features.head())

    labels_2_features = np.delete(labels, z)
    model_2_features = train_linear_model(X_train_2_features, y_train)
    print(model_to_string(model_2_features, labels_2_features))
    print("Test MSE = {}".format(get_MSE(model_2_features, X_test_2_features, y_test)))
    # чем MSE больше - тем больше удалённая переменная влияет на функцию
    print()

# plot visualisation

# tv
plot.scatter(adv[["TV"]], adv[["sales"]])
tv = adv[["TV"]]
regression2 = linear.LinearRegression()
regression2.fit(tv, sales_data)
regression_line_points_tv = regression2.predict(tv)
print(model_to_string(model=regression2, labels=["TV", "sales"], precision=4))

plot.plot(tv, regression_line_points_tv, label="TV")

# radio
plot.scatter(adv[["radio"]], adv[["sales"]])
radio = adv[["radio"]]
regression2.fit(radio, sales_data)
regression_line_points_radio = regression2.predict(radio)
print(model_to_string(model=regression2, labels=["radio", "sales"], precision=4))

plot.plot(radio, regression_line_points_radio, label="radio")

# news
plot.scatter(adv[["newspaper"]], adv[["sales"]])
newspaper = adv[["newspaper"]]
regression2.fit(newspaper, sales_data)
regression_line_points_newspaper = regression2.predict(newspaper)
print(model_to_string(model=regression2, labels=["newspaper", "sales"], precision=4))

plot.plot(newspaper, regression_line_points_newspaper, label="newspaper")

regression = linear.LinearRegression()
regression.fit(ad_data, sales_data)
labels = adv.columns.values
print(model_to_string(model=regression, labels=labels, precision=4))

plot.legend()
plot.show()
