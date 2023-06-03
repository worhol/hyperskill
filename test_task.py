import unittest
import task


class TestTask(unittest.TestCase):
    def test_check_starts_apostrophe(self):
        name = "'Hick"
        self.assertRegex(name, r"^(\'|\b)")

    def test_check_ends_apostrophe(self):
        name = "Hick'"
        self.assertRegex(name, r"(\b|\'$)")

    def test_check_ascii_contains_characters(self):
        name = "Jean-Paul D'duck"
        self.assertTrue(task.check_ascii(name))

    def test_check_ascii_does_not_contain_characters(self):
        name = "Stanisław Oğuz"
        self.assertFalse(task.check_ascii(name))

    def test_check_email(self):
        email = 'abcsd@gmail.com'
        self.assertTrue(task.check_email(email))

    def test_check_length(self):
        word = 'adsajjh'
        self.assertTrue(task.check_length(word))

    def test_invalid_length(self):
        word = 'a'
        self.assertFalse(task.check_length(word))


# if __name__ == '__main__':
#     unittest.main()
