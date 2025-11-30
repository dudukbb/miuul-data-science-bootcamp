
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

#######################################
# GÖREV 1
#######################################

# CSV'yi okuma
df = pd.read_csv("churn.csv")

# Gerçek değerler(y)
# Model olasılık tahminleri
y_true = df["gercek_deger"]
y_proba = df["tahmin_1_olasiligi"]

# Eşik değere göre sınıfa çevirme (1 ya da 0 sınıfı)
threshold = 0.5
y_pred = (y_proba > threshold).astype(int)

print("Gerçek Değerler (y_true):")
print(y_true.values)
print("\nTahmin Edilen Sınıflar ( y_pred):")
print(y_pred.values)

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
tn, fp, fn, tp = cm.ravel()

print("Confusion Matrix:")
print(cm)
print(f"\nTN: {tn}, FP: {fp}, FN: {fn}, TP: {tp}")

# Metriklerin Hesaplanması
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("\nMetrikler")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1: {f1:.2f}")

##############################################
# GÖREV 2
##############################################

# Banka üzerinden yapılan işlemler sırasında dolandırıcılık işlemlerinin yakalanması amacıyla sınıflandırma modeli oluşturulmuştur. %90.5 doğruluk
# oranı elde edilen modelin başarısı yeterli bulunup model canlıya alınmıştır. Ancak canlıya alındıktan sonra modelin çıktıları beklendiği gibi
# olmamış, iş birimi modelin başarısız olduğunu iletmiştir. Aşağıda modelin tahmin sonuçlarının karmaşıklık matriksi verilmiştir.

# Buna göre;
# - Accuracy, Recall, Precision, F1 Skorlarını hesaplayınız.
# - Veri Bilimi ekibinin gözden kaçırdığı durum ne olabilir yorumlayınız.


#                     Tahmin 1              Tahmin 0
#  Gerçek 1             TP                    FN
#  Gerçek 0             FP                    TN

# TP : Model 1'i doğru tahmi etmiş, gerçekten fraud olan bir işlem
# FN : Model 1 olması gerekeni yanlışlıkla 0 tahmin etti, gerçekte fraud olan işleme fraud değil dedi.
# TN : Model 0'ı doğru tahmin etti, gerçekte fraud olmayan işleme model de fraud değil dedi.
# FP : Model 0 olması gerekeni yanlışlıkla 1 tahmin etti,model  gerçekte fraud olmayan işleme fraud dedi.

# Accuracy = (TP + TN)/( TP + TN + FP + FN )
# Precision = TP / ( TP+FP )
# Recall = TP / ( TP+FN )
# F1 Score = 2 * (Precision*Recall) / (Precision+Recall)

TP = 5
TN = 5
FP = 90
FN = 900

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("\nMetrikler")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1: {f1:.2f}")

# YORUM
# Model tüm gözlemlerin %70'ni doğru tahmin etmiş ( ACCURACY : 0.70 )
# Recall, gerçek 1'leri yakalama oranıdır ( RECALL : 0.67 )
# Precision, model 1 dediğinde bunun gerçekten 1 olma oranıdır. ( PRECISION : 0.80 )
# F1, Precision ve Recall'ın birleşik bir başarısıdır. ( F1 : 0.73 )

# Modelin precisionı yüksek.Yani model pozitif tahminleri genelde dogru tahmin ediyor.
# Ancak recall düşük, yani bazı gerçek pozitifleri kaçırıyor.
# F1 Skoru dengeli bir model performansını işaret ediyor.
# Accuracy, genel doğruluk fena değil ama daha iyi olabilir.

