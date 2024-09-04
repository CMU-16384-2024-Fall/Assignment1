import numpy as np

def forward_kinematics_RR(theta1, theta2):
    """
    Returns the forward kinematics for an RR robot given the joint angle positions in radians.
    """
    l1 = 0.316  # length of the first link
    l2 = 0.384+0.088  # length of the second link 

    # To-Do 1: Compute the homogeneous transformation matrices H_1_0, H_2_1, H_3_2, and H_4_3
    H_1_0 = np.eye(3)    
    H_2_1 = np.eye(3)
    H_3_2 = np.eye(3)
    H_4_3 = np.eye(3)
    
    # To-Do 2: Compute the homogeneous transformation matrix H_4_0
    H_4_0 = ...
    
    return {
        'H_1_0': H_1_0,
        'H_2_1': H_2_1,
        'H_3_2': H_3_2,
        'H_4_3': H_4_3,
        'H_4_0': H_4_0
    }