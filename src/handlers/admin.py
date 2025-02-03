from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from core.config import settings
from static import messages

from models.lead import LeadModel

router = Router()

@router.message(Command("leads"))
async def get_leads(message: Message):
    if str(message.from_user.id) in settings.get_admin_ids():
        leads = await LeadModel.all()
        for lead in leads:
            await message.answer(messages.get_lead(lead))
    else:
        await message.answer(messages.ADMIN_ERROR)