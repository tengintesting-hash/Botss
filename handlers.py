from __future__ import annotations

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup, Message

from models import Channel

router = Router()


def subscription_keyboard(channels: list[Channel]) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="Підписатися", url=channel.link)]
        for channel in channels
    ]
    buttons.append([InlineKeyboardButton(text="Перевірити підписку", callback_data="check_subscription")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


@router.chat_join_request()
async def auto_approve_join(request: ChatJoinRequest) -> None:
    await request.approve()
    await request.bot.send_message(
        chat_id=request.user.id,
        text=(
            "👋 Вітаємо у нашій екосистемі PRO#!\n"
            "Тут ви знайдете найкращі CPA-пропозиції та бонуси."
        ),
    )


@router.message(CommandStart())
async def start(message: Message, channels: list[Channel], bot_username: str) -> None:
    is_subscribed = True
    for channel in channels:
        member = await message.bot.get_chat_member(channel.channel_id, message.from_user.id)
        if member.status in {"left", "kicked"}:
            is_subscribed = False
            break

    if not is_subscribed:
        await message.answer(
            "⛔ Доступ заборонено! Підпишись на спонсорів:",
            reply_markup=subscription_keyboard(channels),
        )
        return

    web_app_url = f"https://t.me/{bot_username}/app"
    await message.answer(
        "✅ Ласкаво просимо!",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Відкрити PRO# Hub 🎰",
                        web_app={"url": web_app_url},
                    )
                ]
            ]
        ),
    )


@router.callback_query(F.data == "check_subscription")
async def check_subscription(callback: CallbackQuery, channels: list[Channel]) -> None:
    is_subscribed = True
    for channel in channels:
        member = await callback.bot.get_chat_member(channel.channel_id, callback.from_user.id)
        if member.status in {"left", "kicked"}:
            is_subscribed = False
            break

    if not is_subscribed:
        await callback.answer("Підписка не знайдена. Спробуйте ще раз.", show_alert=True)
        return

    await callback.message.edit_text("✅ Ласкаво просимо!")
    await callback.answer("Підписка підтверджена!", show_alert=True)
