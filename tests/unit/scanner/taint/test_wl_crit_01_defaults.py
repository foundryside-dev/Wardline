import ast

from wardline.core.taints import TaintState as T
from wardline.scanner.taint.variable_level import compute_variable_taints


def _vt(src: str, function_taint=T.UNKNOWN_RAW, taint_map=None, alias_map=None):
    func = ast.parse(src).body[0]
    assert isinstance(func, (ast.FunctionDef, ast.AsyncFunctionDef))
    return compute_variable_taints(func, function_taint, taint_map or {}, alias_map=alias_map)


def test_default_expression_evaluated():
    src = "def f(x=get_untrusted_data()):\n    pass\n"
    out = _vt(src, function_taint=T.ASSURED, taint_map={"get_untrusted_data": T.EXTERNAL_RAW})
    assert out["x"] == T.EXTERNAL_RAW, out["x"]

    src = "def f(x=get_untrusted_data(), y=other()):\n    pass\n"
    out = _vt(src, function_taint=T.ASSURED, taint_map={"get_untrusted_data": T.EXTERNAL_RAW, "other": T.ASSURED})
    assert out["x"] == T.EXTERNAL_RAW, out["x"]
    assert out["y"] == T.ASSURED, out["y"]


def test_kw_defaults_evaluated():
    src = "def f(*, x=get_untrusted_data()):\n    pass\n"
    out = _vt(src, function_taint=T.ASSURED, taint_map={"get_untrusted_data": T.EXTERNAL_RAW})
    assert out["x"] == T.EXTERNAL_RAW, out["x"]
