#!/usr/bin/env python3
"""
Sistema de Modelado de Caída con Paracaídas
Proyecto de Ecuaciones Diferenciales - Soldadito con Paracaídas
"""

import argparse
import numpy as np
from modelos.parachute_model import ParachuteModel
from solvers.numerical import NumericalSolver
from utils.plotter import ResultPlotter
from experiments.parachute_experiment import ParachuteExperiment

def main():
    parser = argparse.ArgumentParser(description='Modelado de caída con paracaídas')
    parser.add_argument('--mode', type=str, default='simulate',
                       choices=['simulate', 'experiment', 'compare'],
                       help='Modo de operación')
    parser.add_argument('--plot', action='store_true', help='Generar gráficas')
    parser.add_argument('--save', action='store_true', help='Guardar resultados')
    
    args = parser.parse_args()
    
    # Crear modelo con datos reales del soldadito
    model = create_parachute_model()
    
    if args.mode == 'simulate':
        run_simulation(model, args)
    elif args.mode == 'experiment':
        run_experiment_analysis(model, args)
    elif args.mode == 'compare':
        run_comparison(model, args)

def create_parachute_model():
    """Crear modelo con datos reales del soldadito"""
    return ParachuteModel(
        mass=0.0073,        # 7.3 gramos
        area=0.9621,        # Área del paracaídas en m²
        drag_coef=0.0635,   # Coeficiente ajustado experimentalmente
        gravity=9.81,
        initial_velocity=0.0,
        initial_position=13.5  # Altura promedio del experimento
    )

def run_simulation(model, args):
    """Ejecutar simulación del modelo"""
    print("="*60)
    print("SIMULACIÓN DE CAÍDA CON PARACAÍDAS")
    print("="*60)
    
    # Mostrar parámetros del modelo
    model.print_parameters()
    
    # Resolver el modelo
    solver = NumericalSolver()
    results = solver.solve(model, t_max=15.0)
    
    # Mostrar resultados
    print("\nRESULTADOS DE LA SIMULACIÓN:")
    print(f"Velocidad terminal teórica: {model.terminal_velocity():.3f} m/s")
    print(f"Tiempo de caída simulado desde {model.initial_conditions[0]}m: {results['time'][-1]:.3f} s")
    
    if args.plot:
        plotter = ResultPlotter()
        plotter.plot_comprehensive(results, model)
    
    if args.save:
        save_results(results, 'simulation_results.csv')

def run_experiment_analysis(model, args):
    """Analizar datos experimentales"""
    print("="*60)
    print("ANÁLISIS DE DATOS EXPERIMENTALES")
    print("="*60)
    
    experiment = ParachuteExperiment()
    experiment.analyze_experimental_data(model)
    
    if args.plot:
        experiment.plot_experimental_comparison()

def run_comparison(model, args):
    """Comparar diferentes configuraciones"""
    print("="*60)
    print("COMPARACIÓN DE CONFIGURACIONES")
    print("="*60)
    
    # Modelo con Cd teórico
    model_theoretical = ParachuteModel(
        mass=0.0073, area=0.9621, drag_coef=1.3,
        gravity=9.81, initial_velocity=0.0, initial_position=13.5
    )
    
    # Modelo con Cd experimental
    model_experimental = model
    
    solver = NumericalSolver()
    results_theoretical = solver.solve(model_theoretical, t_max=15.0)
    results_experimental = solver.solve(model_experimental, t_max=15.0)
    
    if args.plot:
        plotter = ResultPlotter()
        plotter.plot_comparison(
            [results_theoretical, results_experimental],
            [model_theoretical, model_experimental],
            ['Teórico (Cd=1.3)', 'Experimental (Cd=0.0635)']
        )

def save_results(results, filename):
    """Guardar resultados en archivo CSV"""
    import pandas as pd
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    print(f"Resultados guardados en {filename}")

if __name__ == "__main__":
    main()
