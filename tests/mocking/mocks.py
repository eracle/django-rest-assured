class MockObject(object):
    pass


class MockFactory(object):
    @classmethod
    def create(cls):
        return MockObject()
