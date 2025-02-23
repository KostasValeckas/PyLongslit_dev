from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

linewidth=0.7



def FitsReader(filePath):
        spec_file_f = filePath
        spec_f = fits.getdata(spec_file_f,1)
        return np.array([spec_f.field("wave"),spec_f.field("flux")*1E-17, spec_f.field("sigma")*1E-17])

Spec = FitsReader("./SDSS_J213510+2728.fits")


def load_sciece_spec():
    #TODO: combine this with the load_standard_star_spec function, move to utils.py

    filename = "./SDSS_J213510+2728_combined.dat"

    data = np.loadtxt(filename, skiprows=2)
    wavelength = data[:,0]
    spec = data[:,1]
    sigma = np.sqrt(data[:,2])


    return wavelength, spec, sigma

longslit_wave, longslit_spec, longslit_sigma = load_sciece_spec()

#longslit_spec = longslit_spec/2

wave_pypeit, spec_pypeit, sigma_pypeit = Spec

mask = wave_pypeit != 0

print(mask)

    
fig,ax1=plt.subplots(1,1,figsize=(18,12))

ax1.plot(wave_pypeit[mask],spec_pypeit[mask],lw=linewidth,color="k",label="Pypeit")
ax1.plot(wave_pypeit[mask],sigma_pypeit[mask],lw=linewidth,color="k",label="Pypeit 1-sigma noise")

ax1.plot(longslit_wave,longslit_spec,lw=linewidth,color="r",label="Longslit")
ax1.plot(longslit_wave,longslit_sigma,lw=linewidth,color="r",label="Longslit 1-sigma noise")

ax1.legend()


fig.supxlabel("Observed Wavelength (Å)", y=0.05 ,fontsize=12)
fig.supylabel("Flux (erg/s/cm²/Å))",fontsize=12)


plt.savefig("./first_test.png",bbox_inches="tight",facecolor="white")
plt.show()
