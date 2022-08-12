# importing libraries

import pandas as pd
import networkx as nx
import numpy as np
import math

#%% Reading the csv file
df=pd.read_csv('pdc-world-championship-20221994.csv',sep=";")

print(df.head())

#%% Detect missing values for an array-like object and 1 / ‘columns’ : reduce the columns, return a Series whose index is the original index.

print(sum(df.isna().any(1)))

# Checking duplicate values in dataframe
print(sum(df.duplicated()))

#%% Code for splitting networks
a = df.loc[ (1994 <= df['tournament_year']) & (df['tournament_year'] <= 2022)]
print(a)

a.to_csv(r'D:\...s\1994-2022.csv', index=False)

#%% Selecting specific year and drawing network

# 1994 - 2000
print("1994 - 2000")
a = a = df.loc[ (1994 <= df['tournament_year']) & (df['tournament_year'] <= 2000)]


Graphtype = nx.DiGraph()
G = nx.from_pandas_edgelist(a,source='player_1name',target='player_2name',create_using=Graphtype)
pos=nx.spring_layout(G)
nx.draw(G,pos,node_color='#87ceeb',edge_color='#fc0362', with_labels=True)
print(nx.info(G))
#%% Selecting specific year and drawing network
# 2000 - 2006
print("2000 - 2006")
a = a = df.loc[ (2000 <= df['tournament_year']) & (df['tournament_year'] <= 2006)]


Graphtype = nx.DiGraph()
G = nx.from_pandas_edgelist(a,source='player_1name',target='player_2name',create_using=Graphtype)
pos=nx.spring_layout(G)
nx.draw(G,pos,node_color='#87ceeb',edge_color='#fc0362', with_labels=True)
print(nx.info(G))

#%% Selecting specific year and drawing network
# 2006 - 2012
print("2006 - 2012")
a = a = df.loc[ (2006 <= df['tournament_year']) & (df['tournament_year'] <= 2012)]


Graphtype = nx.DiGraph()
G = nx.from_pandas_edgelist(a,source='player_1name',target='player_2name',create_using=Graphtype)
pos=nx.spring_layout(G)
nx.draw(G,pos,node_color='#87ceeb',edge_color='#fc0362', with_labels=True)
print(nx.info(G))

#%% Selecting specific year and drawing network
# 2012 - 2018
print("2012 - 2018")
a = a = df.loc[ (2012 <= df['tournament_year']) & (df['tournament_year'] <= 2018)]


Graphtype = nx.DiGraph()
G = nx.from_pandas_edgelist(a,source='player_1name',target='player_2name',create_using=Graphtype)
pos=nx.spring_layout(G)
nx.draw(G,pos,node_color='#87ceeb',edge_color='#fc0362', with_labels=True)
print(nx.info(G))

#%% Selecting specific year and drawing network
# 1994 - 2022
print("1994 - 2022")
a = df


Graphtype = nx.DiGraph()
G = nx.from_pandas_edgelist(a,source='player_1name',target='player_2name',create_using=Graphtype)
pos=nx.spring_layout(G)
nx.draw(G,pos,node_color='#87ceeb',edge_color='#fc0362', with_labels=True)
print(nx.info(G))

#%% Indexing
liste = []

# Taking unique values of player_1name column into a list
for i in range(len(df['player_1name'].unique())):
    liste.append(df['player_1name'].unique()[i])

# Taking unique values of player_2name column into a list
for i in range(len(df['player_2name'].unique())):    
    liste.append(df['player_2name'].unique()[i])

# Removing duplicate values in list
res = []
for i in liste:
    if i not in res:
        res.append(i)

# List elements to indexes
indexer = []
for i in range(len(res)):
    indexer.append(i)

#print(indexer)

# Replacing old values with indexing list in dataframe
df['player_1name'] = df['player_1name'].replace(res,indexer)
df['player_2name'] = df['player_2name'].replace(res,indexer)


#%% Neighbor Matrix = nei

# Converting column values to list
player1 = df['player_1name'].to_list()
player2 = df['player_2name'].to_list()

# Creating a numpy array that represents neighbor matrix with 0 values
nei = np.zeros((len(res),len(res)))

for i in range(len(player1)):
    if player1[i] != player2[i]:
        m = player1[i]
        #print("m",m)
        n = player2[i]
        #print("n",n)
        nei[m][n] = 1


for i in range(len(player1)):
    if player1[i] != player2[i]:
        m = player2[i]
        #print("m",m)
        n = player1[i]
        #print("n",n)
        nei[m][n] = 1


#%% Adamic Adar Index
Graphtype = nx.complete_graph(len(df))
G1 = nx.from_pandas_edgelist(df, source = 'player_1name', target = 'player_2name', create_using=Graphtype)

# Calculating adamic adar scores onto graph with networkX
adamic_adar_scores = nx.adamic_adar_index(G1, ebunch=None)

# Function of conversion adar adamix scores to matrix 
def adar_adamic_matrix(graph,adj_mat):    
    Adar_Adamic = np.zeros((len(adj_mat),len(adj_mat)))
    #print(Adar_Adamic)
    for u, v, p in adamic_adar_scores:
        #print(u)
        Adar_Adamic[u][v] = p
        #print(f"({u}, {v}) -> {p:.8f}")
        
    return Adar_Adamic
                
adamic_adar_matrix_ = adar_adamic_matrix(adamic_adar_scores,nei)
print("Matrix of adamic adar index scores", adamic_adar_matrix_)



#%% Jaccard Index

Graphtype = nx.complete_graph(len(df))
G1 = nx.from_pandas_edgelist(df, source = 'player_1name', target = 'player_2name', create_using=Graphtype)

# Calculating jaccard scores onto graph with networkX
jaccard_scores = nx.jaccard_coefficient(G1, ebunch=None)

# Function of conversion jaccard scores to matrix 
def jaccard_matrix(graph,adj_mat):    
    Jaccard = np.zeros((len(adj_mat),len(adj_mat)))
    #print(Jaccard)
    for u, v, p in jaccard_scores:
        #print(u)
        Jaccard[u][v] = p
        #print(f"({u}, {v}) -> {p:.8f}")
        
    return Jaccard


jaccard_matrix_ = jaccard_matrix(jaccard_scores,nei)
print("Matrix of jaccard index scores", jaccard_matrix_)



#%% Resource Allocation

Graphtype = nx.complete_graph(len(df))
G1 = nx.from_pandas_edgelist(df, source = 'player_1name', target = 'player_2name', create_using=Graphtype)

# Calculating resource allocation scores onto graph with networkX
resource_allocation_scores = nx.resource_allocation_index(G1, ebunch=None)

# Function of conversion resource allocation scores to matrix 
def resource_allocation_matrix(graph,adj_mat):    
    Resource_allocation = np.zeros((len(adj_mat),len(adj_mat)))
    #print(Jaccard)
    for u, v, p in resource_allocation_scores:
        #print(u)
        Resource_allocation[u][v] = p
        #print(f"({u}, {v}) -> {p:.8f}")
        
    return Resource_allocation


resource_allocation_matrix_ = resource_allocation_matrix(resource_allocation_scores,nei)
print("Matrix of resource allocation index scores", resource_allocation_matrix_)


#%% Preferential Attachment

Graphtype = nx.complete_graph(len(df))
G1 = nx.from_pandas_edgelist(df, source = 'player_1name', target = 'player_2name', create_using=Graphtype)

# Calculating preferential attachment scores onto graph with networkX
preferential_attachment_scores = nx.preferential_attachment(G1, ebunch=None)

# Function of conversion preferential attachment scores to matrix 
def preferential_attachment_matrix(graph,adj_mat):    
    Preferential_attachment = np.zeros((len(adj_mat),len(adj_mat)))
    #print(Jaccard)
    for u, v, p in preferential_attachment_scores:
        #print(u)
        Preferential_attachment[u][v] = p
        #print(f"({u}, {v}) -> {p:.8f}")
        
    return Preferential_attachment


preferential_attachment_matrix_ = preferential_attachment_matrix(preferential_attachment_scores,nei)
print("Matrix of preferential attachment index scores", preferential_attachment_matrix_)


#%% Common Neighbor Index

def common_neighbors(G, u, v):
    
    if u not in G:
        raise nx.NetworkXError("u is not in the graph.")
    if v not in G:
        raise nx.NetworkXError("v is not in the graph.")

    # Return a generator explicitly instead of yielding so that the above
    # checks are executed eagerly.
    return (w for w in G[u] if w in G[v] and w not in (u, v))



def _apply_prediction(G, func, ebunch=None):
    
    if ebunch is None:
        ebunch = nx.non_edges(G)
    return ((u, v, func(u, v)) for u, v in ebunch)

def common_neighbor_centrality(G, ebunch=None, alpha=0.8):
    
    shortest_path = nx.shortest_path(G)

    def predict(u, v):
        #if u != 0 and v != 184 and v != 370 and v != 185 and v != 186 and v != 187:
        return alpha * len(list(common_neighbors(G, u, v))) + (1 - alpha) * (
            G.number_of_nodes() / (len(shortest_path[u][v]) - 1)
            )

    return _apply_prediction(G, predict, ebunch)


Graphtype = nx.complete_graph(len(df))
G1 = nx.from_pandas_edgelist(df, source = 'player_1name', target = 'player_2name', create_using=Graphtype)

# Calculating common neighbor scores onto graph with networkX
common_neighbor_scores = common_neighbor_centrality(G1, ebunch=None)

#Function of conversion common neighbor scores to matrix 
def common_neighbor_matrix(graph,adj_mat):    
    Common_neighbor = np.zeros((len(adj_mat),len(adj_mat)))
    #print(Jaccard)
    for u, v, p in common_neighbor_scores:
        #print(u)
        Common_neighbor[u][v] = p
        print(u)
        print(v)
        print(p)
        
    return Common_neighbor

common_neighbor_matrix_ = common_neighbor_matrix(common_neighbor_scores,nei)
print("Matrix of common neighbor index scores", common_neighbor_matrix_)



#%%

Graphtype = nx.DiGraph()
G = nx.from_pandas_edgelist(df,source='player_1name',target='player_2name',create_using=Graphtype)
pos=nx.spring_layout(G)
nx.draw(G,pos,node_color='#87ceeb',edge_color='#fc0362', with_labels=False)
print(nx.info(G))


#%%

import matplotlib.pyplot as plt
list_degree=list(G.degree()) #this will return a list of tuples each tuple is(node,deg)
nodes , degree = map(list, zip(*list_degree)) #build a node list and corresponding degree list
plt.figure(figsize=(10,10))
nx.draw(G, nodelist=nodes, node_size=[(v * 5)+1 for v in degree])
plt.show() #ploting the graph
