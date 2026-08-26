## 2024-05-18 - Replacing `list(ast.iter_child_nodes(node))` with `ast.iter_child_nodes(node)`
**Learning:** `ast.iter_child_nodes()` returns a generator. Realizing this into a list using `list(ast.iter_child_nodes())` allocates unnecessary memory.
**Action:** When working on memory-intensive AST analysis passes, accept `Iterable[ast.AST]` where child nodes are needed, rather than explicit `list[ast.AST]`.
