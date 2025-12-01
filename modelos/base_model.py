from abc import ABC, abstractmethod
import numpy as np

class BaseModel(ABC):
    """Clase abstracta base para todos los modelos de EDOs"""
    
    def __init__(self, name, initial_conditions):
        self.name = name
        self.initial_conditions = np.array(initial_conditions)
        self.parameters = {}
    
    @abstractmethod
    def equations(self, t, y):
        """
        Define el sistema de ecuaciones diferenciales
        Args:
            t: tiempo actual
            y: vector de estado actual
        Returns:
            dy/dt: derivadas del vector de estado
        """
        pass
    
    def analytical_solution(self, t):
        """
        Solución analítica (si está disponible)
        """
        raise NotImplementedError("Solución analítica no implementada")
    
    def get_initial_conditions(self):
        """Obtener condiciones iniciales"""
        return self.initial_conditions
