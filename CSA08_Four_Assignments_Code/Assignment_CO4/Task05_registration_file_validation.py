def valid_email(email):
    if email.count("@") != 1 or " " in email:
        return False
    local, domain = email.split("@")
    return (
        bool(local) and bool(domain) and "." in domain
        and not domain.startswith(".") and not domain.endswith(".")
    )

def process_registration(files):
    seen, master, event_map, errors = set(), [], {}, []
    for filename, lines in files.items():
        if lines is None:
            errors.append((filename, "File not found"))
            continue
        for line_no, line in enumerate(lines, 1):
            try:
                parts = line.strip().split(",")
                if len(parts) != 5:
                    raise ValueError("Damaged record")
                reg, name, dept, email, events = [part.strip() for part in parts]
                if not reg or not name or not dept:
                    raise ValueError("Missing student details")
                if not valid_email(email):
                    raise ValueError("Invalid email")
                if reg in seen:
                    raise ValueError("Duplicate registration")
                event_list = [event.strip() for event in events.split(";") if event.strip()]
                if not event_list:
                    raise ValueError("No events selected")
                seen.add(reg)
                student = {"register": reg, "name": name, "department": dept, "email": email}
                master.append(student)
                for event in event_list:
                    event_map.setdefault(event, []).append(student)
            except ValueError as error:
                errors.append((filename, line_no, str(error)))

    print("MASTER STUDENT LIST")
    for student in master:
        print(student)
    print("\nEVENT-WISE PARTICIPANTS")
    for event, students in sorted(event_map.items()):
        print("\n", event)
        for student in students:
            print(student["name"])
    print("\nSUMMARY REPORT")
    print("Total Students:", len(master))
    print("Total Events:", len(event_map))
    for event, students in sorted(event_map.items()):
        print(event, ":", len(students), "participants")
    print("\nERROR LOG")
    for error in errors:
        print(error)

files = {
    "CSE.txt": [
        "101,Anu,CSE,anu@gmail.com,Music;Dance",
        "102,Bala,CSE,bala@gmail.com,Drama"
    ],
    "IT.txt": [
        "101,Anu,CSE,anu@gmail.com,Music",
        "103,Charu,IT,charuemail.com,Quiz"
    ],
    "ECE.txt": [
        "104,Devi,ECE,devi@gmail.com,Music;Quiz",
        "105,Ravi,ECE,ravi@gmail.com"
    ],
    "MECH.txt": ["106,Kumar,MECH,kumar@gmail.com,Dance"],
    "CIVIL.txt": None
}
process_registration(files)
