function net = trainp_sh(net, p, t, neps)
% net = trainp_sh(net, p, t, neps)
% Trains a perceptron with two inputs and shows the decision
% boundary after each epoch.
% Input
%  net  - perceptron
%  p    - Two-dimensional input vectors
%  t    - One dimensional target vectors (0 or 1)
%  neps - number of epochs to train, optional DEFAULT = 100
% Return
%  net - the trained perceptron

%nargin returns the number of arguments input when the function is called.
if nargin<4 
  neps = 100;
end

plotpv(p, t);
h = plotpc(net.IW{1}, net.b{1});
e = 1;
ep = 0;
while sum(abs(e))>0 & ep<neps, % while error still exists and the number of epochs not reached
  [net, y, e, pf, af, ar] = adapt(net, p, t); % update the weights of the net and output prediction, error
  h = plotpc(net.IW{1},net.b{1}, h);
  drawnow;
  ep = ep + 1;
end