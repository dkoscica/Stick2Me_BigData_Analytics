# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 22:14:07 2017

@author: Dominik
"""

import networkx as net
import networkx as nx
from operator import itemgetter

class SNAWrapper:
    
    graph = net.Graph()        
    
    def __init__(self, vertexes):
        self.graph = self.create_graph(vertexes)

    def create_graph(self, vertexes):
        
        graph = net.Graph()
        
        for vertexPair in vertexes:
            
            vertex1 = vertexPair["vertex1"]
            vertex2 = vertexPair["vertex2"]

            print("Vertex1:" + str(vertex1))
            print("Vertex2:" + str(vertex2))
            print()
            
            graph.add_edge(vertex1, vertex2)

        return graph
    
    """
    Calculate methods
    """
    def calculate_degree(self):
        dc = nx.degree_centrality(self.graph)
        return sorted(dc.items(), key=itemgetter(1), reverse=True)
    
    def calculate_betweenness(self):
        bc= nx.betweenness_centrality(self.graph)
        return sorted(bc.items(), key=itemgetter(1), reverse=True)
        
    def calculate_closeness(self):
        cc= nx.closeness_centrality(self.graph)
        return sorted(cc.items(), key=itemgetter(1), reverse=True)
    
    def calculate_eigenvector(self):
        ev = nx.eigenvector_centrality(self.graph)
        return sorted(ev.items(), key=itemgetter(1), reverse=True)
    
    """
    Print methods
    """
    def print_basic_graph_info(self):
        print ("Info:")
        print (nx.info(self.graph))
        print ("\nDegree histogram: " + str(nx.degree_histogram(self.graph)))
        print ("Density: " + str(nx.density(self.graph)))
        
    def print_additional_info(self):
         self.print_degree()
         self.print_betweenness()
         self.print_closeness()
         self.print_eigenvector()
        
    def print_degree(self):
        print ("\nSorted degree:")
        degree = self.calculate_degree()
        print (degree[0:5])
        
    def print_betweenness(self):
        print ("\nSorted betweenness:")
        betweenness = self.calculate_betweenness()
        print (betweenness[0:5]) 
        
    def print_closeness(self):
        print ("\nSorted closeness:")
        closeness = self.calculate_closeness()
        print (closeness[0:5])
        
    def print_eigenvector(self):
        print ("\nSorted eigenvector:")
        eigenvector = self.calculate_eigenvector()
        print (eigenvector[0:5])
        
    """
    Draw methods
    """
    def draw_graph(self):
        nx.draw(self.graph)