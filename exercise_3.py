# import requests
import timeit
from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search
# from article_1 import article_1
# from article_2 import article_2
# import random




# url = f"https://drive.usercontent.google.com/u/0/uc?id={doc_id}&export=download"
# response = requests.get(url)
# text = response.text

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def time_counter(func,data):
    main_string,substring = data
    start = timeit.default_timer()
    result = func(main_string[:],substring)
    # print(result)
    time_difference = timeit.default_timer() - start
    return "{:.5f}".format(time_difference)

article_1 = "Being a developer is not easy"

article_2 = "Be a developer"

main_string = "Being a developer is not easy"
# substring = "developer"
real_substring = "Britnea Spirs"
fake_substring = "Aeva"
# position = rabin_karp_search(main_string, substring)
# if position != -1:
#     print(f"Substring found at index {position}")
# else:
#     print("Substring not found")



def search_data (main_string, substring):
    return main_string,substring
    

# First article
# # Real substring
data = search_data(article_1,real_substring)
# # Fake substring
data = search_data(article_1,fake_substring)

# Second article
# # Real substring
data = search_data(article_2,real_substring)
# # Fake substring
data = search_data(article_2,fake_substring)

print("Knuth_Morris_Pratt_search",time_counter(kmp_search,data))
print("Boyer_Moore_search",time_counter(boyer_moore_search,data))
print("Rabin_Karp_search",time_counter(rabin_karp_search,data))

if __name__ == '__main__':
    text1 = read_file('Algorythms/homework/goit-algo-hw-05/task 3/article1.txt')
    text2 = read_file('Algorythms/homework/goit-algo-hw-05/task 3/article2.txt')
    