import unittest
import lambda_function

class LambdaFunctionUnitTests(unittest.TestCase):

    def test_isDateIn(self):
        self.assertTrue(lambda_function.isDateIn('2021-02-09T00:00:00.000Z',['2021-02-04T00:00:00.000Z', '2021-02-09T00:00:00.000Z', '2021-02-17T00:00:00.000Z', '2021-02-18T00:00:00.000Z', '2021-02-20T00:00:00.000Z', '2021-02-21T00:00:00.000Z', '2021-02-27T00:00:00.000Z']))
        self.assertFalse(lambda_function.isDateIn('2021-02-09T00:00:00.000Z',['2021-02-04T00:00:00.000Z', '2021-02-17T00:00:00.000Z', '2021-02-18T00:00:00.000Z', '2021-02-20T00:00:00.000Z', '2021-02-21T00:00:00.000Z', '2021-02-27T00:00:00.000Z']))

    def test_findPeople(self): 
        self.assertEqual(lambda_function.findPeople("Deepwood Motte", "2021-02-09T00:00:00.000Z"),["Eddard \"Ned\" Stark", "Jorah Mormont", "Melisandre", "Sandor Clegane"])
        self.assertNotEqual(lambda_function.findPeople("Deepwood Motte", "2021-02-09T00:00:00.000Z"),["Jorah Mormont", "Melisandre", "Sandor Clegane"])
        self.assertEqual(lambda_function.findPeople("Asshai", "2021-02-01T00:00:00.000Z"),["Bronn", "Jon Snow", "Sansa Stark"])
        self.assertNotEqual(lambda_function.findPeople("Asshai", "2021-02-01T00:00:00.000Z"),["Jon Snow", "Sansa Stark"])
    
    def test_findLocationsFor(self): 
        self.assertEqual(lambda_function.findLocationsFor("Ramsay Bolton", "2021-02-03T00:00:00.000Z"),["Ashemark", "Dragonstone", "Highgarden"])
        self.assertNotEqual(lambda_function.findLocationsFor("Ramsay Bolton", "2021-02-03T00:00:00.000Z"),["Dragonstone", "Highgarden"])
        self.assertEqual(lambda_function.findLocationsFor("Theon Greyjoy", "2021-02-04T00:00:00.000Z"),["Astapor", "Myr", "Summerhall", "The Wall"])
        self.assertNotEqual(lambda_function.findLocationsFor("Theon Greyjoy", "2021-02-04T00:00:00.000Z"),["Myr", "Summerhall", "The Wall"])

    def test_findCloseContacts(self): 
        self.assertEqual(lambda_function.findCloseContacts("Jon Snow", "2021-02-28T00:00:00.000Z"), ["Daenerys Targaryen", "Talisa Maegyr", "Tormund Giantsbane", "Cersei Lannister", "The High Sparrow", "Gendry", "Sandor Clegane"])
        self.assertNotEqual(lambda_function.findCloseContacts("Jon Snow", "2021-02-28T00:00:00.000Z"), [ "Talisa Maegyr", "Tormund Giantsbane", "Cersei Lannister", "The High Sparrow", "Gendry", "Sandor Clegane"])
        self.assertEqual(lambda_function.findCloseContacts("Theon Greyjoy", "2021-02-04T00:00:00.000Z"),["Jeor Mormont", "Daenerys Targaryen", "Davos Seaworth", "Jon Snow", "Samwell Tarly", "Margaery Tyrell", "Brienne of Tarth"])
        self.assertNotEqual(lambda_function.findCloseContacts("Theon Greyjoy", "2021-02-04T00:00:00.000Z"),["Daenerys Targaryen", "Davos Seaworth", "Jon Snow", "Samwell Tarly", "Margaery Tyrell", "Brienne of Tarth"])


if __name__ == '__main__':
    unittest.main()
