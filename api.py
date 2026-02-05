from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import select

from models import Offer, Transaction, User, async_session_factory, init_db

app = FastAPI(title="PRO# CPA API")


class PostbackPayload(BaseModel):
    sub1: int
    status: str


@app.on_event("startup")
async def startup() -> None:
    await init_db()


@app.post("/postback")
async def postback(payload: PostbackPayload) -> dict[str, str]:
    if payload.status.lower() != "deposit":
        return {"message": "Статус оброблено."}

    async with async_session_factory() as session:
        async with session.begin():
            user = await session.get(User, payload.sub1)
            if not user:
                user = User(telegram_id=payload.sub1, balance_pro=0)
                session.add(user)

            offer_result = await session.execute(select(Offer).limit(1))
            offer = offer_result.scalars().first()
            reward_amount = offer.reward_pro if offer else 0

            user.balance_pro += reward_amount
            session.add(
                Transaction(
                    user_id=user.telegram_id,
                    type="deposit_reward",
                    amount=reward_amount,
                    status="completed",
                )
            )

            if user.referrer_id:
                referrer = await session.get(User, user.referrer_id)
                if not referrer:
                    raise HTTPException(status_code=404, detail="Реферер не знайдений.")
                referrer.balance_pro += 5000
                session.add(
                    Transaction(
                        user_id=referrer.telegram_id,
                        type="referral_reward",
                        amount=5000,
                        status="completed",
                    )
                )

    return {"message": "Депозит оброблено."}
