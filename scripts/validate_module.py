#!/usr/bin/env python3
"""Validate one module of the English lab: python scripts/validate_module.py 03

Your work lives in work/mNN/ (and journal/). The exercises and the answer keys live in content/mNN/.
The same script runs on your machine and in GitHub Actions.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Callable, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent))
import checks as C  # noqa: E402

ROOT = C.ROOT
Errors = List[str]


def content(module: str, name: str) -> Path:
    return ROOT / "content" / f"m{module}" / name


def work(module: str, name: str) -> Path:
    return ROOT / "work" / f"m{module}" / name


def need(path: Path) -> Errors:
    return [] if path.exists() else [f"missing file: {path.relative_to(ROOT)}"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def prose_checks(text: str, label: str, min_words: int = 8, max_spell: float = 0.04) -> Errors:
    return C.language_errors(text, label, min_words) + C.spelling_errors(text, label, max_spell)


# ── Modules ───────────────────────────────────────────────────────────────────────────────────

def m00() -> Errors:
    path = work("00", "about-me.md")
    if (errs := need(path)):
        return errs
    text = read(path)
    errors = prose_checks(text, "about-me.md", min_words=40)
    if C.word_count(text) > 150:
        errors.append("about-me.md: keep it under 150 words")
    return errors


def m01() -> Errors:
    path = work("01", "glossary.md")
    if (errs := need(path)):
        return errs
    terms = {m.group(1).lower() for m in re.finditer(r"^- \*\*([\w ]+)\*\*:", read(content("01", "terms.md")), re.M)}
    sections = C.parse_sections(read(path))
    errors: Errors = []
    examples: List[str] = []
    valid = 0
    for term, body in sections.items():
        key = term.strip().lower()
        if key not in terms:
            errors.append(f"glossary.md: '{term}' is not in content/m01/terms.md")
            continue
        pt = re.search(r"^pt:\s*(.+)$", body, re.M)
        ex = re.search(r"^example:\s*(.+)$", body, re.M)
        if not pt or len(pt.group(1).split()) < 1:
            errors.append(f"glossary.md: '{term}' needs a line 'pt: <meaning in Portuguese>'")
            continue
        if not ex or not re.search(rf"\b{re.escape(key)}\w*\b", ex.group(1), re.I):
            errors.append(f"glossary.md: '{term}' needs a line 'example: <English sentence that uses the word>'")
            continue
        if len(C.WORD_RE.findall(ex.group(1))) < 4:
            errors.append(f"glossary.md: the example for '{term}' is too short (at least 4 words)")
            continue
        examples.append(ex.group(1))
        valid += 1
    if valid < 25:
        errors.append(f"glossary.md: {valid} valid entries, need at least 25")
    if examples:
        errors += prose_checks("\n".join(examples), "glossary examples", min_words=40)
    return errors


def m02() -> Errors:
    errors = need(work("02", "answers.txt")) + need(work("02", "explanations.md"))
    if errors:
        return errors
    errors = C.quiz_errors("02", content("02", "quiz.keys"), work("02", "answers.txt"), "quiz", pass_ratio=0.85)
    keywords: Dict[str, List[str]] = json.loads(read(content("02", "keywords.json")))
    sections = C.parse_sections(read(work("02", "explanations.md")))
    all_text = []
    for eid, words_ in keywords.items():
        body = sections.get(eid, "")
        all_text.append(body)
        if C.word_count(body) < 8:
            errors.append(f"explanations.md: '## {eid}' needs at least 8 words")
        elif not any(k in body.lower() for k in words_):
            errors.append(f"explanations.md: '## {eid}' should mention one of: {', '.join(words_)}")
    return errors + prose_checks("\n".join(all_text), "explanations.md", min_words=60)


def m03() -> Errors:
    errors = need(work("03", "answers.txt")) + need(work("03", "summary.md"))
    if errors:
        return errors
    errors = C.quiz_errors("03", content("03", "quiz.keys"), work("03", "answers.txt"), "quiz", pass_ratio=0.85)
    text = read(work("03", "summary.md"))
    n = C.word_count(text)
    if not 25 <= n <= 70:
        errors.append(f"summary.md: {n} words, write between 25 and 70")
    keys = [k.strip() for k in read(content("03", "summary-keywords.txt")).splitlines() if k.strip()]
    hits = [k for k in keys if k in text.lower()]
    if len(hits) < 3:
        errors.append(f"summary.md: mention at least 3 key ideas from the README ({', '.join(keys)})")
    return errors + prose_checks(text, "summary.md", min_words=20)


def m04() -> Errors:
    path = work("04", "commits.txt")
    if (errs := need(path)):
        return errs
    keywords: Dict[str, List[str]] = json.loads(read(content("04", "keywords.json")))
    messages: Dict[str, str] = {}
    for line in read(path).splitlines():
        m = re.match(r"^\s*(S\d+)\s*:\s*(.+)$", line)
        if m:
            messages[m.group(1)] = m.group(2).strip()
    errors: Errors = []
    conventional = 0
    for sid, kws in keywords.items():
        msg = messages.get(sid)
        if not msg:
            errors.append(f"commits.txt: missing line '{sid}: <message>'")
            continue
        errors += C.commit_errors(msg, sid)
        if not any(k in msg.lower() for k in kws):
            errors.append(f"{sid}: the message should mention one of: {', '.join(kws)}")
        if re.match(r"^[a-z]+(\([\w\-./]+\))?!?:\s", msg):
            conventional += 1
    if conventional < 5:
        errors.append(f"commits.txt: use the 'type: subject' format in at least 5 messages (found {conventional})")
    return errors


def m05() -> Errors:
    path = work("05", "orders.py")
    if (errs := need(path)):
        return errs
    source = read(path)
    errors: Errors = []
    pt_words = {w.strip().lower() for w in read(content("05", "portuguese-words.txt")).splitlines() if w.strip()}
    tokens = {t.lower() for t in re.findall(r"[A-Za-zÀ-ÿ]+", source)}
    found = sorted(tokens & pt_words)
    if found:
        errors.append(f"orders.py: still has Portuguese words: {', '.join(found[:10])}")
    if C.ACCENT_RE.search(source):
        errors.append("orders.py: accented letters found in the code, comments or messages")
    comments = " ".join(re.findall(r"#\s*(.+)", source) + re.findall(r'"""(.*?)"""', source, re.S))
    if C.word_count(comments) < 12:
        errors.append("orders.py: keep or write English comments/docstrings (at least 12 words in total)")
    elif (lang := C.language_errors(comments, "comments", 8)):
        errors += lang
    env = dict(os.environ, PYTHONPATH=str(work("05", "").parent / "m05"), PYTHONDONTWRITEBYTECODE="1")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", str(content("05", "test_orders.py"))],
        cwd=ROOT, env=env, capture_output=True, text=True,
    )
    if result.returncode != 0:
        errors.append("tests failed:\n" + "\n".join(result.stdout.strip().splitlines()[-15:]))
    return errors


def _sectioned_docs(module: str, prefix: str, count: int, sections: List[str], min_words: int) -> Errors:
    errors: Errors = []
    texts: List[str] = []
    for i in range(1, count + 1):
        path = work(module, f"{prefix}-{i}.md")
        if (errs := need(path)):
            errors += errs
            continue
        text = read(path)
        texts.append(text)
        first = text.strip().splitlines()[0] if text.strip() else ""
        if not first.startswith("# ") or len(first) > 82:
            errors.append(f"{path.name}: first line must be '# <title>' with at most 80 characters")
        found = C.parse_sections(text)
        for name in sections:
            body = found.get(name)
            if body is None:
                errors.append(f"{path.name}: missing section '## {name}'")
            elif C.word_count(body) < min_words:
                errors.append(f"{path.name}: section '{name}' needs at least {min_words} words")
    if texts:
        errors += prose_checks("\n".join(texts), f"{prefix} files", min_words=40)
    return errors


def m06() -> Errors:
    errors = _sectioned_docs("06", "bug", 3, ["Steps to reproduce", "Expected behavior", "Actual behavior", "Environment"], 4)
    for i in range(1, 4):
        path = work("06", f"bug-{i}.md")
        if path.exists():
            steps = re.findall(r"^\s*\d+\.\s+\S+", C.parse_sections(read(path)).get("Steps to reproduce", ""), re.M)
            if len(steps) < 3:
                errors.append(f"bug-{i}.md: 'Steps to reproduce' needs at least 3 numbered steps")
    return errors


def m07() -> Errors:
    errors = _sectioned_docs("07", "pr", 2, ["What", "Why", "How to test", "Notes"], 6)
    for i in range(1, 3):
        path = work("07", f"pr-{i}.md")
        if path.exists():
            body = C.parse_sections(read(path)).get("How to test", "")
            items = re.findall(r"^\s*(?:- \[[ x]\]|\d+\.)\s+\S+", body, re.M)
            if len(items) < 2:
                errors.append(f"pr-{i}.md: 'How to test' needs at least 2 steps (a numbered list or '- [ ]' items)")
    return errors


SOFT = ["could", "would", "maybe", "perhaps", "what do you think", "suggest", "consider", "i think", "might", "how about", "please", "nit:"]
HARSH = ["stupid", "wrong", "terrible", "awful", "obviously", "idiot", "bad code", "lazy", "useless"]
PRAISE = ["nice", "good", "great", "thanks", "thank you", "well done", "clean", "love"]


def m08() -> Errors:
    errors = need(work("08", "answers.txt")) + need(work("08", "review.md"))
    if errors:
        return errors
    errors = C.quiz_errors("08", content("08", "quiz.keys"), work("08", "answers.txt"), "quiz", pass_ratio=0.85)
    text = read(work("08", "review.md"))
    sections = C.parse_sections(text)
    for i in range(1, 6):
        body = sections.get(f"S{i}", "")
        n = C.word_count(body)
        low = body.lower()
        if not 8 <= n <= 60:
            errors.append(f"review.md: '## S{i}' has {n} words, write between 8 and 60")
        elif not any(s in low for s in SOFT):
            errors.append(f"review.md: '## S{i}' should sound polite (use words like could, maybe, what do you think)")
        if any(h in low for h in HARSH):
            errors.append(f"review.md: '## S{i}' sounds harsh. Criticize the code, not the person.")
    low_all = text.lower()
    if "nit:" not in low_all:
        errors.append("review.md: use the label 'nit:' at least once for a small suggestion")
    if not any(p in low_all for p in PRAISE):
        errors.append("review.md: include at least one positive comment (nice, good, great, thanks)")
    return errors + prose_checks(text, "review.md", min_words=40)


CONNECTORS = ["first", "then", "next", "after", "finally", "because", "so", "if", "when", "otherwise", "also", "before"]


def m09() -> Errors:
    path = work("09", "explanations.md")
    if (errs := need(path)):
        return errs
    source = read(content("09", "functions.py"))
    funcs = re.findall(r"^def (\w+)\(", source, re.M)
    sections = C.parse_sections(read(path))
    errors: Errors = []
    texts: List[str] = []
    for fn in funcs:
        body = sections.get(fn)
        if body is None:
            errors.append(f"explanations.md: missing section '## {fn}'")
            continue
        texts.append(body)
        n = len(C.sentences(body))
        if not 3 <= n <= 6:
            errors.append(f"explanations.md: '{fn}' has {n} sentences, write 3 to 6")
        used = {c for c in CONNECTORS if re.search(rf"\b{c}\b", body.lower())}
        if len(used) < 2:
            errors.append(f"explanations.md: '{fn}' needs at least 2 connectors ({', '.join(CONNECTORS[:6])}...)")
        errors += C.readability_errors(body, f"'{fn}'", 10.0)
    return errors + (prose_checks("\n".join(texts), "explanations.md", min_words=50) if texts else [])


def m10() -> Errors:
    errors = need(work("10", "answers.txt")) + need(work("10", "sentences.md"))
    if errors:
        return errors
    errors = C.quiz_errors("10", content("10", "quiz.keys"), work("10", "answers.txt"), "cloze", pass_ratio=0.85)
    forms: Dict[str, List[str]] = json.loads(read(content("10", "verbs.json")))
    used = set()
    texts = []
    for line in read(work("10", "sentences.md")).splitlines():
        m = re.match(r"^\s*([a-z ]+?)\s*\|\s*(.+)$", line)
        if not m or m.group(1) not in forms:
            continue
        verb, sentence = m.group(1), m.group(2)
        if len(C.WORD_RE.findall(sentence)) < 6:
            errors.append(f"sentences.md: the sentence for '{verb}' needs at least 6 words")
        elif not any(re.search(rf"\b{re.escape(f)}\b", sentence.lower()) for f in forms[verb]):
            errors.append(f"sentences.md: the sentence for '{verb}' does not use the verb")
        else:
            used.add(verb)
            texts.append(sentence)
    if len(used) < 8:
        errors.append(f"sentences.md: {len(used)} valid verbs, need 8 (format: 'verb | sentence')")
    return errors + (prose_checks("\n".join(texts), "sentences.md", min_words=30) if texts else [])


PAST = re.compile(r"\b(\w+ed|wrote|made|built|fixed|did|ran|merged|found|read|sent|had|got|took|began|left|put|set)\b", re.I)
FUTURE = re.compile(r"\b(will|going to|plan to|today i|i am|i'm|i can|need to|want to|start|continue|finish)\b", re.I)


def m11() -> Errors:
    path = work("11", "updates.md")
    if (errs := need(path)):
        return errs
    sections = C.parse_sections(read(path))
    errors: Errors = []
    texts = []
    for i in range(1, 6):
        body = sections.get(f"Day {i}")
        if body is None:
            errors.append(f"updates.md: missing section '## Day {i}'")
            continue
        texts.append(body)
        parts = {k: (re.search(rf"^{k}:\s*(.+)$", body, re.M | re.I) or [None, ""])[1] for k in ("Yesterday", "Today", "Blockers")}
        for k, v in parts.items():
            if not v.strip():
                errors.append(f"updates.md: Day {i} needs a line '{k}: ...'")
        if parts["Yesterday"] and not PAST.search(parts["Yesterday"]):
            errors.append(f"updates.md: Day {i} 'Yesterday' should use the past tense (fixed, wrote, finished...)")
        if parts["Today"] and not FUTURE.search(parts["Today"]):
            errors.append(f"updates.md: Day {i} 'Today' should talk about plans (I will..., I am going to...)")
        if parts["Blockers"] and not re.match(r"^(none|no blockers?)", parts["Blockers"].strip(), re.I) and C.word_count(parts["Blockers"]) < 6:
            errors.append(f"updates.md: Day {i} 'Blockers' says 'None' or explains the problem in 6+ words")
        n = C.word_count(body)
        if not 20 <= n <= 90:
            errors.append(f"updates.md: Day {i} has {n} words, write between 20 and 90")
    return errors + (prose_checks("\n".join(texts), "updates.md", min_words=60) if texts else [])


def m12() -> Errors:
    path = work("12", "article.md")
    if (errs := need(path)):
        return errs
    text = read(path)
    errors: Errors = []
    if not re.match(r"^# .+", text.strip()):
        errors.append("article.md: start with a title line '# Title'")
    heads = [h for h in re.findall(r"^## (.+)$", text, re.M)]
    if len(heads) < 4:
        errors.append(f"article.md: use at least 4 '##' headings (found {len(heads)}), including 'Conclusion'")
    if not any(h.lower().startswith("conclusion") for h in heads):
        errors.append("article.md: add a '## Conclusion' section")
    if "```" not in text:
        errors.append("article.md: include at least one code block")
    n = C.word_count(text)
    if not 300 <= n <= 500:
        errors.append(f"article.md: {n} words, write between 300 and 500")
    errors += C.readability_errors(text, "article.md", 11.0)
    return errors + prose_checks(text, "article.md", min_words=100, max_spell=0.03)


def m13() -> Errors:
    path = work("13", "answers.md")
    if (errs := need(path)):
        return errs
    sections = C.parse_sections(read(path))
    errors: Errors = []
    texts = []
    for i in range(1, 5):
        body = sections.get(f"Q{i}")
        if body is None:
            errors.append(f"answers.md: missing section '## Q{i}'")
            continue
        texts.append(body)
        for label in ("Situation", "Task", "Action", "Result"):
            m = re.search(rf"^{label}:\s*(.+)$", body, re.M)
            if not m or C.word_count(m.group(1)) < 12:
                errors.append(f"answers.md: Q{i} needs a '{label}:' line with at least 12 words")
        if C.word_count(body) < 90:
            errors.append(f"answers.md: Q{i} has {C.word_count(body)} words, write at least 90")
        if len(re.findall(r"\bI\b", body)) < 5:
            errors.append(f"answers.md: Q{i} should say what YOU did (use 'I' at least 5 times)")
        result = re.search(r"^Result:\s*(.+)$", body, re.M)
        if result and not re.search(r"\d", result.group(1)):
            errors.append(f"answers.md: Q{i} 'Result' needs a number (time saved, percent, users...)")
    return errors + (prose_checks("\n".join(texts), "answers.md", min_words=120) if texts else [])


def m14() -> Errors:
    errors: Errors = []
    path = work("14", "evidence.md")
    if (errs := need(path)):
        errors += errs
    else:
        text = read(path)
        if not re.search(r"https://github\.com/[\w.-]+/[\w.-]+/(issues|pull)/\d+", text):
            errors.append("evidence.md: add the link of your issue or pull request (https://github.com/owner/repo/issues/123)")
        if C.word_count(text) < 120:
            errors.append(f"evidence.md: write a reflection of at least 120 words (now {C.word_count(text)})")
        errors += prose_checks(text, "evidence.md", min_words=60)
    days: List[date] = []
    bad = 0
    for f in sorted((ROOT / "journal").glob("*.md")):
        m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", f.stem)
        if not m:
            continue
        text = read(f)
        if C.word_count(text) < 25 or C.language_errors(text, f.name, 20):
            bad += 1
            continue
        days.append(date(int(m.group(1)), int(m.group(2)), int(m.group(3))))
    streak = C.longest_streak(days)
    if streak < 14:
        errors.append(f"journal/: longest streak is {streak} day(s), need 14 consecutive days (25+ English words each; {bad} entries rejected)")
    return errors


MODULES: Dict[str, Callable[[], Errors]] = {
    "00": m00, "01": m01, "02": m02, "03": m03, "04": m04, "05": m05, "06": m06, "07": m07,
    "08": m08, "09": m09, "10": m10, "11": m11, "12": m12, "13": m13, "14": m14,
}


def main(argv: List[str]) -> int:
    if len(argv) != 2 or argv[1] not in MODULES:
        print("usage: python scripts/validate_module.py NN   (00 to 14)", file=sys.stderr)
        return 2
    module = argv[1]
    print(f"▶ Module {module}")
    errors = MODULES[module]()
    if errors:
        for e in errors:
            print(f"✘ {e}")
        print(f"✘ Module {module} is not done yet.")
        return 1
    print(f"✔ Module {module} done.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
