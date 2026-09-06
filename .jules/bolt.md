## 2024-10-25 - Unnecessary list materialization during AST traversal
**Learning:** Eagerly materializing generators like `ast.iter_child_nodes()` into lists inside recursive AST traversal functions forces unnecessary memory allocations and adds overhead during static analysis.
**Action:** When implementing or modifying AST traversal functions, accept `Iterable[ast.AST]` and pass generators directly instead of eagerly materializing them.
