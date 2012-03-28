# -*- coding: utf-8 -*-
'''callchain core keys'''

from callchain.keys.reset import KResetLocal


class KChain(KResetLocal):

    '''chain key'''

    def chain(call, key=False, *args, **kw):  # @NoSelf
        '''
        add `call` or appspaced `call` to call chain, partializing it with any
        passed arguments

        @param call: call or appspaced call label
        @param key: appspace key (default: False)
        '''

    def clear():  # @NoSelf
        '''clear things'''

    def tap(call, key=False):  # @NoSelf
        '''
        add call

        @param call: callable or appspace label
        @param key: link call chain key (default: False)
        '''

    def wrap(call, key=False):  # @NoSelf
        '''build current callable from factory'''


class KEvent(KChain):

    '''event chain key'''

    def on(event, call, key=False, *args, **kw):  # @NoSelf
        '''
        bind call to `event`

        @param event: event label
        @param call: label for call or eventspaced thing
        @param key: key label (default: False)
        '''

    def off(event):  # @NoSelf
        '''
        clear calls bound to `event`

        @param event: event label
        '''

    def trigger(*events):  # @NoSelf
        '''
        extend primary call chain with partials bound to `events`

        @param *events: event labels
        '''
