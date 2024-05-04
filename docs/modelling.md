The most common metrics to use for imbalanced datasets are:

- F1 score
- Precision
- Recall
- AUC score (AUC ROC)
- Average precision score (AP)
- G-Mean

It is good practice to track multiple metrics when developing a machine learning model as each highlights different aspects of model performance.

https://machinelearningmastery.com/tour-of-evaluation-metrics-for-imbalanced-classification/

# Credit Card Transactions Fraud Detection via Continual Learning
## ML modellek alkalmazása

Benyák Bence - Klenk Botond

A feladatunk egy a Kaggleről származó generált bankkártyás tranzakciók adathalmazának feldolgozása és folyamatos tanulással történő csalásdetekciója lesz.

## Pipeline 

Az elkészített és jövőben elkészítendő különböző komponenseinket egy pipelineba szerveztük, amely a következő előnyökkel jár:

- Egyszerűbb és olvashatóbb kód: A pipeline lehetővé teszi, hogy a gépi tanulás folyamatát egyetlen összetett lépéssorozatként definiáljuk. Ez megkönnyíti a kód olvashatóságát és karbantarthatóságát, mivel a folyamat lépései egyértelműen elkülönülnek egymástól.

- Automatikus adattranszformáció: A pipeline lehetővé teszi az adatok automatikus transzformálását a különböző lépések között.

- Keresztvalidáció és hiperparaméter optimalizáció: A pipeline lehetővé teszi a keresztvalidációt és a hiperparaméter optimalizációt a teljes folyamaton. Ez azt jelenti, hogy a pipeline segítségével könnyedén kipróbálhatunk különböző transzformációkat és modelleket, és meghatározhatjuk a legjobb kombinációt a modell teljesítményének maximalizálásához.

- Új adatok könnyű kezelése: Ha új adatokat szeretnénk beilleszteni a modellbe, a pipeline automatikusan alkalmazza az összes szükséges transzformációt a friss adatokra.

- Új modellek könnyű kipróbálása: A pipeline lehetővé teszi, hogy könnyedén kipróbáljunk új modelleket a meglévő folyamatban.

## RandomForestClassifier baseline model

