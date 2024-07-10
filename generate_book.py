from faker import Faker
import random


def generate_book(words_count=10000):
    # create a Faker instance
    faker = Faker()

    word_count = 0
    while word_count < words_count:
        # generate a random sentence with a random number of words
        sentence = faker.sentence(nb_words=random.randint(5, 15))
        print(sentence)

        # increase the word count
        word_count += len(sentence.split(" "))


if __name__ == "__main__":
    generate_book()