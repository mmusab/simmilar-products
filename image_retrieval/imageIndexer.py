import os
import numpy as np
import tensorflow as tf
from sklearn.neighbors import NearestNeighbors
from src.CV_IO_utils import read_imgs_dir
from src.CV_transform_utils import apply_transformer
from src.CV_transform_utils import resize_img, normalize_img
from src.CV_plot_utils import plot_query_retrieval, plot_tsne, plot_reconstructions
from src.autoencoder import AutoEncoder
import csv

# Run mode: (autoencoder -> simpleAE, convAE) or (transfer learning -> vgg19)
modelName = "vgg19"  # try: "simpleAE", "convAE", "vgg19"
trainModel = True
parallel = True  # use multicore processing

# Make paths
dataTrainDir = os.path.join(os.getcwd(), "data", "train")
print(dataTrainDir)

# Read images
extensions = [".jpg", ".jpeg"]
print("Reading train images from '{}'...".format(dataTrainDir))
train_name = os.listdir( dataTrainDir )
imgs_train = read_imgs_dir(dataTrainDir, extensions, parallel=parallel)
shape_img = imgs_train[0].shape
print("Image shape = {}".format(shape_img))


# Load pre-trained VGG19 model + higher level layers
print("Loading VGG19 pre-trained model...")
model = tf.keras.applications.VGG19(weights='vgg19_weights_tf_dim_ordering_tf_kernels_notop.h5', include_top=False,
                                        input_shape=shape_img)
model.summary()
shape_img_resize = tuple([int(x) for x in model.input.shape[1:]])
input_shape_model = tuple([int(x) for x in model.input.shape[1:]])
output_shape_model = tuple([int(x) for x in model.output.shape[1:]])
n_epochs = None


# Apply transformations to all images
class ImageTransformer(object):

    def __init__(self, shape_resize):
        self.shape_resize = shape_resize

    def __call__(self, img):
        img_transformed = resize_img(img, self.shape_resize)
        img_transformed = normalize_img(img_transformed)
        return img_transformed

transformer = ImageTransformer(shape_img_resize)
print("Applying image transformer to training images...")
imgs_train_transformed = apply_transformer(imgs_train, transformer, parallel=parallel)


# Convert images to numpy array
X_train = np.array(imgs_train_transformed).reshape((-1,) + input_shape_model)
# X_test = np.array(imgs_test_transformed).reshape((-1,) + input_shape_model)
print(" -> X_train.shape = {}".format(X_train.shape))


# Create embeddings using model
print("Inferencing embeddings using pre-trained model...")
E_train = model.predict(X_train)
E_train_flatten = E_train.reshape((-1, np.prod(output_shape_model)))
print(" -> E_train.shape = {}".format(E_train.shape))
print(" -> E_train_flatten.shape = {}".format(E_train_flatten.shape))

print(E_train_flatten[0])
rlist = []
for l in E_train_flatten:
	rlist.append([i for i in l])

print(len(rlist))

# print(rlist)

with open('returns.csv', 'w') as f:
    writer = csv.writer(f)
    for val in rlist:
        writer.writerow([val])