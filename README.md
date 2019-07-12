# PerfAutopsy
Performance of Autopsy Software

This script is written in Python and its purpose is to automate tests sequentially in the digital forensics platform and graphical interface to The Sleuth Kit, Autopsy.

The output is a text file named "resultados" in the same location as the python file.  
Folders "Linux" and "Windows" contains actiona scripts, it may need to be reconfigured due to different screen resolutions.  
The file "PreSelected.py" is the same as the PerAutopsy just have the dropdowns with a pre-selected test.  

"Start.ascr" file is an actiona script configured to open Autopsy and create a new case. It was used in the firsts versions.  

Modules:  
1-Recent Activity  
2-Hash Lookup  
3-File Type Identification  
4-Extension Mismatch Detector  
5-Embedded File Extractor  
6-Exif Parser  
7-Keyworkd Search  
8-Email Parser  
9-Encrytion Detection  
10-Interesting Files Identifier  
11-Correlation Engine  
12-PhotoRec Carver  
13-Virtual Machine Extractor  
14-Data Source Integrity  
15-Android Analyser  

## Requirements  

* [Python](https://www.python.org/downloads/) with  
TKinter (sudo apt-get install python3-tk)

### Running

To run the script, simply open a terminal and run:  

```
python3 PerfAutopsy.py
```
§
In linux we recommend the usage of sudo:

```
sudo python3 PerfAutopsy.py
```


## Authors

* **António Silva** 
* **Leandro Antunes** 

