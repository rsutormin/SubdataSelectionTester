# -*- coding: utf-8 -*-
#BEGIN_HEADER
from biokbase.workspace.client import Workspace as workspaceService
#END_HEADER


class SubdataSelectionTester:
    '''
    Module Name:
    SubdataSelectionTester

    Module Description:
    A KBase module: SubdataSelectionTester
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""
    
    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        #END_CONSTRUCTOR
        pass
    

    def get_object_subset(self, ctx, sub_object_ids):
        """
        :param sub_object_ids: instance of list of type "SubObjectIdentity"
           -> structure: parameter "ref" of String, parameter "included" of
           list of String
        :returns: instance of list of type "ObjectData" -> structure:
           parameter "data" of unspecified object
        """
        # ctx is the context object
        # return variables are: data
        #BEGIN get_object_subset
        ws = workspaceService(self.workspaceURL, token=ctx["token"])
        data = ws.get_object_subset(sub_object_ids)
        #END get_object_subset
        # At some point might do deeper type checking...
        if not isinstance(data, list):
            raise ValueError('Method get_object_subset return value ' +
                             'data is not type list as required.')
        # return the results
        return [data]

    def hello_world(self, ctx, name):
        """
        :param name: instance of String
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: message
        #BEGIN hello_world
        message = "Hello, " + name + "!"
        #END hello_world

        # At some point might do deeper type checking...
        if not isinstance(message, basestring):
            raise ValueError('Method hello_world return value ' +
                             'message is not type basestring as required.')
        # return the results
        return [message]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
