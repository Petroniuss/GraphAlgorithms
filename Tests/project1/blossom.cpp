#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <climits>
#include <stdio.h>
#include <string.h>

using namespace std;

struct GraphEdge {
    int u;
    int v;
} typedef GraphEdge;

struct Graph {
    int V;
    vector<int>* adj;
} typedef Graph;

void printGraph(Graph* G) {
    for (int u = 0; u < G -> V; u++) {
        for (auto v : G -> adj[u]) {
            cout << u << " " << v << endl;
        }
    }
}

void addEdge(Graph* G, int u, int v) {
    G -> adj[u].push_back(v);
    G -> adj[v].push_back(u);
}

Graph* createGraph(int V) {
    Graph* G = new Graph;
    
    G -> V = V;
    G -> adj = new vector<int>[V];
}

