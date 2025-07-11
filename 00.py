import os
import pandas as pd

folder = r"C:\Users\itg\Documents\copliot_homework\20250711111244"

for filename in os.listdir(folder):
    if filename.lower().endswith(('.xls', '.xlsx')):
        filepath = os.path.join(folder, filename)
        df = pd.read_excel(filepath)

        base_name = os.path.splitext(filename)[0]
        csv_path = os.path.join(folder, base_name + ".csv")

        df.to_csv(csv_path, index=False, encoding="utf-8-sig")
        print(f"✅ 변환 완료: {csv_path}")