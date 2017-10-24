from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.context import InitCommandContext, ResourceCommandContext
from cloudshell.shell.core.context_utils import context_from_args
from cloudshell.power.pdu.power_resource_driver_interface import PowerResourceDriverInterface

class {{cookiecutter.driver_name}} (ResourceDriverInterface, PowerResourceDriverInterface):

    def cleanup(self):
        """
        Destroy the driver session, this function is called everytime a driver instance is destroyed
        This is a good place to close any open sessions, finish writing to log files
        """
        pass

    def __init__(self):
        """
        ctor must be without arguments, it is created with reflection at run time
        """
        pass

    @context_from_args
    def initialize(self, context):
        """
        Initialize the driver session, this function is called everytime a new instance of the driver is created
        This is a good place to load and cache the driver configuration, initiate sessions etc.
        :param InitCommandContext context: the context the command runs on
        """
        pass

    @context_from_args
    def PowerOn(self, context, ports):
        """ Powers on outlets on the managed PDU
        :param context: context from the command which invoked PowerOn
        :param ports: full addresses of outlets on PDU, example: ['192.168.30.128/4', '192.168.30.128/6']
        :type ports: str
        :returns: command result
        :rtype: str
        """
        pass


    @context_from_args
    def PowerOff(self, context, ports):
        """ Powers off outlets on the managed PDU
        :param context: context from the command which invoked PowerOff
        :param ports: full addresses of outlets on PDU, example: ['192.168.30.128/4', '192.168.30.128/6']
        :type ports: str
        :returns: command result
        :rtype: str
        """
        pass

    @context_from_args
    def PowerCycle(self, context, ports, delay=0):
        """ Powers off outlets, waits during delay, then powers outlets on
        :param context: context from the command which invoked PowerCycle
        :param ports: full addresses of outlets on PDU, example: ['192.168.30.128/4', '192.168.30.128/6']
        :type ports: str
        :param delay: seconds to wait after power off
        :type delay: int
        :returns: command result
        :rtype: str
        """
        pass
    
    @context_from_args
    def example_function(self, context):
        """
        A simple example function
        :param ResourceCommandContext context: the context the command runs on
        """
        pass

    @context_from_args
    def example_function_with_params(self, context, user_param1, user_param2):
        """
        An example function that accepts two user parameters
        :param ResourceCommandContext context: the context the command runs on
        :param str user_param1: A user parameter
        :param str user_param2: A user parameter
        """
        pass

    def _helper_function(self):
        """
        Private functions are always hidden, and will not be exposed to the end user
        """
        pass
