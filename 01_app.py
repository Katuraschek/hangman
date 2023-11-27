import os
from pathlib import Path
os.chdir(Path(__file__).parent)
# pip install ydata_profiling
import pandas as pd
import ydata_profiling
import ProfileReport

# 1. read the csv File
df = pd.read_csv

# 2. create the profile
profile = ProfileReport(df)


# 3. Save the output profile
profile.to_file(output_files='./profile.html')
