# DecodeLabs Internship - Project 3: Tech Stack Recommender

## 📌 Project Overview

A **content-based filtering recommendation engine** that maps a user's skills to the most relevant tech career paths using TF-IDF weighting and cosine similarity.

---

## ⚙️ Pipeline
```
User Skills → TF-IDF Vectorisation → Cosine Similarity Scoring → Top-N Output
```

---

## 🧠 How it Works
 
| Step | What happens |
|------|-------------|
| **Ingestion** | User enters skills as a comma-separated list |
| **TF-IDF Vectorisation** | Skills are transformed into weighted numerical vectors |
| **Cosine Similarity** | Each job role is scored against the user's profile |
| **Top-N Filtering** | Results are sorted and truncated to prevent choice overload |

---

### TF-IDF Weighting
 
| Component | Formula | Purpose |
|-----------|---------|---------|
| TF | `count(term) / total_terms` | Rewards skills central to a role |
| IDF | `log(N / df)` | Penalises generic skills like `git` or `python` |
| TF-IDF | `TF × IDF` | Specific, rare skills score higher |
 
### Cosine Similarity
 
```
cos(θ) = (A · B) / (‖A‖ × ‖B‖)
```
| Score | Meaning |
|-------|---------|
| `1.0` | Perfect match |
| `0.5` | Moderate overlap |
| `0.0` | No shared characteristics |
 
---
  
## ⚙️ Requirements

- **Python 3.10+**
- **No external libraries** - uses only Python's built-in `math`, and `collections`
  
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
Enter your skills (comma-separated): python, machine learning, tensorflow
 
────────────────────────────────────────────────────────────
                  TOP CAREER RECOMMENDATIONS
────────────────────────────────────────────────────────────
 
  🥇  Machine Learning Engineer   ●●●●●●●●●●●●●●○○○○○○  73.2%
  🥈  AI Research Engineer        ●●●●●●●●●●●○○○○○○○○○  58.1%
  🥉  Data Scientist              ●●●●●●●●○○○○○○○○○○○○  41.7%
 
────────────────────────────────────────────────────────────
                     FULL LEADERBOARD
────────────────────────────────────────────────────────────
 
  #1   Machine Learning Engineer   ●●●●●●●●●●●●●●○○○○○○  73.2%
  #2   AI Research Engineer        ●●●●●●●●●●●○○○○○○○○○  58.1%
  #3   Data Scientist              ●●●●●●●●○○○○○○○○○○○○  41.7%
  #4   Full Stack Developer        ●●●●●○○○○○○○○○○○○○○○  27.3%
  ...
 
────────────────────────────────────────────────────────────
                   USER PROFILE VECTOR
────────────────────────────────────────────────────────────
 
  tensorflow                ●●●●●●●●●●●●○○○○○○○○  0.1993
  machine learning          ●●●●●●●●●○○○○○○○○○○○  0.1493
  python                    ●●●●●○○○○○○○○○○○○○○○  0.0599
 
────────────────────────────────────────────────────────────
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
