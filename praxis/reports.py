"""Complete reports with backwards-compatible reading of historical companions.

New compilation has no per-document byte cap and keeps report text/JSON together.
"""

from praxis.errors import PraxisError
from praxis.jsonio import load_json

MARKER = "## Machine-readable report\n\n```json\n"


def partition(name: str, text: str) -> dict[str, str]:
    if name not in ("coverage", "features"):
        raise PraxisError("INVALID_REPORT", "Only coverage and features reports support companion documents")
    # Kept for callers using the older helper. New reports are returned whole;
    # read_report below still supports immutable historical companion layouts.
    return {f"wiki/{name}.md": text}


def read_report(bundle, name: str) -> dict:
    if name not in ("coverage", "features"):
        raise PraxisError("INVALID_REPORT", "Select coverage or features")

    def extract(key):
        path = bundle.manifest.documents.get(key)
        if path is None:
            raise PraxisError("REPORT_UNAVAILABLE", f"Missing registered report document {key}")
        try:
            text = bundle.read(path)
            payload, end = text.split("```json\n", 1)[1].split("\n```", 1)
            data = load_json(payload)
            if not isinstance(data, dict):
                raise ValueError("Report must be an object")
            return data
        except (IndexError, ValueError) as exc:
            raise PraxisError("INVALID_REPORT", f"{key}: missing or invalid complete JSON") from exc

    report = extract(name)
    if report.get("format") == "praxis-report-reference-v1":
        expected = {"format": "praxis-report-reference-v1", "document": f"reports/{name}"}
        if report != expected:
            raise PraxisError("INVALID_REPORT", "Report reference must select its fixed registered companion")
        report = extract(expected["document"])
        if report.get("format") == "praxis-report-reference-v1":
            raise PraxisError("INVALID_REPORT", "Nested report references are forbidden")
    return report
