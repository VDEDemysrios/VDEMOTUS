import sys, unicodedata, re, random

def strip(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.upper()) if unicodedata.category(c) != 'Mn')

def load(path):
    words = set()
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            w = strip(line.strip())
            if re.match(r'^[A-Z]+$', w) and 5 <= len(w) <= 9:
                words.add(w)
    return words

random.seed(42)
all_words = load(sys.argv[1])
solutions = {w for w in all_words if not re.search(r'(.)\1\1', w)}
by_len = {}
for w in solutions:
    by_len.setdefault(len(w), []).append(w)
final = set()
for l in range(5, 10):
    ws = by_len.get(l, [])
    final.update(random.sample(ws, min(2500, len(ws))) if len(ws) > 2500 else ws)

with open('motsSolutions.js', 'w', encoding='utf-8') as f:
    f.write('const SOLUTIONS = [\n')
    for i, w in enumerate(sorted(final, key=lambda w: (len(w), w))):
        f.write(f'"{w}"{"," if i < len(final)-1 else ""}\n')
    f.write('];\n')

with open('motsProposables.js', 'w', encoding='utf-8') as f:
    f.write('const PROPOSABLES = new Set([\n')
    sl = sorted(all_words, key=lambda w: (len(w), w))
    for i, w in enumerate(sl):
        f.write(f'"{w}"{"," if i < len(sl)-1 else ""}\n')
    f.write(']);\n')

print(f"SOLUTIONS: {len(final)} mots")
print(f"PROPOSABLES: {len(all_words)} mots")
```

Puis dans le terminal :
```
python generer_mots.py liste.de.mots.francais.frgut.txt