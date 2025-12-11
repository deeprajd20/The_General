import pdfplumber

class Document_Parser:

    def __init__(self,file_path):
        self.file_path = file_path
        self.information_dict = {}
        self.information_dict['file_path'] = file_path
        

    def create_document_object(self):
        doc_obj = pdfplumber.open(self.file_path)
        pages = [p for p in doc_obj.pages]
        return pages
    

    def get_document_info(self):
        pages = self.create_document_object()

        # total number of pages
        self.information_dict['Total_number_of_pages'] = len(pages)

        # images info 
        if "images" not in self.information_dict:
            self.information_dict['images'] = {}

        if "tables" not in self.information_dict:
            self.information_dict['tables'] = {}
        
        
        for id,page in enumerate(pages):
            number_of_images = len(page.images)
            number_of_tables = len(page.find_tables())

            if number_of_images != 0: 
                self.information_dict['images'][id] = number_of_images
            if number_of_tables !=0:
                self.information_dict['tables'][id] = number_of_tables
        

        return self.information_dict


    def get_corpus(self):
        corpus = ""

        pages  = self.create_document_object()
        for page in pages:
            corpus += page.extract_text() + "\n"

        return corpus
