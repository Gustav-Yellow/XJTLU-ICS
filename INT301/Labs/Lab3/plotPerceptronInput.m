%%% This code is used in the Perceptron simulation.
%%% Related files: initPerceptron.m, trainPerceptron.m, plotDecisionSurf.m, runPerceptron.m

%%% Plot 3-dimensional input patterns as a scatterplot, with the first half of the pattern plotted as o's and the 2nd half as *'s.
plot3(input(1,1:mid),input(2,1:mid),input(3,1:mid),'mo');
plot3(input(1,mid+1:nPats),input(2,mid+1:nPats),input(3,mid+1:nPats),'c*');


