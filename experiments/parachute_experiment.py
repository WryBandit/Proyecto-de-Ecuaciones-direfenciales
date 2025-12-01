import numpy as np
import matplotlib.pyplot as plt

class ParachuteExperiment:
    """Clase para analizar datos experimentales"""
    
    def __init__(self):
        self.experimental_data = {
            'mass': 0.0073,           # kg
            'area': 0.9621,           # m²
            'drop_height': 13.5,      # m
            'fall_time': 7.979,       # s
            'measured_velocity': 13.5 / 7.979  # m/s
        }
    
    def analyze_experimental_data(self, model):
        """Analizar y comparar datos experimentales con el modelo"""
        print("DATOS EXPERIMENTALES:")
        print(f"  Masa: {self.experimental_data['mass']*1000:.1f} g")
        print(f"  Área del paracaídas: {self.experimental_data['area']:.4f} m²")
        print(f"  Altura de caída: {self.experimental_data['drop_height']:.1f} m")
        print(f"  Tiempo de caída: {self.experimental_data['fall_time']:.3f} s")
        print(f"  Velocidad promedio medida: {self.experimental_data['measured_velocity']:.3f} m/s")
        
        # Calcular coeficiente de arrastre experimental
        v_exp = self.experimental_data['measured_velocity']
        Cd_exp = self.calculate_experimental_Cd(v_exp)
        print(f"  Coeficiente de arrastre experimental: {Cd_exp:.4f}")
        
        # Comparar con modelo
        v_model = model.terminal_velocity()
        error = abs(v_exp - v_model) / v_exp * 100
        print(f"\nCOMPARACIÓN CON MODELO:")
        print(f"  Velocidad modelo: {v_model:.3f} m/s")
        print(f"  Velocidad experimental: {v_exp:.3f} m/s")
        print(f"  Error: {error:.1f}%")
    
    def calculate_experimental_Cd(self, measured_velocity):
        """Calcular Cd a partir de datos experimentales"""
        m = self.experimental_data['mass']
        A = self.experimental_data['area']
        g = 9.81
        rho = 1.225
        
        return (2 * m * g) / (A * rho * measured_velocity**2)
    
    def plot_experimental_comparison(self):
        """Graficar comparación entre teoría y experimento"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Gráfica 1: Comparación de velocidades
        models = ['Teórico (Cd=1.3)', 'Experimental (Cd=0.0635)']
        velocities = [1.69, self.experimental_data['measured_velocity']]  # Valores aproximados
        
        bars = ax1.bar(models, velocities, color=['lightblue', 'lightcoral'])
        ax1.set_ylabel('Velocidad (m/s)')
        ax1.set_title('Comparación de Velocidades Terminales')
        
        # Añadir valores en las barras
        for bar, velocity in zip(bars, velocities):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
                    f'{velocity:.2f} m/s', ha='center', va='bottom')
        
        # Gráfica 2: Tiempos de caída
        times_theoretical = 13.5 / 1.69  # Para Cd=1.3
        times_experimental = self.experimental_data['fall_time']
        
        ax2.bar(['Teórico', 'Experimental'], 
                [times_theoretical, times_experimental],
                color=['lightgreen', 'lightyellow'])
        ax2.set_ylabel('Tiempo (s)')
        ax2.set_title('Tiempo de Caída desde 13.5m')
        
        plt.tight_layout()
        plt.savefig('experimental_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()
