"""Tests for the validators themselves. If these fail, the lab is broken (not your English)."""
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import checks as C  # noqa: E402


def test_english_text_passes_language_check():
    text = "I fixed the bug in the login form and I wrote two tests for it today."
    assert C.language_errors(text, "t") == []


def test_portuguese_text_fails_language_check():
    text = "Eu corrigi o erro no formulário de login e não escrevi os testes para isso hoje."
    assert C.language_errors(text, "t")


def test_too_short_text_fails():
    assert "too short" in C.language_errors("Hello there", "t")[0]


def test_code_and_urls_are_ignored():
    text = "See `calcular_total` and https://example.com/pedido for the code.\n```py\nnão = 1\n```"
    assert "não" not in C.words(text)
    assert "calcular" not in C.words(text)


def test_commit_messages():
    assert C.commit_errors("feat: add login button", "c") == []
    assert C.commit_errors("fix(auth): handle empty name", "c") == []
    assert any("imperative" in e for e in C.commit_errors("added a login button", "c"))
    assert any("period" in e for e in C.commit_errors("fix: handle empty name.", "c"))
    assert any("72" in e for e in C.commit_errors("fix: " + "a " * 40, "c"))
    assert any("unknown type" in e for e in C.commit_errors("feature: add button", "c"))


def test_quiz_hash_is_stable_and_case_insensitive():
    assert C.key_hash("02", "q1", "B") == C.key_hash("02", "q1", "b")
    assert C.key_hash("02", "q1", "a") != C.key_hash("02", "q1", "b")
    assert C.key_hash("02", "q1", "a") != C.key_hash("03", "q1", "a")


def test_streak():
    days = [date(2026, 1, d) for d in (1, 2, 3, 5, 6, 7, 8, 9)]
    assert C.longest_streak(days) == 5
    assert C.longest_streak([]) == 0
    assert C.longest_streak([date(2026, 1, 1), date(2026, 1, 1)]) == 1


def test_readability_orders_texts():
    easy = "I like code. It is fun. I write tests. They help me."
    hard = "Notwithstanding considerable organizational complexity, interdisciplinary collaboration necessitates comprehensive documentation."
    assert C.fk_grade(easy) < C.fk_grade(hard)


def test_parse_sections():
    text = "# T\n\n## A\none\ntwo\n\n## B\nthree\n"
    assert C.parse_sections(text) == {"A": "one\ntwo", "B": "three"}


def test_spelling_catches_typos():
    bad = "The progrm has a bugg in the functon that read the fille."
    assert C.spelling_errors(bad, "t", max_rate=0.1)
    good = "The program has a bug in the function that reads the file."
    assert C.spelling_errors(good, "t") == []
