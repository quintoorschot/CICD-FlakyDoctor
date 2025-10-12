# 🚀 FlakyDoctor CI/CD

Integrate FlakyDoctor into the CI/CD pipeline to automatically detect and fix flaky tests.

### 🧩 Prerequisites

This integration requires the following:

- **🐍 Python**: 3.10.12  
- **☕ Java**: 8 and 11  
- **🔧 Maven**: 3.6.3
- **🤖 OpenAI API Key**: Required for accessing OpenAI services

### ⚙️ Installation
[FlakyDoctor CI/CD](https://github.com/quintoorschot/CICD-FlakyDoctor) is directly usable in your [GitHub Actions workflows](https://docs.github.com/en/actions/how-tos/write-workflows), no local setup required.

**1. Add to your workflow**

Create (or edit) a workflow file, for example:
``` yml
name: FlakyDoctor

on:
  pull_request:
  push:

jobs:
  flakydoctor:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run FlakyDoctor
        uses: quintoorschot/CICD-FlakyDoctor@v1

```

**2.**

.........


### 🧭 Usage
tbd

### 🧪 Example workflow output


### 📚 Reference

This work is part of my **Bachelor's Thesis in Computer Science** at [Radboud University](https://www.ru.nl/) in collaboration with [Sogeti](https://www.sogeti.nl/) (part of [Capgemini](https://www.capgemini.com)).
- 📝 *My Thesis Paper*: *(to be added)* 

Based on the paper *“Neurosymbolic Repair of Test Flakiness”* (ISSTA 2024) by **Yang Chan et al.**  
- 📄 [ACM Paper](https://dl.acm.org/doi/10.1145/3650212.3680369)  
- 💻 [FlakyDoctor Repository](https://github.com/Intelligent-CAT-Lab/FlakyDoctor)

### 🧠 Citation
For citing FlakyDoctor CI/CD and the corresponding paper, you can use:
```
@misc{vanoorschot2025flakydoctor,
  author       = {Quint van Oorschot},
  title        = {FlakyDoctor CI/CD: Automated Detection and Repair of Flaky Tests},
  year         = {2025},
  howpublished = {\url{https://github.com/quintoorschot/CICD-FlakyDoctor}}
}
```

<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFv-XbvBJJdW8p1lgMioZvG4ypX46VVoYIrg&s" alt="Radboud University Logo" width="20%"/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNYyQeJ-hmVjvrWS2an2tsnddCQvqsDu93uw&s" alt="Sogeti logo" width="35%"/>
</p>