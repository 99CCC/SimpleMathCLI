# SimpleMathCLI

A simple CLI app functioning as a calculator that shows you a human-like way to solve problems with printing out a step by step guide on how it solved the problem it was fed (Structured in a modular way for now).
Meaning that you will use the CLI to choose your operation.

---

## Features

- Interactive terminal
- Long-style math: step-by-step like on paper
- Modular folder structure for each math domain

---

## Folder Structure

```
SimpleMathCLI/
├── main.py                  # Entry point for CLI
├── menus/                   # Menu logic for each domain
│   └── basic_math_menu.py
├── basic_math/              
│   └── long_addition.py
├── algebra/                 # Coming soon
├── calculus/                # Coming soon
```

---

## How to Use

```bash
# Navigate to the project directory
cd SimpleMathCLI

# Run the main CLI
python main.py
```

Then just follow the recipe from terminal.

---

## Planned Topics

- [x] Long Addition
- [ ] Long Multiplication
- [ ] Long Division
- [ ] Algebra (solving equations with 1 unknown)
- [ ] Calculus (derivatives, integrals)
- [ ] Statistics & Probability
- [ ] Numeric Optimization

---


