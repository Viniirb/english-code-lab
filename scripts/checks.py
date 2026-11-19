"""Reusable checks for the English lab. Standard library only, plus `pyspellchecker` for spelling.

Everything here is a heuristic. It cannot prove your English is good: it catches the common problems
(wrong language, typos, missing parts, robotic structure). For real feedback, use the tutor prompt in docs/TUTOR.md.
"""
from __future__ import annotations

import hashlib
import re
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent

EN_STOP = set(
    """the be to of and a in that have i it for not on with he as you do at this but his by from they we say her
    she or an will my one all would there their what so up out if about who get which go me when make can like
    time no just him know take people into year your good some could them see other than then now look only come
    its over think also back after use two how our work first well way even new want because any these give day
    most us is are was were been has had did does am""".split()
)

# Portuguese words that are NOT also English words, so they work as a "wrong language" signal.
PT_STOP = set(
    """não uma para com dos das você são está isso então mas muito também pelo pela já até quando onde porque
    sobre entre depois sem mesmo ainda seu sua seus suas nosso nossa ele ela eles elas meu minha foi será temos
    tenho tem tinha fazer feito olá""".split()
)

WORD_RE = re.compile(r"[A-Za-zÀ-ÿ]+(?:'[A-Za-z]+)?")
ACCENT_RE = re.compile(r"[À-ÿ]")


# ── Text preparation ──────────────────────────────────────────────────────────────────────────

def strip_code(text: str) -> str:
    """Remove fenced code blocks, inline code, URLs and Markdown markers so only prose is analysed."""
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"^[#>\-*\d.\s]+", " ", text, flags=re.M)
    return text


def words(text: str) -> List[str]:
    return [w.lower() for w in WORD_RE.findall(strip_code(text))]


def sentences(text: str) -> List[str]:
    parts = re.split(r"(?<=[.!?])\s+", strip_code(text).strip())
    return [p for p in parts if len(WORD_RE.findall(p)) >= 2]


# ── Language ──────────────────────────────────────────────────────────────────────────────────

def language_errors(text: str, label: str, min_words: int = 8) -> List[str]:
    ws = words(text)
    if len(ws) < min_words:
        return [f"{label}: too short ({len(ws)} words, need at least {min_words})"]
    en = sum(1 for w in ws if w in EN_STOP) / len(ws)
    pt = sum(1 for w in ws if w in PT_STOP) / len(ws)
    accents = sum(len(ACCENT_RE.findall(w)) for w in ws) / max(1, sum(len(w) for w in ws))
    errors: List[str] = []
    if en < 0.2:
        errors.append(f"{label}: does not look like English (only {en:.0%} common English words)")
    if pt > 0.03:
        errors.append(f"{label}: Portuguese words found ({pt:.0%} of the words). Write in English.")
    if accents > 0.01:
        errors.append(f"{label}: accented letters found. English does not use them.")
    return errors


# ── Spelling ──────────────────────────────────────────────────────────────────────────────────

_ALLOW: Optional[Set[str]] = None


def allowlist() -> Set[str]:
    global _ALLOW
    if _ALLOW is None:
        path = ROOT / "scripts" / "allowlist.txt"
        _ALLOW = {l.strip().lower() for l in path.read_text().splitlines() if l.strip() and not l.startswith("#")}
    return _ALLOW


def spelling_errors(text: str, label: str, max_rate: float = 0.04) -> List[str]:
    try:
        from spellchecker import SpellChecker
    except ImportError:  # pragma: no cover
        return [f"{label}: install the spell checker first: pip install -r requirements.txt"]
    ws = [w for w in words(text) if len(w) > 2 and "'" not in w]
    if not ws:
        return []
    spell = SpellChecker()
    unknown = [w for w in ws if w in (spell.unknown(ws) - allowlist())]
    rate = len(unknown) / len(ws)
    if rate > max_rate:
        sample = ", ".join(sorted(set(unknown))[:8])
        return [f"{label}: possible spelling mistakes ({rate:.0%}): {sample}"]
    return []


# ── Readability ───────────────────────────────────────────────────────────────────────────────

def syllables(word: str) -> int:
    word = word.lower()
    count = len(re.findall(r"[aeiouy]+", word))
    if word.endswith("e") and not word.endswith("le") and count > 1:
        count -= 1
    return max(1, count)


def fk_grade(text: str) -> float:
    """Flesch-Kincaid grade level. Lower is easier. Around 6 to 9 is good for technical writing."""
    ss = sentences(text)
    ws = words(text)
    if not ss or not ws:
        return 0.0
    return 0.39 * len(ws) / len(ss) + 11.8 * sum(syllables(w) for w in ws) / len(ws) - 15.59


def readability_errors(text: str, label: str, max_grade: float) -> List[str]:
    grade = fk_grade(text)
    if grade > max_grade:
        return [f"{label}: too hard to read (grade {grade:.1f}, limit {max_grade}). Use shorter sentences."]
    return []


# ── Commit messages ───────────────────────────────────────────────────────────────────────────

COMMIT_TYPES = {"feat", "fix", "docs", "style", "refactor", "perf", "test", "build", "ci", "chore", "revert"}

VERBS = set(
    """add allow apply avoid bump change check clean clarify close configure convert correct create define delete
    deploy disable document drop enable ensure extract fix handle hide implement improve include increase initialize
    introduce limit load make merge migrate move normalize optimize organize parse prevent print profile publish
    raise read rebuild reduce refactor remove rename replace reset resolve restore return reuse revert rewrite run
    save send set show simplify skip sort speed split start stop store support switch sync test throw track
    translate trim tweak update upgrade use validate verify wrap write bypass cache cover expose format group
    log mark notify pin polish prepare retry scale speed tidy unify upload warn""".split()
)


def commit_errors(line: str, label: str) -> List[str]:
    errors: List[str] = []
    subject = line.strip()
    m = re.match(r"^([a-z]+)(\([\w\-./]+\))?!?:\s+(.*)$", subject)
    if m:
        if m.group(1) not in COMMIT_TYPES:
            errors.append(f"{label}: unknown type '{m.group(1)}' (use one of {', '.join(sorted(COMMIT_TYPES))})")
        subject = m.group(3)
    if not subject:
        return errors + [f"{label}: empty subject"]
    if len(line.strip()) > 72:
        errors.append(f"{label}: longer than 72 characters")
    if subject.endswith("."):
        errors.append(f"{label}: do not end the subject with a period")
    first = subject.split()[0].lower()
    if first not in VERBS:
        errors.append(f"{label}: start with an imperative verb like 'add' or 'fix' (not '{first}')")
    return errors


# ── Quizzes with hashed answer keys ───────────────────────────────────────────────────────────

def key_hash(module: str, question: str, letter: str) -> str:
    return hashlib.sha256(f"{module}:{question}:{letter.lower()}".encode()).hexdigest()


def read_keys(path: Path) -> Dict[str, str]:
    keys: Dict[str, str] = {}
    for line in path.read_text().splitlines():
        if line.strip() and not line.startswith("#"):
            q, h = line.split()
            keys[q] = h
    return keys


def read_answers(path: Path) -> Dict[str, str]:
    answers: Dict[str, str] = {}
    for line in path.read_text().splitlines():
        m = re.match(r"^\s*(q\d+)\s*[:=]\s*([a-dA-D])\s*$", line)
        if m:
            answers[m.group(1).lower()] = m.group(2).lower()
    return answers


def quiz_errors(module: str, keys_path: Path, answers_path: Path, label: str, pass_ratio: float = 1.0) -> List[str]:
    if not answers_path.exists():
        return [f"{label}: missing file {answers_path.relative_to(ROOT)}"]
    keys = read_keys(keys_path)
    answers = read_answers(answers_path)
    missing = [q for q in keys if q not in answers]
    wrong = [q for q, h in keys.items() if q in answers and key_hash(module, q, answers[q]) != h]
    errors: List[str] = []
    if missing:
        errors.append(f"{label}: unanswered questions: {', '.join(missing)}")
    correct = len(keys) - len(missing) - len(wrong)
    if correct / len(keys) < pass_ratio:
        errors.append(f"{label}: {correct}/{len(keys)} correct. Wrong: {', '.join(wrong) or 'none'}. Read the text again.")
    return errors


# ── Streak ────────────────────────────────────────────────────────────────────────────────────

def longest_streak(days: Iterable[date]) -> int:
    ordered = sorted(set(days))
    best = run = 0
    prev: Optional[date] = None
    for d in ordered:
        run = run + 1 if prev is not None and d - prev == timedelta(days=1) else 1
        best = max(best, run)
        prev = d
    return best


def parse_sections(text: str, marker: str = "## ") -> Dict[str, str]:
    """Split Markdown into {heading: body} for headings that start with `marker`."""
    result: Dict[str, str] = {}
    current: Optional[str] = None
    buf: List[str] = []
    for line in text.splitlines():
        if line.startswith(marker):
            if current is not None:
                result[current] = "\n".join(buf).strip()
            current = line[len(marker):].strip()
            buf = []
        elif current is not None:
            buf.append(line)
    if current is not None:
        result[current] = "\n".join(buf).strip()
    return result


def word_count(text: str) -> int:
    return len(words(text))
