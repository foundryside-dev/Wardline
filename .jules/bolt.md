## 2024-05-24 - Avoid list materialization in AST traversal
**Learning:** Eagerly materializing AST node iterators (like `ast.iter_child_nodes()`) into lists causes unnecessary memory allocations and overhead, especially in deeply nested or large codebases. Passing iterators directly avoids this.
**Action:** When implementing or modifying AST traversal functions, accept `Iterable[ast.AST]` and pass generators directly instead of using `list()`.
