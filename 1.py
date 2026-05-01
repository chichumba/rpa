import json


claims = [
    {"id": 1, "policy_active": True, "docs_ok": True, "amount": 10000},
    {"id": 2, "policy_active": False, "docs_ok": True, "amount": 5000},
    {"id": 3, "policy_active": True, "docs_ok": False, "amount": 7000},
    {"id": 4, "policy_active": True, "docs_ok": True, "amount": 25000},
    {"id": 5, "policy_active": True, "docs_ok": True, "amount": 40000},
    {"id": 6, "policy_active": False, "docs_ok": False, "amount": 12000},
    {"id": 7, "policy_active": True, "docs_ok": False, "amount": 3000},
    {"id": 8, "policy_active": True, "docs_ok": True, "amount": 18000},
    {"id": 9, "policy_active": True, "docs_ok": True, "amount": 6500},
    {"id": 10, "policy_active": False, "docs_ok": True, "amount": 22000},
    {"id": 11, "policy_active": True, "docs_ok": True, "amount": 9100},
    {"id": 12, "policy_active": True, "docs_ok": False, "amount": 47000},
    {"id": 13, "policy_active": True, "docs_ok": True, "amount": 13000},
    {"id": 14, "policy_active": False, "docs_ok": False, "amount": 5600},
    {"id": 15, "policy_active": True, "docs_ok": True, "amount": 72000},
]

results = []


for claim in claims:
    if claim["policy_active"] is False:
        decision = "reject"
        reason = "Полис неактивен"
        payout = 0
    elif claim["docs_ok"] is False:
        decision = "manual_review"
        reason = "Нет документов"
        payout = 0
    else:
        decision = "approve"
        reason = "Автоодобрение"
        payout = claim["amount"] * 0.8  


    results.append(
        {
            "id": claim["id"],
            "decision": decision,
            "reason": reason,
            "payout": payout,
        }
    )


print("Результат:")
for item in results:
    print(item)


with open("claims_processed.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Файл claims_processed.json сохранен")
