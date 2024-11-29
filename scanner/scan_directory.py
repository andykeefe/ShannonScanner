#                        SCANNING OPERATION                           #
# ------------------------------------------------------------------- #

import os


def scan(path, automaton):
    results = {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            code = f.read()
    except UnicodeDecodeError:
        try:
            with open(path, 'r', encoding='latin-1') as f:
                code = f.read()
        except UnicodeDecodeError:
            print(f"File not scanned due to encoding problems: {path}")
            return results

    matches = {}
    for end_index, (category,algorithm, pattern) in automaton.iter(code):
        if category not in matches:
            matches[category] = {}
        if algorithm not in matches[category]:
            matches[category][algorithm] = []

        if pattern not in matches[category][algorithm]:
            matches[category][algorithm].append(pattern)
    if matches:
            results[path] = matches

    return results



def directory_analysis(directory, automaton):
    positives = {}
    extensions = {

        '.c', '.cpp', '.cxx', '.h', '.cc', '.hh', '.hpp', '.hxx', '.cppm', '.ixx',  # All possible C/C++ extensions
        '.py', '.pyw', '.pyz', '.pyi', '.pyc', '.pyd',                              # All possible Python extensions
        '.java', '.class', '.jar', '.jmode',                                        # All possible Java extensions
        '.js', '.cjs', '.mjs',                                                      # All possible JavaScript extensions
        '.rs', '.rlib',                                                             # All possible Rust extensions 
        '.rb', '.ru',                                                               # All possible Ruby extensions
        '.go',                                                                      # All possible Go extensions
        '.sh', '.zsh',                                                              # All possible Bash/Shell extensions
        '.cs', '.csx',                                                              # All possible C# extensions
        '.htm', '.html', '.css',                                                    # All possible HTML/CSS extensions
        '.sql',                                                                     # All possible SQL extensions
        '.ts', '.tsx', '.mts', '.cts',                                              # All possible TypeScript extensions
        '.php', '.phar', '.phtml', '.pht', '.phps',                                 # All possible PHP extensions
        '.kt', '.kts', '.kexe', 'klib',                                             # All possible Kotlin extensions
        '.lua',                                                                     # All possible Lua extensions
        '.dart',                                                                    # All possible Dart extensions
        '.swift', '.SWIFT',                                                         # All possible Swift extensions
        '.md'                                                                       # Markdown ext

    }

    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                path = os.path.join(root, file)
                match = scan(path, automaton)
                if match:
                    positives.update(match)
    return positives



