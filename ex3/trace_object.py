import argparse
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from frankapy import FrankaArm
import pickle as pkl
import threading

from forward_kinematics_RR import forward_kinematics_RR

class TraceObject:
    def __init__(self, fa, file_name='franka_traj.pkl'):
        self.fa = fa
        self.file_name = file_name
        self.fig, self.ax = plt.subplots()
        self.end_effector_history = []
        self.line, = self.ax.plot([], [], 'r-', label='End Effector Path')
        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(-1, 1)
        self.ax.legend()
        self.ax.set_xlabel('X Position (m)')
        self.ax.set_ylabel('Y Position (m)')
        self.is_tracing = False
        self.ani = FuncAnimation(self.fig, self.update_plot, interval=100, blit=True, cache_frame_data=False)

        self.fig.canvas.mpl_connect('key_press_event', self.on_press)

    def on_press(self, event):
        if event.key == ' ':
            if not self.is_tracing:
                print('Starting tracing...')
                self.is_tracing = True
            else:
                print('Stopping tracing...')
                self.is_tracing = False
                self.save_data()
                # plt.close(self.fig)
        elif event.key == 'g':
            self.fa.close_gripper()
            print("Press spacebar to start recording")

    def update_plot(self, frame):
        if self.is_tracing:
            current_joints = self.fa.get_joints()
            fk_results = forward_kinematics_RR(-current_joints[1], current_joints[3])  # Using FK model from ex1
            end_effector_position = np.array([fk_results['H_4_0'][1, 2], fk_results['H_4_0'][0, 2]])
            self.end_effector_history.append(end_effector_position)

            self.line.set_data([ee[0] for ee in self.end_effector_history], [ee[1] for ee in self.end_effector_history])

        return self.line,

    def save_data(self):
        data = {
            'end_effector_positions': self.end_effector_history
        }
        pkl.dump(data, open(self.file_name, 'wb'))
        print('Data saved to {}'.format(self.file_name))
    
def run_guidance_mode(fa):
    fa.selective_guidance_mode(duration=60, use_impedance=True, use_joints=True, 
                               k_gains=[600.0, 0.0, 600.0, 0.0, 250.0, 150.0, 50.0],
                               d_gains=[50.0, 0.0, 50.0, 0.0, 30.0, 25.0, 15.0])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--open_gripper', '-o', action='store_true')
    parser.add_argument('--file', '-f', default='franka_traj.pkl')
    args = parser.parse_args()

    print('Starting robot')
    fa = FrankaArm()
    fa.open_gripper()
    print('Moving to initial position')
    fa.goto_joints([0.0, -0.1, 0.0, -2.1, -np.pi/2,  np.pi/2,  0.0])
    print('Robot at initial position')
    guidance_mode_thread = threading.Thread(target=run_guidance_mode, args=(fa,))
    guidance_mode_thread.daemon = True
    guidance_mode_thread.start()
    app = TraceObject(fa, file_name=args.file)
    print("Prepare the marker and press 'g' to close the gripper")
    plt.show()

if __name__ == '__main__':
    main()