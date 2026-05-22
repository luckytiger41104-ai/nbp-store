#!/usr/bin/env python3

# -*- coding: utf-8 -*-

“””
NBP General Store & Puja Bhandar - Billing System
Dhamna, Jamui, Bihar
“””

# ─────────────────────────────────────────────

# PRODUCT CATALOG (naam, daam)

# ─────────────────────────────────────────────

products = {}  #{"id": 1, "name": "Aata (Wheat Flour)", "unit": "1kg", "price": 40, "cat": "grocery"},
    {"id": 2, "name": "Chawal (Rice)", "unit": "1kg", "price": 45, "cat": "grocery"},
    {"id": 3, "name": "Dal Chana", "unit": "1kg", "price": 100, "cat": "grocery"},
    {"id": 4, "name": "Dal Mashur", "unit": "1kg", "price": 80, "cat": "grocery"},
    {"id": 5, "name": "Dal Arhar (Toor)", "unit": "1kg", "price": 130, "cat": "grocery"},
    {"id": 6, "name": "Sarso Tel (Oil)", "unit": "1L", "price": 185, "cat": "grocery"},
    {"id": 7, "name": "Namak (Salt)", "unit": "1kg", "price": 10, "cat": "grocery"},

    {"id": 8, "name": "Cheeni (Sugar)", "unit": "1kg", "price": 50, "cat": "grocery"},
    {"id": 9, "name": "Maida", "unit": "1kg", "price": 40, "cat": "grocery"},
    {"id": 10, "name": "Besan", "unit": "1kg", "price": 120, "cat": "grocery"},
    {"id": 11, "name": "Sooji (Semolina)", "unit": "1kg", "price": 50, "cat": "grocery"},
    {"id": 12, "name": "Poha (chura)", "unit": "500g", "price": 20, "cat": "grocery"},
    {"id": 13, "name": "Rai (Mustard Seeds)", "unit": "100g", "price": 15, "cat": "grocery"},
    {"id": 14, "name": "Jeera (Cumin)", "unit": "100g", "price": 70, "cat": "grocery"},
    {"id": 15, "name": "Lal Mirch Powder", "unit": "100g", "price": 30, "cat": "grocery"},
    {"id": 16, "name": "Haldi Powder", "unit": "100g", "price": 25, "cat": "grocery"},
    {"id": 17, "name": "Dhaniya Powder", "unit": "100g", "price": 25, "cat": "grocery"},
    {"id": 18, "name": "Garam Masala", "unit": "50g", "price": 30, "cat": "grocery"},
    {"id": 19, "name": "Chai Patti dalmia (Tea)", "unit": "50g", "price": 25, "cat": "grocery"},
    {"id": 20, "name": "Maggi Noodles", "unit": "4pk", "price": 40, "cat": "grocery"},
    {"id": 21, "name": "Agarbatti", "unit": "Pack", "price": 30, "cat": "puja"},
    {"id": 22, "name": "Dhoop Batti", "unit": "Pack", "price": 20, "cat": "puja"},
    {"id": 23, "name": "gulal", "unit": "Pack", "price": 10, "cat": "puja"},
    {"id": 24, "name": "Camphor (Kapoor)", "unit": "1Pack", "price": 70, "cat": "puja"},
    {"id": 25, "name": "Haldi Pooja", "unit": "50", "price": 10, "cat": "puja"},
    {"id": 26, "name": "Sindoor", "unit": "Pack", "price": 5, "cat": "puja"},
    {"id": 27, "name": "Roli", "unit": "Pack", "price": 15, "cat": "puja"},
    {"id": 28, "name": "astgandh chandan", "unit": "1Pack", "price": 20, "cat": "puja"},
    {"id": 29, "name": "Gangajal", "unit": "Bottle", "price": 30, "cat": "puja"},
    {"id": 30, "name": "Pooja Thali", "unit": "1pc", "price": 150, "cat": "puja"},
    {"id": 31, "name": "butter Biscuit", "unit": "10pk", "price": 50, "cat": "snacks"},
    {"id": 32, "name": "Marie Biscuit", "unit": "Pack", "price": 40, "cat": "snacks"},
    {"id": 33, "name": "Namkeen", "unit": "200g", "price": 30, "cat": "snacks"},
    {"id": 34, "name": "Chips (Lays)", "unit": "1Pack", "price": 5, "cat": "snacks"},
    {"id": 35, "name": "Toffee (Mango Bite)", "unit": "10pc", "price": 10, "cat": "snacks"},
    {"id": 36, "name": "Kurkure", "unit": "1Pack", "price": 5, "cat": "snacks"},
    {"id": 37, "name": "Sabun detol (Soap)", "unit": "1pc", "price": 10, "cat": "personal"},
    {"id": 38, "name": "Shampoo dove", "unit": "10pc", "price": 20, "cat": "personal"},
    {"id": 39, "name": "Toothpaste", "unit": "1pc", "price": 10, "cat": "personal"},
    {"id": 40, "name": "Toothbrush", "unit": "1pc", "price": 30, "cat": "personal"},
    {"id": 41, "name": "Surf Excel", "unit": "1pc", "price": 10, "cat": "personal"},
    {"id": 42, "name": "guide surf ", "unit": "500gram", "price": 40, "cat": "personal"},
    {"id": 43, "name": "Matchbox", "unit": "1pk", "price": 10, "cat": "other"},
    {"id": 44, "name": "Candle (Mombatti)", "unit": "Pack", "price": 40, "cat": "other"},
    {"id": 45, "name": "Pen", "unit": "5pc", "price": 25, "cat": "other"},
    {"id": 46, "name": "Notebook Hindi (Copy)", "unit": "1pc", "price": 30, "cat": "other"},
    {"id": 47, "name": "Safety Pin", "unit": "Pack", "price": 10, "cat": "other"},
    {"id": 48, "name": "Rubber Band", "unit": "Pack", "price": 10, "cat": "other"},
    {"id": 49, "name": "Tata namak", "unit": "1kg", "price": 30, "cat": "grocery"},
    {"id": 50, "name": "Notebook Hindi(Copy)", "unit": "1pc", "price": 10, "cat": "other"},
    {"id": 51, "name": "Notebook Hindi(Copy)", "unit": "1pc", "price": 20, "cat": "other"},
    {"id": 52, "name": "Notebook White (Copy)", "unit": "1pc", "price": 30, "cat": "other"},
    {"id": 53, "name": "Notebook White (Copy)", "unit": "1pc", "price": 20, "cat": "other"},
    {"id": 54, "name": "Notebook white(Copy)", "unit": "1pc", "price": 10, "cat": "other"},
    {"id": 55, "name": "Toothbrush", "unit": "1pc", "price": 20, "cat": "personal"},
    {"id": 56, "name": "Toothbrush", "unit": "1pc", "price": 10, "cat": "personal"},
    {"id": 57, "name": "Toothpaste", "unit": "1pc", "price": 20, "cat": "personal"},
    {"id": 58, "name": "Shampoo clinic plus", "unit": "10pc", "price": 10, "cat": "personal"},
    {"id": 59, "name": "Shampoo sun silk", "unit": "10pc", "price": 10, "cat": "personal"},
    {"id": 60, "name": "Sabun lifebuoy(Soap)", "unit": "1pc", "price": 10, "cat": "personal"},
    {"id": 61, "name": "Sabun lux (Soap)", "unit": "1pc", "price": 10, "cat": "personal"},
    {"id": 62, "name": "Agarbatti", "unit": "1Pack", "price": 65, "cat": "puja"},
    {"id": 21, "name": "Agarbatti", "unit": "Pack", "price": 20, "cat": "puja"},
    {"id": 21, "name": "Agarbatti", "unit": "Pack", "price": 50, "cat": "puja"},
    {"id": 21, "name": "Agarbatti", "unit": "Pack", "price": 15, "cat": "puja"},
    {"id": 21, "name": "Agarbatti", "unit": "Pack", "price": 50, "cat": "puja"}, { product_id: {“naam”: str, “daam”: float, “unit”: str} }
next_id = 1    # auto-increment product ID

def delivery_charge(item_count):
“””
10-19 items → ₹15
20-29 items → ₹30
30-39 items → ₹45
… har 10 items par ₹15 badhta hai
9 ya kam items → Free
“””
if item_count < 10:
return 0
slab = (item_count - 10) // 10  # 0, 1, 2, …
return 15 * (slab + 1)

# ─────────────────────────────────────────────

# PRODUCT MANAGEMENT

# ─────────────────────────────────────────────

def product_add():
global next_id
print(”\n— Naya Product Add Karo —”)
naam = input(“Product ka naam: “).strip()
if not naam:
print(“❌ Naam khaali nahi ho sakta.”)
return
try:
daam = float(input(“Price (₹): “))
if daam < 0:
raise ValueError
except ValueError:
print(“❌ Galat price. Sirf number daalo.”)
return
unit = input(“Unit (e.g. kg, pcs, litre, packet) [default: pcs]: “).strip() or “pcs”
products[next_id] = {“naam”: naam, “daam”: daam, “unit”: unit}
print(f”✅ ‘{naam}’ add ho gaya! (ID: {next_id})”)
next_id += 1

def product_list():
if not products:
print(”\n⚠️  Abhi koi product nahi hai. Pehle product add karo.”)
return
print(”\n” + “=” * 50)
print(f”  {‘ID’:<5} {‘Product’:<22} {‘Price’:>8}  {‘Unit’}”)
print(”=” * 50)
for pid, p in products.items():
print(f”  {pid:<5} {p[‘naam’]:<22} ₹{p[‘daam’]:>6.2f}  {p[‘unit’]}”)
print(”=” * 50)

def product_delete():
product_list()
if not products:
return
try:
pid = int(input(“Kaun sa ID delete karna hai? “))
if pid not in products:
print(“❌ ID nahi mila.”)
return
naam = products[pid][“naam”]
confirm = input(f”’{naam}’ delete karna chahte ho? (haan/nahi): “).strip().lower()
if confirm in (“haan”, “h”, “yes”, “y”):
del products[pid]
print(f”✅ ‘{naam}’ delete ho gaya.”)
else:
print(“Cancel ho gaya.”)
except ValueError:
print(“❌ Galat input.”)

# ─────────────────────────────────────────────

# BILLING

# ─────────────────────────────────────────────

def new_bill():
if not products:
print(”\n⚠️  Pehle product add karo (Menu → 1).”)
return

```
print("\n--- Naya Bill ---")
customer_naam = input("Customer ka naam: ").strip() or "Customer"
locality = input("Mohalla / Tola: ").strip() or "-"
delivery_type = input("Delivery type (G=Ghar/S=Shop) [G]: ").strip().upper() or "G"
is_delivery = delivery_type != "S"

cart = []  # list of (naam, qty, price_per_unit, unit)

print("\nProduct ID daalo aur quantity. '0' daalo jab khatam ho.\n")
product_list()

while True:
    try:
        pid_input = input("\nProduct ID (0 = done): ").strip()
        if pid_input == "0":
            break
        pid = int(pid_input)
        if pid not in products:
            print("❌ ID nahi mila.")
            continue
        qty = float(input(f"Quantity ({products[pid]['unit']}): "))
        if qty <= 0:
            print("❌ Quantity 0 se zyada honi chahiye.")
            continue
        cart.append({
            "naam": products[pid]["naam"],
            "qty": qty,
            "daam": products[pid]["daam"],
            "unit": products[pid]["unit"]
        })
        subtotal = qty * products[pid]["daam"]
        print(f"  ✅ Added: {products[pid]['naam']} × {qty} = ₹{subtotal:.2f}")
    except ValueError:
        print("❌ Galat input, dobara daalo.")

if not cart:
    print("⚠️  Cart khaali hai, bill nahi bana.")
    return

# Calculations
total_items = sum(item["qty"] for item in cart)
subtotal_amount = sum(item["qty"] * item["daam"] for item in cart)

dc = delivery_charge(int(total_items)) if is_delivery else 0
grand_total = subtotal_amount + dc

# ─── Print Bill ───
bill_lines = []
bill_lines.append("=" * 52)
bill_lines.append("   NBP GENERAL STORE & PUJA BHANDAR")
bill_lines.append("      Dhamna, Jamui, Bihar")
bill_lines.append("=" * 52)
bill_lines.append(f"  Customer : {customer_naam}")
bill_lines.append(f"  Mohalla  : {locality}")
bill_lines.append(f"  Delivery : {'Ghar Delivery' if is_delivery else 'Shop Pickup'}")
bill_lines.append("-" * 52)
bill_lines.append(f"  {'Item':<22} {'Qty':>5}  {'Rate':>7}  {'Amount':>8}")
bill_lines.append("-" * 52)
for item in cart:
    amt = item["qty"] * item["daam"]
    bill_lines.append(f"  {item['naam']:<22} {item['qty']:>5.1f}  ₹{item['daam']:>6.2f}  ₹{amt:>7.2f}")
bill_lines.append("-" * 52)
bill_lines.append(f"  {'Subtotal':<38} ₹{subtotal_amount:>7.2f}")
if is_delivery:
    slab_info = f"({int(total_items)} items)" if dc > 0 else "(9 ya kam items)"
    bill_lines.append(f"  {'Delivery Charge ' + slab_info:<38} ₹{dc:>7.2f}")
bill_lines.append("=" * 52)
bill_lines.append(f"  {'GRAND TOTAL':<38} ₹{grand_total:>7.2f}")
bill_lines.append("=" * 52)
bill_lines.append("   Dhanyawaad! Phir aana. 🙏")
bill_lines.append("=" * 52)

bill_text = "\n".join(bill_lines)
print("\n" + bill_text)

# ─── WhatsApp Message ───
wa_lines = []
wa_lines.append("🛒 *NBP General Store & Puja Bhandar*")
wa_lines.append("📍 Dhamna, Jamui, Bihar")
wa_lines.append("")
wa_lines.append(f"👤 *Customer:* {customer_naam}")
wa_lines.append(f"🏘️ *Mohalla:* {locality}")
wa_lines.append(f"🚚 *Delivery:* {'Ghar Delivery' if is_delivery else 'Shop Pickup'}")
wa_lines.append("")
wa_lines.append("*📦 Order Details:*")
for item in cart:
    amt = item["qty"] * item["daam"]
    wa_lines.append(f"  • {item['naam']} × {item['qty']} {item['unit']} = ₹{amt:.2f}")
wa_lines.append("")
wa_lines.append(f"💰 *Subtotal:* ₹{subtotal_amount:.2f}")
if is_delivery:
    wa_lines.append(f"🛵 *Delivery Charge:* ₹{dc:.2f} ({int(total_items)} items)")
wa_lines.append(f"✅ *Total Amount: ₹{grand_total:.2f}*")
wa_lines.append("")
wa_lines.append("🙏 _Dhanyawaad! Phir zaroor aana._")

wa_text = "\n".join(wa_lines)

print("\n" + "─" * 52)
print("📱 WHATSAPP MESSAGE (copy karo):")
print("─" * 52)
print(wa_text)
print("─" * 52)
```

# ─────────────────────────────────────────────

# DELIVERY CHART

# ─────────────────────────────────────────────

def show_delivery_chart():
print(”\n” + “=” * 35)
print(”  DELIVERY CHARGE CHART”)
print(”=” * 35)
print(f”  {‘Items’:<15} {‘Charge’}”)
print(”-” * 35)
print(f”  {‘1 - 9’:<15} Free”)
for start in range(10, 61, 10):
end = start + 9
charge = delivery_charge(start)
print(f”  {str(start) + ’ - ’ + str(end):<15} ₹{charge}”)
print(f”  {‘60+’:<15} Usi hisaab se”)
print(”=” * 35)

# ─────────────────────────────────────────────

# MAIN MENU

# ─────────────────────────────────────────────

def main():
print(”\n” + “=” * 52)
print(”  🏪 NBP GENERAL STORE & PUJA BHANDAR”)
print(”     Dhamna, Jamui, Bihar”)
print(”     Billing System v1.0”)
print(”=” * 52)

```
while True:
    print("\n📋 MENU:")
    print("  1. Product Add Karo")
    print("  2. Products Dekho")
    print("  3. Product Delete Karo")
    print("  4. Naya Bill Banao")
    print("  5. Delivery Charge Chart Dekho")
    print("  0. Bahar Jao (Exit)")
    print()

    choice = input("  Apna choice daalo: ").strip()

    if choice == "1":
        product_add()
    elif choice == "2":
        product_list()
    elif choice == "3":
        product_delete()
    elif choice == "4":
        new_bill()
    elif choice == "5":
        show_delivery_chart()
    elif choice == "0":
        print("\n🙏 Dhanyawaad! Jai Shri Ram.\n")
        break
    else:
        print("❌ Galat choice. 0-5 mein se kuch daalo.")
```

if **name** == “**main**”:
main()
