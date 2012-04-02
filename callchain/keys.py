# -*- coding: utf-8 -*-
'''callchain reset keys'''

from appspace.keys import AppspaceKey, Attribute


class KDefaults(AppspaceKey):

    '''default settings key'''


class KRequired(AppspaceKey):

    '''required settings key'''


class NoServiceError(Exception):

    '''no service error'''


class KResetType(AppspaceKey):

    '''reset type key'''

    def reset():  # @NoSelf
        '''reset previously accessed `lazybase` attributes'''


class KResetLocal(KResetType):

    '''reset thread local key'''


class KSettings(KResetLocal):

    '''settings key'''


class KCore(KResetLocal):

    '''core key'''

    G = Attribute('external application global settings')

    def __init__(root):  # @NoSelf
        '''
        init

        @param root: root chain
        '''


class KConfig(KCore):

    '''configuration access key'''

    defaults = Attribute('default settings by their lonesome')
    required = Attribute('required settings by their lonesome')


class KRoot(KConfig):

    '''root chain key'''

    def __init__(pattern=None, required=None, defaults=None, **kw):  # @NoSelf
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''

    def __call__(*args):  # @NoSelf
        '''new chain session'''

    def back(branch):  # @NoSelf
        '''
        handle return from branch chain

        @param branch: branch chain
        '''


class KEventRoot(KRoot):

    '''root event key'''

    def __init__(  # @NoSelf
        patterns=None,
        events=None,
        required=None,
        defaults=None,
        *args,
        **kw
    ):
        '''
        init

        @param patterns: pattern config or eventspace label (default: None)
        @param events: events configuration (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''

    def event(event):  # @NoSelf
        '''
        create or fetch `event`

        @param event: event label
        '''

    def unevent(event):  # @NoSelf
        '''
        drop `event`

        @param event: event label
        '''


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


class KCall(KResetLocal):

    '''call key'''

    L = Attribute('local settings extracted')
    Meta = Attribute('local settings')
    port = Attribute('python 2.x <-> python 3.x porting helper')
    space = Attribute('external appspace interface')

    def __enter__():  # @NoSelf
        '''enter execution context'''

    def __exit__(e, t, b):  # @NoSelf
        '''exit execution context'''

    def switch(label, key=False):  # @NoSelf
        '''
        overt switch to linked chain configured in external appspace

        @param label: linked chain label
        @param key: linked chain chain key (default: False)
        '''

    def commit():  # @NoSelf
        '''consume call chain'''


class KEventCall(KCall):

    '''event call key'''

    def fire(*events):  # @NoSelf
        '''
        run calls bound to `events` **NOW**

        @param *events: event labels
        '''

    def queues(*events):  # @NoSelf
        '''
        ordered mapping of processing queues for `events`

        @param *events: event labels
        '''


class KBranch(KCore):

    ''''branch key'''

    G = Attribute('root external global settings')
    M = Attribute('root external appspace manager')
    _G = Attribute('root internal global settings')
    _M = Attribute('root internal appspace manager')
    root = Attribute('root object')


class KEventBranch(KBranch):

    '''event branch key'''

    E = Attribute('local event registry')


class KLinked(KBranch):

    '''linked chain mixin'''

    def close():  # @NoSelf
        '''close out linked chain and switch to root chain'''


class KChainletKey(KBranch):

    def back():  # @NoSelf
        '''switch back to root chain'''
