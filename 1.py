# 1. Buat sebuah fungsi untuk mengubah kalimat berikut menjadi kalimat yang mudah terbaca:
#     italem irad irigayaj
#     iadab itsap ulalreb
#     nalub kusutret gnalali

def reverse_sentence(s):
    words = ''
    for i in s:
        words = i + words  # appending chars in reverse order
    words = words.split()
    words = list(reversed(words))
    return " ".join(words)

sentences =["italem irad irigayaj","iadab itsap ulalreb","nalub kusutret gnalali"]

for i in sentences:
    print(reverse_sentence(i))
