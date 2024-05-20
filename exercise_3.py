import timeit
from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search


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


article_1 = read_file("article_1.txt")
article_2 = read_file("article_2.txt")
real_substring = "Стаття"
fake_substring = "Вигаданий рядок"

def search_data (main_string, substring):
    return main_string,substring
    
# Code for checking results

# First article
# # Real substring
# data = search_data(article_1,real_substring)
# # Fake substring
# data = search_data(article_1,fake_substring)

# Second article
# # Real substring
# data = search_data(article_2,real_substring)
# # Fake substring
data = search_data(article_2,fake_substring)

print("Knuth_Morris_Pratt_search",time_counter(kmp_search,data))
print("Boyer_Moore_search",time_counter(boyer_moore_search,data))
print("Rabin_Karp_search",time_counter(rabin_karp_search,data))

    