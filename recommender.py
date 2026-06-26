"""
---------------------------------------------------------------
DecodeLabs AI Internship - Project 3 : Tech Stack Recommender
---------------------------------------------------------------
Pipeline: User Skills → TF-IDF Vectorisation → Cosine Similarity Scoring → Top-N Output
---------------------------------------------------------------

"""

import math
from collections import defaultdict
print("✅ Imports ready!")

# ─────────────────────────────────────────────
# Dataset
# Each job role is a document. Its skills are the terms.
# ─────────────────────────────────────────────

JOB_ROLES = [
    {"title": "Data Scientist",           "skills": ["python", "machine learning", "sql", "data analysis", "statistics", "tensorflow", "pandas", "numpy"]},
    {"title": "DevOps Engineer",          "skills": ["aws", "docker", "kubernetes", "ci/cd", "linux", "automation", "git", "cloud"]},
    {"title": "Backend Developer",        "skills": ["python", "java", "sql", "apis", "rest", "databases", "git", "algorithms"]},
    {"title": "Frontend Developer",       "skills": ["javascript", "react", "css", "html", "ui/ux", "typescript", "git", "web design"]},
    {"title": "Machine Learning Engineer","skills": ["python", "tensorflow", "deep learning", "neural networks", "machine learning", "pytorch", "algorithms", "mathematics"]},
    {"title": "Cloud Architect",          "skills": ["aws", "cloud", "azure", "gcp", "networking", "security", "automation", "kubernetes"]},
    {"title": "Data Engineer",            "skills": ["python", "sql", "spark", "hadoop", "etl", "data pipelines", "cloud", "databases"]},
    {"title": "Cybersecurity Analyst",    "skills": ["networking", "linux", "security", "ethical hacking", "cryptography", "python", "firewalls", "risk analysis"]},
    {"title": "Full Stack Developer",     "skills": ["javascript", "python", "react", "sql", "rest", "apis", "git", "docker"]},
    {"title": "AI Research Engineer",     "skills": ["python", "mathematics", "neural networks", "deep learning", "research", "tensorflow", "pytorch", "statistics"]},
    {"title": "Systems Administrator",   "skills": ["linux", "networking", "automation", "bash", "security", "cloud", "monitoring", "git"]},
    {"title": "Mobile Developer",         "skills": ["java", "kotlin", "swift", "react", "ui/ux", "apis", "git", "databases"]},
]

print(f"✅ Dataset loaded with {len(JOB_ROLES)} job roles in catalogue")
print(f"\nJob roles:")
for role in JOB_ROLES:
    print(f"     • {role['title']}")

# ─────────────────────────────────────────────
# TF-IDF Feature Extraction:
#     - TF  = count(term) / total_terms
#     - IDF = log(N/df)   — penalises common skills like git or python
#     - TF-IDF = TF x IDF — unique, specific skills score higher
# ─────────────────────────────────────────────

def compute_tf(skill_list):
    """Term Frequency: count of term / total terms in the document."""
    tf    = defaultdict(float)
    total = len(skill_list)
    for skill in skill_list:
        tf[skill.lower()] += 1
    for skill in tf:
        tf[skill] /= total
    return dict(tf)


def compute_idf(all_roles):
    """Inverse Document Frequency: log(N / df)"""
    N  = len(all_roles)
    df = defaultdict(int)
    for role in all_roles:
        for skill in set(s.lower() for s in role["skills"]):
            df[skill] += 1
    return {skill: math.log(N / count) for skill, count in df.items()}


def build_shared_vocabulary(all_roles):
    """All unique skills across the dataset, sorted for vector stability."""
    vocab = set()
    for role in all_roles:
        for skill in role["skills"]:
            vocab.add(skill.lower())
    return sorted(vocab)


def build_tfidf_vector(skill_list, vocabulary, idf):
    """Returns a TF-IDF vector aligned to the shared vocabulary."""
    tf = compute_tf(skill_list)
    return [tf.get(term, 0.0) * idf.get(term, 0.0) for term in vocabulary]


print("✅ TF-IDF functions ready")

# ─────────────────────────────────────────────
# Cosine Similarity
# cos(θ) = (A·B) / (‖A‖ × ‖B‖)
# 1.0 : Perfect match
# 0.5 : Moderate overlap
# 0.0 : No shared characteristics
# ─────────────────────────────────────────────

def cosine_similarity(vec_a, vec_b):
    """cos(θ) = (A·B) / (‖A‖ × ‖B‖)"""
    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    magnitude_a = math.sqrt(sum(a ** 2 for a in vec_a))
    magnitude_b = math.sqrt(sum(b ** 2 for b in vec_b))
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    return dot_product / (magnitude_a * magnitude_b)

print("✅ Cosine similarity ready")

# ─────────────────────────────────────────────
# Full Recommendation Pipeline
# 4-step: Ingestion → Scoring → Sorting → Filtering
# ─────────────────────────────────────────────

def recommend(user_skills, all_roles=JOB_ROLES, top_n=3):
    vocab    = build_shared_vocabulary(all_roles)
    idf      = compute_idf(all_roles)
    user_vec = build_tfidf_vector(user_skills, vocab, idf)

    scored = []
    for role in all_roles:
        role_vec = build_tfidf_vector(role["skills"], vocab, idf)
        score    = cosine_similarity(user_vec, role_vec)
        scored.append({"title": role["title"], "score": score, "skills": role["skills"]})

    ranked = sorted(scored, key=lambda x: x["score"], reverse=True)
    return ranked[:top_n]

print("✅ Recommendation pipeline ready")

# ─────────────────────────────────────────────
# Testing with user input
# ─────────────────────────────────────────────

def display_results(results, user_skills):
    print("\n" + "─" * 60)
    print("                  TOP CAREER RECOMMENDATIONS")
    print("─" * 60)

    medals = ["🥇", "🥈", "🥉"]
    for i, result in enumerate(results):
        medal = medals[i] if i < 3 else f"#{i+1}"
        dots  = int(result["score"] * 20)
        bar   = "●" * dots + "○" * (20 - dots)
        print(f"\n  {medal}  {result['title']:<25} {bar}  {result['score']*100:.1f}%")

    print("\n" + "─" * 60)
    print("\n")



user_input  = input("\nEnter your skills (comma-separated): ")
USER_SKILLS = [s.strip().lower() for s in user_input.split(",") if s.strip()]
TOP_N       = 3

results = recommend(USER_SKILLS, top_n=TOP_N)
display_results(results, USER_SKILLS)

# ─────────────────────────────────────────────
# Full Leaderboard
# ─────────────────────────────────────────────

all_results = recommend(USER_SKILLS, top_n=len(JOB_ROLES))

print("\n" + "─" * 60)
print("                     FULL LEADERBOARD")
print("─" * 60)

for i, r in enumerate(all_results, 1):
    dots = int(r['score'] * 20)
    bar  = "●" * dots + "○" * (20 - dots)
    print(f"\n  #{i:<3} {r['title']:<25} {bar}  {r['score']*100:.1f}%")

print("\n" + "─" * 60)
print("\n")

# ─────────────────────────────────────────────
# User Profile Vector
# ─────────────────────────────────────────────

vocab    = build_shared_vocabulary(JOB_ROLES)
idf      = compute_idf(JOB_ROLES)
user_vec = build_tfidf_vector(USER_SKILLS, vocab, idf)

active = [(vocab[i], round(val, 4)) for i, val in enumerate(user_vec) if val > 0]

print("\n" + "─" * 60)
print("                   USER PROFILE VECTOR")
print("─" * 60)

for skill, weight in sorted(active, key=lambda x: x[1], reverse=True):
    dots = int(weight * 20)
    bar  = "●" * dots + "○" * (20 - dots)
    print(f"\n  {skill:<25} {bar}  {weight:.4f}")

print("\n" + "─" * 60)
print("\n")