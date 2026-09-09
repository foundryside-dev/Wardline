## 2026-06-11 - AST Traversal Generators
**Learning:** Eagerly materializing AST generators like `ast.iter_child_nodes()` into lists inside deeply recursive functions (like `_assignment_callee` and `_collect_return_paths`) causes redundant memory allocations for large AST trees.
**Action:** When implementing or modifying AST traversal functions, pass the raw generators directly by accepting `Iterable[ast.AST]` instead of `list[ast.AST]` to avoid eager materialization overhead.
