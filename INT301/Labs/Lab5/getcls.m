function cls = getcls(vecs)

% cls = getcls(vecs) 
% Input: vecs - matrix of column vectors
% Output: cls    - matrix where the largest element in each column in vecs
%                  is set to 1 and the rest to 0
%                  Ex: vecs = [2 4; 1 5], gives c = [1 0; 0 1]

[ncls, nvecs] = size(vecs);
[tmp, c] = max(vecs);
cls = zeros(ncls,nvecs);
for j=1:nvecs
  cls(c(j),j) = 1;
end