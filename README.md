<div align="center">

# The Guessing Game • Heuristic CLI Number Search
### *Deterministic Random State Generation, Interactive CLI Game Loop & Binary Search Feedback Engine*

[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B_Standard_Library-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero_External_Overhead-success?style=for-the-badge)](https://docs.python.org/3/library/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Complexity: O(1) Memory](https://img.shields.io/badge/Memory_Footprint-O(1)_Constant-brightgreen?style=for-the-badge)](https://github.com/ExeDevCentral)

<p align="center">
  A clean, resilient Python CLI implementation of the classic bounded-range guessing game. Features resilient integer parsing, stateful life tracking, and directional binary-feedback hints.
</p>

</div>

---

## 🎯 Architecture & Design Highlights

- **Robust Input Sanitization:** Handles invalid non-numeric user inputs via exception traps (`try-except ValueError`) without terminating the game loop.
- **Directional State Heuristics:** Delivers immediate high/low feedback to assist the player in executing an intuitive binary search strategy.
- **Bounded Game Loop:** Tracks active life counters with deterministic termination upon goal convergence or budget exhaustion.
- **Pure Python 3 Standard Library:** Zero third-party dependencies; runs anywhere with Python 3 installed.

---

## 🚀 Quickstart & Execution

### Prerequisites
- Python 3.8 or higher installed on your system.

### Running the Game

```bash
# Clone the repository
git clone https://github.com/ExeDevCentral/The-Guessing-Game.git
cd The-Guessing-Game

# Run the game loop
python3 adivina_el_numero.py
```

---

## 📂 Repository Structure

```text
The-Guessing-Game/
├── adivina_el_numero.py   # Main CLI game loop and heuristic feedback logic
├── .gitignore             # Standard Python environment exclusions
└── README.md              # Technical documentation and specifications
```

---

## 👨‍💻 Author

**Exequiel Echevarria**
- GitHub: [@ExeDevCentral](https://github.com/ExeDevCentral)
