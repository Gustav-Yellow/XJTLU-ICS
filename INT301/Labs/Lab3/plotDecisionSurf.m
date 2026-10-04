%%% This code is used in the Perceptron simulation.
%%% Related files: initPerceptron.m, plotPerceptronInput.m, trainPerceptron.m, runPerceptron.m

%%% Create a grid of (X1,X2,X3) values covering the region defined by weights(1)*X1 + weights(2)*X2 + weights(3)*X3 + weights(4) = 0

% Create vectors of co-ordinates for first 2 axes
x1=0:0.1:1;
x2=x1;

% Convert these to matrices of co-ordinates for plotting.
[X1,X2]=meshgrid(x1,x2);

% Create matrix of surface values (X3) at the co-ordinates given in X1,X2. 
% weights(3)*X3 = -1*(weights(1)*X1 + weights(2)*X2 +  weights(4))
SURFACE=-1/weights(3)*(weights(4)*ones(size(X1))+weights(1)*X1+weights(2)*X2);

% plot the grid points
mesh(X1,X2,SURFACE);  
