from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel, RBF
import numpy as np

ppg_train = np.loadtxt('parts1to4_ppg.csv', delimiter=',')
bp_train = np.loadtxt('parts1to4_bp.csv', delimiter=',')
ppg_test = np.loadtxt('parts6_ppg.csv', delimiter=',')
bp_test = np.loadtxt('parts6_bp.csv', delimiter=',')

kernel = RBF()
gaussian_regressor = GaussianProcessRegressor(kernel=kernel, random_state=0)
gaussian_regressor.fit(ppg_train, bp_train)

predictions = gaussian_regressor.predict(ppg_test)
errors = abs(predictions - bp_test)
print('Mean Absolute Error:', (np.mean(errors, axis=0)))
print('Standard Deviation:', np.std(errors, axis=0))

print(predictions[0:50])
print(bp_test[0:50])