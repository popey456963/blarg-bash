from math import*
def g(Q,n):
 f=factorial
 while sum(Q):
  s=sum(Q);p=f(s)
  for k in Q:p/=f(k)
  for j in 0,1,23:
   q=p*Q[j]/s
   if q<n:n-=q
   else:print j;Q[j]-=1;break
  
g([20, 6, 6, 0], 2)
