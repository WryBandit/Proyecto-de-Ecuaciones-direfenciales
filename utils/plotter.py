import matplotlib.pyplot as plt
import numpy as np

class ResultPlotter:
    """Clase para visualizar resultados de simulaciones"""
    
    def __init__(self):
        plt.style.use('default')
        self.fig_size = (12, 10)
    
    def plot_comprehensive(self, results, model):
        """Graficar resultados completos de la simulación"""
        time = results['time']
        position = results['position']
        velocity = results['velocity']
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=self.fig_size)
        
        # Gráfica 1: Posición vs Tiempo
        ax1.plot(time, position, 'b-', linewidth=2, label='Simulación')
        ax1.set_xlabel('Tiempo (s)')
        ax1.set_ylabel('Altura (m)')
        ax1.set_title('Posición vs Tiempo')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # Gráfica 2: Velocidad vs Tiempo
        ax2.plot(time, velocity, 'r-', linewidth=2, label='Simulación')
        v_term = model.terminal_velocity()
        ax2.axhline(y=v_term, color='g', linestyle='--', 
                   label=f'Velocidad terminal ({v_term:.2f} m/s)')
        ax2.set_xlabel('Tiempo (s)')
        ax2.set_ylabel('Velocidad (m/s)')
        ax2.set_title('Velocidad vs Tiempo')
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        
        # Gráfica 3: Velocidad vs Posición
        ax3.plot(position, velocity, 'purple', linewidth=2)
        ax3.set_xlabel('Altura (m)')
        ax3.set_ylabel('Velocidad (m/s)')
        ax3.set_title('Diagrama de Fase: Velocidad vs Posición')
        ax3.grid(True, alpha=0.3)
        
        # Gráfica 4: Aceleración vs Tiempo
        acceleration = np.gradient(velocity, time)
        ax4.plot(time, acceleration, 'orange', linewidth=2)
        ax4.set_xlabel('Tiempo (s)')
        ax4.set_ylabel('Aceleración (m/s²)')
        ax4.set_title('Aceleración vs Tiempo')
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('parachute_simulation.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def plot_comparison(self, results_list, models, labels):
        """Comparar múltiples simulaciones"""
        plt.figure(figsize=(12, 8))
        
        # Gráfica de velocidad comparativa
        for i, (results, label) in enumerate(zip(results_list, labels)):
            plt.plot(results['time'], results['velocity'], 
                    linewidth=2, label=label)
        
        # Datos experimentales
        experimental_time = 7.979  # s
        experimental_velocity = 13.5 / experimental_time  # m/s
        plt.axhline(y=experimental_velocity, color='k', linestyle=':', 
                   linewidth=2, label=f'Experimental ({experimental_velocity:.2f} m/s)')
        
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Velocidad (m/s)')
        plt.title('Comparación: Velocidad vs Tiempo')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig('comparison.png', dpi=300, bbox_inches='tight')
        plt.show()
