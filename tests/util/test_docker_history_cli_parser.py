import unittest
from dagda.util.docker_history_cli_parser import DockerHistoryCLIParser


# -- Test suite

class DockerHistoryCLIParserTestCase(unittest.TestCase):

    def test_empty_args(self):
        empty_args = generate_args(None)
        status = DockerHistoryCLIParser.verify_args("docker_history.py", empty_args)
        self.assertEqual(status, 1)


    def test_ok_args(self):
        empty_args = generate_args('jboss/wildfly')
        status = DockerHistoryCLIParser.verify_args("docker_history.py", empty_args)
        self.assertEqual(status, 0)


# -- Util methods

def generate_args(docker_image_name):
    return AttrDict([('docker_image_name', docker_image_name)])


# -- Util classes

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


if __name__ == '__main__':
    unittest.main()