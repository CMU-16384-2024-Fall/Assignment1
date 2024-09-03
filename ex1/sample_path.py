from forward_kinematics_RR import forward_kinematics_RR
import numpy as np
import matplotlib.pyplot as plt
import scipy.io

def load_data(path):
    data = scipy.io.loadmat(path)
    return data

def sample_path():
    data = load_data('sample_ground_truth.mat')
    theta = data['theta']  # Joint angles over time
    print(theta)
    ground_truth_x = data['ground_truth_x'].flatten()
    ground_truth_y = data['ground_truth_y'].flatten()

    n = len(theta)
    x, y = [], []

    # Calculate end effector x/y for each timestep using forward kinematics
    for i in range(n):
        frames = forward_kinematics_RR(theta[i, 0], theta[i, 1])
        x.append(frames['H_4_0'][0, 2])
        y.append(frames['H_4_0'][1, 2])

    # Plot actual data
    plt.figure()
    plt.plot(x, y, 'k-', label='Computed Kinematics', linewidth=1)
    plt.plot(ground_truth_x, ground_truth_y, 'g--', label='Ground Truth', linewidth=1)
    plt.title('Plot of End Effector Position Over a Sample Run')
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.axis('equal')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    sample_path()