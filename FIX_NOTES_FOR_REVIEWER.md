# Fix notes for reviewer

This corrected package addresses the previous feedback by restoring real data and adding concrete visible outputs.

Main fixes:
- Restored `data/raw/cardio_train.csv` with 70,000 patient records.
- Added executed notebook outputs and interpretation.
- Added processed outputs under `data/processed/`.
- Added figures under `report/figures/`.

Main results:
- Cleaned rows: 68,596
- Hypertension cardio rate: 78.0% vs 34.6%
- Best model: Random Forest, ROC-AUC 0.791
