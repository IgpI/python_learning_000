import logging
from logging import getLogger, StreamHandler,FileHandler ,Formatter


#Loggerオブジェクト設定
logger = getLogger("Test")

#最低出力レベルをDEBUGに設定
logger.setLevel(logging.DEBUG)

#StreamHandlerの設定
st_handler = StreamHandler()
st_handler.setLevel(logging.DEBUG)

#FileHandlerの設定
ft_handler = FileHandler(filename="97.001.ログ出力場所.log", encoding="utf-8")

#フォーマットの調整
handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
st_handler.setFormatter(handler_format)
ft_handler.setFormatter(handler_format)

logger.addHandler(st_handler)
logger.addHandler(ft_handler)

#出力
logger.debug("HelloWorld!!!")
logger.warning("HelloWorld!!!")
