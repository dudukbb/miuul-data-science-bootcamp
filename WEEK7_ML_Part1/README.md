📘 7. Hafta – Makine Öğrenmesi (Part 1)
Basit Doğrusal Regresyon Çalışması

MIUUL Data Science Bootcamp’in 7. haftasında Basit Doğrusal Regresyon (Simple Linear Regression) konusunu uygulamalı olarak çalıştım.
Amaç, bir çalışanın deneyim yılı ile maaşı arasındaki ilişkiyi analiz etmek ve deneyime göre maaş tahmini yapabilen bir model oluşturmaktı.

🎯 Amaç

Deneyim ↔ Maaş arasındaki lineer ilişkiyi incelemek

Doğrusal regresyon modeli kurmak

Modeli MSE, RMSE, MAE ve R² metrikleri ile değerlendirmek

Tahmin edilen maaş değerlerini veri setine eklemek

Regresyon doğrusunu görselleştirmek

📂 Veri Seti

experience_salary.csv

Dosya iki sütundan oluşmaktadır:

experience — Deneyim yılı

salary — Maaş

Python dosyası ile aynı klasörde bulunur.

🛠️ Kullanılan Yöntemler
Adım	Açıklama
1. Veri Yükleme	Pandas ile CSV dosyası okundu ve X–Y ayrımı yapıldı
2. Model Eğitimi	LinearRegression() modeli eğitildi
3. Tahmin Fonksiyonu	Deneyime göre maaş tahmini yapan fonksiyon yazıldı
4. Görselleştirme	seaborn.regplot ile scatter plot + regresyon doğrusu çizildi
5. Performans Ölçümü	MSE, RMSE, MAE ve R² skorları hesaplandı
📊 Model Sonuçları
Metrik	Değer
MSE	4402
RMSE	66.35
MAE	59.73
R² Score	0.94
✔ Yorum

R² = 0.94 → Model maaş değişkeninin %94’ünü açıklıyor

RMSE ve MAE değerleri → Veri setinin standart sapmasına göre oldukça düşük

Sonuç olarak model, güçlü bir lineer ilişkiyi başarılı şekilde öğrenmiş

📁 Veri Setine Eklenen Sütunlar

Model çalıştırıldıktan sonra veri setine şu sütunlar eklenmiştir:

pred_salary

MSE

RMSE

MAE

R2

Bu sütunlar sayesinde gerçek ve tahmin edilen maaşların karşılaştırılması kolaylaşır.

📈 Görselleştirme

Proje kapsamında aşağıdaki grafik oluşturulmuştur:

Deneyim → Maaş scatter plot

Üzerine çizilmiş regresyon doğrusu

Eksensel etiketler ve başlık eklenmiştir

📁 Klasör Yapısı
WEEK7_ML_Part1/
│── ML_Week7_Case1.py
│── experience_salary.csv
└── README.md

✔ Kısa Özet

Bu çalışma, doğrusal regresyonun temelini anlamak ve gerçek bir veri üzerinde uygulamak için yapılmıştır.
Model eğitimi, tahmin üretme, metrik hesaplama ve grafik oluşturma gibi temel adımlar başarıyla tamamlanmıştır.
