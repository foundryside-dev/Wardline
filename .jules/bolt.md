## 2026-09-04 - Avoid eager list materialization in AST traversals
**Learning:** Eagerly materializing AST node generators like `ast.iter_child_nodes()` into lists (e.g. `list(ast.iter_child_nodes(node))`) causes unnecessary memory allocations and slows down performance, especially in highly recursive traversal functions.
**Action:** When implementing or modifying AST traversal functions, type hint them to accept `Iterable[ast.AST]` and pass generators directly instead of lists.
