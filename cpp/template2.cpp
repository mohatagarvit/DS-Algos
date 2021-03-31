#include <bits/stdc++.h>
#include <limits.h>
#include <ext/pb_ds/assoc_container.hpp> 
#include <ext/pb_ds/tree_policy.hpp> 
using namespace __gnu_pbds; 
#define ii pair<int,int>
#define ll long long
#define ld long double
#define pll pair<ll,ll>
using namespace std;
#define iiordered_set tree<pll, null_type,less<pll>, rb_tree_tag,tree_order_statistics_node_update>
template<class T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
// order_of_key(), find_by_order()
template<class T>
using min_heap = priority_queue<T, vector<T>, greater<T>>;
#define MOD 1000000007ll
#define MOD2 998244353ll
#define INFl 1e18
#define vi vector<int>
#define di deque<int>
#define si set<int>
#define pii pair<int, int>
#define vvi vector<vi>
#define vl vector<long long>
#define vvl vector<vl>
#define vll vector<pll>
#define vii vector<ii>
#define sii set<pii>
#define vvii vector<vii>
#define F first
#define S second
#define forl(i,n) for(int i=0;i<n;i++)
#define fore(i,n) for(int i=1;i<=n;i++)
#define rforl(i,n)  for(int i=n-1;i>=0;i--)
#define rfore(i,n)  for(int i=n;i>=1;i--)
#define CASE(t) cout<<"Case #"<<(t)<<": ";
#define INF 1100000009
#define INFl 1e18
#define gcd(a,b) __gcd(a,b)
#define all(x)  x.begin(),x.end()
#define mp make_pair
#define pb push_back
#define Fill(s,v) memset(s,v,sizeof(s))

ll power(ll a,ll b, ll m=MOD)
{
    ll res=1;
    while(b>0)
    {
        if(b&1)
            res=(res*a)%m;
        a=(a*a)%m;
        b>>=1;
    }
    return res;
}

ll inverse(ll a,ll m=MOD)
{
    return power(a,m-2,m);
}
ll modInverseExtendedEuclid(ll a, ll m) 
{ 
    ll m0 = m; 
    ll y = 0, x = 1; 
    if (m == 1) 
      return 0; 
  
    while (a > 1) 
    {
        ll q = a / m; 
        ll t = m; 
        m = a % m, a = t; 
        t = y; 
        y = x - q * y; 
        x = t; 
    } 
    if (x < 0) 
       x += m0;   
    return x; 
} 

int ceil(int a,int b)
{
    return (a+b-1)/b;
}

vvl matmul(const vvl &a,const vvl &b,ll M=MOD)
{
    int n=a.size(),m=a[0].size(),l=b[0].size();
    assert(m==b.size());
    vvl c(n,vl(l,0));
    forl(i,n)
    forl(j,l)
    forl(k,m)
    {
        c[i][j]=(c[i][j]+a[i][k]*b[k][j])%M;
    }
    return c;
}
vvl matpow(vvl a,ll p,ll M=MOD)
{
    assert(a.size()==a[0].size());
    int n=a.size();
    vvl res(n,vl(n,0));
    forl(i,n)   res[i][i]=1;
    while(p>0)
    {
        if(p&1) res=matmul(res,a,M);
        a=matmul(a,a,M);
        p>>=1;
    }
    return res;
}

void sieve(vl& primes,ll mx)
{
    vl is_comp(mx,0);
    for(ll i=2;i<mx;i++)
    {
        if(!is_comp[i])
            primes.pb(i);
        for(ll j=0;j<primes.size()&&primes[j]*i<mx;j++)
        {
            is_comp[i*primes[j]]=1;
            if(i%primes[j]==0)
                break;
        }
    }
}

vl get_prime_facs(ll x) {
    vl res;
    for(ll p=2; p<=sqrt(x); p++) {
        if(x%p == 0) {
            res.pb(p);
            while(x%p == 0)
                x /= p;
        }
    }
    if(x > 1)
        res.pb(x);
    return res;
}

// void GospersHack(int k, int n)
// {
//     int set = (1 << k) - 1;
//     int limit = (1 << n);
//     while (set < limit)
//     {
//         DoStuff(set);

//         // Gosper's hack:
//         int c = set & - set;
//         int r = set + c;
//         set = (((r ^ set) >> 2) / c) | r;
//     }
// }
constexpr int pct(int x) { return __builtin_popcount(x); } // # of bits set
constexpr int bits(ll x) { return 63-__builtin_clzll(x); } // floor(log2(x)) 
ll cdiv(ll a, ll b) { return a/b+((a^b)>0&&a%b); } // divide a by b rounded up
ll fdiv(ll a, ll b) { return a/b-((a^b)<0&&a%b); } // divide a by b rounded down

#define printvec(x)    for(auto it=x.begin();it!=x.end();it++) cout<<*it<<' '; cout<<endl;
#define printvecpair(x)  for(auto it=x.begin();it!=x.end();it++) cout<<it->F<<' '<<it->S<<endl;  
#define fastio ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL) 

// Fenwick tree
// const int MAX=300000;
// int bit[MAX];
// void add(int x,int v=1){
//     x++;
//     for(;x<MAX;x+=x&-x)
//         bit[x]+=v;
// }
// int query(int x){
//     x++;
//     int sum=0;
//     for(;x>0;x-=x&-x)
//         sum+=bit[x];
//     return sum;
// }
// int query(int l,int r){
//     return query(r)-query(l-1);
// }


// struct UnionFind
// {
//     int n;
//     vi p,r;
 
//     UnionFind(int N)
//     {
//         n=N;
//         p.assign(N,0);
//         r.assign(N,1);
//         for(int i=0;i<N;i++)
//             p[i]=i;
//     }
//     int FindSet(int i)
//     {
//         return (p[i]==i)?i:(p[i]=FindSet(p[i]));
//     }
//     bool isSameSet(int i,int j)
//     {
//         return FindSet(i)==FindSet(j);
//     }
//     void UnionSet(int i,int j)
//     {
//         int p1=FindSet(i);
//         int p2=FindSet(j);
//         if(p1!=p2)
//         {
//             if(r[p1]>=r[p2])
//             {
//                 p[p2]=p1;
//                 if(r[p1]==r[p2])
//                     r[p1]++;
//             }
//             else
//                 p[p1]=p2;
//         }
//     }
//     void disp()
//     {
//         for(int i=0;i<n;i++)
//             cout<<p[i]<<' ';
//         cout<<endl;
//     }
// };

void solve(int ttt=-1)
{
    ll i,j,k,l,m,n,r,u,v,x,y;
    // DEBUG CHECK
    // 1. read question correctly
    // 2. corner cases
    // 3. logic error
    // 4. implementation error
    // 5. ulimit -s 131072 (dont make unlimited)
    // 6. g++ -O3 -std=c++14 -o code code.cpp

    int nn,kk,ss;
    ll s;
    cin>>nn>>kk>>ss;
    n=nn;k=kk;s=ss;
    cout<<"Case #"<<ttt<<": "<<((k-1) + min(n+1, k-s + n-s+1))<<endl;    
    
    // cout<<"Case #"<<ttt<<": "<<ans<<endl;    
    // cout<<fixed<<setprecision(10)<<"Case #"<<ttt<<": "<<ans<<endl;
}

int main()
{
    fastio;
    int tt=1; 
    cin>>tt;

    fore(ttt,tt)
    {
        solve(ttt);
    }
    return 0;
}

