# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
# pylint: disable-msg=e0211,e0213
'''callchain keys'''

from callchain.mixins.services.queuing import AQueue

__all__ = ('ACallChain', 'AChainLink')


class AChains(AQueue):
    
    '''chains key'''

    def commit():
        '''invoke call chain'''

    def chain(call, key=False, *args, **kw):
        '''
        add callable or appspaced application to call chain, partializing it
        with any passed parameters

        @param call: callable or application label
        @param key: key label (default: False)
        '''


class ACallChain(AChains):

    '''call chain key'''
    
    def link(label, branch):
        '''
        add linked call chain class

        @param label: linked call chain class label
        @param branch: linked call chain class
        '''

    def switch(label):
        '''
        switch to linked call chain

        @param label: chain label
        '''


class AChainLink(AChains):

    '''linked call chain key'''
    
    def back():
        '''return to root call chain'''
