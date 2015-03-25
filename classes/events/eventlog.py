__author__ = 'jspataro'

import logging

logger = logging.getLogger('landduels')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('game.events.log', mode='w')
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(log_formatter)
console_handler.setFormatter(log_formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
