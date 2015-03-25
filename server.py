__author__ = 'jspataro'

from events.eventlog import logger


class GameServer(object):

    def init(self):
        return True

    def run(self):
        pass


if __name__ == "__main__":
    logger.info('Server: Starting up the game server...')
    logger.info('Server: Calling GameServer.init()...')

    server = GameServer()
    if server.init():
        server.run()
