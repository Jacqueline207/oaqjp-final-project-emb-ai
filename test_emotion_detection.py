import unittest
from emotion_detection import emotion_detector
#should create a class
class TestEmotionDetector(unittest.TestCase):
    def test_emotion_joy(self):
        statement = "I am glad this happened"
        #get the result as well
        result = emotion_detector(statement) #or i could just write the statement as is
        #now for assertion 
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_emotion_anger(self):
        statement = "I am really mad about this"
        result = emotion_detector(statement) 
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_emotion_disgust(self):
        statement = "I am disgusted just hearing about this"
        result = emotion_detector(statement) 
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_emotion_sadness(self):
        statement = "I am so sad about this"
        result = emotion_detector(statement) 
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_emotion_fear(self):
        statement = "I am really afraid this will happen"
        result = emotion_detector(statement)  
        self.assertEqual(result["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()