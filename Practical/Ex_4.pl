% Admission Eligibility
% marks(Person, Maths, Physics, ComputerScience)

marks(hanish, 85, 78, 90).
marks(ravi, 60, 70, 55).
marks(priya, 92, 88, 95).
marks(kumar, 45, 80, 70).

% Eligible if Maths >= 60, Physics >= 60 and Computer Science >= 60
eligible(Person) :-
    marks(Person, M, P, C),
    M >= 60,
    P >= 60,
    C >= 60.

% Message rule
check(Person) :-
    eligible(Person), !,
    write(Person), write(' is eligible for admission.'), nl.
check(Person) :-
    write(Person), write(' is NOT eligible for admission.'), nl.
