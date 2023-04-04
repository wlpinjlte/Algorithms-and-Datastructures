from egzP4btesty import runtests 

class Node:
  def __init__(self, key, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = key
    self.x = None
def minn(x):
  if x.left!=None:
    return minn(x.left)
  else:
    return x
def maxx(x):
  if x.right!=None:
    return maxx(x.right)
  else:
    return x
def prev(x):
  if x.left!=None:
    return maxx(x.left)
  else:
    p_root=x.parent
    while p_root:
      if x!=p_root.left:
        break
      x=p_root
      p_root=x.parent
    return p_root
def succ(x):
  if x.right!=None:
    return minn(x.right)
  else:
    p_root = x.parent
    while p_root:
      if x != p_root.right:
        break
      x = p_root
      p_root = x.parent
    return p_root

def sol(root, T):
  #print(T)
  summ=0
  for i in T:
    # print(i.key)
    # print(prev(i).key)
    # print(succ(i).key)
    # print()
    if prev(i).key+succ(i).key==2*i.key:
      summ+=i.key
  return summ
    
runtests(sol, all_tests = True)