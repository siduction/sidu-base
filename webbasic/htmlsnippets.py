'''
Created on 04.03.2013

@author: hm
'''

import re

class HTMLSnippets:
    '''Administrates (short) HTML fragments which can easily switched on or off.
    The snippets will be defined in a text file.
    Snippets are identified by a name, e.g. ITEM_START and ITEM_END
    
    Example:
    ITEM_START:
    <ul>
    
    ITEM_END:
    </ul>
    '''
    def __init__(self, session):
        '''Constructor.
        @param session: the session info
        '''
        self._dict = {}
        self._session = session
        
    def read(self, name):
        '''Reads the snippet definitions.
        @param name: the specific part of the filename (without path)
        '''
        fn = self._session._homeDir + 'config/' + name + '.snippet.html'
        rexpr = re.compile(r'([A-Z0-9_.-]+):\s*$')
        body = ''
        name = ''
        with open(fn, 'r') as fp:
            for line in fp:
                matcher = rexpr.match(line)
                if matcher == None:
                    body += line
                else:
                    if name != None:
                        if body.endswith('\n\n'):
                            body = body[0:-1]
                        self._dict[name] = body
                    body = ''
                    name = matcher.group(1)
            if body.endswith('\n\n'):
                body = body[0:-1]
            self._dict[name] = body
        fp.close()
        
    def get(self, name):
        '''Returns a snippet given by its name.
        @param name: the wanted snippet
        @return: '': not found.<br>
                otherwise: the body of the snippet
        '''
        if name in self._dict:
            rc = self._dict[name]
        else:
            rc = ''
            self._session.error('HTMLSnippets.get({:s}: not defined'.format(name))

        return rc
            