import logging

from masks import account_number_encoder, card_number_encoder
from utils import getting_data_from_file, transaction_amount_in_rubles

logger = logging.getLogger('__masks__')
file_handler_masks = logging.FileHandler('masks_loger.log', 'w', encoding='utf-8')
file_formatter_masks = logging.Formatter('%(asctime)s %(module)s %(levelname)s %(message)s')
file_handler_masks.setFormatter(file_formatter_masks)
logger.addHandler(file_handler_masks)
logger.setLevel(logging.INFO)
logger.info(f"""{card_number_encoder('1234567891011121')},
{account_number_encoder('12345678910111212345')}""")

logger = logging.getLogger('__utils__')
file_handler_utils = logging.FileHandler('utils_loger.log', 'w', encoding='utf-8')
file_formatter_utils = logging.Formatter('%(asctime)s %(module)s %(levelname)s %(message)s')
file_handler_utils.setFormatter(file_formatter_utils)
logger.addHandler(file_handler_utils)
logger.setLevel(logging.INFO)
logger.info(f"""{getting_data_from_file('operations.json')},
{transaction_amount_in_rubles(getting_data_from_file('operations.json')[1])}""")
