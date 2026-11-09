## Last part

Po usunięciu pliku `dvc checkout` odtworzył oczyszczony dataset z lokalnego cache.
Podgląd potwierdza 80 kolumn oraz przekształcone wartości, np. `SC20` i `May`.

```
(mlops-course-agh-lab-05) manoftheprincess@Andreis-MacBook-Air lab05 % rm data/ames_data_2006_2008.parquet
dvc checkout
python ames_inspect_data.py --file-path=data/ames_data_2006_2008.parquet
Building workspace index                                                                             |3.00 [00:00,  262entry/s]
Comparing indexes                                                                                   |5.00 [00:00, 6.67kentry/s]
Applying changes                                                                                     |1.00 [00:00, 1.46kfile/s]
A       data/ames_data_2006_2008.parquet
    MSSubClass MSZoning  LotFrontage  LotArea  Street  Alley  ...  MiscVal MoSold  YrSold SaleType  SaleCondition SalePrice
989       SC20       RL         87.0    11029       2      0  ...        0    May    2008      WD          Normal    176500
990       SC20       RL          0.0    12925       2      0  ...        0    May    2008      WD          Normal    237500
991       SC60       RL         85.0    11075       2      0  ...        0    Jun    2008      WD          Normal    206900
992       SC60       RL         72.0     8702       2      0  ...        0    Apr    2008      WD          Normal    187500
993       SC60       RL         65.0     8139       2      0  ...        0    Oct    2008      WD          Normal    165000

[5 rows x 80 columns]
```

Przejście do commita `e2c12ce` i wykonanie `dvc checkout` przywróciło surową wersję danych.
Dataset ponownie ma 82 kolumny, w tym `Order` i `PID`, oraz brakujące wartości (`NaN`).

```
(mlops-course-agh-lab-05) manoftheprincess@Andreis-MacBook-Air lab05 % git checkout e2c12ce
dvc checkout
python ames_inspect_data.py --file-path=data/ames_data_2006_2008.parquet
M       lab05/LAB_1_RESULTS.md
Note: switching to 'e2c12ce'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at e2c12ce first task finished
Building workspace index                                                                             |4.00 [00:00,  900entry/s]
Comparing indexes                                                                                   |5.00 [00:00, 6.47kentry/s]
Applying changes                                                                                     |1.00 [00:00,   689file/s]
M       data/ames_data_2006_2008.parquet
     Order        PID  MS.SubClass MS.Zoning  Lot.Frontage  ...  Mo.Sold Yr.Sold Sale.Type Sale.Condition SalePrice
989    990  526351030           20        RL          87.0  ...        5    2008       WD          Normal    176500
990    991  526353050           20        RL           NaN  ...        5    2008       WD          Normal    237500
991    992  526354070           60        RL          85.0  ...        6    2008       WD          Normal    206900
992    993  527105050           60        RL          72.0  ...        4    2008       WD          Normal    187500
993    994  527106050           60        RL          65.0  ...       10    2008       WD          Normal    165000

[5 rows x 82 columns]
```

Po powrocie na `main` polecenie `dvc checkout` przywróciło oczyszczoną wersję z 80 kolumnami.
Potwierdza to, że można odtwarzać różne wersje danych na podstawie metadanych zapisanych w Git.

```
(mlops-course-agh-lab-05) manoftheprincess@Andreis-MacBook-Air lab05 % git checkout main
dvc checkout
python ames_inspect_data.py --file-path=data/ames_data_2006_2008.parquet
M       lab05/LAB_1_RESULTS.md
Previous HEAD position was e2c12ce first task finished
Switched to branch 'main'
Building workspace index                                                                            |4.00 [00:00, 1.01kentry/s]
Comparing indexes                                                                                   |5.00 [00:00, 6.79kentry/s]
Applying changes                                                                                     |1.00 [00:00,   709file/s]
M       data/ames_data_2006_2008.parquet
    MSSubClass MSZoning  LotFrontage  LotArea  Street  Alley  ...  MiscVal MoSold  YrSold SaleType  SaleCondition SalePrice
989       SC20       RL         87.0    11029       2      0  ...        0    May    2008      WD          Normal    176500
990       SC20       RL          0.0    12925       2      0  ...        0    May    2008      WD          Normal    237500
991       SC60       RL         85.0    11075       2      0  ...        0    Jun    2008      WD          Normal    206900
992       SC60       RL         72.0     8702       2      0  ...        0    Apr    2008      WD          Normal    187500
993       SC60       RL         65.0     8139       2      0  ...        0    Oct    2008      WD          Normal    165000

[5 rows x 80 columns]
```
