# DecodeLabs Internship - Project 3: Tech Stack Recommender

## 📌 Project Overview

This is a **content-based filtering recommendation engine** that maps a user's raw skills to the most relevant tech career paths. You enter your skills, and the system mathematically ranks job roles by how closely they match your profile.

---

## 🔍 Key Concepts Demonstrated

- **Content-Based Filtering** vs Collaborative Filtering
- **Vector Space Model** — representing skills as numerical arrays
- **TF-IDF Weighting** — rewarding specific, rare skills over generic ones
- **Cosine Similarity** — magnitude-invariant similarity measurement
- **Cold Start Handling** — guarded against zero-vector profiles
- **Top-N Filtering** — preventing choice overload

---

## ⚙️ Pipeline

```
User Skills → TF-IDF Vectorisation → Cosine Similarity Scoring → Top-N Output
```

---

## 🧠 How the Algorithm Works

### 1. Ingestion (Input)
The script accepts a minimum of **3 user skills** to ensure enough data density for accurate matching.

### 2. TF-IDF Vectorisation
Raw text skills can't be compared mathematically. We transform them into numerical vectors using **TF-IDF weighting**:

| Component | Formula | Purpose |
|-----------|---------|---------|
| **TF** (Term Frequency) | `count(term) / total_terms` | Rewards skills central to a role |
| **IDF** (Inverse Document Frequency) | `log(N / df)` | Penalises generic skills like "git" or "python" that appear everywhere |
| **TF-IDF** | `TF × IDF` | Final weight: unique and specific skills score higher |

### 3. Cosine Similarity (Scoring)
Instead of Euclidean distance (sensitive to vector size), we use **Cosine Similarity** — the industry standard for text-based recommendation:

```
cos(θ) = (A · B) / (‖A‖ × ‖B‖)
```

| Score | Meaning |
|-------|---------|
| `1.0` | Perfect match (identical orientation) |
| `0.5` | Moderate overlap |
| `0.0` | No shared characteristics |

### 4. Sorting & Filtering (Output)
Results are sorted in **descending order** by similarity score, then truncated to the **Top-N** list to prevent choice overload.

---

## ⚙️ Requirements

- **Python 3.10+**
- **No external libraries** — uses only Python's built-in `math`, `csv`, and `collections` modules

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/areesha900/decodelabs_Project3.git
cd decodelabs_Project3

# Run the recommender
python3 recommender.py
```

### Example Session

```
╔══════════════════════════════════════════════════════╗
║       TECH STACK RECOMMENDER  —  DecodeLabs          ║
║       Project 3 · AI Recommendation Logic            ║
║       Algorithm: TF-IDF  +  Cosine Similarity        ║
╚══════════════════════════════════════════════════════╝

  Enter your skills one by one (minimum 3 required).
  Examples: python, machine learning, sql, docker, aws
  Type 'done' when finished.

  Skill #1: python
  ✓  Added: python
  Skill #2: machine learning
  ✓  Added: machine learning
  Skill #3: tensorflow
  ✓  Added: tensorflow

  Add another skill? (yes / done): done

  How many recommendations do you want? [default: 3]: 3

  Running similarity engine …

──────────────────────────────────────────────────────
  Your skills  : python, machine learning, tensorflow
──────────────────────────────────────────────────────
  TOP CAREER RECOMMENDATIONS
──────────────────────────────────────────────────────

  🥇  Machine Learning Engineer
      Match  : [██████████████████████░░░░░░░░] 73.2%
      Skills : python, tensorflow, deep learning, neural networks ...

  🥈  AI Research Engineer
      Match  : [█████████████████░░░░░░░░░░░░░] 58.1%
      Skills : python, mathematics, neural networks, deep learning ...

  🥉  Data Scientist
      Match  : [████████████░░░░░░░░░░░░░░░░░░] 41.7%
      Skills : python, machine learning, sql, data analysis ...

──────────────────────────────────────────────────────

  Export results to CSV? (yes / no): yes
  Results exported → recommendations.csv
```

---

## 🗂️ Job Roles in the Dataset

| Role | Core Skills |
|------|------------|
| Data Scientist | Python, ML, SQL, Statistics, TensorFlow |
| DevOps Engineer | AWS, Docker, Kubernetes, CI/CD, Linux |
| Backend Developer | Python, Java, SQL, APIs, REST |
| Frontend Developer | JavaScript, React, CSS, HTML, TypeScript |
| ML Engineer | Python, TensorFlow, Deep Learning, PyTorch |
| Cloud Architect | AWS, Azure, GCP, Networking, Security |
| Data Engineer | Python, SQL, Spark, ETL, Data Pipelines |
| Cybersecurity Analyst | Networking, Linux, Security, Cryptography |
| Full Stack Developer | JavaScript, Python, React, SQL, Docker |
| AI Research Engineer | Python, Mathematics, Neural Networks, PyTorch |
| Systems Administrator | Linux, Networking, Automation, Bash |
| Mobile Developer | Java, Kotlin, Swift, React, APIs |

---
