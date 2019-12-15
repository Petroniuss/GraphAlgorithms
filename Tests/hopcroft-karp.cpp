#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <climits>

using namespace std;


// for some reason macros don't work :/
#define NIL 0
#define INF INT_MAX 

// -------- GRAPH REPRESENTATION --------
// ------- UNWEIGHTED UNDIRECTED -------

// struct GraphEdge {
//     int u;
//     int v;
// } typedef GraphEdge;

// struct Graph {
//     int V;
//     vector<int>* adj;
// } typedef Graph;

// void printGraph(Graph* G) {
//     for (int u = 0; u < G -> V; u++) {
//         for (auto v : G -> adj[u]) {
//             cout << u << " " << v << endl;
//         }
//     }
// }

// void addEdge(Graph* G, int u, int v) {
//     G -> adj[u].push_back(v);
//     G -> adj[v].push_back(u);
// }

// Graph* createGraph(int V) {
//     Graph* G = new Graph;
    
//     G -> V = V;
//     G -> adj = new vector<int>[V];
// }

// -------- BIPARTITE GRAPH -------- 

struct BiGraph {
    int M, N; // M for left and N for right sides of Bipartite Graph.
    vector<int>* adj; // adj list only for left vertices.
    int* pairU;
    int* pairV;
    int* dist;
} typedef BiGraph;

void addEdge(BiGraph* G, int u, int v) {
    G -> adj[u].push_back(v);
}

BiGraph* createBiGraph(int M, int N) {
    BiGraph* G = new BiGraph;
    
    G -> M = M;
    G -> N = N;
    G -> adj = new vector<int>[M + 1];

    return G;
}

bool dfs(BiGraph* G, int u) {
    if (u != NIL) {
        for(auto v : G -> adj[u]) {
            if (G -> dist[G -> pairV[v]] == G -> dist[u] + 1) {
                if (dfs(G, G -> pairV[v]) == true) {
                    G -> pairV[v] = u;
                    G -> pairU[u] = v;

                    return true;
                }
            }
        }
        G -> dist[u] = INF;
        
        return false;
    }

    return true;
}

bool bfs(BiGraph* G) {
    queue<int> Q;

    for (int u = 1; u <= G -> M; u++) {
        if (G -> pairU[u] == NIL){ 
            G -> dist[u] = 0; 
            Q.push(u);
        } else {
            G -> dist[u] = INF;
        }
    }
    
    G -> dist[NIL] = INF;

    while (!Q.empty()) {
        int u = Q.front();
        Q.pop();

        if (G -> dist[u] < G -> dist[NIL]) {
            for(auto v : G -> adj[u]) {
                if (G -> dist[G -> pairV[v]] == INF) {
                    G -> dist[G -> pairV[v]] = G -> dist[u] + 1;
                    Q.push(G -> pairV[v]);
                }
            }

        }
    }

    return (G -> dist[NIL] != INF);
}

int hopccroftKarp(BiGraph* G) {
    G -> pairU = new int[G -> M + 1];
    G -> pairV = new int[G -> N + 1];
    G -> dist = new int [G -> M + 1];

    // MIGHT BE A BUG!
    for (int u = 0; u <= G -> M; u++) {
        G -> pairU[u] = NIL;
    }

    for (int v = 0; v <= G -> N; v++) {
        G -> pairV[v] = NIL;
    }

    int maxiumMatching = 0;

    while(bfs(G)) {
        for (int u = 1; u <= G -> M; u++) {
            if (G -> pairU[u] == NIL && dfs(G, u)) {
                maxiumMatching += 1;
            }
        }
    }

    return maxiumMatching;
}

BiGraph* specialBiGraph(int V) {
    BiGraph* G = new BiGraph;
    G -> N = V;
    G -> M = V;
    G -> adj = new vector<int>[V + 1];

    return G;
}

int main(int argc, char const *argv[])
{
    string division;
    cin >> division;

    int V, K;
    set<int> setK; // set holding officials.
    cin >> V >> K;

    while(K-- > 0) {
        int u;
        cin >> u;
        setK.insert(u + 1);
    }

    int M;
    cin >> M;

    BiGraph* G = specialBiGraph(V);
    bool special = false;

    for (int dummy = 0; dummy < M; dummy++) {
        int i, j;
        cin >> i >> j;

        i += 1;
        j += 1;

        if (setK.find(i) != setK.end() && setK.find(j) == setK.end()) { // i is official
            addEdge(G, i, j);
        } else if (setK.find(i) == setK.end() && setK.find(j) != setK.end()){ // j is official 
            addEdge(G, j, i);
        } // else --> there's also a case when this graph isn't bipartite <=> i and j are both officials.
          //          this algorithm can't handle that :C
        else {
            addEdge(G, i, j);
            addEdge(G, j, i);
            special = true;
        }
        
    }

    cout << hopccroftKarp(G);

    for(int u = 1; u <= G -> M; u++) {
        if (G -> pairU[u] != NIL) {
            cout << endl << u - 1 << " " << G -> pairU[u] - 1;
        }
        if (special) {
            u++;
        }
    }

    return 0;
}
