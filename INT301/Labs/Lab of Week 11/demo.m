close all, clear all, clc, format compact 
load simplecluster_dataset;
% a 2x1000 matrix of 1000 two-element vectors.
x = simpleclusterInputs; 
% plot clusters 
figure, plot(x(1,:),x(2,:),'g.');
hold on 
grid on

% Create a Self-Organizing Map
dim1 = 10; 
dim2 = 10; 
net = selforgmap([dim1 dim2]); 
% Train the Network 
[net,tr] = train(net,x); 

% View the Network 
view(net) 
% Plots 
figure, plotsomtop(net) 
figure, plotsomnc(net)
figure, plotsomnd(net) 
figure, plotsomplanes(net) 
figure, plotsomhits(net,x) 
figure, plotsompos(net,x) 
