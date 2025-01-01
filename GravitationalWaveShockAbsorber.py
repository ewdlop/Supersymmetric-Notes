import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

class GravitationalWave:
    """
    A class to simulate linearized gravitational waves and their effects on test particles.
    """
    def __init__(self, amplitude_plus=1e-21, amplitude_cross=0, frequency=100):
        """
        Initialize the gravitational wave parameters.
        
        Parameters:
        - amplitude_plus: Amplitude of the plus polarization
        - amplitude_cross: Amplitude of the cross polarization
        - frequency: Wave frequency in Hz
        """
        self.h_plus = amplitude_plus
        self.h_cross = amplitude_cross
        self.frequency = frequency
        self.omega = 2 * np.pi * frequency

    def metric_perturbation(self, t, z=0):
        """
        Calculate the metric perturbation components at time t and position z.
        Returns the h+ and h× components.
        """
        phase = self.omega * (t - z)
        h_plus = self.h_plus * np.cos(phase)
        h_cross = self.h_cross * np.cos(phase)
        return h_plus, h_cross

    def strain_tensor(self, t, z=0):
        """
        Compute the full strain tensor at time t and position z.
        """
        h_plus, h_cross = self.metric_perturbation(t, z)
        
        # Initialize strain tensor
        h = np.zeros((4, 4))
        
        # Fill in spatial components (TT gauge)
        h[1,1] = h_plus
        h[1,2] = h_cross
        h[2,1] = h_cross
        h[2,2] = -h_plus
        
        return h

    def particle_displacement(self, x0, y0, t):
        """
        Calculate the displacement of a test particle initially at (x0, y0).
        """
        h_plus, h_cross = self.metric_perturbation(t)
        
        # Calculate displacements using linearized geodesic equation
        dx = 0.5 * (h_plus * x0 + h_cross * y0)
        dy = 0.5 * (h_cross * x0 - h_plus * y0)
        
        return x0 + dx, y0 + dy

class GravitationalWaveSimulation:
    """
    Class to handle the visualization and animation of gravitational waves.
    """
    def __init__(self, wave, num_particles=16):
        self.wave = wave
        
        # Create a grid of test particles
        x = np.linspace(-1, 1, int(np.sqrt(num_particles)))
        y = np.linspace(-1, 1, int(np.sqrt(num_particles)))
        self.X0, self.Y0 = np.meshgrid(x, y)
        
        # Initialize the plot
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.particles = self.ax.scatter([], [], c='blue', s=50)
        
        # Set plot properties
        self.ax.set_xlim(-1.5, 1.5)
        self.ax.set_ylim(-1.5, 1.5)
        self.ax.set_aspect('equal')
        self.ax.grid(True)
        self.ax.set_title('Gravitational Wave Effect on Test Particles')
        
    def update(self, frame):
        """Update function for animation."""
        t = frame / 50.0  # Convert frame number to time
        
        # Calculate new positions for all particles
        X = np.zeros_like(self.X0)
        Y = np.zeros_like(self.Y0)
        
        for i in range(self.X0.shape[0]):
            for j in range(self.X0.shape[1]):
                X[i,j], Y[i,j] = self.wave.particle_displacement(
                    self.X0[i,j], self.Y0[i,j], t
                )
        
        # Update particle positions
        self.particles.set_offsets(np.c_[X.ravel(), Y.ravel()])
        return self.particles,
    
    def animate(self, duration=10, fps=30):
        """
        Create animation of the gravitational wave effect.
        
        Parameters:
        - duration: Animation duration in seconds
        - fps: Frames per second
        """
        frames = duration * fps
        self.anim = FuncAnimation(
            self.fig, self.update, frames=frames,
            interval=1000/fps, blit=True
        )
        plt.show()

def plot_wave_polarizations():
    """
    Create plots showing both plus and cross polarizations.
    """
    t = np.linspace(0, 1, 1000)
    
    # Create waves with pure plus and pure cross polarizations
    wave_plus = GravitationalWave(amplitude_plus=1e-21, amplitude_cross=0)
    wave_cross = GravitationalWave(amplitude_plus=0, amplitude_cross=1e-21)
    
    # Calculate strain components
    h_plus, _ = wave_plus.metric_perturbation(t)
    _, h_cross = wave_cross.metric_perturbation(t)
    
    # Create the plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    ax1.plot(t, h_plus * 1e21)
    ax1.set_title('Plus (+) Polarization')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Strain (×10⁻²¹)')
    ax1.grid(True)
    
    ax2.plot(t, h_cross * 1e21)
    ax2.set_title('Cross (×) Polarization')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Strain (×10⁻²¹)')
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Create a gravitational wave with realistic LIGO-scale amplitude
    wave = GravitationalWave(
        amplitude_plus=1e-21,  # Typical GW amplitude from binary merger
        amplitude_cross=0.5e-21,
        frequency=100  # 100 Hz, typical for binary mergers
    )
    
    # Create simulation and run animation
    sim = GravitationalWaveSimulation(wave)
    
    # Plot polarization components
    plot_wave_polarizations()
    
    # Run animation
    sim.animate(duration=10, fps=30)
