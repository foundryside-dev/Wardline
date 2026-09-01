## 2024-05-24 - Avoid eager materialization of AST generators
**Learning:** Wrapping AST generators like `ast.iter_child_nodes(node)` in `list()` before passing them to recursive traversal functions forces eager materialization, creating unnecessary memory allocations at every recursion level during static analysis.
**Action:** When implementing or modifying AST traversal functions, always type parameters as `Iterable[ast.AST]` instead of `list[ast.AST]` and pass the generator directly to prevent these allocations.
