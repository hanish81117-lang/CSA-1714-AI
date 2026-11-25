% Library Database

% book(Title, Author)
book('Wings of Fire', 'APJ Abdul Kalam').
book('Godan', 'Premchand').
book('Gitanjali', 'Rabindranath Tagore').
book('Malgudi Days', 'RK Narayan').

% available(Title, Status)
available('Wings of Fire', yes).
available('Godan', no).
available('Gitanjali', yes).
available('Malgudi Days', no).

% Rule: find the author of a book
author_of(Book, Author) :-
    book(Book, Author).

% Rule: check whether a book is available
is_available(Book) :-
    available(Book, yes).
