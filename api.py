from __future__ import annotations

import os

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Header
from pydantic import BaseModel
from sqlalchemy import select

from models import Channel, Offer, Transaction, User, async_session_factory, init_db

load_dotenv()

app = FastAPI(title="PRO# CPA API")
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "")


class PostbackPayload(BaseModel):
    sub1: int
    status: str


@app.on_event("startup")
async def startup() -> None:
    await init_db()


def require_admin(x_admin_token: str | None = Header(default=None)) -> None:
    if not ADMIN_TOKEN:
        raise HTTPException(status_code=500, detail="ADMIN_TOKEN не налаштовано.")
    if x_admin_token != ADMIN_TOKEN:
        raise HTTPException(status_code=401, detail="Невірний токен адміністратора.")


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


@app.get("/admin/users", dependencies=[Depends(require_admin)])
async def admin_users() -> list[dict[str, str | int | None]]:
    async with async_session_factory() as session:
        result = await session.execute(select(User))
        return [
            {
                "telegram_id": user.telegram_id,
                "username": user.username,
                "referrer_id": user.referrer_id,
                "balance_pro": user.balance_pro,
            }
            for user in result.scalars()
        ]


@app.get("/admin/offers", dependencies=[Depends(require_admin)])
async def admin_offers() -> list[dict[str, str | int | bool]]:
    async with async_session_factory() as session:
        result = await session.execute(select(Offer))
        return [
            {
                "id": offer.id,
                "title": offer.title,
                "reward_pro": offer.reward_pro,
                "link": offer.link,
                "is_limited": offer.is_limited,
            }
            for offer in result.scalars()
        ]


class OfferPayload(BaseModel):
    title: str
    reward_pro: int
    link: str
    is_limited: bool = False


@app.post("/admin/offers", dependencies=[Depends(require_admin)])
async def admin_create_offer(payload: OfferPayload) -> dict[str, str]:
    async with async_session_factory() as session:
        async with session.begin():
            session.add(
                Offer(
                    title=payload.title,
                    reward_pro=payload.reward_pro,
                    link=payload.link,
                    is_limited=payload.is_limited,
                )
            )
    return {"message": "Оффер створено."}


@app.get("/admin/channels", dependencies=[Depends(require_admin)])
async def admin_channels() -> list[dict[str, str | int]]:
    async with async_session_factory() as session:
        result = await session.execute(select(Channel))
        return [
            {"channel_id": channel.channel_id, "link": channel.link}
            for channel in result.scalars()
        ]


@app.get("/admin/transactions", dependencies=[Depends(require_admin)])
async def admin_transactions() -> list[dict[str, str | int]]:
    async with async_session_factory() as session:
        result = await session.execute(select(Transaction))
        return [
            {
                "id": transaction.id,
                "user_id": transaction.user_id,
                "type": transaction.type,
                "amount": transaction.amount,
                "status": transaction.status,
            }
            for transaction in result.scalars()
        ]
