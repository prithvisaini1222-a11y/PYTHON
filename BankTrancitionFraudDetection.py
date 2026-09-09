transactions = [
    {"id": 1, "user": "Tannu", "amount": 500, "location": "Delhi"},
    {"id": 2, "user": "Tannu", "amount": 1200, "location": "Delhi"},
    {"id": 3, "user": "Tannu", "amount": 85000, "location": "Mumbai"},
    {"id": 4, "user": "Tannu", "amount": 90000, "location": "London"},
    {"id": 5, "user": "Tannu", "amount": 300, "location": "Delhi"},
]


def detect_fraud(transactions):
    suspicious = []

    for i, transaction in enumerate(transactions):

        risk_score = 0
        reasons = []

        # Rule 1: Very high transaction
        if transaction["amount"] > 50000:
            risk_score += 40
            reasons.append("Very high transaction amount")

        # Rule 2: Location change
        if i > 0:
            previous_location = transactions[i - 1]["location"]

            if transaction["location"] != previous_location:
                risk_score += 30
                reasons.append("Location changed")

        # Rule 3: Rapid large transactions
        if i > 0:
            previous_amount = transactions[i - 1]["amount"]

            if transaction["amount"] > previous_amount * 5:
                risk_score += 20
                reasons.append("Sudden increase in transaction amount")

        # Final risk calculation
        if risk_score >= 60:
            status = "HIGH RISK"
        elif risk_score >= 30:
            status = "MEDIUM RISK"
        else:
            status = "SAFE"

        suspicious.append({
            "id": transaction["id"],
            "amount": transaction["amount"],
            "location": transaction["location"],
            "risk_score": risk_score,
            "status": status,
            "reasons": reasons
        })

    return suspicious


def display_results(results):

    print("\n" + "=" * 60)
    print("          🔐 TRANSACTION FRAUD DETECTOR")
    print("=" * 60)

    for result in results:

        print(f"\nTransaction ID : {result['id']}")
        print(f"Amount         : ₹{result['amount']}")
        print(f"Location       : {result['location']}")
        print(f"Risk Score     : {result['risk_score']}/100")
        print(f"Status         : {result['status']}")

        if result["reasons"]:
            print("Reasons:")
            for reason in result["reasons"]:
                print("  •", reason)
        else:
            print("Reasons        : No suspicious activity")


def main():
    results = detect_fraud(transactions)
    display_results(results)


main()
