import configparser
import os


class Config:
    def __init__(self, config_file='config.ini'):
        """
        Initialize Config class with configuration details from the specified file.

        Args:
            config_file (str): Path to the configuration file.
        """
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_elasticsearch_config(self):
        """
        Get Elasticsearch configuration details from the config file.

        Returns:
            dict: Elasticsearch configuration details.
        """
        elasticsearch_config = {}
        if 'elasticsearch' in self.config:
            elasticsearch_config['host'] = self.config['elasticsearch'].get('host')
            elasticsearch_config['port'] = self.config['elasticsearch'].getint('port')
            elasticsearch_config['username'] = self.config['elasticsearch'].get('username')
            elasticsearch_config['password'] = self.config['elasticsearch'].get('password')
        return elasticsearch_config

    def get_openai_config(self):
        """
        Get Elasticsearch configuration details from the config file.

        Returns:
            dict: Elasticsearch configuration details.
        """
        openai_config = {}
        if 'openai' in self.config:
            openai_config['api_key'] = self.config['openai'].get('api_key')

        return openai_config
