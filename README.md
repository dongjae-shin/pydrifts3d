# Introduction - pydrifts3d
`pydrifts2d` is a python code to convert the experimental raw spectra data from DRIFTS (Diffuse Reflectance Infrared Fourier Transform Spectroscopy) to three dimensional plot. Multiple DRIFTS plots can be automatically generated according to the used-defined plotting parameters.

# How to use
## 1. Using executable file in Windows
1) Download executable file (drifts.exe) from the link:
link: https://www.dropbox.com/s/39ubk45g0n2wp9k/drifts.exe?dl=0
2) Put (multiple) DRIFTS files (csv format) in the same directory of the executable file.
3) Run the executable file by double-clicking (It takes ~30 to 60 seconds before something first pops up, depending on the running environment).
![band_with_no_args](imgs/band_no_args.png)
4) Output png files are generated.

## 2. Using python code in Linux
1) Download the `drifts.py' file from this repository.
2) Put (multiple) DRIFTS files (csv format) in the same directory of the executable file in Linux.
3) Run the code by typing:
```$ python drifts.py```
It may run faster than in Windows.
5) Output png files are generated.



## **1. drifts.exe**
![DRIFTS_PLOT](https://user-images.githubusercontent.com/25687036/154058040-5935b51c-27b3-465e-921e-129184d46916.gif)

## **2. output.png**
![output](https://user-images.githubusercontent.com/25687036/154058125-1c775051-e35c-42af-8b7d-1361c83938fe.png)

## **3. applications of this code**
1. ACS Catal. 2022, 12, 8, 4402–4414 (https://doi.org/10.1021/acscatal.2c00476)   
2. J. Mater. Chem. A, 2022, 10, 24995-25008 (https://doi.org/10.1039/d2ta08217a)
