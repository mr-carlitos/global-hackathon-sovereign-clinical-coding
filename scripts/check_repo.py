"""Offline repository checks, not runtime privacy or clinical validation."""

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def fields(value: object, expected: set[str], label: str) -> dict:
    require(isinstance(value, dict), f"{label}: expected object")
    require(set(value) == expected, f"{label}: missing or unknown fields")
    return value


def text(value: object, label: str) -> str:
    require(isinstance(value, str) and bool(value.strip()), f"{label}: expected text")
    return value


def https_url(value: object, label: str) -> None:
    url = urlsplit(text(value, label))
    require(
        url.scheme == "https" and bool(url.hostname)
        and url.username is None and url.password is None,
        f"{label}: expected credential-free HTTPS URL",
    )


def validate_pack(value: object) -> str:
    """Reject incomplete, permissive or unknown design contracts."""
    pack = fields(value, {
        "schema_version", "id", "country", "locales", "status", "clinical_use",
        "coding", "catalog", "boundary",
    }, "pack")
    require(type(pack["schema_version"]) is int and pack["schema_version"] == 1,
            "schema_version: expected integer 1")
    pack_id = text(pack["id"], "id")
    require(re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", pack_id) is not None,
            "id: invalid identifier")
    country = text(pack["country"], "country")
    require(re.fullmatch(r"[A-Z]{2}", country) is not None, "country: expected two letters")
    locales = pack["locales"]
    require(isinstance(locales, list) and bool(locales), "locales: expected nonempty list")
    for locale in locales:
        require(re.fullmatch(r"[a-z]{2,3}-[A-Z]{2}", text(locale, "locale")) is not None,
                "locale: expected language-country tag")
    require(len(set(locales)) == len(locales), "locales: duplicates")
    require(pack["status"] == "design_only", "status: design_only required")
    require(pack["clinical_use"] is False, "clinical_use: must be false")

    coding = fields(pack["coding"], {
        "task", "care_setting", "system", "edition", "effective_from",
        "effective_to", "applicability",
    }, "coding")
    require(coding["task"] == "diagnosis", "task: diagnosis-only MVP")
    for key in ("care_setting", "system", "edition"):
        text(coding[key], f"coding.{key}")
    dates = []
    for key in ("effective_from", "effective_to"):
        raw = text(coding[key], f"coding.{key}")
        require(re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw) is not None,
                f"coding.{key}: expected YYYY-MM-DD")
        dates.append(date.fromisoformat(raw))
    require(dates[0] <= dates[1], "coding: reversed effective dates")
    require(coding["applicability"] == "operator_verification_required",
            "coding: applicability requires verification")

    catalog = fields(pack["catalog"], {
        "publisher", "source_url", "terms_url", "review_status", "redistribute",
    }, "catalog")
    text(catalog["publisher"], "catalog.publisher")
    for key in ("source_url", "terms_url"):
        https_url(catalog[key], f"catalog.{key}")
    require(catalog["review_status"] == "operator_review_required",
            "catalog: operator review required")
    require(catalog["redistribute"] is False, "catalog: redistribution forbidden")

    boundary = fields(pack["boundary"], {
        "synthetic_only", "identity_location", "failure_mode", "cloud_egress",
    }, "boundary")
    require(boundary["synthetic_only"] is True, "boundary: synthetic data only")
    require(boundary["identity_location"] == "hospital_local", "boundary: identity must stay local")
    require(boundary["failure_mode"] == "block", "boundary: failures must block")
    require(boundary["cloud_egress"] == "not_authorized", "boundary: design packs cannot authorize egress")
    return pack_id


def unique_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f"JSON: duplicate key {key}")
        result[key] = value
    return result


def check_packs(directory: Path) -> int:
    paths = sorted(directory.glob("*.json"))
    require(bool(paths), "no packs found")
    ids = set()
    for path in paths:
        try:
            pack_id = validate_pack(json.loads(path.read_text(), object_pairs_hook=unique_keys))
            require(pack_id not in ids, f"duplicate pack id: {pack_id}")
            require(path.stem == pack_id, f"filename must match pack id: {pack_id}")
        except ValueError as error:
            raise ValueError(f"{path.name}: {error}") from error
        ids.add(pack_id)
    return len(paths)


def check_links(root: Path) -> int:
    """Check simple inline local Markdown file links, not external URLs/anchors."""
    paths = [root / "README.md", root / "CONTRIBUTING.md", root / "AGENTS.md"]
    paths += sorted((root / "docs").glob("*.md"))
    count = 0
    for path in paths:
        for target in re.findall(r"\[[^\]]+\]\(([^)\s]+)\)", path.read_text()):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            linked = (path.parent / unquote(url.path)).resolve()
            require(linked.is_relative_to(root.resolve()), f"{path.name}: link escapes repository")
            require(linked.exists(), f"{path.name}: broken link {target}")
            count += 1
    return count


def main() -> int:
    try:
        packs = check_packs(ROOT / "packs")
        links = check_links(ROOT)
    except (ValueError, OSError) as error:
        print(f"Repository check failed: {error}", file=sys.stderr)
        return 1
    print(f"Validated {packs} design packs and {links} local documentation links.")
    print("No clinical, privacy, licensing or deployment approval is implied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
