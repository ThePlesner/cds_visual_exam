# Assignment 1
Before running the script, ensure that the assignment_1 folder consists of the following directories:

```
data/
output/
```

As the dataset used for this assignment is fairly small, it has been included in the repository. Should there for some reason be a problem, the dataset can be downloaded with the following link:

https://www.robots.ox.ac.uk/~vgg/data/flowers/17/17flowers.tgz

The tarfile just has to be unpacked into the `assignment_1/data` directory.

To run the script make sure that the virtual environment is activated. Make sure that you have changed to the assignment_1 directory and run the following command:

```
python image_search.py [-t target/image/path] [-d data/dir/path] [-o output/csv/path.csv]
```

To run the script with only default arguments:
```
python image_search.py
```
These are:
- target_image_path = `./data/jpg/image_0001.jpg`
- data_dir_path = `./data`
- output_path = `./output/output.csv`

Passing in arguments could look something like this:
```
python image_search.py -t data/jpg/image_0002.jpg -d data/jpg/ -o output/output.csv
```

The output folder should now contain .csv file with each image name in the collection and the distance to the target image. 