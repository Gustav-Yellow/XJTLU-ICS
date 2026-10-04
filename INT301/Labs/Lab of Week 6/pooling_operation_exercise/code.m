% make sure to change the matlab working directory before execution
%% initialization
clear;
close all;
clc;

%% read the input image
% format the input image into grey channel, 
% double data type and range of [0 1]
im = imread('cat_input.jpg');
im = rgb2gray(im);
im = double(im);
im = im/255;

%% resize the input 
% make sure the size can be divided exactly by scale
% if the size of input is 321x426 and the scale is 2
% then we need to resize 321 to 320 or 322 
% so that it can be divided exactly by 2
im = imresize(im,[512 1024]);

%% max pooling the input
% change ... to your own computer path (no space in path)
% e.g. C:\Users\Desktop\intro_to_cnn\pooling_operation_exercise\MaxPooling_function
addpath ...

% [output, idx] = MaxPooling(input, [scale scale])
% returns the pooled data (output) with the corresponding indices (idx) in input
[output_maxp, idx] = MaxPooling(im, [8 8]);

% show the output using imshow() function in MATLAB
figure;
imshow(output_maxp);

%% mean pooling the input
% change ... to your own computer path (no space in path)
% e.g. C:\Users\Desktop\intro_to_cnn\pooling_operation_exercise\MeanPooling_function
addpath ...

% output = MeanPooling(input, scale)
% returns the pooled data (output)
output_meanp = MeanPooling(im, 8);

% show the output using imshow() function in MATLAB
figure;
imshow(output_meanp);









