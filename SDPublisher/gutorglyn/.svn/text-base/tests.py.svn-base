from django.test import Client, TestCase

class menuTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        
    def test_homepage_redirect(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        
    def test_homepage(self):
        response = self.client.get('/gutorglyn/index/')
        self.assertEqual(response.status_code, 200)
        
    def test_poem(self):
        response = self.client.get('http://localhost:8000/gutorglyn/poem/?poem-selection=001&first-line=%23')
        self.assertEqual(response.status_code, 200)        
        
    def test_title_list(self):
        response = self.client.get('/gutorglyn/title-list/')
        self.assertEqual(response.status_code, 200)    
        
    def test_patron_list(self):
        response = self.client.get('/gutorglyn/patron-list/')
        self.assertEqual(response.status_code, 200)                        
    
    def test_personal_names(self):
        response = self.client.get('/gutorglyn/get-personal-names/')
        self.assertEqual(response.status_code, 200) 
        
    def test_place_names(self):
        response = self.client.get('/gutorglyn/get-place-names/')
        self.assertEqual(response.status_code, 200)         
        
    def test_manuscripts(self):
        response = self.client.get('/gutorglyn/get-manuscripts/')
        self.assertEqual(response.status_code, 200)                  
    
    def test_biography(self):
        response = self.client.get('/gutorglyn/biog/')
        self.assertEqual(response.status_code, 200)                
    
    def test_tuchwith(self):
        response = self.client.get('/gutorglyn/tuchwith/')
        self.assertEqual(response.status_code, 200)
        
    def test_about(self):
        response = self.client.get('/gutorglyn/about/')
        self.assertEqual(response.status_code, 200)   
    
    def test_musical_companions(self):
        response = self.client.get('/gutorglyn/musical-companions/')
        self.assertEqual(response.status_code, 200)                           
        
class apiTests(TestCase):     
    
    def setUp(self):
        self.client = Client()

#    Poem
        
    def test_full_poem(self):
        response = self.client.get('/gutorglyn/poem-raw/001')
        self.assertEqual(response.status_code, 200)  

    def test_line_group(self):
        response = self.client.get('/gutorglyn/lines-raw/001/2')
        self.assertEqual(response.status_code, 200) 
         
    def test_line(self):
        response = self.client.get('/gutorglyn/line-raw/001/16')
        self.assertEqual(response.status_code, 200)  
        
    def test_line_ranges(self):
        response = self.client.get('/gutorglyn/lines-range-raw/001/16/18')
        self.assertEqual(response.status_code, 200)  

#    Transcription

    def test_first_transcription(self):
        response = self.client.get('/gutorglyn/transcripts/?poem=001')
        self.assertEqual(response.status_code, 200)  
        
    def test_transcription_named(self):
        response = self.client.get('/gutorglyn/transcripts/?poem=001&transcript=BL14967_035')
        self.assertEqual(response.status_code, 200)          

#    Transcription images

    def test_transcription_images(self):
        response = self.client.get('/gutorglyn/transcriptimages/?poem=001')
        self.assertEqual(response.status_code, 200)    
        
    def test_transcription_images_named(self):
        response = self.client.get('/gutorglyn/transcriptimages/?poem=035&transcript=BL14967_035')
        self.assertEqual(response.status_code, 200)     
        
#    XML list of patrons and IDs

    def test_xml_patrons_ids_CY(self):
        response = self.client.get('/gutorglyn/patron-xml?lang=cym')
        self.assertEqual(response.status_code, 200)  
        
    def test_xml_patrons_ids_EN(self):
        response = self.client.get('/gutorglyn/patron-xml?lang=eng')
        self.assertEqual(response.status_code, 200)       
        
class internalSources(TestCase):
    
    def test_variant_lines(self):
        response = self.client.get('/gutorglyn/variant-lines/?p=001&l=1')
        self.assertEqual(response.status_code, 200) 
        
    def test_patron_details_CY(self):
        response = self.client.get('http://localhost:8000/gutorglyn/patron/?n=nr08')
        self.assertEqual(response.status_code, 200)
                
    def test_patron_details_EN(self):
        response = self.client.get('http://localhost:8000/gutorglyn/patron/?n=nr08&lang=en')
        self.assertEqual(response.status_code, 200)   
        
    def test_important_people(self):
        response = self.client.get('/gutorglyn/people/?poem=018a ')
        self.assertEqual(response.status_code, 200)          
                          
                        
              