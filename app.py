from base import *

def main():
    profiles = load_profiles()
    cs = careers()

    while True:
        print("\n=== Career Advisor ===")
        print("[1] Novo perfil")
        print("[2] Listar perfis")
        print("[3] Editar competências")
        print("[4] Recomendar carreiras")
        print("[5] Exportar JSON")
        print("[0] Sair")
        op = input("Escolha: ").strip()

        if op == "1":
            name = input("Nome: ").strip()
            role = input("Interesse (opcional): ").strip()
            p = Profile(name, role)
            comps = sorted({c for car in cs for c in car.reqs})
            print("Avalie suas competências (0–10):")
            for comp in comps:
                val = prompt_float(comp)
                if val: p.set_competence(comp, val)
            profiles.append(p)
            save_profiles(profiles)
            print("Perfil salvo.")

        elif op == "2":
            if not profiles: print("Nenhum perfil.")
            else:
                for i, p in enumerate(profiles): print(f"\nID {i}\n{p}")

        elif op == "3":
            if not profiles: print("Nenhum perfil.")
            else:
                idx = choose([p.name for p in profiles], "Escolha o perfil")
                p = profiles[idx]
                comps = sorted({c for car in cs for c in car.reqs})
                for c in comps:
                    atual = p.get(c)
                    nv = input(f"{c} (atual {atual}): ").strip()
                    if nv:
                        try:
                            v = float(nv)
                            if 0 <= v <= 10: p.set_competence(c, v)
                        except: print("Valor inválido.")
                save_profiles(profiles)
                print("Atualizado.")

        elif op == "4":
            if not profiles: print("Nenhum perfil.")
            else:
                idx = choose([p.name for p in profiles], "Escolha o perfil")
                p = profiles[idx]
                recs = recommend(p, cs)
                print(f"\nRecomendações para {p.name}:")
                for i, (c, s, gaps) in enumerate(recs, 1):
                    print(f"[{i}] {c.name} — Compatibilidade: {s*100:.1f}%")
                    print(f"    {c.desc}")
                    if gaps:
                        print("    Lacunas:")
                        for g, d in gaps.items():
                            print(f"      - {g}: +{d:.1f}")
                    else:
                        print("    Perfil muito alinhado!")
                    print("    Recursos:")
                    for r in c.resources: print(f"      • {r}")
                    print()

        elif op == "5":
            with open("export_profiles.json", "w", encoding="utf-8") as f:
                json.dump([p.to_dict() for p in profiles], f, ensure_ascii=False, indent=2)
            print("Exportado com sucesso.")

        elif op == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()