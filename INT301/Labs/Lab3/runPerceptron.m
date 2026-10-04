%%% This code is used in the Perceptron simulation.
%%% Related files: initPerceptron.m, plotPerceptronInput.m, trainPerceptron.m, plotDecisionSurf.m

%% figure setting
clf  %%% clear the figure window
hold on  %%% 'hold on' to allow incremental plotting of input and weights
view(-37.5,30) %%% fix the angle of view: horizontal -37.5 degree; vertical 30 degree 
plotPerceptronInput %% read plotPerceptronInput.m
xlabel('x1')
ylabel('x2')
zlabel('x3')
title('Classification boundary for a 3-input, 1-output perceptron')
grid on

%% train perceptron
for patNum = 1:nPats
  weights = trainPerceptron(patNum, weights,input,target,lRate); %% read trainPerceptron.m
end
plotDecisionSurf %% read plotDecisionSurf.m
weights %% show weights in command window
