import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([500, 600, 700, 700, 800, 800, 750, 550, 650, 825]).reshape((-1, 1))
y = np.array([7.31, 6.70, 5.95, 6.40, 5.40, 5.70, 5.90, 7.00, 6.50, 5.70])
# x = np.array([500, 600, 700, 700, 800, 800, 750, 550, 650, 825]).reshape((-1, 1))
# y = np.array([7.31, 6.70, 5.95, 6.40, 5.40, 5.70, 5.90, 7.00, 6.50, 5.70])

model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
b =  r_sq * x[0] - y[0]
print('value of b' , b)

interest_rate = model.predict(np.array([625]).reshape(-1, 1))
print(interest_rate)