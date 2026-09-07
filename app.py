import pandas as pd
import numpy as np
from datetime import datetime

class DataGuardianAgent:
    """Autonomous AI Agent for Data Quality & Governance"""

    def __init__(self):
        self.issues_found = []
        self.fixes_applied = 0

    def scan_dataset(self, df: pd.DataFrame):
        print(f" Scanning {len(df)} records...")
        report = {
            "nulls": df.isnull().sum().to_dict(),
            "duplicates": df.duplicated().sum(),
            "anomalies": self.detect_anomalies(df)
        }
        return report

    def detect_anomalies(self, df):
        anomalies = []
        for col in df.select_dtypes(include=[np.number]).columns:
            mean, std = df[col].mean(), df[col].std()
            outliers = df[(df[col] < mean - 3*std) | (df[col] > mean + 3*std)]
            if len(outliers) > 0:
                anomalies.append(f"{col}: {len(outliers)} outliers")
        return anomalies

    def auto_fix(self, df: pd.DataFrame):
        df_clean = df.copy()
        # Auto-fix nulls with median/mode
        for col in df_clean.columns:
            if df_clean[col].isnull().sum() > 0:
                if df_clean[col].dtype in ['int64','float64']:
                    df_clean[col].fillna(df_clean[col].median(), inplace=True)
                else:
                    df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)
                self.fixes_applied += 1
        df_clean.drop_duplicates(inplace=True)
        return df_clean

# Demo
if __name__ == "__main__":
    agent = DataGuardianAgent()
    print(" DataGuardian AI - Autonomous Data Quality Agent Ready")
    print(f"Timestamp: {datetime.now()}")
