## 2025-02-12 - Prevent unnecessary list materialization in AST traversal
**Learning:** AST traversal often materializes children into lists (e.g., `list(ast.iter_child_nodes(node))`) which causes high overhead during static analysis. Passing the generator directly is much faster (by around 3x in tight loops).
**Action:** When implementing or modifying AST traversal functions, accept `Iterable[ast.AST]` and pass generators directly instead of eagerly materializing them into lists to prevent unnecessary memory allocations.
