# Exam portfolio for visual analytics
Mikkel Plesner Ottosen
## Prerequisites
To be able to run this scripts in this portfolio you will need to have python 3 installed and bash. All scripts has been tested on python 3.9.4 on windows. They have also been tested on worker 2.

## Setup
- Clone this repository
- Open Bash and cd into the cloned repository.
- While at the root of the directory run the following command
`./create_venv_win.sh`
If you're on windows or
`./create_venv_unix.sh`
If you're on a unix-system

## Running scripts
To run scripts the virtual environment needs to be activated by running the following command:
`source venv/Scripts/activate`
If you're on windows or
`source venv/bin/activate`
If you're on a unix-system

## Assignments
Following is a guide on how to execute the code for each assignment.
### Assignment 1
- Change into the directory using 
> `cd assignment_1`.
- Run the script with the following command: 
> `python image_search`
- if you want the default arguments
 or 
> `python image_search -t target/path -d data/dir/path/ -o output/path` 
- for custom data path. 
- `output/` should now contain a csv-file with the result data in it and the terminal should've printed our the most similar image to the target. 
### Assignment 2
- Change into the directory using
> `cd assignment_2`
- Run the script with the following command:
> `python edge-detection.py`
- `output/` should now contain 3 images: `image_cropped.jpg`, `image_letters.jpg` and `image_with_ROI.jpg`
### Assignment 3
- Change into the directory using
> `cd assignment_3`
- For the logistic regression classifier, run the following command:
> `python lr-mnist.py`
- For default arguments or
> `python lr-mnist.py -d data/path`
- For custom arguments.
- For the neural network run the following command:
> `python nn-mnist.py`
- For the default arguments or
> `python nn-mnist.py -d data/dir/path -e number_of_epochs`
- In the `output/` directory there should now be two txt-files, one named `logress_metrics.txt` and one named `nn_metrics.txt` 