import numpy as np
import matplotlib.pyplot as plt

def endEffector_RR(theta, linkLengths):
    s1 = np.sin(theta[0])
    c1 = np.cos(theta[0])
    s12 = np.sin(theta[0] + theta[1])
    c12 = np.cos(theta[0] + theta[1])

    l1 = linkLengths[0]
    l2 = linkLengths[1]

    x = l1 * c1 + l2 * c12
    y = l1 * s1 + l2 * s12
    return x, y

def workspace_analysis_RR(linkLengths):
    nSamples = 50
    minAngle = 0
    maxAngle = 2 * np.pi

    theta_1 = np.linspace(minAngle, maxAngle, nSamples)
    theta_2 = np.linspace(minAngle, maxAngle, nSamples)
    x = np.zeros(nSamples**2)
    y = np.zeros(nSamples**2)

    for i in range(nSamples):
        for j in range(nSamples):
            theta = [theta_1[i], theta_2[j]]
            index = i * nSamples + j
            x[index], y[index] = endEffector_RR(theta, linkLengths)

    plt.figure()
    plt.plot(x, y, 'o')
    plt.title('End Effector Workspace')
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.axis('equal')
    plt.axis('tight')
    plt.show()

# Example usage
linkLengths = [0.375, 0.310]
workspace_analysis_RR(linkLengths)