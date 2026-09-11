## 2024-05-24 - Avoid eager materialization of AST traversals
**Learning:** Eagerly materializing AST node generators (like `ast.iter_child_nodes`) into lists during deep recursive traversals in the `wardline` scanner causes unnecessary memory allocations and overhead, impacting performance.
**Action:** Always accept `Iterable[ast.AST]` in traversal functions and pass generators directly to avoid creating temporary lists in memory, reducing generator overhead while keeping the recursive nature of the algorithm intact.
