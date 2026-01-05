from sqlalchemy.orm import Session
from core import tables


def create_debt_manager(db: Session, ism: str, nomer: str, summa: int, turi: str):
    user = db.query(tables.User).filter(tables.User.phone == nomer).first()
    if not user:
        user = tables.User(name=ism, phone=nomer)
        db.add(user)
        db.commit()
        db.refresh(user)

    new_debt = tables.Debt(
        amount=summa,
        type=turi,
        user_id=user.id
    )
    db.add(new_debt)
    db.commit()
    db.refresh(new_debt)

    return {
        "status": "Muvaffaqiyatli",
        "ism": user.name,
        "nomer": user.phone,
        "qarz_summasi": new_debt.amount,
        "turi": new_debt.type
    }


def get_all_debts_manager(db: Session):
    return db.query(tables.Debt).all()