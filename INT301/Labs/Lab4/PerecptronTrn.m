function [w,b,pass]=PerecptronTrn(x,y)
% %Rosenblatt's Perecptron
tic
[l,p]=size(x);
w=zeros(p,1); % initialize weights
b=0;          % initialize bias
ier=1;        % initialize a misclassification indicator
pass=0;       % number of iterations
n=0.5;        % learning rate
r=max(sqrt(sum(x))); % max norm
iter = 0;     % iteration index
while ier==1 %repeat until no error
       ier=0; iter = iter + 1;
       e=0; % number of training errors
       for i=1:l  % a pass through x           
           xx=x(i,:);
           ey=xx*w+b; % estimated y
           if ey>=2 % threshold
              ey=1;
           else
              ey=0;
           end
           if y(i)~=ey
              er=y(i)-ey;      % error difference
              w=w'+(er*n)*x(i,:);             
              e=e+1 ;         % number of training errors
              w=w';   
           end
       end
       e_list(iter)=e;
       ee=e;    % number of training errors
       if ee>0  % continue if there is still errors
          ier=1;           
       end
       pass=pass+1; % stop after 10000 iterations
       if pass==10000
          ier=0;
          pass=0;
       end
end

figure;
plot([0:length(e_list)-1], e_list, '-ko' , 'LineWidth', 0.1);
xlabel('iteration')
ylabel('e-training')

disp(['Training_Errors=' num2str(e) '     Training data Size=' num2str(l)])
toc

 