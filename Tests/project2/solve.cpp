#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <climits>
#include <iostream> 
#include <set> 
#include <iterator>

using namespace std;

#define NIL 0
#define INF INT_MAX 

struct Edge {
    int to;
    int u;
    int l;
} typedef Edge;

struct BiGraph {
    int M, N; // M for left and N for right sides of Bipartite Graph.
    vector<int>* adj; // adj list only for left vertices.
    int* pairU;
    int* pairV;
    int* dist;
    vector<Edge*>* edges;
} typedef BiGraph;



Edge* edge(int to, int l, int u) {
    Edge* edge = new Edge;
    
    edge -> to = to;
    edge -> u = u;
    edge -> l = l;

    return edge;
}

Edge* findEdge(BiGraph* G, int from, int to) {
    for (auto e: G -> edges[from]) {
        if (e -> to == to)
            return e;
    }

    cout << "error!";
}

void addEdge(BiGraph* G, int u, int v) {
    G -> adj[u].push_back(v);
}

BiGraph* specialBiGraph(int V) {
    BiGraph* G = new BiGraph;
    G -> N = V;
    G -> M = V;
    G -> adj = new vector<int>[V + 1];
    G -> edges = new vector<Edge*>[V + 1];

    G -> pairU = new int[G -> M + 1];
    G -> pairV = new int[G -> N + 1];
    G -> dist = new int [G -> M + 1];

    return G;
}

bool dfs(BiGraph* G, int u, int x) {
    if (u != NIL) {
        for(auto v : G -> adj[u]) {
            auto edge = findEdge(G, u, v);
            if (edge -> l <= x && edge -> u >= x && 
                    G -> dist[G -> pairV[v]] == G -> dist[u] + 1) {
                if (dfs(G, G -> pairV[v], x) == true) {
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

bool bfs(BiGraph* G, int x) {
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
                auto edge = findEdge(G, u, v);
            
                if (edge -> l <= x && edge -> u >= x && G -> dist[G -> pairV[v]] == INF) {
                    G -> dist[G -> pairV[v]] = G -> dist[u] + 1;
                    Q.push(G -> pairV[v]);
                }
            }

        }
    }

    return (G -> dist[NIL] != INF);
}

int hopccroftKarp(BiGraph* G, int x) {
    for (int u = 0; u <= G -> M; u++) {
        G -> pairU[u] = NIL;
    }

    for (int v = 0; v <= G -> N; v++) {
        G -> pairV[v] = NIL;
    }

    int maxiumMatching = 0;

    while(bfs(G, x)) {
        for (int u = 1; u <= G -> M; u++) {
            if (G -> pairU[u] == NIL && dfs(G, u, x)) {
                maxiumMatching += 1;
            }
        }
    }

    return maxiumMatching;
}

void solve() {
    int n; // number of vertices.
    cin >> n;    

    int m; // number of edges;
    cin >> m;
    int dummy = m;

    int* L = new int[n + 1];
    int* U = new int[n + 1];
    
    BiGraph* G = specialBiGraph(n);
    vector<Edge*>* edges = G -> edges;
    set<int> xs; 

    while (dummy-- > 0) {
        int from, to, l, u;
        Edge* e;

        cin >> from >> to >> l >> u;
        e = edge(to, l, u);

        addEdge(G, from, to);
        edges[from].push_back(e);
        
        xs.insert(l);
        xs.insert(u);
    }

    for (auto x: xs) {
        int matching = hopccroftKarp(G, x);
    
        if (matching == G -> N) {

            cout << x << endl;
            for(int u = 1; u <= G -> M; u++) {
                if (G -> pairU[u] != NIL) {
                    cout << u << " " << G -> pairU[u] << endl;
                }
            }
            return;
        }
    }

    cout << -1 << endl;
}

int main(int argc, char const *argv[]) {
    int tests;
    cin >> tests;
    
    while (tests-- > 0) {
        solve();  
    }

    return 0;
}