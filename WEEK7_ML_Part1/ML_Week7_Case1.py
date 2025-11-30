
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score


pd.set_option('display.float_format', lambda x: '%.2f' % x)

df = pd.read_csv("experience_salary.csv")

# gölem birimi sayısı
df.shape

X = df[["experience"]]
Y = df[["salary"]]

###############################
# MODEL
###############################
# y_hat = 275 + 90*X

reg_model = LinearRegression().fit(X, Y)
reg_model.intercept_= 275

# pred_salary hesaplıyor
def predict(experience):
 return reg_model.intercept_ + reg_model.coef_[0][0]*experience

for exp in df["experience"]:
    pred = predict(exp)

df["pred_salary"] = df["experience"].apply(predict)

df.describe().T

####################################
# Modelin Görselleştirilmesi
####################################

g = sns.regplot(x=X, y=Y, scatter_kws={'color': 'b', 's': 40},
                ci=False, color="r")

g.set_title(f"Model Denklemi: Salary = {round(reg_model.intercept_, 2)} + Experience*{round(reg_model.coef_[0][0], 2)}")
g.set_ylabel("Maaş")
g.set_xlabel("Deneyim Yılı")

plt.xlim(0, X.iloc[:, 0].max() + 2)
plt.ylim(0, Y.iloc[:, 0].max() + 200)

plt.show()

###########################################
# Modelin tahmin başarısı
###########################################
y_pred = reg_model.predict(X)

# MSE
mse = mean_squared_error(Y, y_pred)
# 4402

# RMSE
rmse = np.sqrt(mean_squared_error(Y, y_pred))
# 66.35

# MAE
mae = mean_absolute_error(Y, y_pred)
# 59.73

# R-KARE
r2 = reg_model.score(X, Y)
# 0.94 : model bağımlı değişkendeki (salary) değişimin %94'ü
# bağımsız değişken olan (experience) ile açıklanabilir demektir.
# R2 yüksek ------> lineer ilişki güçlü

Y.mean()
# for salary
# 682.50

Y.std()
# for salary
# 290.49

# YORUM: RMSE değeri std'den çok küçük olduğu
# için model iyi performans gösteriyor diyebiliriz.
# R² = 0.94 ile model maaş varyansının %94’ünü açıklıyor
# ve RMSE/MAE değerleri std'den oldukça  düşük olduğu
# için model oldukça başarılı.

df["MSE"] = mse
df["RMSE"] = rmse
df["MAE"] = mae
df["R2"] = r2

df.describe().T