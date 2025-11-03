# 🚀 FlakyDoctor CI/CD

Integrate FlakyDoctor into the CI/CD pipeline to automatically detect and fix flaky tests.

### ⚠️ Note:
The current implementation of FlakyDoctor CI/CD only aims to detect and patch implementation-dependent (ID) flakiness in test suites.

### 🧩 Prerequisites

This integration requires the following:

- **🐍 Python**: 3.10.12  
- **☕ Java**: 8 and 11  
- **🔧 Maven**: 3.6.3
- **🤖 OpenAI API Key**: Required for accessing OpenAI services

### ⚙️ Installation
[FlakyDoctor CI/CD](https://github.com/quintoorschot/CICD-FlakyDoctor) is directly usable in your [GitHub Actions workflows](https://docs.github.com/en/actions/how-tos/write-workflows), no local setup required.

#### 1. Add OpenAI secret key to your GitHub repository

Follow these steps in the **target repository**:

1. Open **Settings → Secrets and variables → Actions**.
2. Click **New repository secret**.
3. Set:
   - **Name:** `OPENAI_API_KEY`
   - **Secret:** your OpenAI API key value
4. Click **Add secret**.

#### 2. Set workflow permissions

1. Go to **Repository → Settings → Actions → General**  
2. Under **Workflow permissions**, select **Read and write permissions**  
3. Check **Allow GitHub Actions to create and approve pull requests**  
4. Click **Save**

#### 3. Add Action to your project's workflows

Copy the [FlakyDoctor action](https://github.com/quintoorschot/FlakyDoctor-Workflow/blob/main/flakydoctor.yml) into the `.github/workflows` folder of your target repo.

Or run this command in the root of your target folder:<br>
```sh
mkdir -p .github/workflows
curl -fsSL https://raw.githubusercontent.com/quintoorschot/FlakyDoctor-Workflow/main/flakydoctor.yml \
  | tail -n +4 > .github/workflows/action.yml

```


### 🧭 Usage
After installation, FlakyDoctor runs automatically in GitHub Actions on every push or pull request.  
It analyzes your test suite for flakiness and, when possible, applies patches to fix detected issues.

### 🧪 Example workflow output
Consider a Maven project with the following test file (`AppTest.java`):
```java
package com.example;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static org.junit.Assert.assertEquals;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;

import org.junit.Test;

public class AppTest {

  @Test
  public void listsFiles() throws IOException {
    Path dir = Files.createTempDirectory("d-");
    Files.createFile(dir.resolve("a.txt"));
    Files.createFile(dir.resolve("b.txt"));
    Files.createFile(dir.resolve("c.txt"));

    List<String> names = Arrays.asList(dir.toFile().list());

    // The expected list assumes a fixed order, but actual order from File.list() is non-deterministic.
    assertEquals(Arrays.asList("a.txt", "b.txt", "c.txt"), names);
  }
}

```
When this code is pushed to the repository or included in a pull request, FlakyDoctor CI/CD automatically runs as part of the workflow (if correctly configured).<br>
It analyzes the test suite, detects flaky behavior, and tries to generate a patch to make the tests deterministic.

FlakyDoctor creates a new PR where the flaky test shown above is patched as:
```java
package com.example;
import java.util.stream.Collectors;


import static org.junit.Assert.assertEquals;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;

import org.junit.Test;

public class AppTest {

  @Test
  public void listsFiles() throws IOException {
      Path dir = Files.createTempDirectory("d-");
      Files.createFile(dir.resolve("a.txt"));
      Files.createFile(dir.resolve("b.txt"));
      Files.createFile(dir.resolve("c.txt"));

      List<String> names = Arrays.stream(dir.toFile().list()).sorted().collect(Collectors.toList());

      assertEquals(Arrays.asList("a.txt", "b.txt", "c.txt"), names);
  }
}
```

Additionaly to the PR, FlakyDoctor CI/CD also produces an artifact containing the logs of the entire FlakyDoctor process.

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