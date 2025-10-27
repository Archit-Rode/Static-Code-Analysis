## REFLECTION
1.Which issues were the easiest to fix, and which were the hardest? Why?

Easiest to fix:
Global state / mutable default argument – changing logs=[] to logs=None and passing stock_data as a parameter was straightforward and didn’t require complex logic.
PEP8/style issues – adding blank lines and renaming functions to snake_case were simple formatting changes.

Hardest to fix:
Eval usage – removing eval() required understanding the purpose of the original code and replacing it safely with ast.literal_eval(). This was crucial because using eval could lead to arbitrary code execution, so the fix had to be secure.
Input validation – ensuring item and qty had the correct types and values required adding checks and raising exceptions, while maintaining backward compatibility with valid operations.

2. Did the static analysis tools report any false positives? If so, describe one example.

Example: Pylint flagged except (OSError, TypeError) in save_data() as a potential “broad exception caught” warning.

Reality: In this context, catching both exceptions is intentional to handle file I/O and JSON serialization errors safely. It is not actually unsafe, so this is a minor false positive.

3. How would you integrate static analysis tools into your actual software development
workflow? Consider continuous integration (CI) or local development practices.

Local development:
Run Flake8 or Pylint as part of pre-commit hooks to catch style and naming issues before code is committed.
Use Bandit to check for security vulnerabilities in code changes locally.

Continuous Integration (CI):
Integrate tools in CI pipelines (GitHub Actions, GitLab CI, Jenkins) to automatically analyze every pull request.
Fail the build if high-severity security issues or critical style violations are found, ensuring consistent code quality across the team.

4. What tangible improvements did you observe in the code quality, readability, or potential
robustness after applying the fixes?

Code quality: Functions are modular, well-named, and follow Python conventions (snake_case, docstrings).

Readability: Clear structure, consistent spacing, and f-string usage make it easier to read and maintain.

Robustness:
Input validation prevents invalid data from corrupting inventory.

Specific exception handling avoids silent failures.

Removal of eval eliminates a major security risk.

Maintainability: Passing stock_data as a parameter and avoiding global state allows easier testing and reusability of functions.
