# Round 4 Track D — native regression test collaboration

The prior AnyIO #1439 and pydantic-settings #1109 comments received no reply and their candidate heads had not changed at initial readback. No prior adoption is claimed.

A tests-only contribution to the existing pydantic-settings #1109 author's active branch now exists as https://github.com/Hugohong258/pydantic-settings/pull/1 . This is an external collaboration PR, not a duplicate upstream production fix.

Exact test code commit: `8178898fe7fb07232cef52d05ff9080c1f6c27af`.

The seven cases were integrated into `tests/test_settings.py`: dictionary keys matching scalar value-model fields and a validation alias, plus two controls.

Validation:
- Candidate 36f3d9f: targeted 7 passed; full settings module 528 passed, 1 skipped.
- Revert only env.py to base 7e2dacb: targeted 5 failed, 2 controls passed.
- Ruff check, Ruff format check and git diff check passed.
- Exact dependencies and raw output files preserved.

An initial full-module run after restoring env.py still used timestamp/size-valid baseline bytecode and failed the 8 expected base cases. This failed output is retained as full-settings.txt. Removing only generated env bytecode and running against verified restored candidate source produced full-settings-verified-source.txt (528 passed, 1 skipped). No production source difference remains in the PR.

The PR/code readback verifies that the external PR contains 26 added test lines. Author response, external execution, acceptance into upstream #1109 and merge remain UNKNOWN / not observed.
