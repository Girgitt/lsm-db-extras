import os
import time
import logging
from unittest import TestCase, skip
from lsm import LSM
from lsm_extras import Shelf, LSMDict

root = logging.getLogger()
hdlr = root.handlers[0]
fmt = logging.Formatter('%(asctime)s,%(msecs)d %(levelname)-8s [%(name)s] [%(filename)s:%(lineno)d] %(message)s')
hdlr.setFormatter(fmt)

log = logging.getLogger("[TEST]")
log.propagate = True


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            log.debug ('%r  %2.3f s' % \
                  (method.__name__, (te - ts)))
        return result
    return timed


class TestLsmDb(TestCase):
    def setUp(self):
        pass

    @timeit
    def write_test(self, lsm, iterations=1000):

        lsm._db.begin()
        for i in range(iterations):
            lsm[i] = '0' * 32000

            if i % 10000 == 0:
                lsm._db.commit()
                lsm._db.flush()
                lsm._db.begin()

        lsm._db.commit()
        lsm._db.commit()

            #lsm.update({i: '0' * 32000})

        #for i in range(iterations):
        #    lsm[i] = '0' * 32000
    @timeit
    def read_test(self, lsm, iterations=1000):
        for i in range(iterations):
            log.debug(len(lsm))
            for index in sorted(lsm.keys()):
                d = lsm[index]
                if index % 10000 == 0:
                    log.debug("%s: %s" % (index, len(d)))
                    #log.debug("%s" % index)
            #log.debug("%s" % len(lsm.keys()))

    def test_lsm_init(self):
        try:
            os.unlink('test.db')
        except:
            pass

        #with LSMDict('test.db', autocheckpoint=8*1024, autowork=False) as lsm:
        #with LSMDict('test.db', autowork=False, autoflush=500000, autocheckpoint=900000, automerge=8, multiple_processes=False, write_safety=False, transaction_log=False) as lsm:
        with LSMDict('test.db', autowork=False,  multiple_processes=False, write_safety=False, transaction_log=False) as lsm:
            self.write_test(lsm, iterations=30000)
            self.read_test(lsm, iterations=1)
            self.assertEqual(30000, len(lsm.keys()))
            self.assertEqual('0' * 32000, lsm[0])
            self.assertEqual('0' * 32000, lsm[1000])
        lsm.close()
        #self.fail()

    def test_set_uniqueness(self):
        s = set()
        s.add('a')
        s.add('a')
        s.add('b')
        s.add('c')
        self.assertEqual(sorted({'a', 'b', 'c'}), sorted(s))