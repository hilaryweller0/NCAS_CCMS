# Download Nino 3.4 time series and plot a power spectrum
# Settings
download=False
url='https://psl.noaa.gov/data/timeseries/month/data/nino34.long.csv'
# Module imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import urllib.request as ur

# Download the data if needed
if download:
    datafile, errorLog = ur.urlretrieve(url, 'rawData/'+url.split('/')[-1])
else:
    datafile = 'rawData/' + url.split('/')[-1]

# Load the data into a dataframe (df)
df = pd.read_csv(datafile, skiprows=1, names=["Date", "Nino34"])
# Convert the 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
# Replace missing values (-9999.0) with NaN and drop them
df["Nino34"] = pd.to_numeric(df["Nino34"], errors='coerce')
df = df[df["Nino34"] != -9999.0]

# Plot the time series and save an svg file
plt.figure(figsize=(14, 6))
plt.plot(df["Date"], df["Nino34"],label="Nino 3.4 SST",color='black')
plt.xlabel("Date", fontsize=14)
plt.ylabel("Nino 3.4 SST (C)", fontsize=14)
plt.grid(True); plt.tight_layout()
plt.savefig("plots/nino34_SST.svg"); plt.show()

# Fourier Transform to get Fourier coefficients
nino34 = df["Nino34"].values
# Frequency bins. d=1 for monthly data, *12 for per year
freq = np.fft.fftfreq(len(nino34), d=1)*12
Fcoeffs = np.fft.fft(nino34)
Fpower = np.abs(Fcoeffs)**2

# Only keep the positive frequencies
mask = freq > 0
freq = freq[mask]
Fpower = Fpower[mask]

# Plot the power spectrum
plt.figure(figsize=(12, 6))
plt.loglog(freq, Fpower, color='black')
# Ticks at 2^-3, 2^-2, ... 2^7 (backwards)
ticks=2.**np.arange(-3,7,1)
plt.xticks(ticks=1/ticks, labels=ticks.astype(str))
plt.xlabel("Years", fontsize=14)
plt.ylabel("Power", fontsize=14)
plt.grid(True); plt.tight_layout()
plt.savefig("plots/nino34_powerSpectrum.svg"); plt.show()
