#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int main(){
    FILE *infp = fopen ("rosalind_bfs.txt",r);
    assert(infp!=NULL);
    int n;
    int m;

    fscanf(infp,"%d %d\n",&n,&m);
    printf("n:: %d, m: %d\n",n,m);
    
    int *degrees;
    int *num_edges;
    int *adj;
    
    degrees = (int*)malloc(n*sizeof(int));
    num_edges = (int*)malloc((n+1)*sizeof(int));
    adj = (int*)malloc(m*sizeof(int));
    assert(degrees != NULL);
    assert(num_edges !=NULL);
    assert(adj !=NULL);

    for (int i = 0; i<n; i++){
        degrees[i] = 0;
    }
    for (int i = 0; i<m; i++){
        int u; int v;
        fscanf(infp,"%d %d\n",&u, &v);
        u--; v--;
        int vpos = num_edges[u]+degrees[u]++;
        degrees[u]++;
    }
    num_edges[0] = 0;
    for(int i = 1, i<=n; i++)
    {
        num_edges[i] = num_edges[i-1] + degrees[i-1];
    }
    rewind(infp);
    int n2;
    int m2;
    fscanf(infp, "%d %d\n",&u,&v);
    u--;v--;
    assert(n2 ==n);
    assert(m2 == m);
    
    for(int i = 0;i<m;i++)
    {
        int u; int v;
         fscanf(infp,"%d %d\n",&u, &v);
        u--; v--;
        int vpos = num_edges[u] + degrees[u]++;
        adj[vpos] = v;
    }
    fclose(infp);
    free(degrees)
    int *D = (int*)malloc(n*sizeof(int));
    assert(D!=NULL);
    for(int i = 0; i<n; i++)
    {
        D[i]= -1;
    }
    D[0] = 0;
// BFS
 int *q = (int*)malloc(n*sizeof(int));
 assert(q!=NULL);
 q[0] = 0;
 int curr_loc = 0;
 int num_visited = 1;

 while(curr_loc<num_visited){
     int u = q[curr_loc];
     for(int i j = num_edges[u]; j<num_edges[u+1];j++){
    int v = adj[j];
    if(D[v]==-1){
        D[v]= D[u]+1;
        q[num_visited++]=v;
    }         
     }
 curr_loc++;
 }
// 
    FILE *outfp = fopen("BFS.text","w");
    for(int i = 0; i<n; i++)
    {
        fprintf("%d",D[i]);
    }
    fprintf(outfp,"\n"),
    fclose(outfp);
    return 0;
}
