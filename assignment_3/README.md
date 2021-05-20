# Assignment 3
Before running the scripts, ensure that the assignment_1 folder consists of the following directories:

```
data/
output/
utils/
```

Also ensure that the `utils/` directory contains the following files:

```
classifier_utils.py
load_mnist.py
neuralnetwork.py
```
The dataset needed for this assignment will be loaded automatically by the load_mnist utility-function.

To run the script make sure that the virtual environment is activated. Make sure that you have changed to the assignment_3 directory.

### Logistic regression
To run the logistic regression script run the following command:
```
python lr-mnist.py [-d data/dir/path]
```

To run the script with only default arguments:
```
python lr-mnist.py
```
These are:
- data_dir_path = `./data`

Passing in arguments could look something like this:
```
python lr-mnist.py data/
```
The output directory should now contain a txt-file called `logress_metrics.txt`

### Neural network
To run the neural network script run the following command:
```
python nn-mnist.py [-d data/dir/path] [-e number_of_epochs]
```

To run the script with only default arguments:
```
python nn-mnist.py
```
These are:
- data_dir_path = `./data`
- number_of_epochs = 5

Passing in arguments could look something like this:
```
python nn-mnist.py data/ 6
```
The output directory should now contain a txt-file called `nn_metrics.txt`