library = {
    "books": [
        {
            "title": "The Silent Patient",
            "author": "Alex Michaelides",
            "genre": "Thriller",
            "pages": 336,
            "year": 2019,
            "rating": 4.1
        },
        {
            "title": "Atomic Habits",
            "author": "James Clear",
            "genre": "Self-Help",
            "pages": 320,
            "year": 2018,
            "rating": 4.8
        },
        {
            "title": "Dune",
            "author": "Frank Herbert",
            "genre": "Science Fiction",
            "pages": 688,
            "year": 1965,
            "rating": 4.6
        },
        {
            "title": "Sapiens",
            "author": "Yuval Noah Harari",
            "genre": "History",
            "pages": 498,
            "year": 2011,
            "rating": 4.7
        }
    ],
    "librarian": {
        "name": "Sarah Whitman",
        "years_experience": 12
    }
}


def get_list():
    
    for k, v in library.items():
        print(f"\n{k.upper()}\n")
        if isinstance(v, list):
            for item in v:
                for k, v in item.items():
                    print(f"{k}: {v}\n")
        else:
            print(f"{v}\n")


get_list()