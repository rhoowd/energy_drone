import logging
import time


# === Logging setup === #
logger = logging.getLogger('Energy')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('./energy.log')
sh = logging.StreamHandler()
fm = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > [%(name)s] %(message)s')
fh.setFormatter(fm)
sh.setFormatter(fm)
logger.addHandler(fh)
logger.addHandler(sh)

# now = time.localtime()
# s_time = "%02d%02d-%02d%02d%02d" % (now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
# result = logging.getLogger('Result')
# result.setLevel(logging.INFO)
# result_fh = logging.FileHandler("./result/r-" + s_time + ".txt")
# result_fm = logging.Formatter('[%(filename)s:%(lineno)s] %(asctime)s\t%(message)s')
# result_fh.setFormatter(result_fm)
# result.addHandler(result_fh)
