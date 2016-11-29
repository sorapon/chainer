# chainer
## scripts
```bash
example_0.py : define variables & calcurate backforward  
example_1.py : vector calcuration 1  
example_2.py : vactor calcuration 2  
example_linear.py : linear regression  
example_sin.py : learning sin curve (NN)  
example_exp.py : leaining exp curve (NN)
```
```bash
tutorial_0.py : same as example_0.py  
tutorial_1.py : same as example_linear.py
```
## regression_1d
```bash
regression_1d_rand_prototype.py : x-y regression prototype  
regression_1d_rand.py : x-y regression (random x)  
regression_1d_rand_mln.py : x-y regression (random x) with 4 layers network  
regression_1d_c.py : x-y regression (continuous x)  
regression_1d_c_mln.py : x-y regression (continuous x) with 4 layers network (continuous)  
regression_1d_c_2chain.py : x-y regression with 2 Chain classes
```
## regression_2d
```bash
plotter.py : 3D figure drawing  
regression_2d_prototype.py : (x1,x2)-y regression prototype  
regression_2d.py : (x1,x2)-y regression  
regression_2d_trainer_prototype.py : (x1,x2)-y regression with trainer prototype  
regression_2d_trainer.py : (x1,x2)-y regression with trainer
```
#### projects
trainer
```bash
get_dataset.py : dataset generator  
network_structure.py : chainer class  
visualizer.py : visualize result  
main.py : main function
```
model_save
```bash
get_dataset.py : dataset generator  
network_structure.py : chainer class  
visualizer.py : visualize result  
learner.py : run learning cycle  
loader.py : load model and draw regression result
```
## regression_2i2o
#### projects
classification_class
```bash
get_dataset.py : dataset generator  
network_structure.py : chainer class  
visualizer.py : visualize result  
learner.py : run learning cycle  
loader.py : load model and draw regression result
```
regression_class
```bash
```
## MNIST
#### projects
mlp
```bash
network_structure.py : chainer class (multi layer perceptron)  
visualizer.py : visualize result  
learner.py : run learning cycle  
loader.py : load model and draw classification result
```
cnn
```bash
network_structure.py : chainer class (CNN)  
visualizer.py : visualize result  
learner.py : run learning cycle  
loader.py : load model and draw classification result
```
