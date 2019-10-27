# BNS Attribute Curve Fitting

Find the relation curve between attributes' value and rate

## I/O

### Input

You need to specify your input file name and path in *read_csv()*

The script accepts .csv files as input with the following format

```
critValue,critRate
0,0.0000
1599,0.1626
...
```

Some sample input data are provided in the following directory

```
/Raw Data/raw_data_*_lv60.csv
```

### Output

1. Optimal values of A, B, C will be shown in console
2. A matplotlib Figure of will be shown during runtime

## Running the file

Explain how to run the file

### Prerequisites

Things you need to install before running the file

```
1. Python https://www.python.org/
```

### Run from an IDE or a Text Editor

If you have an IDE that allows you to run Python scripts from inside the environment, simply use the *Run* or *Build* command in the env.

Commonly used IDEs: Eclipse-PyDev, PyCharm, Eric, NetBeans

Commonly used text editors: Sublime Text, VS Code

### Run from Windows Command Prompt

Run the following command in cmd

```
FULL_PATH_OF_PYTHON FULL_PATH_OF_PY_FILE
e.g. C:/Users/user/AppData/Local/Programs/Python/Python37-32/python.exe "c:/Users/user/Desktop/rawdata_crit_lv60.py"
```

If you added Python to the Windows Path (Environment Variables), simply run the following command

```
python FULL_PATH_OF_PY_FILE
e.g. python "c:/Users/user/Desktop/rawdata_crit_lv60.py"
```

## Authors

* **dbnryanc92** - *Initial work* - [dbnryanc92](https://github.com/dbnryanc92)

## Acknowledgments

N/A