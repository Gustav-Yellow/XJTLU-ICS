% Demo code of lab of week 9
% Suggestion: try multiple times for better performance

clf;clc;close all;clear;
n = 20; % training data size
m = 30; % testing data size
K = 15; % hidden unit size
epochs = 300; % number of epochs

%% training stage
% create training data
x = ones(n,1); % initialize the input series with all ones
for i=3:n
    x(i) = 0.75 * x(i-1)^2 + 0.2 * x(i-2); % update the input series from 3rd element onwards
end    
plot(x,'b.'); hold on;
y = x(3:n); % target in training set
x = [x(1:n-2) x(2:n-1)]; % input in training set

% train Elman network
net = newelm(x',y',[K]);
[net,tr] = train(net,x',y');
view(net);

%% testing stage
x_pred = [1 1]; % initialize first two inputs in testing set
plot(1,x_pred(1),'ro'); hold on;
plot(2,x_pred(2),'ro'); hold on;
for i=2:m+1
    next = sim(net,x_pred'); % make prediction using trained Elman network using testing input
    plot(i+1,next,'ro'); hold on;
    x_pred = [x_pred(2) next]; % update testing input: original x_pred=[x_pred(1) x_pred(2)]; updated x_pred=[x_pred(2) next];
end    



