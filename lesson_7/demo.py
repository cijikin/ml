import pandas as pd
import matplotlib.pyplot as plot
import sklearn.preprocessing as preprocessing
import sklearn.linear_model as linear
import sklearn.metrics as metrics
import numpy as np
import sklearn.model_selection as selection


def create_model(x, y, degree):
    pt = preprocessing.PolynomialFeatures(degree=degree)
    x_transformed = pt.fit_transform(x)
    m = linear.LinearRegression()
    m.fit(x_transformed, y)
    return m


def get_mse(m, x, y_true):
    y_predicted = m.predict(x)
    mse = metrics.mean_squared_error(y_true, y_predicted)
    return mse


def optimal_polynomial_degree(x, y, degree):
    plot.scatter(x, y)
    x_train, x_test, y_train, y_test = selection.train_test_split(x, y, shuffle=True)
    all_mse_test = []
    all_mse_train = []
    for i in range(degree):
        m = create_model(x_train, y_train, i)
        pt = preprocessing.PolynomialFeatures(degree=i)

        x_train_transformed = pt.fit_transform(x_train)
        x_test_transformed = pt.fit_transform(x_test)

        mse_train = get_mse(m, x_train_transformed, y_train)
        mse_test = get_mse(m, x_test_transformed, y_test)

        all_mse_test.append(mse_test)
        all_mse_train.append(mse_train)
    degree = int(np.argmin(all_mse_test))
    return degree, all_mse_train[degree], all_mse_test[degree]


muscles = pd.read_csv("muscle_mass.csv")
muscles.sort_values(by="training_time", inplace=True)

time = muscles[["training_time"]]
mass = muscles[["muscle_mass"]]

plot.scatter(time, mass)

optimal_degree_for_test, mse_train, mse_test = optimal_polynomial_degree(time, mass, 30)

print("MSE train = {}".format(mse_train))
print("MSE test = {}".format(mse_test))

print("Optimal degree = {}".format(optimal_degree_for_test))

polynomial_transformer = preprocessing.PolynomialFeatures(degree=optimal_degree_for_test)
time_transformed = polynomial_transformer.fit_transform(time)

model = linear.LinearRegression()
model.fit(time_transformed, mass)

print(model.coef_)
print(model.intercept_)

modeled_mass = model.predict(time_transformed)

mse = get_mse(model, time_transformed, mass)

plot.plot(time, modeled_mass, color="r")
plot.show()
