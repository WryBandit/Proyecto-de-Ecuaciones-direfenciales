import numpy as np
from .base_model import BaseModel

class ParachuteModel(BaseModel):
    """Modelo de caída con paracaídas considerando resistencia del aire"""
    
    def __init__(self, mass, area, drag_coef, gravity=9.81, 
                 initial_velocity=0.0, initial_position=0.0):
        # y = [posición, velocidad]
        initial_conditions = np.array([initial_position, initial_velocity])
        super().__init__("Modelo de Paracaídas", initial_conditions)
        
        self.mass = mass
        self.area = area
        self.drag_coef = drag_coef
        self.gravity = gravity
        self.air_density = 1.225  # kg/m³
        
        # Guardar parámetros
        self.parameters = {
            'Masa (kg)': mass,
            'Área paracaídas (m²)': area,
            'Coeficiente arrastre (Cd)': drag_coef,
            'Gravedad (m/s²)': gravity,
            'Densidad aire (kg/m³)': self.air_density,
            'Velocidad inicial (m/s)': initial_velocity,
            'Posición inicial (m)': initial_position
        }
    
    def equations(self, t, y):
        """
        Sistema de ecuaciones:
        dy0/dt = v (velocidad)
        dy1/dt = g - (Cd·A·ρ/(2m)) · v² (aceleración)
        """
        position, velocity = y
        
        # Fórmula de arrastre cuadrático (más realista para paracaídas)
        drag_force = 0.5 * self.drag_coef * self.area * self.air_density * velocity**2
        acceleration = self.gravity - (drag_force / self.mass)
        
        return np.array([velocity, acceleration])
    
    def analytical_solution(self, t):
        """Solución analítica aproximada para velocidad constante"""
        v_term = self.terminal_velocity()
        position = self.initial_conditions[0] - v_term * t
        velocity = np.full_like(t, v_term)
        
        return {
            'position': position,
            'velocity': velocity
        }
    
    def terminal_velocity(self):
        """Calcular velocidad terminal teórica"""
        return np.sqrt((2 * self.mass * self.gravity) / 
                      (self.drag_coef * self.area * self.air_density))
    
    def print_parameters(self):
        """Imprimir parámetros del modelo"""
        print("PARÁMETROS DEL MODELO:")
        for param, value in self.parameters.items():
            print(f"  {param}: {value}")
        print(f"  Velocidad terminal: {self.terminal_velocity():.3f} m/s")
