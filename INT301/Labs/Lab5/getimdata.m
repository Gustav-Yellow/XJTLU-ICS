function [ data,target ] = getimdata( path )
%GETIMDATA Summary of this function goes here
%   Detailed explanation goes here 
    files = dir([path '*.bmp']);
    data=[];
    target=[];
    for file = files'
        im = imread([path file.name]);
        data = [data im(:)];
        if strcmp(file.name(1),'0')
            target=[target [1;0;0;0;0;0]];
        elseif strcmp(file.name(1),'1')
            target=[target [0;1;0;0;0;0]];
        elseif strcmp(file.name(1),'2')
            target=[target [0;1;0;0;0;0]];
        elseif strcmp(file.name(1),'3')
            target=[target [0;0;1;0;0;0]];
        elseif strcmp(file.name(1),'4')
            target=[target [0;0;0;1;0;0]];
        elseif strcmp(file.name(1),'5')
            target=[target [0;0;0;0;1;0]];    
        end    
    end

end

