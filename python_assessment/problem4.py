# Python program to print connected
# components in an undirected graph
class Graph:

    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFSUtil(self, temp, v, visited):

        # Mark the current vertex as visited
        visited[v] = True

        # Store the vertex to list
        temp.append(v)

        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:
                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp


    # method to add an undirected edge
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    # Method to retrieve connected components in an undirected graph
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc


if __name__ == "__main__":

    # Input list of connections
    input_list = [('Pradnya', 'Anisha'), ('Austin', 'Pradnya'), ('Austin', 'Melburne'), ('Vishal', 'Akash'), ('Rahul', 'Pavan')]
    # List to store all the unique employees
    employees = []
    # List to store the connections in the form of indices
    index_list = []

    # Gets all the unique employees and index_list by traversing through all the connections of the input list of connections
    for connection in input_list:
        employee1 = connection[0]
        employee2 = connection[1]
        # If the employee is already not present in the unique list, add it to the list
        if employee1 not in employees:
            employees.append(employee1)
        if employee2 not in employees:
            employees.append(employee2)
        # Add the tuple (u, v) where u is the index of the employee1 and v is the index of the employee2
        index_list.append((employees.index(employee1), employees.index(employee2)))

    n_employees = len(employees)

    print("Input employee connections are {}".format(input_list))
    print("Unique employees are {}".format(employees))
    print("Total employees are {}".format(n_employees))
    print("Input list in the form of indices instead of names {}".format(index_list))

    # Create a graph with unique employees
    g = Graph(n_employees)

    # Add all the connections to the graph
    for connection in index_list:
        g.addEdge(connection[0], connection[1])
    cc = g.connectedComponents()
    print("Following are connected components")
    print(cc)

    # named connected components
    # convert the above obtained connected components to named components using employee indices
    named_cc = []
    for connection in cc:
        temp = []
        for i in connection:
            temp.append(employees[i])
        named_cc.append(temp)

    print("Total number of employee groups are {}".format(len(named_cc)))
    print("Following are the employee groups")
    print(named_cc)

    def check_connection(employee_groups, employee1, employee2):
        """checks if two employees are connected or not
        Attributes:
            employee_groups: named connected components list
            employee1: name of employee1
            employee2: name of employee2
        Returns:
            boolean: True if there is a connection else False
        """
        for group in employee_groups:
            if employee1 in group and employee2 in group:
                return True
        return False

    employee1 = 'Pradnya'
    employee2 = 'Melburne'
    print("Employees {} and {} are connected - {}".format(employee1, employee2, check_connection(named_cc, employee1, employee2)))

    employee1 = 'Pavan'
    employee2 = 'Vishal'
    print("Employees {} and {} are connected - {}".format(employee1, employee2, check_connection(named_cc, employee1, employee2)))
