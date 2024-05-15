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

## DataLoader osztály

A `DataLoader` osztály felelős az adatok betöltéséért. Az initben megadott fájlnév alapján elkérhetjük az egész adathalmazt a 'load' metódussal, vagy részekre botva a 'load_state_by_id' metódussal.

## DataPreparation osztály

A `DataPreparation` osztály felelős az adatok előkészítéséért és átalakításáért a feldolgozás előtt. Az osztály két fő metódust tartalmaz: `fit` és `transform`.

### Metódusok

#### fit(self, X, y=None)

Ez a metódus előkészíti a mappinget a kiválasztott kategorikus oszlopok encode-olásához. Az `X` és `y` paraméter nem szükséges hozzá.

#### transform(self, X)

Ez a metódus átalakítja az adatokat a következőképpen:

- Felbontott időbeli oszlopokat hoz létre a tranzakció időpontjából, és a tulajdonos születési dátumából.
- Az adatelemzés alapján megjelöli, ha a foglalkozás vagy a kategória magas kockázatú.
- Alkalmazza a mappinget a kiválasztott oszlopokra.
- Eltávolítja a felesleges oszlopokat.

#### get_feature_names(self)

Ez a metódus visszaadja a DataFrame oszlopainak neveit.

### Változók

- `high_risk_jobs`: lista a magas kockázatú foglalkozásokról.
- `high_risk_categories`: lista a magas kockázatú kategóriákról.
- `cols_to_drop`: lista az eldobandó oszlopokról.

## ContinousDataPreparation osztály

A `DataPreparation` osztály leszármazottja, amely csak azokat a modosításokat végzi el amit a valóságban tudnánk, ha csak részekben kapnánk meg az adatot.

Így a magas kockázatú részt kihagyja és helyette a munka és kategória oszlopokat is mappelve encode-olja.

## Pipeline

A modellek egyszerű használatához létrehoztunk egy Pipeline osztályt, amelybe bekötöttük a:
- `DataPreparation`
- `StandardScaler`
- `SMOTE`
- `választott modell`
elemeket.

A scaler-t azért használjuk, hogy bármilyen modell használható legyen a pipeline-ban, a SMOTE-ot pedig azért, hogy a kiegyenlítettlen adathalamzunkban a kisebb osztály arányát feljebb húzzuk.