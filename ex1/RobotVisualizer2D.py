import matplotlib.pyplot as plt
import numpy as np

class RobotVisualizer2D:
    def __init__(self, num_frames, axis_length=0.1):
        self.fig, self.ax = plt.subplots()
        self.num_frames = num_frames
        self.axis_length = axis_length
        self.initialize_figure()

    def initialize_figure(self):
        self.ax.set_aspect('equal')
        self.ax.grid(True)
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)

    def set_frames(self, frames):
        for i in range(self.num_frames):
            T = frames[:,:,i]
            origin = np.array([0, 0, 1])
            x_end = T @ np.array([self.axis_length, 0, 1])
            y_end = T @ np.array([0, self.axis_length, 1])
            
            # Draw the frame axes
            self.ax.plot([origin[0], x_end[0]], [origin[1], x_end[1]], 'r-')
            self.ax.plot([origin[0], y_end[0]], [origin[1], y_end[1]], 'g-')

    def show(self):
        plt.show()