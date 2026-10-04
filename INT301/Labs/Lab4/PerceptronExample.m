 function PerceptronExample
% Rosenblatt's Perecptron
% References :
%      Neural Networks for Pattern Recognition By C. Bishop

clc
%============================================
% Generate 2 dimensions linear separable data 
%===========================================

% You may change the size of the data from here or input your own data
 %   note that the drawing is for two dimensions only, hence you need to 
 %   modify the code for different data.
mydata = rand(500,2);
% Separate the data into two classes
acceptindex = abs(mydata(:,1)-mydata(:,2))>0.012;
mydata = mydata(acceptindex,:); % data
myclasses = mydata(:,1)>mydata(:,2); % labels
[m n]=size(mydata);

% The next two lines divide the data into training and testing parts
%training data
x=mydata(1:400,:);  y=myclasses(1:400);
% test data
xt=mydata(401:m,:); yt=myclasses(401:m);
%=====================================
% Train the perceptron
%=====================================
[w,b,pass] = PerecptronTrn(x,y);
Iterations=pass

%=====================================
% Test
%=====================================
e=PerecptronTst(xt,yt,w,b);
disp(['Test_Errors=' num2str(e) '     Test Data Size= ' num2str(m-400)])

%=====================================
% Draw the result (sparating hyperplane)
%=====================================
 l=y;
 figure;
 hold on
 plot(x(l,1),x(l,2),'k.' );
 plot(x(~l,1),x(~l,2),'b.');
 plot([0,1],[0,1],'r-')
 axis([0 1 0 1]), axis square, grid on
 drawnow


 