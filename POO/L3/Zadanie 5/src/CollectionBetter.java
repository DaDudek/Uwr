import java.util.Collection;
import java.util.Iterator;

/*
Taka wersja interfejsu spełnia wszystkie wymagania które powinna spełniać dowolna kolekcja.
Całą resztę możemy zbudować w razie potrzeby za pomocą tych 4 klocków. W szczególności nawet operacje
size i contains można byłoby wyrzucić jednak są to na tyle uniwersalne (chociażby przy pętlach po kolekcji), że
moim zdaniem powinny zostać.

Rozważałem również dodanie metody get (nie pojawia się on w oryginalnej wersji interfejsu) ale uznałem,że jest to
metoda któa jest zbyt różnorodna. W przypadku nie których zbiorów nie ma co mówić o pobieraniu elementu innego niż
pierwszy/ostatni. W innym wypadku (zbiór) nie jesteśmy nawet w stanie wskazać co get miałby zwracać - losowy obiekt ze
zbioru? Natomiast w przypadku tablicy nie ma co mówić o gecie bez indexu. Zdecydowałem zatem, że interfejs nie powinien
zawierać tej metody aby nie ograniczać twórców danej kolekcji szkieletem  tej funkcji.
 */

public interface CollectionBetter {

    int size();

    boolean contains(Object o);

    boolean add(Object o);

    boolean remove(Object o);
}
