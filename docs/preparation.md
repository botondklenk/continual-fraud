# Credit Card Transactions Fraud Detection via Continual Learning
## Adathalmaz előkészítés

Benyák Bence - Klenk Botond

A feladatunk egy a Kaggleről származó generált bankkártyás tranzakciók adathalmazának feldolgozása és folyamatos tanulással történő csalásdetekciója lesz.

## Célok

1. Olyan formára hozni az adatokat, hogy a baseline modelt betaníthassuk és kiértékelhessük rajtuk.
2. Felhasználni a data analízis által megfigyelt összefüggéseket, azok alapján tanszformációk alkalmazása.
3. Adathalmaz feldarabolása folyamatos tanulási módszerek alkalmazásához.
    - államokra bontás
    - időablakokra osztás
4. További módszerek alkalmazása a jobb eredmények elérésének érdekében.
    - SMOTE oversampler használata

## DataPreparation osztály

A `DataPreparation` osztály felelős az adatok előkészítéséért és átalakításáért a feldolgozás előtt. Az osztály két fő metódust tartalmaz: `fit` és `transform`.

### Metódusok

#### fit(self, X, y=None)

Ez a metódus előkészíti a LabelEncoder-t a kiválasztott oszlopokhoz. Az `X` paraméter a bemeneti DataFrame, míg az `y` paraméter opcionális.

#### transform(self, X)

Ez a metódus átalakítja az adatokat a következőképpen:

- Felbontott időbeli oszlopokat hoz létre a tranzakció dátumából és időpontjából.
- Az adatelemzés alapján megjelöli, ha a foglalkozás magas kockázatú.
- Alkalmazza a LabelEncoder-t a kiválasztott oszlopokra.
- Eltávolítja a felesleges oszlopokat.

#### get_feature_names(self)

Ez a metódus visszaadja a DataFrame oszlopainak neveit.

### Változók

- `high_risk_jobs`: lista a magas kockázatú foglalkozásokról.
- `high_risk_categories`: lista a magas kockázatú kategóriákról.
- `cols_to_drop`: lista az eldobandó oszlopokról.