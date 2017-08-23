"""Params for WGAN-GP."""

# params for dataset and data loader
data_root = "../data/"
dataset_mean_value = 0.5
dataset_std_value = 0.5
dataset_mean = (dataset_mean_value, dataset_mean_value, dataset_mean_value)
dataset_std = (dataset_std_value, dataset_std_value, dataset_std_value)
batch_size = 64
image_size = 64

# params for setting up models
model_root = "../model/"
num_channels = 3
num_extra_layers = 0
z_dim = 128
d_conv_dim = 64
g_conv_dim = 64
d_model_restore = None
g_model_restore = None

# params for training network
num_gpu = 1
num_epochs = 20000
log_step = 1
sample_step = 1000
save_step = 1000
manual_seed = None

# params for optimizing models
d_steps = 5
# g_steps = 1
d_learning_rate = 1e-4
g_learning_rate = 1e-4
beta1 = 0.5
beta2 = 0.9
use_Adam = True
use_BN = False

# params for WGAN and WGAN-GP
use_gradient_penalty = True  # quickly switch WGAN and WGAN-GP
penalty_lambda = 10
# TODO(corenel) add extra layers for D and G?
