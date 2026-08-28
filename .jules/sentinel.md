## 2025-02-14 - Prevent Git Config Code Execution
**Vulnerability:** Invoking `git` via `subprocess` against untrusted directories without overriding config can allow malicious repositories to execute code via `.git/config` hooks like `core.fsmonitor`.
**Learning:** `git` uses configurations from the `.git/config` file in the current working directory or `cwd` argument, which could be controlled by an attacker when analyzing untrusted codebases.
**Prevention:** Explicitly pass `("-c", "core.fsmonitor=false")` as `_SAFE_GIT_CONFIG` to all `git` subprocess commands in the codebase.

## 2026-06-21 - [Add Unsafe PyYAML Loaders to Taint Tracking]
**Vulnerability:** The static analyzer was missing `yaml.unsafe_load` and `yaml.full_load` in its `_SERIALISATION_SINKS` mapping, potentially leading to false negatives when tracking untrusted data flowing into these dangerous deserialization functions.
**Learning:** Even if functions are listed in rule specifications (like `_SINK_SPECS`), they also need to be properly categorized in the core taint propagation logic (`_SERIALISATION_SINKS`) to ensure the analyzer correctly sheds validation provenance (converting output to `UNKNOWN_RAW`).
**Prevention:** When adding new sinks to rule definitions, always verify if they need to be added to core propagation mappings like `_SERIALISATION_SINKS` or `_PROPAGATING_BUILTINS`.

## 2026-08-28 - Prevent Taint Leakage via Parameter Defaults
**Vulnerability:** Parameter default value expressions were evaluated using `function_taint` as the fallback base taint in the L2 static analyzer. This caused untrusted data in default expressions (e.g., `x=get_untrusted_data()`) to inherit `ASSURED` when the function was `@trusted(level="ASSURED")`, masking the leakage.
**Learning:** Default parameter expressions are evaluated at the call site at runtime, not from within the function's scope. They should not inherit the function's overall trust level during static analysis.
**Prevention:** When evaluating default parameter expressions in `wardline`'s L2 taint analysis (`_seed_parameters`), always evaluate them with a clean base state (`TaintState.INTEGRAL`) rather than inheriting `function_taint`.
