import sys
sys.path.append("..")
import argparse
from pathlib import Path

from utils.load_mnist import load_mnist

from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def main(data_path):
    # Load data - load_mnist returns a numpy array
    image, label = load_mnist(data_path)

    # Normalization
    image = image / 255.0

    # Split data into test and training sets
    image_train, image_test, label_train, label_test = train_test_split(image, label, random_state=1111, test_size=0.2)

    # classifier 
    classifier = LogisticRegression(penalty='none', 
                                    tol=0.1, 
                                    solver='saga',
                                    multi_class='multinomial').fit(image_train, label_train)

    # Make predictions for images in test-set
    label_predict = classifier.predict(image_test)

    # Get metrics on the comparison between prediction and dataset
    classifier_metrics = metrics.classification_report(label_test, label_predict)

    # Save metrics as a file. A neat format is already present, so txt will do. 
    with open('output/logress_metrics.txt', 'w') as output:
        output.write(classifier_metrics)

    print(classifier_metrics)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "train logistic regression model on the full MNIST dataset and view the classifier metrics")
    parser.add_argument("--data_path", default=Path('./data/'), type = Path, help = "path to where the MNIST csv-files dataset is saved or where to save it")
    args = parser.parse_args()
    
    main(data_path = args.data_path)