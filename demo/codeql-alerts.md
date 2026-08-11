# CodeQL alert examples

The `demo/codeql-alerts` branch contains five intentionally vulnerable,
standalone examples. They are not imported by the application and must not be
merged into production code.

| Example | Expected CodeQL family | Typical severity |
| --- | --- | --- |
| User-controlled shell command | Command injection | High |
| User-controlled file path | Path injection | High |
| User-controlled URL | Server-side request forgery | High |
| User-controlled serialized payload | Unsafe deserialization | High |
| User-controlled template | Template injection | High |

Open the branch's CodeQL run under **Actions**, or open
**Security and quality → Code scanning** and filter by
`demo/codeql-alerts`. Review each data-flow path and fix the examples before
merging anything from this branch.
