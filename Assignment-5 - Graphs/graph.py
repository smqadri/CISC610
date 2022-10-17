class Graph:
        def __init__(self):                     # Constructor
                self.graph = dict()   
                self.person = {}                
                self.personId = {}              

        def insert(self, person):                       # Insert a person
                self.person[person.name] = person
                self.personId[person.id] = person
                self.graph[person.id] = {}

        def getPerson(self, name):                      # Get a person's details
                person = self.person[name]
                pid = person.id
                print ("\nName: ", person.name)
                print ("ID: ", person.id)
                print ("Gender: ", person.gender)
                print ("Age: ", person.age)
                print ("\nRelations: ")
                for relation in self.graph[pid].keys():
                        if len(self.graph[pid][relation]) > 0:
                                print (relation, ": ", [self.personId[i].name for i in self.graph[pid][relation]])
                print ('\n') 

        def remove(self, name):                         # Remove a person
                pid = self.person[name].id
                self.personId.pop(pid)
                self.person.pop(name)
                self.graph.pop(pid)

                for _, relations in self.graph.items():                 # Remove the person from all relations
                        for relation in relations.keys():
                                if pid in relations[relation]:
                                        relations[relation].remove(pid)

        def edit(self, name, new_name, new_gender, new_age):            # Edit a person
                person = self.person[name]                              # Get the person
                person.name = new_name                                  # Edit the name
                person.gender = new_gender                              # Edit the gender
                person.age = new_age                                    # Edit the age

                self.person.pop(name)                                   # Remove the person from the dictionary
                self.person[new_name] = person                          # Add the updated person to the dictionary

        def addRelation(self, name1, name2, relation):                  # Add a relation
                pid1 = self.person[name1].id                             # Get the id of the first person
                pid2 = self.person[name2].id                             # Get the id of the second person

                if relation in {'Sibling', 'Spouse', 'Divorced'}:               # Add relation to both persons
                        if relation == 'Spouse':                                # If the relation is spouse
                                if relation in self.graph[pid1]:                 # If the relation already exists, add the other spouse to the relation
                                        assert len(self.graph[pid1][relation]) == 0
                                if relation in self.graph[pid2]:                 # If the relation already exists, add the other spouse to the relation
                                        assert len(self.graph[pid2][relation]) == 0

                        if relation not in self.graph[pid1]:             # Add relation to person1
                                self.graph[pid1][relation] = set ()
                        self.graph[pid1][relation].add(pid2)              # Add person2 to the relation
                        if relation not in self.graph[pid2]:             # Add relation to person2
                                self.graph[pid2][relation] = set ()             
                        self.graph[pid2][relation].add(pid1)              # Add person1 to the relation

                        if relation == 'Sibling':                               # If the relation is sibling
                                for i in self.graph[pid1][relation]:                             # Add relation to all siblings
                                        if i not in self.graph[pid2][relation] and i !=pid2:   
                                                self.graph[pid2][relation].add(i)                # Add person1 to the relation
                                for i in self.graph[pid2][relation]:                             # Add relation to all siblings
                                        if i not in self.graph[pid1][relation] and i !=pid1:      
                                                self.graph[pid1][relation].add(i)                # Add person2 to the relation

                if relation == 'Child':                                 # Add Parent/Child relationships
                        if 'Child' not in self.graph[pid1]:              # Add Child to person1
                                self.graph[pid1]['Child'] = set ()       
                        self.graph[pid1]['Child'].add(pid2)               # Add person2 to the Child relation
                        if 'Parent' not in self.graph[pid2]:             # Add Parent to person2
                                self.graph[pid2]['Parent'] = set ()      
                        self.graph[pid2]['Parent'].add(pid1)              # Add person1 to the Parent relation

                if relation == 'Parent':                                # Add Child relationships
                        self.addRelation(name2, name1, 'Child')

                if relation == 'Adopted':                               # Add Parent/Adopted relationships
                        if 'Adopted' not in self.graph[pid1]:            # Add Adopted to person1
                                self.graph[pid1]['Adopted'] = set ()     # Add person2 to the Adopted relation
                        self.graph[pid1]['Adopted'].add(pid2)
                        if 'Parent' not in self.graph[pid2]:             # Add Parent to person2
                                self.graph[pid2]['Parent'] = set ()      # Add person1 to the Parent relation
                        self.graph[pid2]['Parent'].add(pid1)             
        
        def print(self):                                                # Print the graph
        
                for pid, relations in self.graph.items():               # Print all relations
                        print ('\n')
                        for relation in relations.keys():               # Print all persons in the relation
                                if relations[relation] != None and len(relations[relation]) > 0:                        # If the relation is not empty
                                        current_name = self.personId[pid].name                                          # Get the name of the current person
                                        current_relative = ([self.personId[i].name for i in relations[relation]])       # Get the names of the persons in the relation
                                        print (current_name, " is ", relation, " of ", current_relative)                # Print the relationships
                print ('\n')                       
                                                





"""
graph = dict() 
graph['A'] = ['B', 'C'] 
graph['B'] = ['E','C', 'A'] 
graph['C'] = ['A', 'B', 'E','F'] 
graph['E'] = ['B', 'C'] 
graph['F'] = ['C']

matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)  

adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)] 

edges_list = [] 


for key in matrix_elements: 
    for neighbor in graph[key]: 
       edges_list.append((key,neighbor)) 


print(edges_list)



for edge in edges_list: 
        index_of_first_vertex = matrix_elements.index(edge[0]) 
        index_of_second_vertex = matrix_elements.index(edge[1]) 
        adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1 


println(adjacency_matrix)
"""