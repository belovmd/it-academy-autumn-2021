# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.

n = int(input('The number of pupils: '))
all_languages = []
for pupil in range(n):
    m = int(input('How many languages does the pupil know: '))
    for language in range(m):
        lang = str(input())
        all_languages.append(lang)
all_languages = set(all_languages)
print('The number of the languages spoken at this school: ', len(all_languages))
print(all_languages)
