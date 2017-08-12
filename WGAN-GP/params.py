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
z_dim = 100
d_conv_dim = 64
g_conv_dim = 64
d_model_restore = None
g_model_restore = None

# params for training network
num_gpu = 1
num_epochs = 100
log_step = 1
sample_step = 100
save_step = 10
manual_seed = None

# params for optimizing models
d_steps = 5
g_steps = 1
d_learning_rate = 0.00005
g_learning_rate = 0.00005
beta1 = 0.5
beta2 = 0.999
use_Adam = False
use_BN = True

# params for WGAN and WGAN-GP
use_gradient_penalty = False  # quickly switch WGAN and WGAN-GP
clamp_upper = 0.01
clamp_lower = -0.01
penalty_lambda = 10
# TODO(corenel) add extra layers for D and G?
