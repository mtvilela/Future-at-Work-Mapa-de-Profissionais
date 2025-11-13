#!/usr/bin/env python3
import json
from os.path import exists

DATA_FILE = "profiles.json"

# ---------- MODELOS ----------
class Profile:
    def __init__(self, name, role_interest=""):
        self.name = name
        self.role_interest = role_interest
        self.competences = {}  # {nome_competencia: nota 0–10}

    def set_competence(self, name, score):
        self.competences[name] = float(score)

    def get(self, name):
        return self.competences.get(name, 0.0)

    def to_dict(self):
        return {"name": self.name, "role_interest": self.role_interest, "competences": self.competences}

    @staticmethod
    def from_dict(d):
        p = Profile(d["name"], d.get("role_interest", ""))
        p.competences = d.get("competences", {})
        return p

    def __str__(self):
        txt = f"Perfil: {self.name} ({self.role_interest})"
        for k, v in sorted(self.competences.items()):
            txt += f"\n  {k:<22}: {v:.1f}"
        return txt


class Career:
    def __init__(self, name, reqs, desc="", resources=None):
        self.name = name
        self.reqs = reqs
        self.desc = desc
        self.resources = resources or []

    def similarity(self, prof: Profile):
        score = total = 0
        for c, desired in self.reqs.items():
            have = prof.get(c)
            sim = 1 - abs(desired - have) / 10
            sim = max(0, sim)
            score += sim * desired
            total += desired
        return score / total if total else 0

    def gaps(self, prof: Profile):
        return {c: d - prof.get(c) for c, d in self.reqs.items() if prof.get(c) < d}


# ---------- FUNÇÕES DE APOIO ----------
def load_profiles():
    if not exists(DATA_FILE): return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return [Profile.from_dict(d) for d in json.load(f)]
    except: return []

def save_profiles(profiles):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([p.to_dict() for p in profiles], f, ensure_ascii=False, indent=2)


def prompt_float(text):
    while True:
        v = input(f"{text} [0-10]: ").strip()
        if not v: return 0.0
        try:
            v = float(v)
            if 0 <= v <= 10: return v
        except: pass
        print("Valor inválido.")


def choose(items, msg):
    for i, it in enumerate(items):
        print(f"[{i}] {it}")
    while True:
        sel = input(msg + ": ").strip()
        if sel.isdigit() and int(sel) < len(items): return int(sel)
        print("Escolha inválida.")


# ---------- BASE DE CARREIRAS ----------
def careers():
    return [
        Career("Cientista de Dados",
               {"Lógica": 8, "Estatística": 8, "Python": 8, "Machine Learning": 7, "Comunicação": 6},
               "Modelagem e análise preditiva.",
               ["Curso ML (Andrew Ng)", "Kaggle", "Livro: Practical Statistics"]),
        Career("Engenheiro de Software",
               {"Lógica": 8, "Python": 8, "Arquitetura": 7, "Colaboração": 6},
               "Desenvolvimento e arquitetura de sistemas.",
               ["Livro: Clean Code", "Udemy System Design"]),
        Career("Especialista em RPA",
               {"Lógica": 7, "Python": 6, "Automação": 8, "Processos": 7},
               "Automação de processos empresariais.",
               ["UiPath Academy", "Curso: Selenium"]),
        Career("Product Manager",
               {"Comunicação": 8, "Visão de Produto": 8, "Colaboração": 8, "Análise de Dados": 6},
               "Gestão de produtos e stakeholders.",
               ["Livro: Inspired", "Curso: Product Management"]),
        Career("Cibersegurança",
               {"Lógica": 7, "Segurança": 8, "Criptografia": 7, "Pensamento Crítico": 8},
               "Proteção de sistemas e dados.",
               ["CompTIA Security+", "OWASP", "CTF Platforms"])
    ]


# ---------- RECOMENDAÇÕES ----------
def recommend(profile, all_careers, top=3):
    results = []
    for c in all_careers:
        score = c.similarity(profile)
        gaps = c.gaps(profile)
        results.append((c, score, gaps))
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:top]


# ---------- CLI ----------

