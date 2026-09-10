## 2026-09-10 - Avoid Eager Generator Materialization in AST Traversal
**Learning:** When traversing the AST, eagerly materializing generators like `ast.iter_child_nodes(node)` into lists (e.g., `list(ast.iter_child_nodes(node))`) causes unnecessary memory allocations and overhead, especially in deeply nested or large ASTs.
**Action:** Pass generators directly to recursive traversal functions (e.g., by typing the parameter as `Iterable[ast.AST]`) instead of materializing them.
