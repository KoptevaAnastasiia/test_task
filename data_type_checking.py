import os
import pandas as pd

csv_directory = '/home/anastasiia/Documents/tast_task_work_12.24'

csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]
for csv_file in csv_files:
    file_path = os.path.join(csv_directory, csv_file)

    try:
        df = pd.read_csv(file_path)
        print(f"DATA  : {csv_file}")
        print(df.dtypes)
        print("\n" + "-" * 40 + "\n")

    except Exception as e:
        print(f"ERROR {csv_file}: {e}")
