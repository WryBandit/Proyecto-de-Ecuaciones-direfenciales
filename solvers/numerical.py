import numpy as np
from scipy.integrate import solve_ivp

class NumericalSolver:
    """Clase para resolver EDOs numéricamente"""
    
    def __init__(self, n_points=1000):
        self.n_points = n_points
    
    def solve(self, model, method='RK45', t_max=10.0, t_min=0.0):
        """
        Resolver el modelo usando scipy.integrate.solve_ivp
        """
        t_span = (t_min, t_max)
        t_eval = np.linspace(t_min, t_max, self.n_points)
        y0 = model.get_initial_conditions()
        
        # Usar scipy para solución robusta
        solution = solve_ivp(
            model.equations, 
            t_span, 
            y0, 
            t_eval=t_eval, 
            method=method,
            rtol=1e-6
        )
        
        return self._format_results(solution.t, solution.y)
    
    def _format_results(self, t, y):
        """Formatear resultados en diccionario"""
        return {
            'time': t,
            'position': y[0],
            'velocity': y[1]
        }
