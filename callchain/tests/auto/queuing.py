# -*- coding: utf-8 -*-
'''auto queuing call chain test mixins'''


class AQMixin(object):
    ''

    ###########################################################################
    ## queue manipulation #####################################################
    ###########################################################################

    def test_debug(self):
        self.assertIsNotNone(self.qclass.debug('this is a debug message'))

    def test_info(self):
        self.assertIsNotNone(self.qclass.info('this is a info message'))

    def test_warning(self):
        self.assertIsNotNone(self.qclass.warning('this is a info message'))

    def test_error(self):
        self.assertIsNotNone(self.qclass.error('this is a error message'))

    def test_critical(self):
        self.assertIsNotNone(
            self.qclass.critical('this is a critical message')
        )

    def test_exception(self):
        try:
            raise TypeError()
        except TypeError:
            self.assertIsNotNone(
                self.qclass.exception('this is a exception message')
            )

    def test_ro(self):
        self.assertListEqual(
            self.qclass([1, 2, 3, 4, 5, 6]).ro().peek(), [1, 2, 3, 4, 5, 6],
        )

    def test_extend(self):
        self.assertEqual(
            self.qclass().extend([1, 2, 3, 4, 5, 6]).outsync().end(),
            [1, 2, 3, 4, 5, 6],
        )

    def test_extendleft(self):
        self.assertListEqual(
            self.qclass().extendleft([1, 2, 3, 4, 5, 6]).outsync().end(),
            [6, 5, 4, 3, 2, 1]
        )

    def test_append(self):
        autoq = self.qclass().append('foo').outsync()
        self.assertEqual(autoq.end(), 'foo')

    def test_appendleft(self):
        autoq = self.qclass().appendleft('foo').outsync()
        self.assertEqual(autoq.end(), 'foo')

    def test_inclear(self):
        self.assertEqual(len(list(self.qclass([1, 2, 5, 6]).inclear())), 0)

    def test_outclear(self):
        self.assertEqual(
            len(list(self.qclass([1, 2, 5, 6]).outclear().outgoing)), 0
        )

    ###########################################################################
    ## queue balancing ########################################################
    ###########################################################################

    def test_insync(self):
        q = self.qclass([1, 2, 3, 4, 5, 6]).outshift().inclear().shift()
        self.assertListEqual(list(q.incoming), list(q.outgoing))

    def test_inshift(self):
        q = self.qclass([1, 2, 3, 4, 5, 6]).outshift().sync()
        self.assertListEqual(list(q.incoming), list(q.outgoing))

    def test_outsync(self):
        q = self.qclass([1, 2, 3, 4, 5, 6]).outshift()
        self.assertListEqual(list(q.incoming), list(q.outgoing))

    def test_outshift(self):
        q = self.qclass([1, 2, 3, 4, 5, 6]).outsync()
        self.assertListEqual(list(q.incoming), list(q.outgoing))

    ##########################################################################
    # queue information ######################################################
    ##########################################################################

    def test_results(self):
        self.assertListEqual(
            list(self.qclass(1, 2, 3, 4, 5, 6).outsync().results()),
            [1, 2, 3, 4, 5, 6],
        )
