#python library
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import json

#python script
import get_dataset as d

#visualize loss reduction
def loss_visualizer():

    epoch = []
    train_loss = []
    test_loss = []

    f = open('./result/log', 'r') #load log file
    data = json.load(f)
    f.close()

    value = []

    for i in range(0,len(data)):
        value = data[i]
        epoch.append(value["epoch"])
        train_loss.append(value["main/loss"])
        test_loss.append(value["validation/main/loss"])

    plt.figure(1)
    plt.plot(epoch,train_loss,"b",label = "train LOSS")
    plt.plot(epoch,test_loss,"g",label = "test LOSS")
    #pli.xlim(0,1000)
    #plt.ylim(1e-04,1)
    plt.yscale('log')
    plt.title("LOSS reduction")
    plt.legend()
    plt.xlabel("epoch")
    plt.ylabel("LOSS")


#visualize regression result in draw 3-D graph
def test_result_visualizer(actual_x,actual_y,test_x,estimated_y):

    actual_x1=[]
    actual_x2=[]
    test_x1 = []
    test_x2 = []

    for i in range (len(actual_x)):
        actual_x1.append(actual_x[i][0])
        actual_x2.append(actual_x[i][1])

    for j in range (len(test_x)):
        test_x1.append(test_x[j][0])
        test_x2.append(test_x[j][1])

    fig2 = plt.figure(2)
    ax = Axes3D(fig2)
    p1 = ax.scatter3D(actual_x1,actual_x2,actual_y,color=(1.0,0,0),marker='o',s=10,label='actual data')
    p2 = ax.scatter3D(test_x1,test_x2,estimated_y,color=(0,0,1.0),marker='o',s=10,label='estimated data')

    plt.title("regression for test dataset")
    ax.legend()
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_zlabel("y")


#draw 3D graph
def function_visualizer(model):

    x1_mesh = np.arange(-5,5,0.25)
    x2_mesh = np.arange(-5,5,0.25)

    X1,X2 = np.meshgrid(x1_mesh,x2_mesh)
    X_mesh =[]

    actual_Z = d.real_function(X1,X2)

    for i in range(0,len(x1_mesh)):
        for j in range(0,len(x2_mesh)):
            X_mesh.append([x1_mesh[i],x2_mesh[j]])

    X_mesh = np.array(X_mesh,dtype = np.float32)
    estimated_Z = np.array((model.predictor(X_mesh).data).reshape((len(x1_mesh),len(x2_mesh))))

    fig3 = plt.figure(figsize = plt.figaspect(0.5))

    ax1 = fig3.add_subplot(1, 2, 1, projection='3d')
    w1 = ax1.plot_wireframe(X1,X2,actual_Z,color=(1.0,0,0),label='actual function')
    ax1.legend()
    ax1.set_xlabel("x1")
    ax1.set_ylabel("x2")
    ax1.set_zlabel("y")

    ax2 = fig3.add_subplot(1, 2, 2, projection='3d')
    w2 = ax2.plot_wireframe(X1,X2,estimated_Z,color=(0,0,1.0),label='estimated function')
    ax2.legend()
    ax2.set_xlabel("x1")
    ax2.set_ylabel("x2")
    ax2.set_zlabel("y")
