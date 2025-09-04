
import re
from typing import Optional

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def is_valid_email(email: str) -> bool:
    if not email:
        return False
    return EMAIL_RE.match(email) is not None

def split_name(full_name: str):
    if not full_name or not full_name.strip():
        return ("","")
    parts = full_name.strip().split()
    if len(parts) == 1:
        return (parts[0], "")
    return (parts[0], " ".join(parts[1:]))

def domain_from_email(email: str) -> Optional[str]:
    if not email or "@" not in email:
        return None
    return email.split("@",1)[1].lower()

def business_email_domain(domain: str) -> bool:
    if not domain: return False
    # crude personal email check
    personal = {"gmail.com","yahoo.com","outlook.com","hotmail.com","icloud.com","aol.com","proton.me","protonmail.com","live.com","msn.com","pm.me"}
    return domain not in personal
