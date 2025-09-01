# Test that you can run this code with Python or a Jupyter notebook

import numpy as np      # External library for numerical calculations
import matplotlib.pyplot as plt   # Plotting library
import pandas as pd               # For reading in spreadsheets
import urllib.request as ur       # For downloading data

# Download, read in data and clean the data
url='https://psl.noaa.gov/data/timeseries/month/data/nino34.long.csv'
datafile, errorLog = ur.urlretrieve(url, url.split('/')[-1])
df = pd.read_csv(datafile, skiprows=1, names=["Date", "Nino34"])
# Convert the 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
# Replace missing values (-9999.0) with NaN and drop them
df["Nino34"] = pd.to_numeric(df["Nino34"], errors='coerce')
df = df[df["Nino34"] != -9999.0]

# Fourier tansform and plot power spectrum
Fcoeffs = np.fft.fft(df["Nino34"].values)
plt.loglog(np.abs(Fcoeffs)**2)
plt.show()