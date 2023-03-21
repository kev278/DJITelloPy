vicon_data = zeros(5, 3);

for i = 1: 1: 100
    vicon_data = vicon_data + i;
    
end

writematrix(vicon_data)
type 'vicon_data.txt'
