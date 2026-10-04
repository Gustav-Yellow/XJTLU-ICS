function output = MeanPooling(input, scale)
z = convn(input, ones(scale) / (scale ^ 2));   %  !! replace with variable
output = z(1 :scale : end, 1 :scale : end, :);
end