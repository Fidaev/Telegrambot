from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


inl_btn_obshes_trans = InlineKeyboardButton(text='Общественный транспорт', callback_data='Общественный транспорт')
inl_btn_avtomobil = InlineKeyboardButton(text='Автомобиль', callback_data='Автомобиль')
inl_btn_peshkom = InlineKeyboardButton(text='В основном хожу пешком', callback_data='В основном хожу пешком')
inl_btn_velosiped = InlineKeyboardButton(text='Велосипед', callback_data='Велосипед')
inl_btn_no_answer = InlineKeyboardButton(text='Затрудняюсь ответить', callback_data='Затрудняюсь ответить')

inl_kb_q42 = InlineKeyboardMarkup().add(inl_btn_obshes_trans).add(inl_btn_avtomobil)\
                                  .add(inl_btn_peshkom).add(inl_btn_velosiped)\
                                  .add(inl_btn_no_answer)

inl_btn_nalichniye = InlineKeyboardButton(text='Наличные кондуктору/водителю', callback_data='Наличные кондуктору/водителю')
inl_btn_proyezdnaya = InlineKeyboardButton(text='Абонемент/проездная карточка', callback_data='Абонемент/проездная карточка')
inl_btn_ne_polzuyus_obsh = InlineKeyboardButton(text='Не пользуюсь общ. транспортом', callback_data='Не пользуюсь общ. транспортом')
inl_btn_drugoe = InlineKeyboardButton(text='Другое', callback_data='Другое')
inl_btn_net_otveta = InlineKeyboardButton(text='Нет ответа', callback_data='Нет ответа')
inl_btn_dalee = InlineKeyboardButton(text='Далее', callback_data='Далее')


inl_kb_q5 = InlineKeyboardMarkup().add(inl_btn_nalichniye).add(inl_btn_proyezdnaya)\
                                  .add(inl_btn_ne_polzuyus_obsh).add(inl_btn_drugoe)\
                                  .add(inl_btn_net_otveta).add(inl_btn_dalee)
