import os
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_openml

def load_mnist(data_dir_path):
    image_csv_path = os.path.join(data_dir_path, 'image.csv')
    label_csv_path = os.path.join(data_dir_path, 'label.csv')

    if os.path.isfile(image_csv_path) and os.path.isfile(label_csv_path):
        image = pd.read_csv(image_csv_path)
    
        #'squeeze' the pandas dataframe into a series
        label = pd.read_csv(label_csv_path).squeeze()

        #Convert to numpy array as sklearn might need an explicit conversion
        return (np.array(image), np.array(label))
    else:
        image, label = fetch_openml('mnist_784', version=1, return_X_y=True)

        # use pandas functionality to make csv from the data
        image.to_csv(image_csv_path, sep=',', encoding='utf-8', index=False)
        label.to_csv(label_csv_path, sep=',', encoding='utf-8', index=False)

        #Convert to numpy array as sklearn might need an explicit conversion
        return (np.array(image), np.array(label))