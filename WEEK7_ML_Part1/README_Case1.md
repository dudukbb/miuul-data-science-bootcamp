# 📘 7. Hafta – Makine Öğrenmesi (Part 1)
## Basit Doğrusal Regresyon Çalışması

MIUUL Data Science Bootcamp’in 7. haftasında Basit Doğrusal Regresyon (Simple Linear Regression)
konusunu uygulamalı olarak çalıştım. Amaç, bir çalışanın deneyim yılı ile maaşı arasındaki ilişkiyi
incelemek ve deneyime göre maaş tahmini yapabilen bir model oluşturmaktı.

---

## 🎯 Amaç
- Deneyim ↔ Maaş arasındaki lineer ilişkiyi incelemek  
- Doğrusal regresyon modeli kurmak  
- Modeli MSE, RMSE, MAE ve R² metrikleri ile değerlendirmek  
- Tahmin edilen maaş değerlerini veri setine eklemek  
- Regresyon doğrusunu görselleştirmek  

---

## 📂 Veri Seti
**experience_salary.csv**

İki sütundan oluşur:
- experience — Deneyim yılı  
- salary — Maaş  

Python dosyası ile aynı klasörde bulunur.

---

## 🛠️ Kullanılan Yöntemler
- **Veri Yükleme:** Pandas ile CSV dosyası okundu, X–Y ayrımı yapıldı  
- **Model Eğitimi:** `LinearRegression()` modeli eğitildi  
- **Tahmin Fonksiyonu:** Deneyime göre maaş tahmini yapan fonksiyon yazıldı  
- **Görselleştirme:** `seaborn.regplot` ile scatter plot + regresyon doğrusu çizildi  
- **Performans Ölçümü:** MSE, RMSE, MAE ve R² skorları hesaplandı  

---

## 📊 Model Sonuçları
- **MSE:** 4402  
- **RMSE:** 66.35  
- **MAE:** 59.73  
- **R² Score:** 0.94  

### ✔ Yorum
- R² = 0.94 → Model maaş değişkeninin %94’ünü açıklıyor  
- RMSE ve MAE değerleri → Standart sapmaya göre oldukça düşük  
- Sonuç: Model güçlü bir lineer ilişkiyi başarılı şekilde öğrenmiş  

---

## 📁 Veri Setine Eklenen Sütunlar
- pred_salary  
- MSE  
- RMSE  
- MAE  
- R2  

Bu sütunlar, gerçek ve tahmin edilen maaşların kolayca karşılaştırılmasını sağlar.

---

## 📈 Görselleştirme
Oluşturulan grafikler:
- Deneyim → Maaş scatter plot  
- Üzerine çizilmiş regresyon doğrusu  
- Ek açıklamalar, etiketler ve başlık eklenmiştir  

---

## 📁 Klasör Yapısı
WEEK7_ML_Part1/  
│── ML_Week7_Case1.py  
│── experience_salary.csv  
└── README.md  

---

## ✔ Kısa Özet
Bu çalışma, doğrusal regresyonun temel mantığını kavramak ve gerçek bir veri üzerinde uygulamak için yapılmıştır.
Model eğitimi, tahmin üretme, metrik hesaplama ve grafik oluşturma adımları başarıyla tamamlanmıştır.

