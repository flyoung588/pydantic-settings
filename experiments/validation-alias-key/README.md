# Remaining validation-alias collision coverage after #1109 merged

Test-only code commit: b8fb3260f9fc40d7a8baca7b0cc008d5b5c72125; base 94150a0d24967026724031a08e6949b9849df3c5.

Upstream #1109 merged as 9e02de082f68e3115f378efaa0c91d0bfcb66dec. Its later author commit adds name/count dictionary-key collision coverage. That outcome matches part of our earlier evidence, but no explicit attribution or code adoption is established. Do not present the upstream merge as merging our seven-case companion PR.

The remaining test is narrower: a dictionary key equal to a value model validation_alias must remain a dictionary key. It adds label plus an other-key control in 17 test lines, without production/config/license changes.

Current code: 2 targeted cases pass; full tests/test_settings.py: 529 passed, 1 skipped. Ruff check/format pass. A deliberately synthetic alias-only negative control leaves all pre-existing module tests passing (527 passed, 1 skipped) while the new collision case fails and the control passes. This shows independent coverage value; it is NOT a newly discovered current production bug. Python3.11.12/Pydantic2.14.1. Separate PYTHONPYCACHEPREFIX directories avoided stale-source bytecode between variants.

Reproduce in an isolated checkout of the test commit with test dependencies:

```sh
PYTHONPATH=. pytest tests/test_settings.py -k matching_validation_alias -q
PYTHONPATH=. pytest tests/test_settings.py -q
```

The included alias-only-mutant.patch can be applied only for the negative-control runs, then reversed. No production change from that patch is proposed. Raw outputs are in evidence/. Earlier broad author-fork companion is superseded by this reduced follow-up; external running, acceptance, and merge are not established.
