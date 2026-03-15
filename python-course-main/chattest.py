import unittest
import chat

class TestChatbot(unittest.TestCase):

    def test_analyze_mood_happy(self):
        result = chat.analyze_mood("I feel very happy today")
        return self.assertEqual(result, "happy")

    def test_analyze_mood_sad(self):
        result = chat.analyze_mood("I am sad and upset")
        return self.assertEqual(result, "sad")

    def test_analyze_mood_neutral(self):
        result = chat.analyze_mood("Today is a normal day")
        return self.assertEqual(result, "neutral")

    def test_joke_response(self):
        response = chat.get_response("tell me a joke", "Nittai")
        return self.assertIn(response, chat.jokes)

    def test_color_question(self):
        response = chat.get_response("favorite color", "Nittai")
        return self.assertEqual(response, "My favorite color is blue! What's yours?")

    def test_greeting(self):
        response = chat.get_response("hello", "Nittai")
        return self.assertIn(response, chat.greetings)

    def test_math(self):
        response = chat.get_response("10 + 5", "Nittai")
        return self.assertEqual(response, "The result is: 15")

    def test_default_response(self):
        response = chat.get_response("random text", "Nittai")
        return self.assertIn(response, chat.default_response("Nittai"))

if __name__ == "__main__":
    unittest.main()
