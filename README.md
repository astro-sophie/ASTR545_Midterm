# Sophie Clark ASTR 545 Midterm
### Code used to create exact figures included in Midterm PDF are in 'plotting.ipynb'. Functions are included in 'plotting_functions.py' ****
#### MESA Models each have their own folder--MESA-Web inputs are included in the inlist file within each folder.

Required packages: numpy, matplotlib, pandas, and astropy

To use models and functions, import plotting_functions.py into your code, then use the desired functions from below.

Functions & inputs:

read_history_file(filepath): reads trimmed_history file outputs from MESA-Web using np.genfromtxt
* filepath: the filepath to the desired trimmed history file

plot_radial_profiles(model, saveas): plots radial evolution as a function of model number and star age, and prints the points when solar values are reached 
* model: output array from read_history_file
* saveas: desired filename to save to (will be saved into a Figures folder)

planetary_engulfment(model): prints the point at which a planet at 1 AU would be engulfed by the star in the model
* model: output array from read_history_file

plot_radial_profile_cases(models_by_case, saveas): prints radial evolution for a variety of models with different cases
* models_by_case: dictionary with a variety of models and a description of their condition (i.e. models_by_case = {'Nuclear burning & chemical evolution': sun_simple_model,'No chemical evolution': sun_simple_model_no_chemical_evolution,...})
* saveas: desired filename to save to (will be saved into a Figures folder)

zams_and_tams(model): returns array indices corresponding to  ZAMS and TAMS
* model: output array from read_history_file

plot_hr_and_radial_profiles_cases(models_by_case, saveas): plots HR diagram and radial evolution as a function of age for a variety of models
* models_by_case: dictionary with a variety of models and a description of their condition (i.e. models_by_case = {'Nuclear burning & chemical evolution': sun_simple_model,'No chemical evolution': sun_simple_model_no_chemical_evolution,...})
* saveas: desired filename to save to (will be saved into a Figures folder)

radius_vs_metallicity(z_vals, models_by_case): outputs plots of radius vs. metallicity at ZAMS, the middle of the main sequence, and TAMS
* z_vals: array with metallicity values
* models_by_case: dictionary with models at different metallicities (i.e. {'Z=0.03': sun_z_0_03,'Z=0.02': sun_simple_model,...})







