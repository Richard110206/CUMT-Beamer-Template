"""Check protected assets and common content-layer overrides (Python 3, stdlib only)."""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def asset_digest(path):
    data = path.read_bytes()
    # Git may check text out as CRLF on Windows and LF on other systems.
    if path.suffix == '.sty':
        data = data.replace(b'\r\n', b'\n')
    return hashlib.sha256(data).hexdigest()


def main():
    errors = []
    manifest = json.loads((ROOT / 'template-lock.json').read_text(encoding='utf-8'))
    for name, expected in manifest['sha256'].items():
        path = ROOT / name
        if not path.is_file():
            errors.append(f'Missing template asset: {name}')
        elif asset_digest(path) != expected:
            errors.append(f'Template asset changed: {name}')

    # Pass all content files explicitly when using a different entry or extra inputs.
    names = sys.argv[1:] or ['slide.tex', 'content.tex']
    sources = []
    forbidden = re.compile(
        r'\\(?:setbeamertemplate|addtobeamertemplate|defbeamertemplate\*?|'
        r'setbeamercolor\*?|setbeamerfont\*?|usetheme|useoutertheme|useinnertheme|'
        r'usecolortheme|usefonttheme|AtBeginSection|AtBeginSubsection|'
        r'beamertemplates?)[\s{\[]|'
        r'\\begin\s*\{frame\}\s*\[[^\]]*\bplain\b|'
        r'\\(?:renewcommand|def|let)\s*\{?\\CUMT(?!ThanksEnglish\b|ThanksChinese\b)'
    )
    for name in names:
        path = ROOT / name
        if not path.is_file():
            errors.append(f'Missing content file: {name}')
            continue
        source = re.sub(r'(?<!\\)%[^\n]*', '', path.read_text(encoding='utf-8'))
        sources.append(source)
        for match in forbidden.finditer(source):
            line = source.count('\n', 0, match.start()) + 1
            errors.append(f'Content-layer theme override: {name}:{line}: {match.group()}')
    combined = '\n'.join(sources)
    for pattern, label in [
        (r'\\usepackage\s*\{CUMT\}', 'CUMT package'),
        (r'\\usepackage\s*\{CUMT-campus\}', 'CUMT-campus package'),
        (r'\\CUMTMakeTitle\b', 'cover command'),
        (r'\\CUMTMakeThanks\b', 'closing command'),
        (r'\\section\s*\{', 'sections for navigation'),
    ]:
        if not re.search(pattern, combined):
            errors.append(f'Missing {label}')
    if errors:
        print('\n'.join(errors))
        return 1
    print('PASS: protected template assets and content entry checks.')
    print('Compile with XeLaTeX until references stabilize; visually check artwork, navigation and layout.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
