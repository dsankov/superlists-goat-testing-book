from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):
    """тест на тосксичность"""
    
    def test_bad_maths(self):
        """тест на неверную матемтику"""
        
        self.assertEqual(1 + 1, 3)
        