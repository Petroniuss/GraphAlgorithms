#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <climits>
#include <stdio.h>
#include <string.h>

#define NIL 0
#define INF INT_MAX 

using namespace std;

struct BiGraph {
    int E, N; // E for left and N for right sides of Bipartite Graph.
    vector<int>* adj; // adj list only for left vertices.
    int* pairU;
    int* pairV;
    int* dist;
} typedef BiGraph;

void addEdge(BiGraph* G, int u, int v) {
    G -> adj[u].push_back(v);
}

BiGraph* createBiGraph(int E, int N) {
    BiGraph* G = new BiGraph;
    
    G -> E = E;
    G -> N = N;
    G -> adj = new vector<int>[E + 1];

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

    for (int u = 1; u <= G -> E; u++) {
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
    G -> pairU = new int[G -> E + 1];
    G -> pairV = new int[G -> N + 1];
    G -> dist = new int [G -> E + 1];

    for (int u = 0; u <= G -> E; u++) {
        G -> pairU[u] = NIL;
    }

    for (int v = 0; v <= G -> N; v++) {
        G -> pairV[v] = NIL;
    }

    int maxiumMatching = 0;

    while(bfs(G)) {
        for (int u = 1; u <= G -> E; u++) {
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
    G -> E = V;
    G -> adj = new vector<int>[V + 1];

    return G;
}

// BLOSSOM --> Some ugly code stolen from the internet :P

const int M = 500;

struct struct_edge{
    int v;
    struct_edge* n;
};

typedef struct_edge* edge;
struct_edge pool[M * M * 2];
edge top = pool, adj[M];
int V, E, match[M], qh, qt, q[M], father[M], base[M];
bool inq[M], inb[M], ed[M][M];

void add_edge(int u,int v) {
    top -> v = v;
    top -> n = adj[u];
    adj[u] = top++;
    top -> v = u;
    top -> n = adj[v];
    adj[v] =top++;
}
int LCA(int root, int u, int v) {
    static bool inp[M];
    memset(inp, 0, sizeof(inp));

    while(1) {
        inp[u = base[u]] = true;
        if (u == root)
            break;
        u = father[match[u]];
    }
    while(1) {
        if (inp[v = base[v]])
            return v;
        else
            v = father[match[v]];
    }
}

void mark_blossom(int lca,int u) {
    while (base[u] != lca) {
        int v = match[u];
        inb[base[u]] = inb[base[v]] = true;
        u = father[v];
        if (base[u] != lca)
            father[u] = v;
    }
}

void blossom_contraction(int s, int u, int v) {
    int lca = LCA(s, u, v);
    memset(inb, 0, sizeof(inb));

    mark_blossom(lca, u);
    mark_blossom(lca, v);
    
    if (base[u] != lca)
        father[u] = v;
    if (base[v] != lca)
        father[v]=u;
    for (int u = 0; u < V;u++)
        if (inb[base[u]]) {
            base[u]=lca;
        if (!inq[u])
            inq[q[++qt] = u] = true;
    }
}

int find_augmenting_path(int s) {
    memset(inq, 0, sizeof(inq));
    memset(father, -1, sizeof(father));
    for (int i = 0; i < V; i++)
        base[i]=i;
    inq[q[qh = qt = 0] = s] = true;
    while (qh <= qt) {
        int u = q[qh++];
        for (edge e = adj[u]; e; e = e->n) {
            int v = e -> v;
            if (base[u] != base[v] && match[u] != v) {
                if ((v == s) || (match[v] != -1 && father[match[v]] !=-1))
                    blossom_contraction(s,u,v);
                else if (father[v] == -1) {
                    father[v]=u;
                    if (match[v] == -1)
                        return v;
                    else if (!inq[match[v]])
                        inq[q[++qt] = match[v]] = true;
                }
            }
        }
    }
    return -1;
}

int augment_path(int s, int t) {
    int u = t, v, w;
    while (u != -1) {
        v = father[u];
        w = match[v];
        match[v] = u;
        match[u] = v;
        u = w;
    }
    return t != -1;
}

int edmonds() {
    int matchc = 0;
    
    memset(match, -1, sizeof(match));
    
    for (int u = 0; u < V; u++) {
        if (match[u] == -1)
            matchc += augment_path(u, find_augmenting_path(u));
    }

    return matchc;
}

int main(int argc, char const *argv[]) {
    string division;
    cin >> division;

    int V, K, E;
    set<int> setK; // set holding officials.
    cin >> V >> K;

    while(K-- > 0) {
        int u;
        cin >> u;
        setK.insert(u + 1);
    }

    cin >> E;

    BiGraph* G = specialBiGraph(V);
    bool isBipartite = true;

    for (int dummy = 0; dummy < E; dummy++) {
        int i, j;
        cin >> i >> j;

        if (!ed[i][j]) {
            add_edge(i, j);
            ed[i][j]= ed[i][j] = true;
        }

        i += 1;
        j += 1;

        if (setK.find(i) != setK.end() && setK.find(j) == setK.end()) { // i is official
            addEdge(G, i, j);
        } else if (setK.find(i) == setK.end() && setK.find(j) != setK.end()){ // j is official 
            addEdge(G, j, i);
        } // else --> there's also a case when this graph isn't bipartite <=> i and j are both officials.
          //          hopcroft can't handle that :/
        else {
            isBipartite = false;
        }
        
    }

    if (isBipartite) {
        cout << hopccroftKarp(G);

        for (int u = 1; u <= G -> E; u++) {
            if (G -> pairU[u] != NIL) {
                cout << endl << u - 1 << " " << G -> pairU[u] - 1;
            }
        }
    } else {
        cout << edmonds();
        for (int i = 0; i < V; i++) {
            if (i < match[i])
               cout << endl << i <<" "<< match[i];
        }
    }

    return 0;
}