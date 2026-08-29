## 2024-05-23 - AST Traversal Generator Preservation
**Learning:** Eagerly materializing AST generators into lists (e.g. `list(ast.iter_child_nodes())`) in recursive functions causes unnecessary memory allocations and overhead, especially in deep ASTs.
**Action:** When implementing or modifying AST traversal functions, accept `Iterable[ast.AST]` and pass generators directly to avoid creating intermediate lists.
