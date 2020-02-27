import sys
sys.path.append(r"/usr/lib/freecad/Ext")
sys.path.append(r"/usr/lib/freecad-python3/lib")

import FreeCAD
import ObjectsFem
from femmesh import gmshtools
from femtools import *
from femsolver.calculix import solver
from femtools.ccxtools import *
from FreeCAD import Part, Rotation, Mesh


class FEM:
    def __init__(self):
        self.doc = FreeCAD.newDocument()
        self.rock = False
        
        # create fem objects
    
    def add_rock_sphere(self, rock):
        self.rock = self.doc.addObject("Part::Sphere","Rock")
        self.rock.Radius = str(rock.get_radius()) + " mm"
        self.doc.recompute()
        
        self.add_material


class Analysis:
    def __init__(doc):
        self.object = ObjectsFem.makeAnalysis(doc, "Analysis")
        
        # Solver (use the well tested CcxTools solver object)
        self.setup_solver()
        self.object.addObject(self.solver_object)
    
    def setup_solver(self):
        self.solver_object = ObjectsFem.makeSolverCalculixCcxTools(doc, "CalculiX")
        self.solver_object.GeometricalNonlinearity = 'linear'
        self.solver_object.AnalysisType = thermal
        self.solver_object.ThermoMechSteadyState = False
        self.solver_object.MatrixSolverType = 'default'
        self.solver_object.IterationsControlParameterTimeUse = False
        

        