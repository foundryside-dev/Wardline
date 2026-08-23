## 2026-08-23 - Avoid eager materialization of AST generators
**Learning:** Eagerly materializing AST generators like `ast.iter_child_nodes()` into lists (e.g., `list(ast.iter_child_nodes(node))`) causes unnecessary memory allocations and overhead, particularly during deep AST traversals in static analysis.
**Action:** Accept `Iterable[ast.AST]` in AST traversal functions and pass generators directly (e.g., `ast.iter_child_nodes()`) instead of eagerly materializing them into lists.
