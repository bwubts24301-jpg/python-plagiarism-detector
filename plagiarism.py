"""Source Code Plagiarism Detection using Token Streams (Python files).

Usage:  python plagiarism.py <folder>
"""
import sys, os, io, ast, csv, keyword, tokenize, itertools
from difflib import SequenceMatcher

N = 5  # n-gram size


# ---------- 1. Tokenizer + normalization ----------
def get_tokens(code):
    out = []
    try:
        for t in tokenize.generate_tokens(io.StringIO(code).readline):
            if t.type == tokenize.NAME:
                out.append(t.string if keyword.iskeyword(t.string) else "ID")
            elif t.type == tokenize.NUMBER:
                out.append("NUM")
            elif t.type == tokenize.STRING:
                out.append("STR")
            elif t.type == tokenize.OP:
                out.append(t.string)
            # comments, newlines, indents are ignored
    except (tokenize.TokenError, IndentationError, SyntaxError):
        pass
    return out


# ---------- 2. Token matching (n-gram Jaccard) ----------
def ngrams(tokens, n=N):
    return {tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)}


def token_similarity(t1, t2):
    a, b = ngrams(t1), ngrams(t2)
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b)


# ---------- 3. AST comparison ----------
def ast_sequence(code):
    try:
        return [type(n).__name__ for n in ast.walk(ast.parse(code))]
    except SyntaxError:
        return []


def ast_similarity(s1, s2):
    if not s1 or not s2:
        return 0.0
    return SequenceMatcher(None, s1, s2).ratio()


# ---------- 4. Combine + report ----------
def label(score):
    if score >= 80:
        return "HIGH (likely plagiarism)"
    if score >= 50:
        return "MEDIUM (suspicious)"
    return "LOW"


def main(folder):
    files = sorted(f for f in os.listdir(folder) if f.endswith(".py"))
    data = {}
    for f in files:
        with open(os.path.join(folder, f), encoding="utf-8", errors="ignore") as fh:
            code = fh.read()
        data[f] = (get_tokens(code), ast_sequence(code))

    results = []
    for a, b in itertools.combinations(files, 2):
        ts = token_similarity(data[a][0], data[b][0])
        as_ = ast_similarity(data[a][1], data[b][1])
        final = (0.5 * ts + 0.5 * as_) * 100
        results.append((a, b, round(ts * 100, 1), round(as_ * 100, 1), round(final, 1)))

    results.sort(key=lambda r: r[4], reverse=True)

    print(f"{'File A':20} {'File B':20} {'Token%':>7} {'AST%':>7} {'Final%':>7}  Verdict")
    print("-" * 80)
    for a, b, ts, as_, fin in results:
        print(f"{a:20} {b:20} {ts:7} {as_:7} {fin:7}  {label(fin)}")

    with open("report.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["File A", "File B", "Token %", "AST %", "Final %", "Verdict"])
        for a, b, ts, as_, fin in results:
            w.writerow([a, b, ts, as_, fin, label(fin)])
    print("\nSaved report.csv")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python plagiarism.py <folder>")
        sys.exit(1)
    main(sys.argv[1])
