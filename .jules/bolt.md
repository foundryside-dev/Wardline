## 2024-05-13 - [Generator overhead vs memory allocations]
**Learning:** `list(ast.iter_child_nodes(node))` in recursive functions forces full eager materialization of all children before yielding, which uses memory unnecessarily when iterating.
**Action:** When working on AST traversal, accept `Iterable[ast.AST]` (or iterate over the generator directly) instead of `list[ast.AST]` to avoid this overhead, avoiding `list()` on generators.
