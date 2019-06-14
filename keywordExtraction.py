from rake_nltk import Rake

sample_text=input("Text to extract keyword from: ")

def extractKeywords(text):
    rake_object=Rake()
    rake_object.extract_keywords_from_text(text)
    keyword_list=rake_object.get_ranked_phrases()

    return keyword_list

keyword_list=extractKeywords(sample_text)
print(keyword_list)











