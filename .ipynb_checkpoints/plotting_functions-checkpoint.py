import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import astropy.units as u

def read_history_file(filepath):
    return np.genfromtxt(filepath, skip_header=5, names=True)

# Function I used to plot radial evolution for the Sun-like star
def plot_radial_profiles(model, saveas)
    idx_age, idx_radius = np.argmin(np.abs(model['star_age'] - 4.5e9)), np.argmin(np.abs(10**model['log_R'] - 1))
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 4), sharey=False)    # Radius vs. model number
    ax1.plot(model['model_number'], 10**model['log_R'])
    ax1.vlines(model['model_number'][idx_age], ymin=0, ymax=np.max(10**model['log_R']), linestyle = '--', color='red', label='Solar age (4.5 Gyr)', alpha=0.5)
    ax1.vlines(model['model_number'][idx_radius], ymin=0, ymax=np.max(10**model['log_R']), linestyle = '--', color='green', label=r'Solar radius (1$R_\odot$)', alpha=0.5)
    ax1.grid()
    ax1.set_xlabel('Model Number')
    ax1.set_ylabel(r'Radius ($R_\odot$)')
    ax1.set_yscale('log')
    ax1.legend(loc='lower center')
    # Radius vs. star age
    ax2.plot(model['star_age']/1e9, 10**model['log_R'])
    ax2.vlines(model['star_age'][idx_age]/1e9, ymin=0, ymax=np.max(10**model['log_R']), linestyle = '--', color='red', label='Solar age (4.5 Gyr)', alpha=0.5)
    ax2.vlines(model['star_age'][idx_radius]/1e9, ymin=0, ymax=np.max(10**model['log_R']), linestyle = '--', color='green', label=r'Solar radius (1$R_\odot$)', alpha=0.5)
    ax2.grid()
    ax2.set_xlabel('Star age (Gyr)')
    ax2.set_ylabel(r'Radius ($R_\odot$)')
    ax2.set_yscale('log')
    ax2.legend(loc='lower center')
    plt.savefig(f'Figures/{savename}.png', dpi=500, bbox_inches='tight')
    plt.show()
    print(f"The present day value is {10**sun_simple_model['log_R'][idx_age]:.3f}. The radius equals 1 R_sun at {sun_simple_model['star_age'][idx_radius]/1e9:.4e} Gyrs.")

# Function I used to determine when a planet at 1 AU is engulfed by a Sun-like star
def planetary_engulfment(model):
    r_sun_1au = 1*u.AU.to(u.Rsun)
    idx_engulfment = np.argmin(abs(10**model['log_R'] - r_sun_1au))
    print(f"A planet at 1 AU would be engulfed at t={model['star_age'][idx_engulfment]} yrs, at model {model['model_number'][idx_engulfment]}.")
    print(f"The maximum age reached by this stellar model was t={np.max(model['star_age'])} yrs.")

# Function I used to plot the radial evolution for different burning modifiers
def plot_radial_profile_cases(models_by_case, saveas):
    cases = list(models_by_case.keys())
    nC = len(cases)
    fig, axes = plt.subplots(nrows=nC,ncols=2,figsize=(10, 4 * nC),sharex=False,sharey=False)
    if nC == 1:
        axes = np.array([axes])
    for i, case in enumerate(cases):
        model = models_by_case[case]
        idx_age, idx_radius = np.argmin(np.abs(model['star_age'] - 4.5e9)), np.argmin(np.abs(10**model['log_R'] - 1))
        ax1, ax2 = axes[i]
        radius = 10**model['log_R']
        maxR = np.max(radius)
        # Radius vs. model number
        ax1.plot(model['model_number'], radius)
        ax1.vlines(model['model_number'][idx_age], 0, maxR,linestyle='--', color='red', alpha=0.5,label='4.5 Gyr')
        ax1.vlines(model['model_number'][idx_radius], 0, maxR,linestyle='--', color='green', alpha=0.5,label=r'1 $R_\odot$')
        ax1.grid()
        ax1.set_xlabel('Model Number')
        ax1.set_ylabel(f'{case}\n Radius '+r'($R_\odot$)')
        ax1.set_yscale('log')
        ax1.legend(loc='best')
        # Radius vs. star age
        age = model['star_age'] / 1e9  # convert to Gyr
        ax2.plot(age, radius)
        ax2.vlines(age[idx_age], 0, maxR,linestyle='--', color='red', alpha=0.5, label='4.5 Gyr')
        ax2.vlines(age[idx_radius], 0, maxR,linestyle='--', color='green', alpha=0.5, label=r'1 $R_\odot$')
        ax2.grid()
        ax2.set_xlabel('Star Age (Gyr)')
        ax2.set_ylabel(r'Radius ($R_\odot$)')
        ax2.set_yscale('log')
        ax2.legend(loc='best')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(f'Figures/{saveas}.png',dpi=500, bbox_inches='tight')
    plt.show()

### Stellar evolution ###
def zams_and_tams(model):
    diffs = abs(model['center_h1']-(0.99*model['center_h1'][0]))
    zams = np.where(diffs == np.min(diffs))
    diffs = abs(model['center_h1']-(0.01*model['center_h1'][0]))
    tams = np.where(diffs == np.min(diffs))
    return zams, tams

# Function I used to plot the HR diagrams and radial evolution for stars with different metallicities
def plot_hr_and_radial_profiles_cases(models_by_case, saveas):
    cases = list(models_by_case.keys())
    nC = len(cases)
    fig, axes = plt.subplots(nrows=nC,ncols=2,figsize=(10, 4 * nC),sharex=False,sharey=False)
    if nC == 1:
        axes = np.array([axes])
    for i, case in enumerate(cases):
        model = models_by_case[case]
        zams, tams = zams_and_tams(model)
        idx_age, idx_radius = np.argmin(np.abs(model['star_age'] - 4.5e9)), np.argmin(np.abs(10**model['log_R'] - 1))
        ax1, ax2 = axes[i]
        radius = 10**model['log_R']
        maxR = np.max(radius)
        # HR diagram
        ax1.plot(model['log_Teff'], model['log_L'])
        ax1.scatter(model['log_Teff'][zams], model['log_L'][zams], label='ZAMS', color='red')
        ax1.scatter(model['log_Teff'][tams], model['log_L'][tams], label='TAMS', color='green')
        ax1.legend()
        ax1.grid()
        ax1.set_xlabel(r'log($T_\mathrm{eff}$)')
        ax1.set_ylabel(f'{case}\n log(L'+r'/$L_\odot$)')
        # Radius vs. star age
        age = model['star_age'] / 1e9  # convert to Gyr
        ax2.plot(age, radius)
        ax2.vlines(age[idx_age], 0, maxR,linestyle='--', color='red', alpha=0.5, label='4.5 Gyr')
        ax2.vlines(age[idx_radius], 0, maxR,linestyle='--', color='green', alpha=0.5, label=r'1 $R_\odot$')
        ax2.scatter(age[zams], radius[zams], label='ZAMS', color='red')
        ax2.scatter(age[tams], radius[tams], label='TAMS', color='green')
        ax2.grid()
        ax2.set_xlabel('Star Age (Gyr)')
        ax2.set_ylabel(r'Radius ($R_\odot$)')
        ax2.set_yscale('log')
        ax2.legend(loc='best')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(f'Figures/{saveas}.png',dpi=500, bbox_inches='tight')
    plt.show()

### R(Z) trend ###
def radius_vs_metallicity(z_vals, models_by_case):
    cases = list(models_by_case.keys())
    fig, (ax1, ax2, ax3)  = plt.subplots(nrows=1,ncols=3,figsize=(14, 4),sharex=False,sharey=False)
    zams_r_vals, tams_r_vals, middle_r_vals = [], [], []
    for i, case in enumerate(cases):
        model = models_by_case[case]
        zams, tams = zams_and_tams(model)
        middle_of_ms = zams[0][0]+round((tams[0][0]-zams[0][0])/2)
        print(zams, tams, middle_of_ms)
        zams_r_vals.append(10**model['log_R'][zams])
        tams_r_vals.append(10**model['log_R'][tams])
        middle_r_vals.append(10**model['log_R'][middle_of_ms])
    ax1.plot(z_vals, zams_r_vals)
    ax1.scatter(z_vals, zams_r_vals)                        
    ax1.set_xlabel('Z')
    ax1.set_ylabel(r'Radius ($R_\odot$)')
    ax1.set_title('ZAMS')
    ax1.grid()
    ax2.plot(z_vals, tams_r_vals)
    ax2.scatter(z_vals, tams_r_vals)
    ax2.set_xlabel('Z')
    ax2.set_ylabel(r'Radius ($R_\odot$)')
    ax2.set_title('TAMS')
    ax2.grid()
    ax3.plot(z_vals, middle_r_vals)
    ax3.scatter(z_vals, middle_r_vals)
    ax3.set_xlabel('Z')
    ax3.set_ylabel(r'Radius ($R_\odot$)')
    ax3.set_title('Middle of main sequence')
    ax3.grid()               
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(f'Figures/r_vs_z',dpi=500, bbox_inches='tight')
    plt.show()

