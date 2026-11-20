import re
import time

def normalize_phone(phone):
    if not phone:
        return ""
    digits = re.sub(r"\D", "", phone)
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    return digits

def normalize_name(name):
    return " ".join(name.lower().split())

def normalize_email(email):
    return email.strip().lower() if email else ""

def merge_contacts(contacts):
    merged, phone_index, email_index = {}, {}, {}
    for contact in contacts:
        phones = {normalize_phone(p) for p in contact.get("phones", []) if normalize_phone(p)}
        emails = {normalize_email(e) for e in contact.get("emails", []) if normalize_email(e)}
        existing = None
        for phone in phones:
            if phone in phone_index:
                existing = phone_index[phone]
                break
        if existing is None:
            for email in emails:
                if email in email_index:
                    existing = email_index[email]
                    break
        if existing is None:
            existing = len(merged)
            merged[existing] = {"name": contact.get("name", ""), "phones": set(), "emails": set()}
        merged[existing]["phones"].update(phones)
        merged[existing]["emails"].update(emails)
        for phone in phones:
            phone_index[phone] = existing
        for email in emails:
            email_index[email] = existing
    return merged

contacts = [
    {"name": "Dr. Ravi", "phones": ["+91 98400 12345"], "emails": ["ravi@gmail.com"]},
    {"name": "ravi kumar", "phones": ["9840012345", "9876543210"], "emails": ["ravi@gmail.com"]},
    {"name": "Priya", "phones": ["+91 98765 43210"], "emails": ["priya@gmail.com"]},
    {"name": "Arun", "phones": [], "emails": ["arun@gmail.com"]},
    {"name": "Kumar", "phones": ["9000011111"], "emails": []}
]
start = time.perf_counter()
result = merge_contacts(contacts)
elapsed = time.perf_counter() - start
print("MERGED CONTACTS")
for contact in result.values():
    print("\nName:", contact["name"])
    print("Phone Numbers:", sorted(contact["phones"]))
    print("Email Addresses:", sorted(contact["emails"]))
print("\nTotal Contacts:", len(result))
print("Execution Time:", elapsed, "seconds")
