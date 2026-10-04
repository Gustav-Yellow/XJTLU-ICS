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

%% read the kernel image
% format the input image into grey channel, 
% double data type and range of [-1 1]
kernel = imread('kernel_1.jpg');
kernel = rgb2gray(kernel);
kernel = double(kernel);
kernel = (kernel/255-0.5)*2;

%% calculate the convolution result
% using convn() function in MATLAB
output = convn(im, kernel);

%% visualization of input, kernel and convolutional output
% using imagesc() function in MATLAB
figure;
imagesc(im);
figure;
imagesc(kernel);
figure;
imagesc(output);









