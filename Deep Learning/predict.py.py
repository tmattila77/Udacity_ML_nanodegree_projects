import tensorflow as tf
import numpy as np
import argparse
from PIL import Image
import json

with open('label_map.json', 'r') as f:
    class_names = json.load(f)


# process the image
def process_image(image_path):
    im = Image.open(image_path)
    image = np.asarray(im)

    image_tf = tf.convert_to_tensor(image)
    image_tf = tf.image.resize(image_tf, [224,224])
    image_tf /= 255
    image_np = image_tf.numpy()
    return image_np

#make a prediction
def predict(savedModel_directory, image_path):
    reloaded_SavedModel = tf.saved_model.load(savedModel_directory) 
    processed_image = process_image(image_path)
    processed_image_4 = np.expand_dims(processed_image, axis = 0)
    final_image = tf.convert_to_tensor(processed_image_4)
    prediction = reloaded_SavedModel(final_image, training=False)
    indeces = (-prediction.numpy()).argsort() 
    indeces2 = indeces[0][0:5]
    probs = []
    classes = []
    for index, i in zip(indeces2, range(5)):
        probs.append((prediction.numpy())[0][index])
        classes.append(indeces2[i]+1)
    print("The list of probabilities: ",probs)
    print("This list of corresponding classes ",classes)
    
    names = []
    for label in classes:
        label_str = str(label)
        name = class_names.get(label_str)
        names.append(name)
        
    print("The list of probabilities: ", probs)
    print("The list of class names: ", names)

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("f", help = "The directory of label_map.json")
    parser.add_argument("savedModel_directory", help = "The directory that contains the saved Keras model")
    parser.add_argument("image_path", help = "the path to the test image")
    
    args = parser.parse_args()
    result = predict(args.savedModel_directory, args.image_path)
    return result
    
if __name__ == '__main__':
    Main()
    
    
