import sys

sys.setrecursionlimit(200000)


class Solution:

  def palindromePath(
      self, n: int, edges: list[list[int]], s: str, queries: list[str]
  ) -> list[bool]:
    g = [[] for _ in range(n)]
    for u, v in edges:
      g[u].append(v)
      g[v].append(u)

    parent = [0] * n
    depth = [0] * n
    sub_size = [0] * n
    heavy = [-1] * n

    def dfs1(u, p, d):
      parent[u] = p
      depth[u] = d
      sub_size[u] = 1
      max_sub = 0
      for v in g[u]:
        if v != p:
          dfs1(v, u, d + 1)
          sub_size[u] += sub_size[v]
          if sub_size[v] > max_sub:
            max_sub = sub_size[v]
            heavy[u] = v

    dfs1(0, -1, 0)

    head = [0] * n
    tin = [0] * n
    cur_pos = 0

    def dfs2(u, h):
      nonlocal cur_pos
      head[u] = h
      tin[u] = cur_pos
      cur_pos += 1
      if heavy[u] != -1:
        dfs2(heavy[u], h)
      for v in g[u]:
        if v != parent[u] and v != heavy[u]:
          dfs2(v, v)

    dfs2(0, 0)

    tree = [0] * (4 * n)
    s_list = list(s)
    init_vals = [0] * n
    for i in range(n):
      init_vals[tin[i]] = 1 << (ord(s_list[i]) - ord('a'))

    def build_tree(node, l, r):
      if l == r:
        tree[node] = init_vals[l]
        return
      mid = (l + r) // 2
      build_tree(2 * node, l, mid)
      build_tree(2 * node + 1, mid + 1, r)
      tree[node] = tree[2 * node] ^ tree[2 * node + 1]

    build_tree(1, 0, n - 1)

    def update(node, l, r, idx, val):
      if l == r:
        tree[node] = val
        return
      mid = (l + r) // 2
      if idx <= mid:
        update(2 * node, l, mid, idx, val)
      else:
        update(2 * node + 1, mid + 1, r, idx, val)
      tree[node] = tree[2 * node] ^ tree[2 * node + 1]

    def query(node, l, r, ql, qr):
      if ql > r or qr < l:
        return 0
      if ql <= l and r <= qr:
        return tree[node]
      mid = (l + r) // 2
      return query(2 * node, l, mid, ql, qr) ^ query(
          2 * node + 1, mid + 1, r, ql, qr
      )

    def get_path_xor(u, v):
      res = 0
      while head[u] != head[v]:
        if depth[head[u]] < depth[head[v]]:
          u, v = v, u
        res ^= query(1, 0, n - 1, tin[head[u]], tin[u])
        u = parent[head[u]]
      if depth[u] > depth[v]:
        u, v = v, u
      res ^= query(1, 0, n - 1, tin[u], tin[v])
      return res

    ans = []
    for q in queries:
      parts = q.split()
      if parts[0] == 'update':
        u = int(parts[1])
        c = parts[2]
        s_list[u] = c
        new_val = 1 << (ord(c) - ord('a'))
        update(1, 0, n - 1, tin[u], new_val)
      else:
        u = int(parts[1])
        v = int(parts[2])
        mask = get_path_xor(u, v)
        ans.append(mask == 0 or (mask & (mask - 1)) == 0)

    return ans