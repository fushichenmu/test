from abc import ABCMeta, abstractmethod


class ResourceCommonHandler:

    def __init__(self
                 , workstation
                 , input_data=None
                 , use_default_setting=True
                 , params_dict=None
                 , resource=None
                 ):
        '''
        @param workstation:
        @param resource:
        @param input_data:
        @param common_params_:
        @param params_dict:
        '''
        self.workstation = workstation
        self.input_data = input_data
        self.use_default_setting = use_default_setting
        self.params_dict = params_dict
        self.resource = resource

    def contour_map(self):
        pass
