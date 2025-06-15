from collections import Counter

CLASS_NAMES = {
    0: "Hardhat",
    1: "Person",
    2: "Safety Vest"
}

def check_compliance(class_ids):
    counts = Counter(class_ids)

    compliant_items = counts.get(0, 0) + counts.get(2, 0)
    total_persons = counts.get(1, 0)
    non_compliant = max(total_persons - compliant_items, 0)

    return {
        "Total Persons": total_persons,
        "Compliant Gear Items": compliant_items,
        "Non-Compliant Persons (est.)": non_compliant,
        "Detected Items": {CLASS_NAMES.get(k, f"Class {k}"): v for k, v in counts.items()}
    }
