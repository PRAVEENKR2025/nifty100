# src/analytics/cashflow_kpis.py
import csv

def free_cash_flow(operating_activity, investing_activity):
    # Negative values allowed
    return operating_activity + investing_activity

def cfo_quality_score(cfo_values, pat_values):
    """
    CFO / PAT ratio averaged over 5 years
    >1.0 = High Quality
    0.5–1.0 = Moderate
    <0.5 = Accrual Risk
    """
    if len(cfo_values) < 5 or len(pat_values) < 5:
        return None, "INSUFFICIENT"
    ratios = []
    for cfo, pat in zip(cfo_values[-5:], pat_values[-5:]):
        if pat == 0:
            return None, None
        ratios.append(cfo / pat)
    avg_ratio = sum(ratios) / len(ratios)
    if avg_ratio > 1.0:
        return avg_ratio, "High Quality"
    elif avg_ratio >= 0.5:
        return avg_ratio, "Moderate"
    else:
        return avg_ratio, "Accrual Risk"

def capex_intensity(investing_activity, sales):
    if sales == 0:
        return None, None
    intensity = abs(investing_activity) / sales * 100
    if intensity < 3:
        return intensity, "Asset Light"
    elif intensity <= 8:
        return intensity, "Moderate"
    else:
        return intensity, "Capital Intensive"

def fcf_conversion_rate(fcf, operating_profit):
    if operating_profit == 0:
        return None
    return (fcf / operating_profit) * 100

def classify_capital_allocation(cfo, cfi, cff, cfo_pat_ratio=None):
    """
    Pattern labels based on signs of (CFO, CFI, CFF)
    """
    cfo_sign = "+" if cfo >= 0 else "-"
    cfi_sign = "+" if cfi >= 0 else "-"
    cff_sign = "+" if cff >= 0 else "-"

    pattern_label = None
    if (cfo_sign, cfi_sign, cff_sign) == ("+", "-", "-"):
        if cfo_pat_ratio and cfo_pat_ratio > 1.2:
            pattern_label = "Shareholder Returns"
        else:
            pattern_label = "Reinvestor"
    elif (cfo_sign, cfi_sign, cff_sign) == ("+", "+", "-"):
        pattern_label = "Liquidating Assets"
    elif (cfo_sign, cfi_sign, cff_sign) == ("-", "+", "+"):
        pattern_label = "Distress Signal"
    elif (cfo_sign, cfi_sign, cff_sign) == ("-", "-", "+"):
        pattern_label = "Growth Funded by Debt"
    elif (cfo_sign, cfi_sign, cff_sign) == ("+", "+", "+"):
        pattern_label = "Cash Accumulator"
    elif (cfo_sign, cfi_sign, cff_sign) == ("-", "-", "-"):
        pattern_label = "Pre-Revenue"
    elif (cfo_sign, cfi_sign, cff_sign) == ("+", "-", "+"):
        pattern_label = "Mixed"

    return cfo_sign, cfi_sign, cff_sign, pattern_label

def export_capital_allocation(data, output_path="output/capital_allocation.csv"):
    """
    data = list of dicts: {company_id, year, cfo, cfi, cff, cfo_pat_ratio}
    """
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["company_id", "year", "cfo_sign", "cfi_sign", "cff_sign", "pattern_label"])
        for row in data:
            cfo_sign, cfi_sign, cff_sign, label = classify_capital_allocation(
                row["cfo"], row["cfi"], row["cff"], row.get("cfo_pat_ratio")
            )
            writer.writerow([row["company_id"], row["year"], cfo_sign, cfi_sign, cff_sign, label])
