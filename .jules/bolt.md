## 2024-05-15 - AST Iteration Memory Optimization
**Learning:** In deeply recursive AST traversal functions like those used for taint analysis, eagerly materializing lists from generators (e.g., `list(ast.iter_child_nodes(node))`) causes unnecessary memory allocations and overhead.
**Action:** When implementing or modifying AST traversal functions, pass iterators directly by typing the parameter as `Iterable[ast.AST]` rather than `list[ast.AST]`.
