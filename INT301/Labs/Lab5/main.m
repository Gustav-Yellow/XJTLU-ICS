%% getting data 
clc;clear;close all;
train_path = './traindigit/';
test_path = './testdigit/';
[data_tr,target_tr] = getimdata(train_path); % read getimdata for details
[data_ts,target_ts] = getimdata(test_path);

%% train NN
nhidden = 25; %number of hidden layers
net=newff(data_tr,target_tr,[nhidden,nhidden,nhidden,nhidden],{},'traingd');
% train net
net.trainParam.epochs = 100; %number of training epochs
% train a neural network
[net,tr,Y,E] = train(net,data_tr,target_tr);
% show network
view(net);
Y_test = sim(net,data_ts);
training_acc = rate(getcls(Y), target_tr)
testing_acc = rate(getcls(Y_test), target_ts)