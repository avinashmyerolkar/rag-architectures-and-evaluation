# Contributing

Thank you for your interest in contributing! This project welcomes bug fixes, new notebooks, improved explanations, and additional retrieval techniques.

## Getting Started

1. Fork the repository and create a feature branch:
   ```bash
   git checkout -b feature/your-topic
   ```

2. Set up the environment:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Make your changes, then open a pull request against `main`.

## Notebook Guidelines

- One concept per notebook — keep them focused and self-contained
- Start every notebook with a markdown cell that covers: **What**, **Why**, and **When to use**
- End with a **Key Takeaways** section
- Use `python-dotenv` to load API keys — never hardcode credentials
- Clear all output before committing (`Kernel → Restart & Clear Output`)
- Keep cells runnable top-to-bottom without manual intervention

## Code Style

- Follow [PEP 8](https://pep8.org/)
- Use type hints in all `src/` Python files
- Run `black` and `isort` before committing:
  ```bash
  pip install black isort
  black src/ && isort src/
  ```

## Reporting Issues

Open a GitHub Issue with:
- Which module/notebook is affected
- Steps to reproduce
- Expected vs actual behavior
- Python version and relevant package versions (`pip freeze`)

## Pull Request Checklist

- [ ] Notebook output is cleared
- [ ] Code follows PEP 8
- [ ] No API keys or secrets in any file
- [ ] README updated if a new notebook was added
- [ ] PR description explains what changed and why
