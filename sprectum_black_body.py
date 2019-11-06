# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:53:56 2019
Blackbody sprectrum at T=2.725K
@author: Jagannath
"""
from matplotlib import pyplot as plt
import numpy as np
h=6.626*10**-34
c=3*10**8   # all physical quantities are in S.I. units
T=2.725
k=1.38*10**-23    
file ='black_body_data.txt'
a= np.loadtxt(file, skiprows=18, usecols =(0, 1))
freq=a[0:len(a),0]*100*c # Converting to s^-1 i.e. Hz unit
cmb_flux= a[0:len(a),1]
# Given data is in MJy/sr unit so here also the theoretical 
# intensity is converted by multiplying 10^20
intensity=10**20*(2*h*freq**3)/(c**2*(np.exp(h*freq/(k*T))-1)) # this is the 
                    # theoretical radiation intensity
ax = plt.subplot(111)
ax.plot(freq,intensity,label='Theoretical Plot')
ax.plot(freq,cmb_flux,'*',label='From the data COBE')
plt.title('Black Body Radiation Curve at T=2.725K')
plt.ylabel('Radiation Intensity  (MJy/sr)')
plt.xlabel('Freqency of Radiation  (10^11 Hz)')
ax.legend()
plt.show()
max=np.argmax(cmb_flux)
print (c/freq[max])  # wavelength of maximum radiation intensity