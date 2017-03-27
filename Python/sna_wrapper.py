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
    collection_name = ""       
    
    def __init__(self, collection_name, vertexes):
        self.collection_name = collection_name
        self.graph = self.create_graph(vertexes)

    def create_graph(self, vertexes):
        
        graph = net.Graph()
        
        for vertexPair in vertexes:
            
            vertex1 = vertexPair["vertex1"]
            vertex2 = vertexPair["vertex2"]

            print("Vertex1:" + str(vertex1))
            print("Vertex2:" + str(vertex2))
            print()
            
            if vertex1 is not None and vertex2 is not None:
                graph.add_edge(vertex1, vertex2)

        return graph
    
    def create_sna_analysis(self):
        self.print_basic_graph_info()
        self.print_additional_info()
        self.draw_graph()
        
    def create_sna_analysis_html(self):
        
        formated_date = self.collection_name.strip("db.tweets.From_").replace("_To_", " - ").replace("_", ".")
        image_name = "sna_" + self.collection_name.strip("db.tweets.From_") + ".png"
        
        print("<h3>SNA " + formated_date + "</h3><br>")
        
        self.print_basic_html_graph_info()
        self.print_additional_html_info()
        
        print("<br>")
        print('<img src="Images/' + image_name + '">')
        
        self.draw_graph()
    
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
        try:
            ev = nx.eigenvector_centrality(self.graph)
            return sorted(ev.items(), key=itemgetter(1), reverse=True)
        except:
            return []
        
    def calculate_average_degree(self):
        average_degree = ""
        nnodes = self.graph.number_of_nodes()
        if len(self.graph) > 0:
            if self.graph.is_directed():
                average_degree+="%8.4f\n"%\
                    (sum(self.graph.in_degree().values())/float(nnodes))
                average_degree+="%8.4f"%\
                    (sum(self.graph.out_degree().values())/float(nnodes))
            else:
                s=sum(self.graph.degree().values())
                average_degree+="%8.4f"%\
                    (float(s)/float(nnodes))
        return average_degree
    
    """
    Print methods
    """
    def print_basic_graph_info(self):
        print ("Info:")
        print (nx.info(self.graph))
        print ("\nDegree histogram: " + str(nx.degree_histogram(self.graph)))
        print ("Density: " + str(nx.density(self.graph)))
        
    def print_basic_html_graph_info(self):
        print("<b>Number of nodes: </b>" + str(self.graph.number_of_nodes())) 
        print("<br>")
        print("<b>Number of edges: </b>" + str(self.graph.number_of_edges()))
        print("<br>")
        print("<b>Average degree: </b>" + str(self.calculate_average_degree()))
        print("<br>")
        print("<b>Degree histogram: </b>" + str(nx.degree_histogram(self.graph)))
        print("<br>")
        print("<b>Density: </b> " + str(nx.density(self.graph)))
        
    def print_additional_info(self):
         self.print_degree()
         self.print_betweenness()
         self.print_closeness()
         self.print_eigenvector()
         
    def print_additional_html_info(self):
         print("<br><br>")
         self.print_degree_html()
         print("<br><br>")
         self.print_betweenness_html()
         print("<br><br>")
         self.print_closeness_html()
         print("<br><br>")
         self.print_eigenvector_html()
        
    def print_degree(self):
        print ("\nSorted degree:")
        degree = self.calculate_degree()
        print (degree[0:5])
        
    def print_degree_html(self):
        print ("<b>Sorted degree</b>")
        degree = self.calculate_degree()
        for key, value in degree[0:5]:
            print("<br>")
            print(key + ", " + str(value))
        
    def print_betweenness(self):
        print ("\nSorted betweenness:")
        betweenness = self.calculate_betweenness()
        print (betweenness[0:5]) 
        
    def print_betweenness_html(self):
        print ("<b>Sorted betweenness</b>")
        betweenness = self.calculate_betweenness()
        for key, value in betweenness[0:5]:
            print("<br>")
            print(key + ", " + str(value))
        
    def print_closeness(self):
        print ("\nSorted closeness:")
        closeness = self.calculate_closeness()
        print (closeness[0:5])
        
    def print_closeness_html(self):
        print ("<b>Sorted closeness</b>")
        closeness = self.calculate_closeness()
        for key, value in closeness[0:5]:
            print("<br>")
            print(key + ", " + str(value))
        
    def print_eigenvector(self):
        print ("\nSorted eigenvector:")
        eigenvector = self.calculate_eigenvector()
        print (eigenvector[0:5])
        
    def print_eigenvector_html(self):
        print ("<b>Sorted eigenvector</b>")
        eigenvector = self.calculate_eigenvector()
        for key, value in eigenvector[0:5]:
            print("<br>")
            print(key + ", " + str(value))
        
    """
    Draw methods
    """
    def draw_graph(self):
        nx.draw(self.graph)