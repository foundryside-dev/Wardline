## 2024-05-30 - Avoid Eager Materialization of AST Child Nodes
**Learning:** Materializing `ast.iter_child_nodes` into lists using `list(ast.iter_child_nodes(node))` during deep recursive AST traversal (e.g., in taint tracking) causes unnecessary memory allocations and performance overhead. Generators should be passed directly to recursive functions that accept iterables.
**Action:** When implementing or modifying AST traversal functions, accept `Iterable[ast.AST]` and pass generators directly instead of eagerly materializing them into lists to reduce memory footprint and improve speed.
