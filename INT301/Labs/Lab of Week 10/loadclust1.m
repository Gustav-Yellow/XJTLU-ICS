function [P,T] = loadclust1(N);

% function [P,T] = loadclust1(Ndata);
%
% Generates (up to) N 2-dimensional data points sampled from 6 normal
% distributions with small widths. The data are stored in P and the
% cluster-membership in T.
%
% March 2010, Mattias Ohlsson
% Email: mattias@thep.lu.se

% The locations of the clusters
loc = [3 10 6 -3 -3 -4; -2 2 7 9 2 -5];

% Misc parameters
sigma = 0.80;
M = floor(N/6);

% Make the dataset
for i=1:6
  P(1:2,(i-1)*M+1:i*M) = sigma * randn(2,M) + loc(:,i)*ones(1,M);
  T((i-1)*M+1:i*M) = i;
end

% Rescale
scale = max(max(P));
P = P / scale;
