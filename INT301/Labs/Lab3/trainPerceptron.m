%%% This code is used in the Perceptron simulation. 
%%% Related files: initPerceptron.m, plotPerceptronInput.m, plotDecisionSurf.m, runPerceptron.m

function [newWts] = trainPerceptron(patNum,wts,pats,targ,lrate) %% patNum, weights,input,target,lRate from runPerceptron.m
nOutputs = size(targ,1);
for i = 1:nOutputs
   inputVector = pats(:,patNum);
   targetOutput = targ(i,patNum);
   totalInput = dot(wts(i,:),inputVector); %% Vector dot product
   if (totalInput > 0) 
     activation = 1;
   else activation = -1;
   end	
   % computer weight change
   if (activation > targetOutput)
     % unit is on but should be off 
     wts(i,:) = wts(i,:) - lrate * inputVector';
   elseif (activation < targetOutput)
     % unit is off but should be on
     wts(i,:) = wts(i,:) + lrate * inputVector';
   end
end 
newWts = wts; %% update weight once after each data sample (each column of input and target)
