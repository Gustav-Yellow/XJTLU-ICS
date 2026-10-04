function [r, nr]=rate(t1, t2)

% [r] = rate(t1, t2)
% Computes  the percentage of equal columns in t1 and t2, can be used to compute the rate 
% of correct classified patterns in a pattern recognition application 
% t1 - matrix of class vectors (nr of vector element X nr of patterns)
% t2 - matrix of class vectors (nr of vector element X nr of patterns)
% r - the percentage of matching vectors
% nr - Number of matching vectors

[m, n] = size(t1);

nr = 0;

for i=1:n,
  if sum(t1(:,i) == t2(:,i)) == m
    nr = nr + 1;
  end
end

r = 100 * nr / n;