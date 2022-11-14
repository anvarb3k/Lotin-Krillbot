from aiogram.dispatcher.filters.state import State, StatesGroup

class Convert(StatesGroup):
    main = State()
    tolatin = State()
    tokiril = State()