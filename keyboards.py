from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud import s, get_all_dev_types, get_dev_by_title


def gen_start_kb():
    devs = get_all_dev_types(s)
    types = []
    for d in devs:
        if d.device_type not in types:
            types.append(d.device_type)
    butt = [[InlineKeyboardButton(text= d, callback_data='first_' +d)] for d in types]

    start_kb = InlineKeyboardMarkup(inline_keyboard=butt)
    return start_kb


def gen_companyies_kb(typ):
    devs = [d for d in get_all_dev_types(s) if d.device_type == typ]
    types = []
    for d in devs:
        if d.company not in types:
            types.append(d.company)
    
    butt = [[InlineKeyboardButton(text= d, callback_data='second_' +d+ '_'+typ)] for d in types]
    butt.append([InlineKeyboardButton(text= 'Назад', callback_data='start')])


    sec_kb = InlineKeyboardMarkup(inline_keyboard=butt)
    return sec_kb


def gen_devices_kb(typ, comp, last_cb):
    devs = [d for d in get_all_dev_types(s) if (d.company == comp and d.device_type == typ)]
    types = []
    for d in devs:
        if d.device_title not in types:
            types.append(d.device_title)

    butt = [[InlineKeyboardButton(text=d, callback_data='devs_' + str(d))] for d in types]
    butt.append([InlineKeyboardButton(text= 'Назад', callback_data='first_' + typ)])


    dev_kb = InlineKeyboardMarkup(inline_keyboard=butt)
    return dev_kb


def gen_devices_param_kb(dev_title, last_cb):
    devs = get_dev_by_title(s, dev_title)
    types = []
    for d in devs:
        if d.params not in types:
            types.append(d.params)

    butt = [[InlineKeyboardButton(text=k, callback_data='params_'+dev_title+'#' + str(k))] for k in types]
    butt.append([InlineKeyboardButton(text= 'Назад', callback_data='second_' + devs[0].company + '_' + devs[0].device_type)])
    dev_kb = InlineKeyboardMarkup(inline_keyboard=butt)
    return dev_kb

def gen_last_kb(dev_title):
    dev_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text= 'Назад', callback_data='devs_' + dev_title)]])
    return dev_kb