# Model-valued dictionary key collision regression evidence

Supplemental tests for pydantic/pydantic-settings PR #1109, which fixes #1107.
The existing PR's tests cover nested containers. This probe adds BaseModel dictionary values and keys equal to their field names or validation aliases.

- Baseline `7e2dacb6db07b41abb0c80d0608e46e197265554`: 5 failed, 2 passed.
- Candidate `36f3d9f481df0310ee75370c06017d8825ed5447`: 7 passed.
- macOS, CPython 3.11.12; exact dependencies in environment.txt.

Run from a repository checkout at either commit, with dependencies from environment.txt:

```sh
PYTHONPATH=. python -m pytest experiments/model-dict-key/probe_model_keys.py -v
```

No duplicate fix PR. These are focused regression checks, not a full review or platform matrix. No adoption has been observed.
