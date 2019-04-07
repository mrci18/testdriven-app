class BaseConfig:
    """Base configuration"""
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    pass

class TestConfig(BaseConfig):
    """Test configuration"""
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass




