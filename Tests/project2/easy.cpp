#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <climits>

using namespace std;

#define NIL 0
#define INF INT_MAX 

struct BiGraph {
    int M, N; // M for left and N for right sides of Bipartite Graph.
    vector<int>* adj; // adj list only for left vertices.
    int* pairU;
    int* pairV;
    int* dist;
} typedef BiGraph;

struct Edge {
    int to;
    int u;
    int l;
} typedef Edge;

Edge* edge(int to, int l, int u) {
    Edge* edge = new Edge;
    
    edge -> to = to;
    edge -> u = u;
    edge -> l = l;

    return edge;
}

void addEdge(BiGraph* G, int u, int v) {
    G -> adj[u].push_back(v);
}

BiGraph* specialBiGraph(int V) {
    BiGraph* G = new BiGraph;
    G -> N = V;
    G -> M = V;
    G -> adj = new vector<int>[V + 1];

    return G;
}

BiGraph* createBiGraph(int M, int N) {
    BiGraph* G = new BiGraph;
    
    G -> M = M;
    G -> N = N;
    G -> adj = new vector<int>[M + 1];

    return G;
}

void printBiGraph(BiGraph* G) {
    cout << endl << "----- BiGraph ----- " << endl << "V = " << G -> M << endl; 
    for (int i = 1; i <= G -> M; i++ ) {
        for (auto v : G -> adj[i]) {
            cout << i << " <-> " << v << endl;
        }
    }
    cout << "-------------------";
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

int checkMin(int currentMin, int l) {
    if (currentMin < l) return l;
    else                return currentMin;
        
}

int checkMax(int currentMax, int u) {
    if (currentMax < u) return currentMax;
    else                return u;
}

// ---- Notes ---- 
/*
    - Vertices now are numerated from 1 not 0 as it was previosuly!
    - We store adj list for left side!
*/

void solveTest() {
    int n; // number of vertices.
    cin >> n;    

    int m; // number of edges;
    cin >> m;
    int dummy = m;

    int* L = new int[n + 1];
    int* U = new int[n + 1];
    
    BiGraph* G = specialBiGraph(n);
    vector<Edge*>* edges = new vector<Edge*>[n + 1];

    while (dummy-- > 0) {
        int from, to, l, u;
        Edge* e;

        cin >> from >> to >> l >> u;
        e = edge(to, l, u);

        addEdge(G, from, to);
        edges[from].push_back(e);
    }

    int maxiumMatching = hopccroftKarp(G);

    cout << endl << "Maximum Matching = " << maxiumMatching << endl << "Edges: ";
    for(int u = 1; u <= G -> M; u++) {
        if (G -> pairU[u] != NIL) {
            cout << endl << u << "<->" << G -> pairU[u];
        }
    }

    int x = INF;
    int min = INT_MIN;
    int max = INT_MAX;

    for(int u = 1; u <= G -> M; u++) {
        if (G -> pairU[u] != NIL) {
            cout << endl << u << "<->" << G -> pairU[u];

            for (auto e: edges[u]) {
                if (e -> to == G -> pairU[u]) {
                    min = checkMin(min, e -> l);
                    max = checkMax(max, e -> u);
                    cout << " :" << e -> l << ", " << e -> u;
                    break;
                }
            }
        }
    }

    cout << endl << "Min: " << min << ", max: " << max << endl;

    if (min > max) {
        cout << -1 << endl;
        return;
    }

    cout << min << endl;

    for(int u = 1; u <= G -> M; u++) {
        if (G -> pairU[u] != NIL) {
            cout << endl << u << "<->" << G -> pairU[u];
        }
    }

    cout << endl;
}

int main(int argc, char const *argv[]) {
    int tests;
    cin >> tests;
    
    while (tests-- > 0) {
        solveTest();   
    }

    return 0;
}

int project1() {
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
            cout << "It should not go here!";
        }
        
    }

    cout << hopccroftKarp(G);

    for(int u = 1; u <= G -> M; u++) {
        if (G -> pairU[u] != NIL) {
            cout << endl << u - 1 << " " << G -> pairU[u] - 1;
        }
    }

    return 0;
}
